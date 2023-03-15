### Gradient descent and the Delta rule

- Gradient descent is a way to find a minimum in a high-dimensional space. You go in direction of the steepest descent.
- The Delta rule is an update rule for single layer perceptrons. It makes use of gradient descent.
- The Delta rule can be derived from the principle of minimizing the mean squared error between the desired output and the actual output of the perceptron.
- The Delta rule can be expressed as:

$$\Delta w_{ij} = \eta (t_i - y_i) x_j$$

where:

  - $\Delta w_{ij}$ is the change in weight from input $j$ to output $i$
  - $\eta$ is the learning rate
  - $t_i$ is the desired output for output $i$
  - $y_i$ is the actual output for output $i$
  - $x_j$ is the input for input $j$

- The Delta rule can be applied iteratively to update the weights until the error is minimized or a stopping criterion is met.
- The Delta rule is important because it provides the basis for the backpropagation algorithm, which can learn networks with multiple hidden layers.