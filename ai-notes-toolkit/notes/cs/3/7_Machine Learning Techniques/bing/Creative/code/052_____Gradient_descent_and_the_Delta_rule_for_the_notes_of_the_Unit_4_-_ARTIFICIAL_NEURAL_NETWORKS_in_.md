### Gradient descent and the Delta rule

- Gradient descent is a way to find a minimum in a high-dimensional space. You go in direction of the steepest descent.
- The Delta rule is an update rule for single layer perceptrons. It makes use of gradient descent.
- The Delta rule's main idea is to explore the hypothesis space of potential weight vectors using gradient descent to discover the weights that best suit the training instances.
- The Delta rule is derived from the gradient of the mean squared error function with respect to the weights.
- The Delta rule can be expressed as:

$$\Delta w_{ij} = \eta (t_i - o_i) x_j$$

where $\Delta w_{ij}$ is the change in weight from input $j$ to output $i$, $\eta$ is the learning rate, $t_i$ is the target output, $o_i$ is the actual output, and $x_j$ is the input value.

- The Delta rule can be applied in batch mode or online mode. In batch mode, the weight updates are accumulated over all the training examples and applied at the end of an epoch. In online mode, the weight updates are applied after each training example.
- The Delta rule can be extended to multi-layer perceptrons using the backpropagation algorithm, which propagates the errors from the output layer to the hidden layers and updates the weights accordingly.