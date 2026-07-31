### Back Propagation Learning Methods

Back propagation is a widely used algorithm to train feed-forward neural networks. It is an iterative method that adjusts the weights of the network to minimize the error between the predicted output and the actual output. In this section, we will discuss the back propagation learning methods in detail.

1. **Forward Propagation:** In the forward propagation phase, the input values are propagated through the network to calculate the output of the network. The output of each neuron is calculated by applying the activation function to the weighted sum of its inputs.

2. **Error Calculation:** The error in the output of the network is calculated by comparing the predicted output with the actual output. The error is calculated using a loss function such as mean squared error or cross-entropy.

3. **Backward Propagation:** In the backward propagation phase, the error is propagated back through the network to adjust the weights of the network. The weights are adjusted using the gradient descent algorithm.

4. **Gradient Descent:** The gradient descent algorithm is used to adjust the weights of the network to minimize the error. The gradient of the error with respect to the weights is calculated and the weights are updated in the opposite direction of the gradient.

5. **Learning Rate:** The learning rate is a hyperparameter that determines the step size of the weight updates. It is important to choose an appropriate learning rate to ensure that the network converges to the optimal weights.

6. **Batch Size:** The batch size is the number of samples used in each iteration of the training process. The choice of batch size can have an impact on the convergence of the network.

7. **Epochs:** An epoch is a complete pass through the training dataset. The number of epochs determines how many times the network will be trained on the entire dataset.

8. **Overfitting:** Overfitting occurs when the network becomes too complex and starts to fit the noise in the training data. Regularization techniques such as dropout and weight decay can be used to prevent overfitting.

9. **Hyperparameter Tuning:** The performance of the network can be improved by tuning the hyperparameters such as learning rate, batch size, and regularization parameters.

In conclusion, back propagation learning methods are an essential part of training feed-forward neural networks. By adjusting the weights of the network using the gradient descent algorithm, the network can learn to make accurate predictions on new data. It is important to choose appropriate hyperparameters and regularization techniques to ensure that the network does not overfit the training data.