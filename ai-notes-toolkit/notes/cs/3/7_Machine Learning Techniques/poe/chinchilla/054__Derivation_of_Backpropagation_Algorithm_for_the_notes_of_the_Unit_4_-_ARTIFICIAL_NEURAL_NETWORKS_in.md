### Derivation of Backpropagation Algorithm for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques.

Backpropagation is a widely used algorithm in training artificial neural networks. It is a supervised learning algorithm for training multi-layer neural networks. In this algorithm, the gradients of the error with respect to the weights are computed and used to update the weights. The following are the steps involved in the derivation of the backpropagation algorithm:

1. Forward Propagation: The input is fed into the network, and the output is computed by propagating through the layers of the network. Each layer applies a linear transformation to the input followed by a non-linear activation function. The output of the last layer is the predicted output of the network.

2. Error Computation: The error between the predicted output and the actual output is computed using a loss function. The loss function measures the difference between the predicted output and the actual output.

3. Backward Propagation: The gradients of the error with respect to the weights are computed using the chain rule. The chain rule is used to propagate the error back through the layers of the network. The partial derivatives of the error with respect to the output of each layer are computed, and the gradients of the weights are computed by multiplying the output of the previous layer with the partial derivative of the error with respect to the output of the current layer.

4. Weight Update: The weights are updated using the computed gradients. The weights are updated in the opposite direction of the computed gradients to minimize the error. The learning rate is used to control the step size of the weight update.

5. Repeat: Steps 1-4 are repeated for multiple iterations until the error is minimized.

In summary, the backpropagation algorithm is a supervised learning algorithm for training neural networks. It involves forward propagation to compute the output and backward propagation to compute the gradients of the error with respect to the weights. The weights are updated using the computed gradients to minimize the error. The algorithm is repeated for multiple iterations until the error is minimized.