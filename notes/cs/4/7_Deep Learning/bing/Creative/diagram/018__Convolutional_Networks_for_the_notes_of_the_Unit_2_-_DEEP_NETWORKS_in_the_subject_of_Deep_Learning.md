A convolutional neural network (CNN) is a type of artificial neural network that can process data with a grid-like structure, such as images. A CNN consists of an input layer, one or more hidden layers, and an output layer. The hidden layers typically include convolutional layers, pooling layers, and fully connected layers. The convolutional layers apply filters to the input data and produce feature maps that capture the spatial information of the data. The pooling layers reduce the dimensionality of the feature maps and introduce some invariance to translation. The fully connected layers perform the classification task based on the extracted features.

The following diagram illustrates the basic architecture of a CNN:

```
Input layer
    |
    v
Convolutional layer 1
    |
    v
Pooling layer 1
    |
    v
Convolutional layer 2
    |
    v
Pooling layer 2
    |
    v
Fully connected layer 1
    |
    v
Fully connected layer 2
    |
    v
Output layer
```

Each layer can have multiple channels or filters, which are represented by the depth of the layer. For example, the input layer can have three channels for red, green, and blue colors of an image. The convolutional layer can have multiple filters that produce different feature maps. The pooling layer can have the same number of channels as the previous convolutional layer. The fully connected layer can have a variable number of neurons depending on the desired output size. The output layer can have one neuron for binary classification, or multiple neurons for multi-class classification.