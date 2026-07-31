 Here is the content in Markdown format without any emojis or external links:

### Architecture for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of Application of Soft Computing:

1. Introduction to Backpropagation Networks
- A feedforward neural network trained with an algorithm that calculates the gradient of the performance function with respect to the network weights and uses gradient descent to update the weights in the direction that minimizes the performance function.
- Comprises of input layer, one or more hidden layers and an output layer.
- Signals travel in only one direction, forward, from input to output.
- Learning involves propagating backwards from output to input.

2. The Backpropagation Algorithm
- Output layer: Compare actual and target outputs to get errors.
- Hidden layers: Compute errors and assign blame to nodes.
- Update weights: Adjust weights to reduce errors.
- Repeat until error is acceptably small.

3. Steps in Backpropagation
- Feedforward: Compute outputs of all layers.
- Backward pass:
- Output layer: Compute error terms.
- Hidden layers: Compute error terms and weight updates.
- Update weights: Adjust weights to reduce errors.

4. Convergence of Backpropagation
- If the error surface is convex, gradient descent is guaranteed to find a local minimum.
- For non-convex error surfaces, gradient descent can get stuck in local minima.
- Adding momentum or varying the learning rate may help avoid local minima.
- Backpropagation works well in practice for many problems.

The content is written in a formal tone with points and without any emojis or external links as specified. Please let me know if you would like me to modify or add any other content.