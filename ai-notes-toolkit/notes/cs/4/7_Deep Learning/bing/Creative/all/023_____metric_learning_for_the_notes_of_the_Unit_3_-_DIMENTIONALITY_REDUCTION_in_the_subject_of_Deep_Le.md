# Metric Learning

Metric learning is a branch of machine learning that aims to learn a distance function or a similarity measure between data points. Metric learning can be useful for tasks such as clustering, classification, retrieval, ranking, and recommendation.

## Deep Metric Learning

Deep metric learning is a subfield of metric learning that leverages deep neural networks to learn nonlinear and high-dimensional feature representations and distance functions. Deep metric learning can benefit from the advantages of both deep learning and metric learning, such as the ability to learn from raw data, handle complex patterns, and enhance the discrimination power of the learned features.

## Methods of Deep Metric Learning

There are various methods of deep metric learning, which can be categorized based on the type of supervision, the type of network architecture, and the type of loss function.

### Supervision

Depending on the type of supervision available for the training data, deep metric learning methods can be divided into:

- Supervised learning: the algorithm has access to a set of data points, each of them belonging to a class (label) as in a standard classification problem.
- Semi-supervised learning: the algorithm has access to a set of labeled data points and a larger set of unlabeled data points, and tries to leverage the information from both sets to learn a better distance function.
- Unsupervised learning: the algorithm has no access to any label information, and tries to learn a distance function that captures the intrinsic structure or distribution of the data.
- Weakly supervised learning: the algorithm has access to some weak or noisy label information, such as pairwise or triplet constraints, relative comparisons, or ranking orders.

### Network Architecture

Depending on the type of network architecture used to learn the feature representations and the distance function, deep metric learning methods can be divided into:

- Single network: the algorithm uses a single deep neural network to map the input data points to a feature space, and then computes the distance between the features using a predefined or learned metric, such as Euclidean distance, cosine similarity, or Mahalanobis distance.
- Siamese network: the algorithm uses two identical deep neural networks with shared weights to map two input data points to a feature space, and then computes the distance between the features using a predefined or learned metric.
- Triplet network: the algorithm uses three identical deep neural networks with shared weights to map three input data points (an anchor, a positive, and a negative) to a feature space, and then computes the distance between the features using a predefined or learned metric.
- Quadruplet network: the algorithm uses four identical deep neural networks with shared weights to map four input data points (an anchor, a positive, a negative, and a negative of a different class) to a feature space, and then computes the distance between the features using a predefined or learned metric.
- Autoencoder: the algorithm uses a deep neural network with an encoder and a decoder to map the input data points to a feature space, and then reconstructs the input data points from the features using a predefined or learned metric.

### Loss Function

Depending on the type of loss function used to optimize the feature representations and the distance function, deep metric learning methods can be divided into:

- Contrastive loss: the algorithm tries to minimize the distance between similar data points and maximize the distance between dissimilar data points, using a margin-based hinge loss.
- Triplet loss: the algorithm tries to minimize the distance between an anchor and a positive data point and maximize the distance between an anchor and a negative data point, using a margin-based hinge loss.
- Quadruplet loss: the algorithm tries to minimize the distance between an anchor and a positive data point and maximize the distance between an anchor and a negative data point, as well as the distance between a negative data point and a negative data point of a different class, using a margin-based hinge loss.
- Lifted structured loss: the algorithm tries to minimize the distance between similar data points and maximize the distance between dissimilar data points, using a softmax-based loss that considers all possible pairs within a mini-batch.
- N-pair loss: the algorithm tries to minimize the distance between an anchor and a positive data point and maximize the distance between an anchor and N negative data points, using a softmax-based loss that considers all possible N-pairs within a mini-batch.
- Proxy-NCA loss: the algorithm tries to minimize the distance between a data point and a proxy (a learnable vector) that represents its class, and maximize the distance between a data point and other proxies