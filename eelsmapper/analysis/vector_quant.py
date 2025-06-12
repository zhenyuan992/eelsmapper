import numpy as np

def vector_quantization(X, n_clusters=5, random_state=0):
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    Xq = kmeans.fit_predict(X)
    centroids = kmeans.cluster_centers_
    Xvq = centroids[Xq]
    return Xvq, kmeans
