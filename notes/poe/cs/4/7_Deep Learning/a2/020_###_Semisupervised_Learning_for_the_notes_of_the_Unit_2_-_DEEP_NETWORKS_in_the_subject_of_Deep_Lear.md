 Here is the content in markdown format for the topic ### Semi-supervised Learning for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning:

### Semi-supervised Learning

- Semi-supervised learning is a type of machine learning technique that makes use of both labeled and unlabeled data for training a model.
- It is used when labeled data is limited but unlabeled data is abundant.
- The goal is to improve the learning accuracy by using the unlabeled data in addition to the labeled data.
- Some of the popular approaches for semi-supervised learning are:
  - Self-Training: The model is first trained on the labeled data. The predictions on the unlabeled data are then used to automatically label them. The model is then re-trained on the combined labeled and "auto-labeled" data. This process can be repeated.
  - Transductive SVMs: A support vector machine is trained considering both labeled and unlabeled data. The decision boundary is positioned to separate the labeled data and minimize errors on the unlabeled data.
  - Graph-based methods: Data points are represented as nodes in a graph. Similar data points are connected. Label information is propagated through the graph to predict labels for unlabeled data.
- Advantages: Improves accuracy when limited labeled data is available. Utilizes abundant unlabeled data.
- Disadvantages: Incorrect auto-labeling can reduce accuracy. Does not always outperform supervised learning with limited labeled data.
- Applications: Sentiment analysis, image classification, recommendation systems, etc.

Some mnemonics for remembering semi-supervised learning:

- "Semi" means half - uses half labeled (supervised) and half unlabeled (unsupervised) data
- "Self-training" - model trains itself on auto-labeled data in addition to original labeled data
- "Graphs connect the dots" - graph-based methods connect similar data points and propagate labels

Hope this helps! Let me know if you would like me to elaborate on any of the points or add more details.