```markdown
### Stochastic gradient descent

- Stochastic gradient descent (SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable).
- SGD is often used for machine learning, especially for deep learning, where the objective function is the loss function that measures the discrepancy between the predicted and true labels of the data .
- SGD works by updating the parameters (e.g. weights and biases) of the model in the opposite direction of the gradient of the objective function with respect to the parameters. The gradient is computed using a single or a small batch of randomly selected data points, rather than the entire data set, which makes SGD faster and more scalable than batch gradient descent   .
- SGD has some advantages and disadvantages compared to batch gradient descent   :
  - Advantages:
    - SGD can escape from local minima or saddle points, since the noise introduced by the random sampling can help the algorithm explore different regions of the parameter space  .
    - SGD can handle large and streaming data sets, since it only requires a small amount of data at each iteration and can be updated online   .
    - SGD can be easily parallelized and distributed across multiple machines or devices, since each worker can compute the gradient using its own data and communicate with a central server to update the parameters .
  - Disadvantages:
    - SGD can have high variance in the gradient estimates, which can lead to oscillations and slow convergence   .
    - SGD can be sensitive to the choice of the learning rate, which determines the step size of the parameter updates. A learning rate that is too large can cause divergence, while a learning rate that is too small can cause slow convergence or stagnation   .
    - SGD can be affected by noisy or outliers data, which can bias the gradient estimates and harm the performance of the model  .
- SGD can be improved or modified by using various techniques, such as momentum, adaptive learning rates, regularization, mini-batch sampling, etc   .
```