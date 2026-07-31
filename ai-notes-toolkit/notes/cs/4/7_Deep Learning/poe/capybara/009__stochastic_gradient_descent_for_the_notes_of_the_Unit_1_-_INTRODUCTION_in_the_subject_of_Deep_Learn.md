### Stochastic Gradient Descent (SGD) 

Stochastic Gradient Descent (SGD) is an optimization algorithm used in machine learning for training deep learning models. It is a widely used method for minimizing the cost function in neural networks.

Here are some important points to note about SGD:

- SGD is a type of gradient descent algorithm that is used to update the weights of a neural network.

- In SGD, the weights are updated after every batch of training data is processed.

- The learning rate, which determines the size of the weight updates, is an important parameter in SGD. A small learning rate can lead to slow convergence, while a large learning rate can cause the algorithm to overshoot the minimum of the cost function.

- One of the advantages of SGD is that it can converge faster than batch gradient descent. This is because it updates the weights more frequently, which can help the algorithm to escape from local minima.

- However, since SGD updates the weights after every batch, the updates can be noisy and may not always lead to the optimal solution.

- To address this issue, various modifications to SGD have been proposed, such as momentum, which uses a moving average of the weight updates to reduce the noise.

Overall, SGD is an important optimization algorithm in deep learning that is widely used in practice. It is important to understand the key parameters and trade-offs involved in using SGD in order to effectively train deep learning models.