### Concept of Convolution for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- Convolution is a mathematical operation that combines two functions to produce a third function that expresses how one function is modified by the other.
- In artificial neural networks, convolution is used to extract features from input data, such as images, speech, or audio signals  .
- Convolutional neural networks (CNNs) are a specialized type of artificial neural networks that use convolution in place of general matrix multiplication in at least one of their layers.
- CNNs are designed to process pixel data and are used in image recognition and processing.
- The architecture of a CNN is a multi-layered feed-forward neural network, made by stacking many hidden layers on top of each other in sequence.
- It is this sequential design that allows CNNs to learn hierarchical features, from low-level to high-level, from the input data.
- A CNN consists of three main types of layers: convolutional layer, pooling layer, and fully-connected layer.
- The convolutional layer is the first layer of a CNN, where the input data is convolved with a set of learnable filters or kernels, each producing a feature map .
- The pooling layer is used to reduce the spatial dimensions of the feature maps, by applying a downsampling operation, such as max pooling or average pooling .
- The fully-connected layer is the last layer of a CNN, where the flattened feature maps are fed into a standard neural network, which performs the final classification or regression task .
- A simple example of a CNN architecture for image classification is shown below:

![CNN architecture](https://upload.wikimedia.org/wikipedia/commons/6/63/Typical_cnn.png)

: Convolutional Neural Network Definition | DeepAI
: Convolutional neural network - Wikipedia
: Convolutional Neural Network - NVIDIA Data Science Glossary