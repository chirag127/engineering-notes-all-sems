# Single Layer Artificial Neural Network

- A single layer artificial neural network is a type of neural network that has just one layer between the input and output layers. This type of neural network is also known as a perceptron.
- A perceptron can be used to perform binary classification tasks, such as predicting whether an email is spam or not, or whether a tumor is benign or malignant.
- A perceptron consists of a set of input nodes, each with a corresponding weight, a bias term, an activation function, and an output node .
- The output of the perceptron is computed by multiplying each input by its weight, adding the bias term, and applying the activation function .
- The activation function is usually a step function, which returns 1 if the input is greater than or equal to a threshold, and 0 otherwise .
- The perceptron can be trained using a learning algorithm, such as the perceptron learning rule, which updates the weights and bias based on the error between the predicted and actual output .
- The perceptron learning rule is given by:

  - w<sub>i</sub> = w<sub>i</sub> + &alpha;(y - &hat;y)x<sub>i</sub>
  - b = b + &alpha;(y - &hat;y)

  where w<sub>i</sub> is the weight of the i-th input, b is the bias term, &alpha; is the learning rate, y is the actual output, &hat;y is the predicted output, and x<sub>i</sub> is the i-th input .

- The perceptron learning rule can be applied iteratively until the perceptron converges to a solution, or until a maximum number of iterations is reached .
- The perceptron can only learn linearly separable patterns, meaning that there exists a hyperplane that can separate the data into two classes .
- The perceptron cannot learn nonlinear patterns, such as the XOR function, which requires more than one layer of neurons .
- A single layer artificial neural network can be extended to a multilayer artificial neural network, which has one or more hidden layers between the input and output layers.
- A multilayer artificial neural network can learn more complex and nonlinear patterns, using different activation functions, such as sigmoid, tanh, or relu.
- A multilayer artificial neural network can be trained using a more advanced learning algorithm, such as backpropagation, which propagates the error from the output layer to the hidden layers, and updates the weights and bias accordingly.