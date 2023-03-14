 Here is the content in markdown format for the topic ### back propagation for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Backpropagation

Backpropagation is a method used in training artificial neural networks for supervised learning. It involves calculating the gradient of the loss function with respect to the weights of the network.

- The goal of backpropagation is to find the weights that minimize the loss function.
- It calculates the gradient of the loss with respect to the weights by propagating backwards through the network.
- It uses the chain rule to calculate the gradients.
- The weights are updated in the direction of the negative gradient, which causes the loss to decrease.

**Mnemonics:**

- Backpropagation goes backwards, updating weights to reduce loss
- Chain rule is used to calculate gradients for each layer
- Weights are updated in the negative gradient direction

**Advantages:**

- Simple and efficient algorithm for training neural networks
- Capable of learning complex nonlinear relationships
- Converges to a local minimum of the loss function

**Disadvantages:**

- Convergence is not guaranteed and depends on hyperparameters and initialization
- May get stuck in local minima and not find the global minimum
- Requires calculating gradients, which can be computationally expensive for deep networks

**Example:**

A 3-layer neural network is trained on a dataset using backpropagation. The loss is calculated at the output layer and gradients are propagated back to the input layer, updating the weights to reduce the loss. This process is repeated over multiple epochs until the loss is sufficiently low.

**Applications:**

- Image classification
- Speech recognition
- Machine translation
- Time series forecasting
- Robot control
- And many other supervised learning tasks