### Stochastic Optimization for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning.

In deep learning, optimization is the process of finding the values of the parameters in a model that minimize the error between the predicted outputs and the actual outputs. Stochastic optimization is a popular technique for optimizing deep learning models. Here are some key points to keep in mind when using stochastic optimization:

1. Stochastic optimization is a variant of gradient descent that uses a small subset of the training data to compute the gradient of the cost function at each iteration.

2. The subset of the training data used at each iteration is called a mini-batch. The size of the mini-batch is a hyperparameter that can be tuned to achieve better performance.

3. Compared to batch gradient descent, which computes the gradient using the entire training set, stochastic optimization has lower memory requirements and is faster to compute.

4. Stochastic optimization can be used with a variety of optimization algorithms, including stochastic gradient descent (SGD), Adam, and Adagrad.

5. SGD is a popular optimization algorithm for deep learning models. It works by computing the gradient of the cost function with respect to the parameters for each mini-batch and updating the parameters in the direction of the negative gradient.

6. One challenge with SGD is that it can get stuck in local minima or saddle points, which can prevent the algorithm from finding the global minimum.

7. To address this challenge, several techniques have been proposed, including momentum, which adds a fraction of the previous update to the current update, and learning rate schedules, which adjust the learning rate over time.

8. Another popular optimization algorithm is Adam, which uses adaptive learning rates for each parameter based on the first and second moments of the gradient.

9. Adagrad is another optimization algorithm that adapts the learning rate for each parameter based on the historical gradients.

10. In summary, stochastic optimization is a powerful technique for optimizing deep learning models. By using mini-batches of training data and a variety of optimization algorithms, it is possible to train deep learning models that achieve state-of-the-art performance on a wide variety of tasks.