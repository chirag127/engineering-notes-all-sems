## Unit 1 - Neural Networks-I (Introduction & Architecture)

Neural networks are computational models that are inspired by the structure and function of the biological brain. They consist of artificial neurons that can process information and learn from data. Neural networks can be used for various artificial intelligence tasks, such as classification, regression, clustering, generation, etc.

The architecture of a neural network refers to the way the neurons are organized and connected. The architecture determines the complexity and the capabilities of the network. There are different types of neural network architectures, such as feedforward, recurrent, convolutional, etc.

The following are some of the main components of a neural network architecture:

- **Input layer**: This is the layer that receives the input data, such as images, text, audio, etc. The input layer has as many neurons as the number of features or dimensions of the input data.
- **Output layer**: This is the layer that produces the output of the network, such as labels, scores, probabilities, etc. The output layer has as many neurons as the number of classes or categories of the output data.
- **Hidden layer(s)**: These are the layers that are between the input and output layers. They perform the computations and transformations of the input data. The hidden layers can have different numbers and sizes of neurons, depending on the network architecture and the task. The more hidden layers and neurons, the more complex and expressive the network can be, but also the more prone to overfitting and harder to train.
- **Weights and biases**: These are the parameters of the network that are learned during the training process. They determine how the neurons are connected and how much influence they have on each other. The weights are the values that multiply the inputs of each neuron, and the biases are the values that are added to the inputs of each neuron. The weights and biases are updated by using a learning algorithm, such as gradient descent, that minimizes a loss function that measures the error between the network output and the desired output.
- **Activation function**: This is the function that determines the output of each neuron, based on its input. The activation function introduces non-linearity to the network, which allows it to learn complex patterns and relationships. There are different types of activation functions, such as sigmoid, tanh, ReLU, etc. The choice of the activation function depends on the network architecture and the task.

The following is an example of a simple neural network architecture with one input layer, one hidden layer, and one output layer:

![Neural network example](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Colored_neural_network.svg/300px-Colored_neural_network.svg.png)

The input layer has three neurons, corresponding to three features of the input data. The hidden layer has four neurons, with different weights and biases. The output layer has two neurons, corresponding to two classes of the output data. The activation function of each neuron is the sigmoid function, which maps the input to a value between 0 and 1.

The output of the network can be computed by applying the following formula to each layer:

$$output = sigmoid(weights \cdot input + bias)$$

For example, the output of the first neuron in the hidden layer can be computed as:

$$output_1 = sigmoid(w_{11} \cdot x_1 + w_{12} \cdot x_2 + w_{13} \cdot x_3 + b_1)$$

where $x_1, x_2, x_3$ are the inputs, $w_{11}, w_{12}, w_{13}$ are the weights, and $b_1$ is the bias.

The output of the network can be used to make predictions, such as classifying the input data into one of the two classes. The network can be trained by using a learning algorithm that adjusts the weights and biases to minimize the loss function, such as cross-entropy, that measures the difference between the network output and the true output.