### Backpropagation

- Backpropagation, short for backward propagation of errors, is a widely used method for calculating derivatives inside deep feedforward neural networks.
- Backpropagation forms an important part of a number of supervised learning algorithms for training feedforward neural networks, such as stochastic gradient descent.
- Backpropagation is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to any parameter of the network by propagating the error from the output layer to the input layer .
- Backpropagation identifies which pathways are more influential in the final answer and allows us to strengthen or weaken connections to arrive at a desired prediction.
- Backpropagation is such a fundamental component of deep learning that it will invariably be implemented for you in the package of your choosing.

#### Backpropagation Formula

- Let us consider a multilayer feedforward neural network with N layers.
- The network takes an input vector x and produces an output vector y.
- The network has a set of parameters W, which are the weights and biases of each layer.
- The network has a loss function L, which measures the discrepancy between the output y and the target t.
- The goal of backpropagation is to compute the gradient of L with respect to W, denoted by ∇WL.
- The gradient ∇WL is a vector that has the same dimension as W, and each element of ∇WL is the partial derivative of L with respect to the corresponding element of W.
- The gradient ∇WL tells us how to adjust the parameters W to reduce the loss L.
- The backpropagation algorithm consists of two steps: forward pass and backward pass .

##### Forward Pass

- In the forward pass, we compute the output of each layer of the network, starting from the input layer and ending at the output layer.
- For each layer n, we have an input vector an-1 and an output vector an, where a0 = x and aN = y.
- The output vector an is computed by applying a nonlinear activation function fn to the linear combination of the input vector an-1 and the parameters Wn of the layer, i.e., an = fn(Wnan-1).
- The activation function fn can be different for different layers, and some common choices are sigmoid, tanh, ReLU, softmax, etc.
- The output of the last layer aN is compared with the target t to compute the loss L.

##### Backward Pass

- In the backward pass, we compute the gradient of the loss L with respect to the parameters W of each layer, starting from the output layer and ending at the input layer.
- For each layer n, we have a gradient vector δn, which is the derivative of the loss L with respect to the input of the layer, i.e., δn = ∂L/∂an.
- The gradient vector δn is computed by applying the chain rule of calculus, i.e., δn = ∂L/∂an = (∂L/∂an+1)(∂an+1/∂an).
- The term ∂L/∂an+1 is the gradient vector of the next layer, which is already computed in the previous step of the backward pass.
- The term ∂an+1/∂an is the derivative of the output of the layer with respect to the input of the layer, which can be computed by applying the chain rule again, i.e., ∂an+1/∂an = (∂an+1/∂zn+1)(∂zn+1/∂an).
- The term ∂an+1/∂zn+1 is the derivative of the activation function fn+1, which can be easily computed for common choices of fn+1, such as sigmoid, tanh, ReLU, softmax, etc.
- The term ∂zn+1/∂an is the derivative of the linear combination of the input of the layer and the parameters of the layer, which is simply Wn+1.
- Once we have the gradient vector δn for each layer, we can compute the gradient of the loss L with respect to the parameters Wn of the layer by applying the chain rule again, i.e., ∇WnL = ∂L/∂Wn = (∂L/∂an)(∂an/∂Wn).
- The