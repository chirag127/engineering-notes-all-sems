### Back Propagation Algorithm

Back propagation is a widely used algorithm for training artificial neural networks. It is a supervised learning algorithm that uses gradient descent optimization to minimize the error between the predicted output and the actual output.

The back propagation algorithm involves the following steps:

1. Initialize the weights and biases of the neural network randomly.
2. Forward propagate the input through the network to obtain the predicted output.
3. Calculate the error between the predicted output and the actual output.
4. Backward propagate the error through the network to update the weights and biases.
5. Repeat steps 2-4 for a number of epochs or until the error is minimized.

The back propagation algorithm uses the chain rule of calculus to calculate the gradients of the error with respect to the weights and biases of the network. The gradients are then used to update the weights and biases in the opposite direction of the gradient.

The back propagation algorithm has several variants, including batch, mini-batch, and stochastic gradient descent. Batch gradient descent updates the weights and biases after processing the entire training set, while mini-batch gradient descent updates the weights and biases after processing a small subset of the training set. Stochastic gradient descent updates the weights and biases after processing a single training example.

The back propagation algorithm has several limitations, including the possibility of getting stuck in local minima and the sensitivity to the initial weights and biases. To overcome these limitations, various modifications have been proposed, including momentum, weight decay, and adaptive learning rate.

In summary, the back propagation algorithm is a powerful and widely used algorithm for training artificial neural networks. It involves initializing the weights and biases randomly, forward propagating the input through the network, calculating the error, and backward propagating the error to update the weights and biases. The algorithm has several variants and limitations, which can be overcome by using modifications such as momentum and weight decay.