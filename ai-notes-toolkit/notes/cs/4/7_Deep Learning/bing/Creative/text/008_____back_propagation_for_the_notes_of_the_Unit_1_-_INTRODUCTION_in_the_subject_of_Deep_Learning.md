### Backpropagation

- Backpropagation, short for backward propagation of errors, is a widely used method for calculating derivatives inside deep feedforward neural networks.
- Backpropagation forms an important part of a number of supervised learning algorithms for training feedforward neural networks, such as stochastic gradient descent.
- Backpropagation is based on the chain rule of calculus, which allows us to compute the gradient of a loss function with respect to any parameter of the network by propagating the error from the output layer to the input layer .
- Backpropagation identifies which pathways are more influential in the final answer and allows us to strengthen or weaken connections to arrive at a desired prediction.
- Backpropagation is such a fundamental component of deep learning that it will invariably be implemented for you in the package of your choosing.
- Backpropagation consists of two phases: forward pass and backward pass.
  - In the forward pass, the input data is fed to the network and the output is computed. The output is then compared with the desired output (target) and the error (loss) is calculated.
  - In the backward pass, the error is propagated back through the network, starting from the output layer and ending at the input layer. The weights and biases of each layer are updated according to the gradient of the error with respect to them.
- Backpropagation can be applied to any network architecture that is composed of differentiable functions, such as convolutional neural networks, recurrent neural networks, and transformers.
- Backpropagation is the essence of neural net training. It is the practice of fine-tuning the weights of a neural net based on the error rate (i.e. loss) obtained in the previous epoch (i.e. iteration).
- Proper tuning of the weights ensures lower error rates, making the model reliable by increasing its generalization.