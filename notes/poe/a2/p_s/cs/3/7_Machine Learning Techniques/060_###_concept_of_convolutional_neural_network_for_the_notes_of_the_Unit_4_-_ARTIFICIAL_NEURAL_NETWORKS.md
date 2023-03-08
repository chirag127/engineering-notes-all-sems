 Here is the content in markdown format for the topic ### Concept of Convolutional Neural Network:

Convolutional Neural Network (CNN) is a type of feed-forward artificial neural network in which the connectivity pattern between its neurons is inspired by the organization of the animal visual cortex. The core concept of CNN is convolution.

#### What is Convolution?
Convolution is a mathematical operation on two functions that produces a third function that describes how the shape of one is modified by the other. In CNN, convolution is applied between the input and a filter (kernel) to produce a feature map. Multiple filters are slid over the input and produce multiple feature maps.

#### Architecture of CNN
A typical CNN architecture contains multiple layers as below:
1. Convolutional Layer - This layer contains convolutional filters that perform convolution operation on the input and produce feature maps. Multiple filters are applied to get multiple features.
2. Pooling Layer - This layer performs downsampling operation along the spatial dimensions (width and height) of the input. It helps in reducing the dimensionality and capturing the dominant features. Common pooling types are max pooling and average pooling.
3. Fully Connected Layer - This layer flattens the feature maps and feeds them into a regular neural network. It helps in final classification.
4. Activation Function - This function adds non-linearity to the network. Common choices are ReLU, Sigmoid, Tanh, etc.

#### Advantages of CNN
- Hierarchical feature extraction - CNN automatically extracts hierarchical features from the input leading to better representations.
- Sharing of weights - CNN uses tied weights that are shared across the spatial dimensions leading to reduction in parameters.
- Invariance to translations - CNN develops invariant features to small translations / distortions in the input.
- Hardware efficiency - CNN can be implemented efficiently on parallel hardware like GPUs due to extensive parameter sharing and sparse connectivity.

CNN has achieved significant success in various computer vision tasks like image classification, object detection, semantic segmentation, etc. due to its strong capabilities of hierarchical feature extraction and invariance properties.