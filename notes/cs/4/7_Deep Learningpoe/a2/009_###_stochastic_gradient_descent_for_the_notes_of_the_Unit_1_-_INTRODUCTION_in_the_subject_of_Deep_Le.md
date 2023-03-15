 Here is the content in markdown format for the topic ### stochastic gradient descent for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Stochastic Gradient Descent

- Stochastic Gradient Descent (SGD) is a gradient descent technique for training machine learning models on large datasets.
- In SGD, the gradient is estimated using only a single or a few training examples on every iteration, rather than using the whole training set to compute the gradient at once like in batch gradient descent.
- This makes SGD faster and more scalable than batch gradient descent as it can update the model quickly based on new data and doesn't have to wait for the full batch. However, the path taken by SGD to the minimum is more noisy and less smooth compared to the batch gradient descent.
- Some pros and cons of SGD are:

Pros:

- Fast and scalable for large datasets.
- Able to update models based on new data quickly.

Cons:

- Noisy and zig-zag path to the minimum.
- May not converge to optimal weights/parameters.
- Hyperparameter tuning required (learning rate, batch size, etc.).

- Some tips for using SGD:

1. Start with a low learning rate and increase gradually.
2. Try running multiple epochs of SGD with different random seeds and choose the best result.
3. Increase the batch size for more stability but this may reduce the speed. Find the right balance.
4. Use adaptive learning rate methods like AdaGrad, RMSProp, Adam, etc. to better tune the learning rate.

- Overall, SGD is a very popular optimization method for training machine learning models on large datasets due to its efficiency and scalability, despite some disadvantages. With proper tuning, it can produce good results.