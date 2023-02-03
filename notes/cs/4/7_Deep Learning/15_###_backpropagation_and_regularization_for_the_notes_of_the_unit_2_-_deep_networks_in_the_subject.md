### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

Backpropagation is an algorithm used to train deep neural networks. It is a supervised learning method that uses gradient descent to update the weights of the network based on the error between the predicted output and the actual output. 

The algorithm starts by making a forward pass through the network to calculate the predicted output. Then, it calculates the error between the predicted output and the actual output. The error is then propagated backwards through the network, and the weights are updated to minimize the error. This process is repeated multiple times until the error is minimized.

Regularization is a technique used to prevent overfitting in deep neural networks. Overfitting occurs when the network is too complex and has too many parameters, leading to poor generalization performance on unseen data. Regularization helps to reduce the complexity of the network by adding a penalty term to the loss function.

There are two main types of regularization techniques used in deep learning:

1. L1 regularization: Adds a penalty term to the loss function that is proportional to the absolute values of the weights.

2. L2 regularization: Adds a penalty term to the loss function that is proportional to the square of the values of the weights.

Advantages of regularization include:

1. Improved generalization performance: Regularization helps to prevent overfitting and improve the generalization performance of the network on unseen data.

2. Simplified network structure: Regularization helps to simplify the network structure by reducing the number of parameters and limiting the complexity of the network.

Disadvantages of regularization include:

1. Increased training time: Regularization can increase the training time as it requires additional computation to add the penalty term to the loss function.

2. Reduced model performance: Regularization can also reduce the performance of the model if the regularization term is too strong.

In conclusion, backpropagation is an algorithm used to train deep neural networks, and regularization is a technique used to prevent overfitting and improve the generalization performance of the network on unseen data.
