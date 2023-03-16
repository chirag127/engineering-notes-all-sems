### Semi-Supervised Learning for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Semi-supervised learning is a learning paradigm that combines labeled and unlabeled data to train a model.
- Semi-supervised learning can be useful when labeled data is scarce, expensive, or time-consuming to obtain, but unlabeled data is abundant and cheap.
- Semi-supervised learning can leverage the information from unlabeled data to improve the generalization and robustness of the model, as well as to discover new patterns or categories in the data.
- Semi-supervised learning can be applied to deep neural networks, which are powerful models that can learn complex and high-level features from data.
- Semi-supervised learning with deep neural networks can be categorized into four main approaches:
  - Self-training: The model is first trained on the labeled data, then used to generate pseudo-labels for the unlabeled data, and then re-trained on the combined data.
  - Co-training: The model is split into two or more sub-models, each trained on a different view or representation of the data, and then used to label the unlabeled data for each other.
  - Graph-based methods: The data is represented as a graph, where nodes are samples and edges are similarities or distances, and then label propagation or graph convolutional networks are used to infer the labels of the unlabeled nodes.
  - Generative models: The model is trained to generate realistic samples from the data distribution, and then use the generated samples or the latent variables to regularize or augment the supervised learning objective.
- Some examples of semi-supervised learning with deep neural networks are:
  - Ladder networks: A model that combines a supervised feedforward network with an unsupervised denoising autoencoder, and uses a cost function that minimizes the reconstruction error and the classification error jointly.
  - MixMatch: A model that uses a combination of data augmentation, entropy minimization, consistency regularization, and label guessing to train on batches of labeled and unlabeled data.
  - DeepCluster: A model that alternates between clustering the features learned by a convolutional network and updating the network weights by assigning pseudo-labels based on the cluster assignments.