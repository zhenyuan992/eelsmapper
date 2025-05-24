from sklearn.manifold import TSNE

def tsne_embed(X, n_components=2, perplexity=30, random_state=0):
    tsne = TSNE(n_components=n_components, perplexity=perplexity, random_state=random_state)
    X_embedded = tsne.fit_transform(X)
    return X_embedded
