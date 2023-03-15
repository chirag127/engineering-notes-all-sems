### Single Layer Artificial Neural Network

- A single layer artificial neural network is a type of neural network that has just one layer between the input and output layers. This type of neural network is also known as a perceptron .
- A perceptron can be used to perform binary classification tasks, such as predicting whether an email is spam or not, or whether a tumor is benign or malignant .
- A perceptron consists of a set of input nodes, each with a corresponding weight, a bias term, an activation function, and an output node .
- The output of the perceptron is computed by multiplying each input by its weight, adding the bias term, and applying the activation function to the sum .
- The activation function is usually a step function, which returns 1 if the input is greater than or equal to a threshold, and 0 otherwise .
- The weights and bias of the perceptron are learned by adjusting them based on the error between the predicted output and the actual output for a given set of inputs .
- The error is calculated by subtracting the predicted output from the actual output, and the weights and bias are updated by adding a fraction of the error times the input to the current values .
- The fraction of the error that is used to update the weights and bias is called the learning rate, and it controls how fast the perceptron learns from the data .
- The perceptron learning algorithm is repeated for a number of iterations, or until the error is minimized or reaches a desired level .
- A single layer neural network can only learn linearly separable patterns, meaning that the data points can be separated by a straight line .
- A single layer neural network cannot learn nonlinear patterns, such as XOR, which requires a curved boundary to separate the data points .
- To learn nonlinear patterns, a neural network needs to have more than one layer, or a deep neural network .
- A deep neural network consists of multiple layers of perceptrons, or other types of artificial neurons, that are connected to each other and have different activation functions .
- A deep neural network can learn complex and abstract features from the data, and perform more advanced tasks, such as image recognition, natural language processing, and speech synthesis .