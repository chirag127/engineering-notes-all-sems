Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on what a shallow network computes for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning. Here is the content I have written in markdown format:

### What a shallow network computes

- A shallow network is a neural network that has only one hidden layer between the input and the output layers.
- A shallow network can be seen as a function that maps an input vector **x** to an output vector **y** by applying a series of linear and nonlinear transformations.
- The output of the hidden layer is given by **h = f(Wx + b)**, where **W** is the weight matrix, **b** is the bias vector, and **f** is the activation function, such as sigmoid, tanh, or ReLU.
- The output of the network is given by **y = g(Vh + c)**, where **V** is another weight matrix, **c** is another bias vector, and **g** is another activation function, such as softmax, linear, or sigmoid.
- A shallow network can compute a variety of functions, depending on the choice of the activation functions and the parameters **W, b, V, c**.
- A shallow network can approximate any continuous function on a compact domain, according to the universal approximation theorem, as long as the activation function is non-constant, bounded, and continuous, and the network has enough hidden units.
- A shallow network can also learn to classify data into different categories, by using a softmax activation function at the output layer and a cross-entropy loss function to measure the discrepancy between the predicted and the true labels.
- A shallow network can be trained using gradient-based optimization methods, such as gradient descent, stochastic gradient descent, or backpropagation, which update the parameters **W, b, V, c** by computing the partial derivatives of the loss function with respect to them.