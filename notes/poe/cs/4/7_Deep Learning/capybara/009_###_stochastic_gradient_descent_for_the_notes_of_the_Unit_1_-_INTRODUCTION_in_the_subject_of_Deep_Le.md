### Stochastic Gradient Descent for the Notes of Unit 1 - Introduction in the Subject of Deep Learning

Stochastic Gradient Descent (SGD) is a popular optimization algorithm used in Deep Learning. It is an iterative method used to minimize the cost function of a Neural Network. The algorithm updates the weights of the Neural Network in the direction of the steepest descent by taking small steps at each iteration. This helps to reach the global minimum of the cost function.

The algorithm is called "stochastic" because instead of computing the gradient of the cost function over the entire dataset, it computes the gradient over a small subset of the dataset. This small subset is called a "mini-batch". The algorithm then updates the weights using the gradient computed over the mini-batch.

Here are some key points to remember about Stochastic Gradient Descent:

- SGD is an iterative algorithm that updates the weights of a Neural Network in the direction of the steepest descent.
- It is called "stochastic" because it computes the gradient over a small subset of the dataset, rather than the entire dataset.
- The small subset is called a "mini-batch".
- The algorithm then updates the weights using the gradient computed over the mini-batch.
- The learning rate is an important hyperparameter in SGD. It controls the size of the steps taken at each iteration.

Mnemonics and Tricks:

- "SGD, take a mini-batch and update the weights with a small step to reach the global minimum of the cost function."

Advantages of Stochastic Gradient Descent:

- SGD is computationally efficient because it only computes the gradient over a small subset of the dataset.
- It can handle large datasets because it processes the data in mini-batches.
- SGD can converge faster than Batch Gradient Descent because it updates the weights more frequently.

Disadvantages of Stochastic Gradient Descent:

- SGD can be sensitive to the learning rate. If the learning rate is too high, the algorithm can oscillate and fail to converge. If the learning rate is too low, the algorithm can take a long time to converge.
- SGD can get stuck in local minima. This can be mitigated by using techniques like momentum and learning rate annealing.

Examples and Applications:

- SGD is used in many applications of Deep Learning, including Computer Vision, Natural Language Processing, and Speech Recognition.
- It is used to train Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and other types of Neural Networks.

In conclusion, Stochastic Gradient Descent is an important optimization algorithm used in Deep Learning. It is computationally efficient and can handle large datasets. However, it can be sensitive to the learning rate and can get stuck in local minima. By understanding the key points and using the appropriate techniques, SGD can be an effective tool for training Neural Networks.