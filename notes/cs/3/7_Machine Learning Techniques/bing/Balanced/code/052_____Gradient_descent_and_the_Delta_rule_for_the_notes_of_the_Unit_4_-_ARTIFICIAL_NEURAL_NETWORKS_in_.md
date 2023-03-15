### Gradient descent and the Delta rule

- Gradient descent is a way to find a minimum in a high-dimensional space. You go in direction of the steepest descent.
- The Delta rule is an update rule for single layer perceptrons. It makes use of gradient descent.
- The key idea behind the Delta rule is to use gradient descent to search the hypothesis space of possible weight vectors to find the weights that best fit the training examples.
- The Delta rule is important because gradient descent provides the basis for the BACKPROPAGATON algorithm, which can learn networks with many interconnected units.
- The Delta rule can be derived from the gradient descent algorithm by applying the chain rule of calculus to the error function and the activation function of the perceptron .
- The Delta rule can be expressed as:

$$\Delta w_{ij} = \eta (t_i - o_i) x_j$$

where $\Delta w_{ij}$ is the change in the weight from input $x_j$ to output $o_i$, $\eta$ is the learning rate, $t_i$ is the target output, and $o_i$ is the actual output .
- The Delta rule can be applied to both linear and nonlinear activation functions, such as the sigmoid function .
- The Delta rule can be generalized to multilayer networks using the BACKPROPAGATION algorithm, which propagates the error from the output layer to the hidden layers and updates the weights accordingly .