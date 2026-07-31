### Back Propagation Algorithm

Back Propagation is a supervised learning algorithm used for training Artificial Neural Networks. It is a method to update the weights of the neural network based on the error obtained in the output. The algorithm is used to minimize the cost function by adjusting the weights of the network in the direction of the negative gradient of the cost function with respect to the weights.

The steps involved in the Back Propagation algorithm are as follows:

1. **Forward Propagation**: The input is fed to the input layer of the neural network and the output is obtained from the output layer. The output is calculated by multiplying the weights with the inputs and adding the bias term. The result is then passed through an activation function.

2. **Backward Propagation**: The error is calculated by taking the difference between the desired output and the actual output obtained from the forward propagation step. The error is then propagated backward through the network, and the weights are updated based on the gradient of the cost function with respect to the weights.

3. **Weight Update**: The weights are updated using the gradient descent algorithm. The weights are updated in the direction of the negative gradient of the cost function with respect to the weights.

4. **Repeat**: The above steps are repeated until the cost function reaches a minimum value or the maximum number of iterations is reached.

Back Propagation is an efficient algorithm for training neural networks and is widely used in various applications of soft computing. It is an important topic in the study of neural networks and is covered in Unit 2 - Neural Networks-II (Back propagation networks) of the subject of Application of Soft Computing.