Metric learning is a branch of deep learning that aims to learn a similarity metric that can measure the distance between data points in a feature space. Metric learning can be used for tasks such as face recognition, person re-identification, semantic textual similarity, etc.

One way to implement metric learning is to use a siamese network, which consists of two identical sub-networks that share the same weights and parameters. The siamese network takes two input data points and outputs a similarity score between them. The network is trained with a contrastive loss function, which encourages the network to output high similarity scores for data points that belong to the same class, and low similarity scores for data points that belong to different classes.

The following diagram illustrates the basic architecture of a siamese network for metric learning:

```
+-----------------+     +-----------------+
| Input data point|     | Input data point|
+-----------------+     +-----------------+
         |                       |
         |                       |
         v                       v
+-----------------+     +-----------------+
| Sub-network 1   |     | Sub-network 2   |
| (shared weights)|     | (shared weights)|
+-----------------+     +-----------------+
         |                       |
         |                       |
         v                       v
+-----------------+     +-----------------+
| Feature vector  |     | Feature vector  |
+-----------------+     +-----------------+
         |                       |
         |                       |
         v                       v
+-----------------+     +-----------------+
| Similarity score|<----| Similarity score|
+-----------------+     +-----------------+
         |                       |
         |                       |
         v                       v
+-----------------+     +-----------------+
| Contrastive loss|<----| Contrastive loss|
+-----------------+     +-----------------+
```