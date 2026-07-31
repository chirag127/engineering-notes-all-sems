# Backpropagation

- Backpropagation is a supervised learning algorithm for training multi-layer feedforward neural networks .
- It is a widely used method for calculating derivatives inside deep neural networks.
- It forms an important part of a number of supervised learning algorithms, such as stochastic gradient descent.
- It is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to any parameter of the network .
- It consists of two phases: forward propagation and backward propagation .
- In forward propagation, the input data is passed through the network layer by layer, and the output is compared with the target value to compute the loss .
- In backward propagation, the loss is propagated back through the network, and the weights are updated according to the gradient of the loss with respect to each weight .
- Backpropagation identifies which pathways are more influential in the final output and allows us to strengthen or weaken connections to arrive at a desired prediction.
- It is such a fundamental component of deep learning that it will invariably be implemented for you in the package of your choosing.
- Backpropagation is the essence of neural net training, as it ensures lower error rates and higher generalization.