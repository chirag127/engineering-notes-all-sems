# Metric Learning

Metric learning is a branch of machine learning that aims to learn a distance function or a similarity measure between data points. The goal is to make similar data points closer and dissimilar data points farther in a metric space. Metric learning can be useful for tasks such as clustering, classification, retrieval, ranking, and recommendation.

## Deep Metric Learning

Deep metric learning is a subfield of metric learning that leverages deep neural networks to learn nonlinear and high-dimensional feature representations and distance functions. Deep metric learning can benefit from the advantages of deep learning, such as end-to-end learning, scalability, and generalization, as well as the advantages of metric learning, such as discrimination, robustness, and interpretability.

## Types of Deep Metric Learning

Depending on the type of supervision available, deep metric learning can be categorized into three types:

- Supervised deep metric learning: the algorithm has access to a set of data points, each of them belonging to a class (label) as in a standard classification problem. The objective is to learn a distance function that minimizes the intra-class distance and maximizes the inter-class distance. Examples of supervised deep metric learning methods are contrastive loss, triplet loss, and deep discriminant analysis.

- Semi-supervised deep metric learning: the algorithm has access to a set of labeled data points and a set of unlabeled data points. The objective is to leverage both types of data to learn a distance function that can generalize well to new data. Examples of semi-supervised deep metric learning methods are self-training, co-training, and graph-based methods.

- Unsupervised deep metric learning: the algorithm has access to a set of unlabeled data points. The objective is to learn a distance function that captures the intrinsic structure and diversity of the data. Examples of unsupervised deep metric learning methods are autoencoders, generative adversarial networks, and self-supervised methods.