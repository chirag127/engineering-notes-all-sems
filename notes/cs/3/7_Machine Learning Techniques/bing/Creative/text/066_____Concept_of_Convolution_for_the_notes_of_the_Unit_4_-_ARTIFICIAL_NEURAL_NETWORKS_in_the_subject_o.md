### Concept of Convolution for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- Convolution is a mathematical operation that combines two functions to produce a third function that expresses how one function is modified by the other.
- Convolution is used in artificial neural networks to extract features from input data, such as images, speech, or audio signals  .
- Convolutional neural networks (CNNs) are a specialized type of artificial neural networks that use convolution in place of general matrix multiplication in at least one of their layers.
- CNNs are designed to process pixel data and are used in image recognition and processing.
- The architecture of a CNN is a multi-layered feed-forward neural network, made by stacking many hidden layers on top of each other in sequence.
- It is this sequential design that allows CNNs to learn hierarchical features, from low-level to high-level, from the input data.
- CNNs have three main types of layers, which are:
  - Convolutional layer: This layer applies a set of filters to the input data, each filter producing a feature map that captures some aspect of the data.
  - Pooling layer: This layer reduces the size of the feature maps by applying a downsampling operation, such as max pooling or average pooling, to improve computational efficiency and reduce overfitting.
  - Fully-connected layer: This layer connects every neuron in the previous layer to every neuron in the next layer, and performs the final classification or regression task.
- CNNs can have multiple convolutional and pooling layers, followed by one or more fully-connected layers at the end .
- CNNs can also have other types of layers, such as batch normalization, dropout, or activation layers, to improve the performance and stability of the network .