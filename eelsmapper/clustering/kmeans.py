from sklearn.cluster import KMeans

def kmeans_cluster(X, n_clusters=5, random_state=0):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    labels = kmeans.fit_predict(X)
    return labels, kmeans
