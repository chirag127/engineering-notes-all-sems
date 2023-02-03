### Non-convex optimization for deep networks for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning

Non-convex optimization refers to the process of finding the global minimum of a non-convex function. In deep learning, non-convex optimization is used to optimize the parameters of deep neural networks. 

There are several challenges associated with non-convex optimization in deep networks: 
1. The optimization problem is highly non-linear and has many local minima. 
2. The optimization problem is high-dimensional, with the number of parameters growing with the size of the network. 
3. The optimization problem is often ill-conditioned, meaning that small changes in the parameters can result in large changes in the output. 

Despite these challenges, non-convex optimization is widely used in deep learning because it has been found to work well in practice. There are several popular optimization algorithms that are used to optimize deep networks, including gradient descent, Stochastic Gradient Descent (SGD), and Adam. 

Gradient descent is a first-order optimization algorithm that updates the parameters by taking the gradient of the loss function with respect to the parameters. SGD is a variant of gradient descent that uses only a single training sample to compute the gradient. Adam is a more advanced optimization algorithm that uses a combination of gradient descent and SGD. 

In order to make non-convex optimization more effective in deep networks, several techniques have been developed, including regularization, early stopping, and dropout. Regularization is a technique that adds a penalty to the loss function to discourage overfitting. Early stopping is a technique that stops training when the validation loss stops improving. Dropout is a technique that randomly drops out neurons during training to prevent overfitting. 

In conclusion, non-convex optimization is a critical component of deep learning and has been found to work well in practice despite the challenges associated with it. There are several popular optimization algorithms and techniques that can be used to optimize deep networks and improve their performance.
