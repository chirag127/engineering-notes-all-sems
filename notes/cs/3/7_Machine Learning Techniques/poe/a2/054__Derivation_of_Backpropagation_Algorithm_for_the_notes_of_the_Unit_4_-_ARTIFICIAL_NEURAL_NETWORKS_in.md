 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Derivation of Backpropagation Algorithm

1. Forward propagation: In forward propagation, we calculate the output of each layer based on the inputs and weights. We get the final output of the network.
2. Cost function: We then calculate the cost function which is the error between the predicted output and the actual output. The objective is to minimize the cost function.
3. Backpropagation: In backpropagation, we calculate the gradient of the cost function w.r.t the weights. This is done in the reverse order of forward propagation.
4. Weight update: We then update the weights in the direction of decreasing cost. The weights are updated by subtracting a small value (learning rate) multiplied by the gradients from the weights.
5. Repeat: We repeat steps 1-4 multiple times which is called training the neural network. As we keep updating the weights, the cost function decreases and the model improves.

The key steps in backpropagation are:
1. Calculate the gradient of the cost function w.r.t the output of the last layer
2. Calculate the gradient of the cost function w.r.t the weights of the last layer
3. Repeat the above two steps for the second last layer and so on until we reach the first layer

The derivation involves application of chain rule to calculate the gradients. The goal of backpropagation is to efficiently calculate the gradients which are then used to update the weights and reduce the cost function.

This content should serve as formal study notes for the given topic without any emojis or external links as required. Please let me know if you would like me to modify or expand the content in any way.