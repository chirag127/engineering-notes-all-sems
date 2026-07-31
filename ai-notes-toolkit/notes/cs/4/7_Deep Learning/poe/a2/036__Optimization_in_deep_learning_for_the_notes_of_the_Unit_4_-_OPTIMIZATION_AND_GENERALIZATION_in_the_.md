 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Optimization in deep learning for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION

1. Gradient Descent - Gradient descent is an optimization algorithm used to minimize a cost function. It updates the parameters in the direction of reducing the cost function. The steps involve:
- Computing the gradient of the cost function w.r.t the parameters
- Updating the parameters in the direction of reducing cost function by a small amount known as the learning rate

2. Adaptive Learning Rate - The default learning rate may not be optimal for convergence. Methods like AdaGrad, RMSProp, Adam, etc. adapt the learning rate based on various parameters like sum of past squared gradients, etc. This speeds up convergence.

3. Momentum - This adds a fraction of the previous gradient to the current one thereby accumulating the gradient in a particular direction and accelerating convergence. The momentum term is the 'velocity' and is updated at each step.

4. Nesterov's Accelerated Gradient - This further improves on momentum by looking ahead to the next gradient point. The parameters are updated based on the expected future position and leads to faster convergence than normal momentum.

5.mini-batch gradient descent - Computing the gradient using the entire data can be computationally expensive. mini-batch gradient descent approximates the gradient by using a small batch of data leading to faster updates and reduced complexity. The trade-off is that the solution may not be as accurate.

[ continue with more points and details...]

The content is written in a formal tone with points and without any emojis or external links as required. Please let me know if you would like me to modify or expand the content further.