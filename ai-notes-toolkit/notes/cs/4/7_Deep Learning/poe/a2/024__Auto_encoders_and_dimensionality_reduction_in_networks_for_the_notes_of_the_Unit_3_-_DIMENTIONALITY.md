 Here is the content in markdown format without any emotions or external links:

### Auto encoders and dimensionality reduction in networks

1. Auto encoders are neural networks that are trained to copy their inputs to their outputs. They are trained to reproduce their inputs.
2. They are composed of two parts:
 - Encoder: Which compresses the input into a latent-space representation.
 - Decoder: Which reconstructs the original input from the latent-space representation.
3. The goal of auto encoders is to learn a compressed representation of the input data, also known as dimensionality reduction. The encoder compresses the input into a lower-dimensional latent space and the decoder reconstructs the original input from this latent space.
4. The latent space can be thought of as a "semantic" space in which semantically similar data points are modeled by nearby points and dissimilar points are modeled by distant points. This enables various applications such as clustering, anomaly detection, etc.
5. There are 3 main types of auto encoders:
 - Sparse auto encoder: Models sparsity in the latent space and activations. Useful for robust representations.
 - Denoising auto encoder: Trained on corrupted inputs, helps learning robust features.
 - Contractive auto encoder: Explicitly minimizes the sensitivity of the latent space to small changes in the input. Produces more robust representations.
6. The dimensionality reduction achieved can be either shallow (features are a non-linear projection of the input) or deep (features are obtained via multiple layers of non-linear transformations).
7. Applications of auto encoders include:
 - Pretraining: Initialize the weights of a network.
 - Feature extraction and dimensionality reduction.
 - Anomaly detection: Reconstructed inputs of anomalies will be of lower quality.
 - Recommender systems: Model user-item interactions.
 - Generation: Generate new data from input data distribution.