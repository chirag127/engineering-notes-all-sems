### Fully Connected Neural Network

- A fully connected neural network is a type of artificial neural network where all the nodes or neurons in one layer are connected to all the neurons in the next layer.
- A fully connected layer is a function from ℝ m to ℝ n that applies a linear transformation to the input vector through a weights matrix.
- The major advantage of fully connected networks is that they are “structure agnostic” i.e. there are no special assumptions about the input data.
- The major disadvantage of fully connected networks is that they are computationally expensive and prone to overfitting due to the large number of parameters.
- Fully connected networks are often used as the final layer of a deep neural network to produce the output vector of labels or scores .
- Fully connected networks can be implemented using matrix multiplication and bias addition, followed by an activation function such as sigmoid, tanh, or ReLU .