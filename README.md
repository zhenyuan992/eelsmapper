# eelsmapper

**eelsmapper** is a data-driven pipeline for analyzing STEM-EELS spectra to perform high-resolution compositional mapping without relying on reference spectra. It integrates PCA, t-SNE, clustering, mutual information, and vector quantization to uncover subtle chemical differences and discover novel material phases.

---

## Purpose

STEM-EELS data is high-dimensional and noisy, making it challenging to interpret with traditional methods. **eelsmapper** offers a robust, modular pipeline for:

- Denoising spectra (PCA)
- Visualizing compositional patterns (t-SNE and/or UMAP)
- Clustering spectra (K-Means)
- Identifying correlated elemental regions (Mutual Information)
- Enhancing signal quality (Vector Quantization)
- Discovering new material phases without needing reference spectra