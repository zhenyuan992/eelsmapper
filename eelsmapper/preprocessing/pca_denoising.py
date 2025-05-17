import numpy as np
from sklearn.decomposition import PCA

def pca_denoise(X, n_components=10):
    pca = PCA(n_components=n_components)
    X_reduced = pca.fit_transform(X)
    X_denoised = pca.inverse_transform(X_reduced)
    return X_denoised, pca
