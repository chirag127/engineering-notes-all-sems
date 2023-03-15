 Here is the content in markdown format for the topic ### Stochastic Optimization for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning:

### Stochastic Optimization
- Stochastic optimization refers to optimizing a objective function that depends on random variables/parameters.
- In deep learning, the training data is a random variable and the objective function is the loss function. So, the process of minimizing the loss function by tuning the model parameters is a stochastic optimization problem.
- Some key points about stochastic optimization:
-- The minimum of the objective function is a random variable. We try to find a parameter value that minimizes the expected value of the objective function.
-- The gradient estimates are noisy due to the randomness in the training data. This makes the optimization challenging.
-- Stochastic gradient descent is a popular approach that uses noisy gradient estimates to iteratively update the parameters. It has a low per-iteration cost but may take a long time to converge.
-- Variants of stochastic gradient descent like Adam, RMSProp, etc. exist to accelerate the convergence.

[Diagrams and examples can be added here to aid understanding]

Some advantages of stochastic optimization:
- It can be used when the dataset is too large to compute the gradient over the complete dataset for each update.
- It tends to find a good local minimum even with noisy gradients.

Some disadvantages:
- It can lead to oscillations and slow convergence if the noise in gradient estimates is high.
- The final minimum found can depend on the random sequence of training samples chosen. So, multiple runs of stochastic optimization may lead to different final parameters.

[More details, applications, and codes can be added here if required.]