### Activation function for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- An activation function is a mathematical function that is applied to the output of a neuron or a layer of neurons in a neural network.
- The activation function determines whether the neuron should be activated or not, based on the input signals it receives.
- The activation function also introduces non-linearity into the network, which enables it to learn complex patterns and functions from the data.
- The activation function you choose will affect the results and accuracy of your machine learning model, so you need to be aware of the different types of activation functions and their properties .

Some of the commonly used activation functions are:

- **Linear**: This is the simplest activation function, which directly outputs the input value. It is also called the identity function. It has the form: `f(x) = x`
- **Sigmoid**: This is a smooth and bounded activation function, which outputs a value between 0 and 1. It has the form: `f(x) = 1 / (1 + exp(-x))`
- **Tanh**: This is also a smooth and bounded activation function, which outputs a value between -1 and 1. It has the form: `f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))`
- **ReLU**: This is a piecewise linear activation function, which outputs zero if the input is negative, and the input itself if the input is positive or zero. It has the form: `f(x) = max(0, x)`
- **Leaky ReLU**: This is a variation of the ReLU function, which outputs a small positive value if the input is negative, instead of zero. It has the form: `f(x) = max(0.01x, x)`
- **Softmax**: This is a special activation function, which is usually used for the output layer of a multi-class classification problem. It outputs a probability distribution over the classes, such that the sum of the probabilities is 1. It has the form: `f(x_i) = exp(x_i) / sum(exp(x_j))` for all `j`

The choice of the activation function depends on the type of problem, the data, and the network architecture. Some general guidelines are :

- For hidden layers, the ReLU function is the modern default, as it is simple, fast, and avoids the vanishing gradient problem.
- For output layers, the linear function is suitable for regression problems, the sigmoid function is suitable for binary classification problems, and the softmax function is suitable for multi-class classification problems.
- For other problems, you may need to experiment with different activation functions and compare their performance.