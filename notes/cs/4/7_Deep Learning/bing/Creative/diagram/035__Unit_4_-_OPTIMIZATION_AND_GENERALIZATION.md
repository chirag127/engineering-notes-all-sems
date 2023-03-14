## Unit 4 - Optimization and Generalization

The following diagram illustrates the basic architecture of a transductive learning algorithm that includes multi-scale graph neural networks (GNNs) . The algorithm consists of three main components: a feature extractor, a weak learner, and a gradient booster. The feature extractor maps the input graph data to a high-dimensional feature space, where each node is represented by a vector of features. The weak learner is a simple classifier that predicts the labels of the nodes based on their features. The gradient booster is a technique that iteratively improves the weak learner by adding new classifiers that correct the errors of the previous ones. The final prediction is obtained by a weighted combination of the classifiers.

The multi-scale structure of the feature extractor is designed to mitigate the over-smoothing problem of GNNs, which occurs when the node features become indistinguishable after many layers of aggregation. The feature extractor consists of multiple GNN layers, each of which performs a different type of aggregation: local, global, or intermediate. The local aggregation captures the features of the immediate neighbors of each node, the global aggregation captures the features of the entire graph, and the intermediate aggregation captures the features of the nodes at different distances from each node. The feature extractor concatenates the outputs of all the GNN layers to form the final feature vector for each node.

The diagram uses the following symbols:

- G: the input graph data
- X: the node features
- Y: the node labels
- F: the feature extractor
- H: the weak learner
- B: the gradient booster
- Z: the final prediction
- L: the local aggregation
- I: the intermediate aggregation
- R: the global aggregation

The diagram is drawn using ASCII characters as follows:

```
+-----+     +-----+     +-----+     +-----+
|  G  |---->|  F  |---->|  H  |---->|  B  |---->+-----+
+-----+     +-----+     +-----+     +-----+     |  Z  |
                                                 +-----+
                                                   ^
                                                   |
                                                   |
+-----+     +-----+     +-----+     +-----+     +-----+
|  X  |---->|  L  |---->|  I  |---->|  R  |---->|  F  |
+-----+     +-----+     +-----+     +-----+     +-----+
                                                   ^
                                                   |
                                                   |
                                                 +-----+
                                                 |  Y  |
                                                 +-----+
```