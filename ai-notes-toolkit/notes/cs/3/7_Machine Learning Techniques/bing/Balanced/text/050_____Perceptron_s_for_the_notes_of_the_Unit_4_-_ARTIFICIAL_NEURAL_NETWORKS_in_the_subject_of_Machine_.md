### Perceptron's for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- A perceptron is an algorithm for supervised learning of binary classifiers .
- A binary classifier is a function that can decide whether an input, represented by a vector of numbers, belongs to some specific class.
- A perceptron is also a single-layer neural network, which is the simplest possible neural network.
- A perceptron consists of an input layer, a weighted sum function, and an activation function.
- The input layer receives the input vector and passes it to the weighted sum function, which computes the dot product of the input vector and a weight vector.
- The activation function, also called the threshold function, outputs a binary value (0 or 1) based on whether the weighted sum is greater than or less than a threshold value.
- The perceptron can be trained by adjusting the weight vector and the threshold value based on the error between the predicted output and the actual output for each input vector .
- The perceptron learning algorithm consists of the following steps:
  - Initialize the weights and the threshold to zero or small random values.
  - For each input vector in the training set, perform the following steps:
    - Compute the weighted sum and the activation function for the input vector.
    - Compare the predicted output with the actual output and calculate the error.
    - Update the weights and the threshold by adding the product of the error and the input vector to the weights and the error to the threshold.
  - Repeat the above steps until the error is zero or below a certain tolerance level, or until a maximum number of iterations is reached.
- The perceptron can learn linearly separable patterns, which means that the input vectors belonging to different classes can be separated by a straight line .
- The perceptron cannot learn nonlinearly separable patterns, which means that the input vectors belonging to different classes cannot be separated by a straight line .
- The perceptron is the primary unit of computation in an artificial neural network, which is a network of interconnected perceptrons that can learn more complex patterns .