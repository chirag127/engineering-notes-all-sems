### Stochastic gradient descent for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- Stochastic gradient descent (SGD) is an iterative method often used for machine learning, optimizing the gradient descent during each search once a random weight vector is picked. [1]
- Gradient descent is a strategy that searches through a large or infinite hypothesis space whenever there are hypotheses continuously being parameterized and the errors are differentiable based on the parameters. [1]
- The problem with gradient descent is that converging to a local minimum takes extensive time and determining a global minimum is not guaranteed. [1]
- In SGD, the user initializes the weights and the process updates the weight vector using one data point. [2] The gradient descent continuously updates it incrementally when an error calculation is completed to improve convergence. [3]
- The method seeks to determine the steepest descent and it reduces the number of iterations and the time taken to search large quantities of data points. [4]
- Stochastic gradient descent is being used in neural networks and decreases machine computation time while increasing complexity and performance for large-scale problems. [5]

#### Stochastic Gradient Descent Algorithm

- SGD modifies the batch gradient descent algorithm by calculating the gradient for only one training example at every iteration. [6]
- The steps for performing SGD are as follows: [6]
  - Step 1: Randomly shuffle the data set of size m
  - Step 2: Select a learning rate
  - Step 3: Select initial parameter values as the starting point
  - Step 4: For i = 1, 2, ..., m, update all parameters from the gradient of the i-th training example, i.e. compute
  - Step 5: Repeat Step 4 until a local minima is reached or a stopping criterion is met
- Under SGD, the gradient is calculated at every step against a single data point. When the training data is large, computation may be faster and require less computer memory than batch gradient descent. [2]

#### Advantages and Disadvantages of SGD

- Advantages: [7]
  - Speed: SGD is faster than other variants of Gradient Descent such as Batch Gradient Descent and Mini-Batch Gradient Descent since it uses only one example to update the parameters.
  - Memory Efficiency: Since SGD updates the parameters for each training example one at a time, it is memory-efficient and can handle large datasets that cannot fit into memory.
  - Noise Reduction: Since SGD uses a random sample at each iteration, it can reduce the noise and variance in the gradient updates and escape from local minima.
- Disadvantages: [7]
  - Instability: SGD can be unstable and oscillate around the optimal value due to the randomness of the samples. This can be mitigated by using a decreasing learning rate or a momentum term.
  - Hyperparameter Tuning: SGD requires careful tuning of the learning rate and the momentum term to achieve good performance and convergence.
  - Irregularity: SGD does not guarantee a smooth decrease of the objective function and may produce erratic results.

#### Mnemonics and Learning Tricks

- A possible mnemonic to remember the steps of SGD is: **S**huffle, **L**earn, **I**nitialize, **U**pdate, **R**epeat. (SLIUR)
- A possible learning trick to understand the difference between batch gradient descent and SGD is to imagine a mountain with many valleys and ridges. Batch gradient descent would use a map of the whole mountain to find the lowest point, while SGD would use a compass to point to the steepest downhill direction at each step. Batch gradient descent would be more accurate but slower, while SGD would be faster but less precise.