### Backpropagation

Backpropagation is a supervised learning algorithm for training multi-layer feedforward neural networks . It is a widely used method for calculating derivatives inside deep neural networks. It forms an important part of a number of supervised learning algorithms, such as stochastic gradient descent.

Backpropagation is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to any parameter of the network by propagating the error backwards from the output layer to the input layer . Backpropagation identifies which pathways are more influential in the final answer and allows us to strengthen or weaken connections to arrive at a desired prediction.

Backpropagation consists of two phases: forward propagation and backward propagation .

- In forward propagation, the input data is passed through the network layer by layer, and the output of each layer is computed by applying an activation function to the weighted sum of the inputs. The final output of the network is compared with the desired output (target) to calculate the loss function .
- In backward propagation, the loss function is differentiated with respect to each parameter of the network (weights and biases) using the chain rule. The resulting gradients are used to update the parameters in the opposite direction of the gradient, i.e., to reduce the loss. The process is repeated until the loss is minimized or a convergence criterion is met .

Backpropagation is the key to supervised learning of deep neural networks and has enabled the recent surge in popularity of deep learning algorithms since the early 2000s. It is such a fundamental component of deep learning that it will invariably be implemented for you in the package of your choosing.