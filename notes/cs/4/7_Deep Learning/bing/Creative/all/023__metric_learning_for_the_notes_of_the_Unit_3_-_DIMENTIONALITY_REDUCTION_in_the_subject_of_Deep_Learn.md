### Metric learning for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- Metric learning is a branch of machine learning that aims to learn a distance function that can measure the similarity or dissimilarity between data points .
- Metric learning can be useful for tasks such as k-NN classification, clustering, information retrieval, face recognition, image retrieval, etc .
- Metric learning can be divided into two main categories depending on the type of supervision available: supervised and weakly supervised.
  - Supervised metric learning: the algorithm has access to a set of data points, each of them belonging to a class (label). The goal is to learn a distance metric that puts points with the same label close together while pushing away points with different labels.
  - Weakly supervised metric learning: the algorithm has access to a set of data points with supervision only at the tuple level (typically pairs, triplets, or quadruplets of data points). The goal is to learn a distance metric that puts positive pairs close together and negative pairs far away.
- In metric-learn, all algorithms currently implemented learn so-called Mahalanobis distances, which are defined as follows:

  ```
  D(x, x') = (Lx - Lx')^T (Lx - Lx')
  ```

  where L is a real-valued parameter matrix of shape (num_dims, n_features) and x and x' are data points. A Mahalanobis distance is a Euclidean distance after a linear transformation of the feature space defined by L. Mahalanobis distance metric learning can thus be seen as learning a new embedding space of dimension num_dims.
- In deep metric learning, the parameter matrix L is replaced by a neural network that can learn nonlinear transformations of the feature space. The neural network is trained with a loss function that encourages the desired distance properties between the data points .
- Some examples of loss functions for deep metric learning are:
  - Contrastive loss: a pairwise loss that penalizes large distances between positive pairs and small distances between negative pairs .
  - Triplet loss: a triplet-wise loss that penalizes large distances between an anchor point and a positive point, and small distances between an anchor point and a negative point .
  - N-pair loss: a tuple-wise loss that penalizes large distances between an anchor point and a positive point, and small distances between an anchor point and any of the N-1 negative points in a minibatch.
  - Angular loss: a tuple-wise loss that penalizes large angles between an anchor point, a positive point, and a negative point.
  - Lifted structured loss: a set-wise loss that penalizes large distances between positive pairs and small distances between negative pairs within a minibatch.
- Some advantages of deep metric learning are:
  - It can learn from raw data without the need for feature engineering or preprocessing.
  - It can learn nonlinear and complex distance functions that capture the intrinsic structure of the data.
  - It can handle high-dimensional and heterogeneous data.
- Some disadvantages of deep metric learning are:
  - It requires a large amount of data and computational resources to train the neural network.
  - It can suffer from overfitting and poor generalization if the data is noisy or imbalanced.
  - It can be sensitive to the choice of the loss function, the network architecture, and the hyperparameters.
- Some applications of deep metric learning are:
  - Face recognition: learning a distance function that can identify faces from different angles, expressions, and lighting conditions.
  - Image retrieval: learning a distance function that can retrieve similar images from a large database based on visual content.
  - Recommender systems: learning a distance function that can measure the similarity between users and items based on their preferences and behavior.

: [2201.09267] Spectral, Probabilistic, and Deep Metric Learning: Tutorial and Survey
: 1. What is Metric Learning? — metric-learn 0.6.2 documentation
: A Beginners Guide to Deep Metric Learning - Analytics India Magazine