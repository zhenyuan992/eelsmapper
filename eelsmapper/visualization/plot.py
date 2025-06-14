import matplotlib.pyplot as plt

def plot_tsne(X_embedded, labels):
    plt.scatter(X_embedded[:,0], X_embedded[:,1], c=labels, cmap='viridis', s=5)
    plt.title("t-SNE Clustering")
    plt.show()
