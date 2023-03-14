Stochastic optimization refers to the use of randomness in the objective function or in the optimization algorithm. It is often used in deep learning to train deep neural networks, as it can help overcome the challenges of high-dimensional, nonlinear, and noisy objective functions that may have multiple local optima.

One of the most common stochastic optimization algorithms in deep learning is stochastic gradient descent (SGD), which updates the network weights by computing the gradient of the objective function on a randomly selected subset of the training data, called a mini-batch. SGD can be improved by using momentum, which adds a fraction of the previous weight update to the current one, to accelerate the convergence and escape from local optima. Another improvement is to use adaptive learning rates, which adjust the learning rate for each network weight independently, based on the history of the gradients. Examples of adaptive learning rate methods are Adagrad, Adadelta, RMSprop, Adam, Nadam, AdaMax, and AMSGrad.

The following diagram illustrates the basic architecture of a stochastic optimization algorithm for deep learning:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Objective     |       |  Optimization  |       |  Network       |
|  Function      |       |  Algorithm     |       |  Weights       |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       ^                       ^                       |
       |                       |                       |
       |                       |                       |
       |                       |                       v
       |                       |               +----------------+
       |                       |               |                |
       |                       |               |  Weight        |
       |                       |               |  Update        |
       |                       |               |                |
       |                       |               +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       v
       |                       |               +----------------+
       |                       |               |                |
       |                       +---------------+  Gradient      |
       |                                       |  Computation   |
       |                                       |                |
       |                                       +----------------+
       |                                               |
       |                                               |
       |                                               v
       |                                       +----------------+
       |                                       |                |
       +---------------------------------------+  Mini-batch    |
                                               |  Selection     |
                                               |                |
                                               +----------------+
                                                       |
                                                       |
                                                       v
                                               +----------------+
                                               |                |
                                               |  Training      |
                                               |  Data          |
                                               |                |
                                               +----------------+
```