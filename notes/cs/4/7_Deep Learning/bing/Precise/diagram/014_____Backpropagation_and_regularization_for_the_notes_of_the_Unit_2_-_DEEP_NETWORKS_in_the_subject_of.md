### Unit 2 - DEEP NETWORKS: Backpropagation and Regularization

Backpropagation and regularization are two important concepts in deep learning. Here are some key points to remember:

- **Backpropagation** is an algorithm used to train neural networks by minimizing the loss function. It calculates the gradient of the loss function with respect to the weights of the network, which is then used to update the weights in the direction of the negative gradient.

- **Regularization** is a technique used to prevent overfitting in neural networks. Overfitting occurs when the model is too complex and fits the training data too well, including the noise and random fluctuations. Regularization adds a penalty term to the loss function, which encourages the model to have smaller weights and thus be less complex.

- There are several types of regularization techniques, including L1 and L2 regularization. L1 regularization adds the absolute value of the weights to the loss function, while L2 regularization adds the square of the weights to the loss function.

- Regularization can also be achieved by using techniques such as dropout, where a certain percentage of the neurons in the network are randomly "dropped out" or turned off during each iteration of training. This helps to prevent the model from relying too heavily on any one feature and encourages it to learn more robust representations.

- Backpropagation and regularization are important tools in the training of deep neural networks. By using these techniques, it is possible to train more complex models that can achieve high levels of accuracy on a wide range of tasks.