### Derivation of Backpropagation Algorithm 

#### Introduction
- Backpropagation is an algorithm used for supervised learning of artificial neural networks.
- It is used to train the weights of a neural network in order to minimize the error between the predicted output and the actual output.
- In this section, we will discuss the derivation of the backpropagation algorithm.

#### Forward Pass
- In the forward pass, the input is propagated through the neural network to produce the output.
- Each neuron in the network receives input from the previous layer and applies an activation function to produce its output.
- The output of the last layer is the predicted output.

#### Backward Pass
- In the backward pass, the error between the predicted output and the actual output is propagated backwards through the network.
- The error is used to calculate the gradient of the cost function with respect to the weights of the network.
- The weights are then updated using the gradient descent algorithm.

#### Derivation of the Gradient
- The gradient of the cost function with respect to the weights of the network is calculated using the chain rule.
- The chain rule is applied recursively to calculate the gradients for each layer in the network.
- The gradient for a particular weight is the product of the following:
    - The error at the output of the network.
    - The derivative of the activation function at the output of the neuron.
    - The output of the neuron in the previous layer.

#### Weight Update
- Once the gradient of the cost function with respect to the weights has been calculated, the weights are updated using the gradient descent algorithm.
- The gradient descent algorithm involves subtracting a fraction of the gradient from the current weight.
- The fraction is known as the learning rate and determines how quickly the weights are updated.

#### Conclusion
- Backpropagation is a widely used algorithm for training artificial neural networks.
- It involves a forward pass, where input is propagated through the network to produce output, and a backward pass, where the error is propagated backwards through the network to update the weights.
- The gradient of the cost function with respect to the weights is calculated using the chain rule, and the weights are updated using the gradient descent algorithm.