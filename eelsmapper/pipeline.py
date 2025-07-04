from eelsmapper.preprocessing.pca_denoising import pca_denoise
from eelsmapper.embedding.tsne import tsne_embed
from eelsmapper.clustering.kmeans import kmeans_cluster
from eelsmapper.analysis.mutual_info import mutual_info_matrix
from eelsmapper.analysis.vector_quant import vector_quantization

def run_pipeline(X):
    X_denoised, _ = pca_denoise(X)
    X_embedded = tsne_embed(X_denoised)
    labels, _ = kmeans_cluster(X_embedded)
    X_vq, _ = vector_quantization(X_denoised)
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
    