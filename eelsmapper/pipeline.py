import numpy as np

from eelsmapper.preprocessing.pca_denoising import pca_denoise
from eelsmapper.embedding.tsne import tsne_embed
from eelsmapper.clustering.kmeans import kmeans_cluster
from eelsmapper.analysis.mutual_info import mutual_info_matrix
from eelsmapper.analysis.vector_quant import vector_quantization


def run_pipeline(X):
    X = np.asarray(X)
    if X.ndim == 3:
        X = X.reshape(-1, X.shape[-1])
    if X.ndim != 2:
        raise ValueError("X must be a 2-D spectra matrix or a 3-D spectra cube")

    n_samples, n_features = X.shape
    n_components = min(10, n_samples, n_features)
    n_clusters = min(5, n_samples)
    perplexity = min(30, max(1, (n_samples - 1) / 3))

    X_denoised, _ = pca_denoise(X, n_components=n_components)
    X_embedded = tsne_embed(X_denoised, perplexity=perplexity)
    labels, _ = kmeans_cluster(X_embedded, n_clusters=n_clusters)
    X_vq, _ = vector_quantization(X_denoised, n_clusters=n_clusters)
    mi_matrix = mutual_info_matrix(labels[:, None])
    return {
        "denoised": X_denoised,
        "embedded": X_embedded,
        "clusters": labels,
        "vq": X_vq,
        "mutual_info": mi_matrix
    }


def test_output():
    print("hello world")
