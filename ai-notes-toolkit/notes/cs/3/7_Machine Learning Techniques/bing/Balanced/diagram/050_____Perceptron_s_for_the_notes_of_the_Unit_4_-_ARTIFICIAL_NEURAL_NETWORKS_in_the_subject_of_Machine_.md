### Perceptron's

- A perceptron is an algorithm for supervised learning of binary classifiers .
- A binary classifier is a function that can decide whether an input, represented by a vector of numbers, belongs to some specific class.
- A perceptron is also a single-layer neural network, which is the simplest possible neural network.
- A neural network is a collection of artificial neurons that are connected by weights and can perform computations on input data.
- A perceptron consists of the following components  :
  - An input layer, which receives the input vector x and adds a bias term 1 to it.
  - A weight vector w, which assigns a weight to each input component.
  - An activation function, which computes the output of the perceptron as a function of the weighted sum of the inputs. The most common activation function is the step function, which returns 1 if the weighted sum is positive and 0 otherwise.
  - An output layer, which returns the output of the activation function as the prediction of the perceptron.
- A perceptron can be trained using the following steps  :
  - Initialize the weight vector w to zero or to a small random value.
  - For each example j in the training set D, perform the following steps:
    - Compute the output of the perceptron y_j for the input vector x_j.
    - Compare the output y_j with the true label t_j and compute the error e_j = t_j - y_j.
    - Update the weight vector w by adding the product of the error e_j and the input vector x_j, multiplied by a learning rate alpha: w = w + alpha * e_j * x_j.
  - Repeat the above steps until the error is zero or below a certain threshold, or until a maximum number of iterations is reached.
- A perceptron can be used to classify linearly separable data, which means that there exists a hyperplane that can separate the data into two classes  .
- A perceptron cannot classify nonlinearly separable data, which means that there is no such hyperplane that can separate the data into two classes  .
- A perceptron can be extended to a multilayer perceptron, which is a neural network with more than one layer of perceptrons, and can learn more complex functions and classify nonlinearly separable data .

: https://en.wikipedia.org/wiki/Perceptron
: https://www.surfactants.net/the-perceptron-a-machine-learning-algorithm/
: https://deepai.org/machine-learning-glossary-and-terms/perceptron
: https://www.w3schools.com/ai/ai_perceptrons.asp