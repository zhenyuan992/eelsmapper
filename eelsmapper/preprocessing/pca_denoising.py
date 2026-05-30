import numpy as np
from sklearn.decomposition import PCA


def pca_denoise(X, n_components=10):
    X = np.asarray(X)
    if X.ndim != 2:
        raise ValueError("X must be a 2-D array with shape (n_samples, n_features)")

    n_components = min(int(n_components), X.shape[0], X.shape[1])
    pca = PCA(n_components=n_components)
    X_reduced = pca.fit_transform(X)
    X_denoised = pca.inverse_transform(X_reduced)
    return X_denoised, pca
