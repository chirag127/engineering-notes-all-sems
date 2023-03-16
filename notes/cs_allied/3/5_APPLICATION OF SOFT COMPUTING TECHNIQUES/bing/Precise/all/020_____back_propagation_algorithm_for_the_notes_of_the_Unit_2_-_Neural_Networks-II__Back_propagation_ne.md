# Back Propagation Algorithm

Back Propagation is a supervised learning algorithm used for training Artificial Neural Networks. It is commonly used to train deep neural networks, a term referring to neural networks with more than one hidden layer. The algorithm works by computing the gradient of the loss function with respect to each weight by the chain rule, computing the gradient one layer at a time, iterating backward from the last layer to avoid redundant calculations of intermediate terms in the chain rule.

The steps involved in the back propagation algorithm are as follows:

1. **Forward Propagation**: The input is passed through the network to generate an output. The output is compared with the desired output to calculate the error.

2. **Backward Propagation**: The error is propagated backward through the network. The gradient of the error with respect to the weights is calculated.

3. **Weight Update**: The weights are updated using gradient descent or other optimization algorithms to minimize the error.

4. **Repeat**: The above steps are repeated until the error is minimized or a stopping criterion is met.

Back Propagation is a powerful algorithm that has been widely used in various applications. However, it has its limitations, such as the vanishing gradient problem, which can make it difficult to train deep neural networks. Various techniques, such as using different activation functions and weight initialization methods, have been proposed to mitigate these issues.
