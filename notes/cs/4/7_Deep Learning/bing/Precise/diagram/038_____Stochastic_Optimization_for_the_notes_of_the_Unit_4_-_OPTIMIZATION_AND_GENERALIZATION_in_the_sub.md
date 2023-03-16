### Stochastic Optimization

Stochastic optimization refers to a collection of methods for minimizing or maximizing an objective function when randomness is present. In the context of deep learning, the objective function is usually a loss function that measures the discrepancy between the predicted values of the neural network and the true values.

Here are some key points to remember about stochastic optimization:

1. Stochastic optimization methods are iterative in nature and make use of gradient information to update the model parameters.
2. The most commonly used stochastic optimization method in deep learning is stochastic gradient descent (SGD).
3. SGD updates the model parameters using an estimate of the gradient computed from a randomly selected subset of the training data, called a mini-batch.
4. The use of mini-batches introduces randomness in the optimization process, which can help the algorithm escape local minima and saddle points.
5. Other popular stochastic optimization methods used in deep learning include Adam, Adagrad, and RMSprop.
6. These methods adaptively adjust the learning rate during training, which can lead to faster convergence and improved performance.
