 Here is the content in markdown format for the topic ### Semi-supervised Learning for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning:

### Semi-supervised Learning

- Semi-supervised learning uses both labeled and unlabeled data for training a machine learning model.
- It is used when labeled data is limited and unlabeled data is abundant.
- The goal is to use the unlabeled data to improve the learning accuracy.
- Some approaches for semi-supervised learning are:

#### Self-Training
- Initial model is trained on labeled data
- Model predicts labels for unlabeled data
- Add most confident predictions to the training data
- Retrain the model on updated training data
- Repeat steps 3 and 4 until stopping criterion is met

**Mnemonic:** Model trains itself by using its own predictions.

#### Transductive SVMs
- Initial model is trained on labeled data
- Define a loss function over both labeled and unlabeled data
- Optimize the loss function to find the decision boundary

**Pros:** Can handle non-linear decision boundaries, handles multiple classes
**Cons:** Does not scale well to large data sets

#### Graph-based Methods
- Construct a graph where nodes are data points and edges represent similarity
- Assign initial labels to nodes based on labeled data
- Propagate label information through the graph
- Refine labels based on propagation

**Pros:** Can utilize cluster structure in data, handles non-linearities
**Cons:** Choice of graph model and propagation strategy is difficult

[Detailed diagrams and examples can be added here if required...]

Applications of semi-supervised learning include:
- Image classification with limited labeled data
- Anomaly detection
- Recommendation systems

Advantages over supervised learning:
- Utilizes abundant unlabeled data
- Can improve accuracy if unlabeled data provides useful information

Disadvantages:
- Require careful choice of approach and tuning
- May not always outperform supervised learning