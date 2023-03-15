# Multilayer Perceptron

- A multilayer perceptron (MLP) is a type of artificial neural network (ANN) that consists of multiple layers of neurons connected by weighted links.
- A MLP can learn non-linear functions and complex patterns by using one or more hidden layers between the input and output layers.
- A MLP is a feedforward network, which means that the information flows from the input layer to the output layer without any feedback loops.
- A MLP can be trained using supervised learning algorithms, such as backpropagation, which adjust the weights of the links based on the error between the desired and actual outputs.
- A MLP can be used for various tasks, such as classification, regression, clustering, dimensionality reduction, and feature extraction.

## Structure of a MLP

- A MLP consists of three types of layers: input layer, hidden layer, and output layer.
- The input layer receives the input data, such as images, text, or audio, and passes it to the first hidden layer.
- The hidden layer performs some computation on the input data and transfers the result to the next hidden layer or the output layer.
- The output layer produces the final output of the network, such as labels, scores, or probabilities.
- Each layer consists of one or more neurons, which are the basic units of computation in a MLP.
- Each neuron has a weighted connection to every neuron in the previous and next layer, except for the input and output neurons, which have no connections to other layers.
- Each neuron also has a bias term, which is a constant value that shifts the activation function of the neuron.
- Each neuron computes a linear combination of its inputs and applies a non-linear activation function to produce its output.

## Activation function

- An activation function is a mathematical function that determines the output of a neuron based on its input.
- An activation function introduces non-linearity to the network, which enables it to learn complex functions and patterns.
- Some common activation functions are:

  - Sigmoid: It maps the input to a value between 0 and 1, and has a S-shaped curve. It is often used for binary classification or probability estimation.
  - Tanh: It maps the input to a value between -1 and 1, and has a hyperbolic tangent curve. It is similar to sigmoid, but has a steeper gradient and is centered at zero.
  - ReLU: It maps the input to a value between 0 and the input, and has a rectified linear curve. It is often used for hidden layers, as it is computationally efficient and avoids the vanishing gradient problem.
  - Softmax: It maps the input to a vector of values between 0 and 1, and has a normalized exponential curve. It is often used for multi-class classification, as it produces a probability distribution over the output classes.

## Backpropagation

- Backpropagation is a learning algorithm that adjusts the weights and biases of a MLP based on the error between the desired and actual outputs.
- Backpropagation consists of two phases: forward propagation and backward propagation.
- In forward propagation, the input data is passed through the network layer by layer, and the output of each neuron is computed and stored.
- In backward propagation, the error of the output layer is calculated and propagated back to the previous layers, and the weights and biases of each link are updated according to a learning rule.
- The learning rule is based on the gradient descent method, which minimizes a loss function that measures the difference between the desired and actual outputs.
- The learning rule also depends on a learning rate, which determines the size of the weight updates, and a momentum term, which adds a fraction of the previous weight update to the current one to accelerate the convergence.