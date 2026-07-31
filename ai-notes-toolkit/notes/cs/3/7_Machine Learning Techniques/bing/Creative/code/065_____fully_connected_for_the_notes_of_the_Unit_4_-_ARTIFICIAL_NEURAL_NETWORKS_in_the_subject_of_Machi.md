# Fully Connected Neural Network

- A fully connected neural network consists of a series of fully connected layers that connect every neuron in one layer to every neuron in another layer .
- A fully connected layer is a function from ℝ m to ℝ n that applies a linear transformation to the input vector through a weights matrix.
- The output of a fully connected layer is given by: y = Wx + b, where W is the weights matrix, x is the input vector, b is the bias vector, and y is the output vector.
- The major advantage of fully connected networks is that they are “structure agnostic” i.e. there are no special assumptions about the input data, such as spatial or temporal relationships.
- The major disadvantage of fully connected networks is that they are prone to overfitting, especially when the input dimension is large, as they have a lot of parameters to learn.
- Fully connected networks are often used as the final layer of a convolutional neural network (CNN) to perform classification, after the convolutional and pooling layers have extracted features from the input images .