from sklearn.metrics import mutual_info_score
import numpy as np

def compute_mutual_info(labels1, labels2):
    return mutual_info_score(labels1, labels2)

def mutual_info_matrix(cluster_labels):
    n = cluster_labels.shape[1]
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = compute_mutual_info(cluster_labels[:, i], cluster_labels[:, j])
    return matrix
