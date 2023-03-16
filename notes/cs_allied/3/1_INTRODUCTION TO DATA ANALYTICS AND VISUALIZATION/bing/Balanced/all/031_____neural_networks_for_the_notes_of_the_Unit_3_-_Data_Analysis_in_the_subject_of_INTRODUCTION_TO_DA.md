# Neural Networks

Neural networks are a subset of machine learning and are at the heart of deep learning algorithms. They are composed of artificial neurons or nodes that mimic the way that biological neurons signal to one another. Neural networks can learn from data and perform tasks such as function approximation, classification, pattern recognition, novelty detection, and sequential decision making.

Some key concepts and terms related to neural networks are:

- **Input layer**: The first layer of a neural network that receives the data and passes it to the hidden layers.
- **Hidden layer**: One or more layers of a neural network that perform computations on the input data and pass the results to the output layer or another hidden layer.
- **Output layer**: The last layer of a neural network that produces the final output or prediction.
- **Weight**: A numerical value that determines the strength of the connection between two neurons. Weights are adjusted during the learning process to minimize the error between the actual and desired output.
- **Bias**: A constant term that is added to the weighted sum of the inputs of a neuron. Bias helps to shift the activation function and control the output of the neuron.
- **Activation function**: A mathematical function that determines the output of a neuron based on its input. Common activation functions include sigmoid, tanh, ReLU, and softmax.
- **Backpropagation**: A learning algorithm that updates the weights and biases of a neural network by propagating the error from the output layer to the input layer.
- **Gradient descent**: An optimization technique that finds the optimal values of the weights and biases by iteratively moving in the direction of the steepest descent of the error function.
- **Learning rate**: A hyperparameter that controls the size of the steps taken by the gradient descent algorithm. A high learning rate can speed up the learning process but also cause instability, while a low learning rate can ensure stability but also slow down the learning process.
- **Epoch**: One complete pass through the entire training data set.
- **Batch**: A subset of the training data set that is used to update the weights and biases in one iteration of the gradient descent algorithm.
- **Loss function**: A function that measures the difference between the actual and desired output of a neural network. Common loss functions include mean squared error, cross-entropy, and hinge loss.
- **Regularization**: A technique that reduces the complexity of a neural network and prevents overfitting by adding a penalty term to the loss function. Common regularization methods include L1, L2, and dropout.
- **Overfitting**: A situation where a neural network learns the noise or specific details of the training data and fails to generalize well to new or unseen data.
- **Underfitting**: A situation where a neural network is too simple or has not learned enough from the training data and fails to capture the underlying patterns or relationships in the data.