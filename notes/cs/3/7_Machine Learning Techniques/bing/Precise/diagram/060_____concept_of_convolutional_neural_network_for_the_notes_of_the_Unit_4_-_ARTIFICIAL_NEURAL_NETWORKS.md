### Concept of Convolutional Neural Network

A convolutional neural network (CNN) is a type of artificial neural network commonly used in image recognition and processing tasks. It is designed to take in input data in the form of images and process the data through multiple layers, each of which applies a different set of filters to the data to extract different features.

The architecture of a CNN is designed to take advantage of the 2D structure of an input image. This is achieved with local connections and tied weights followed by some form of pooling which results in translation invariant features. Another benefit of CNNs is that they are easier to train and have many fewer parameters than fully connected networks with the same number of hidden units.

The basic architecture of a CNN consists of an input layer, multiple hidden layers, and an output layer. The hidden layers typically consist of convolutional layers, ReLU layers, pooling layers, and fully connected layers.

1. **Convolutional Layer:** The convolutional layer is the core building block of a CNN. The layer's parameters consist of a set of learnable filters, which have a small receptive field, but extend through the full depth of the input volume. During the forward pass, each filter is convolved across the width and height of the input volume, computing the dot product between the entries of the filter and the input and producing a 2-dimensional activation map of that filter. As a result, the network learns filters that activate when it detects some specific type of feature at some spatial position in the input.

2. **ReLU Layer:** The ReLU layer applies the non-saturating activation function f(x)=max(0,x). It increases the nonlinear properties of the decision function and of the overall network without affecting the receptive fields of the convolution layer.

3. **Pooling Layer:** The pooling layer is used to reduce the spatial size of the representation, to reduce the number of parameters, memory footprint and amount of computation in the network, and hence to also control overfitting. The most common form is a pooling layer with filters of size 2x2 applied with a stride of 2 downsamples at every depth slice in the input by 2 along both width and height, discarding 75% of the activations.

4. **Fully Connected Layer:** The fully connected layer is a traditional multi-layer perceptron that uses a softmax activation function in the output layer. The term “Fully Connected” implies that every neuron in the previous layer is connected to every neuron on the next layer.

In summary, a CNN is a powerful neural network that is able to extract and learn features from images through the use of convolutional and pooling layers, followed by fully connected layers that can classify the image based on the learned features. It is widely used in image recognition and processing tasks and has achieved state-of-the-art performance in many applications.