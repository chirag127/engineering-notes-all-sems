## Unit 2 - Neural Networks-II (Back propagation networks)

Neural Networks are a powerful class of machine learning algorithms inspired by the structure and function of the human brain. In this unit, we will focus on back propagation networks, which are a type of neural network that can learn to recognize patterns in data.

### What are Back Propagation Networks?

Back propagation networks are a type of feedforward neural network, which means that the information flows in one direction from the input layer to the output layer. These networks consist of multiple layers of interconnected nodes or neurons, where each neuron receives input from the neurons in the previous layer and produces an output that is passed on to the neurons in the next layer.

The back propagation algorithm is used to train these networks, where the weights of the connections between the neurons are adjusted to minimize the difference between the actual output and the desired output. This is done by propagating the error backwards through the network and updating the weights using gradient descent.

### Architecture of Back Propagation Networks

The architecture of a back propagation network consists of three types of layers:

1. Input Layer: This is the first layer in the network, where the input data is fed into the network. The number of neurons in this layer is equal to the number of features in the input data.

2. Hidden Layers: These are one or more layers between the input and output layers, where the computation is performed. The number of neurons in each hidden layer is a hyperparameter that needs to be set before training the network.

3. Output Layer: This is the last layer in the network, where the output of the network is produced. The number of neurons in this layer depends on the type of problem being solved. For example, if the problem is a binary classification problem, then the output layer will have one neuron that produces a binary output.

### Back Propagation Algorithm

The back propagation algorithm consists of two phases:

1. Forward Propagation: In this phase, the input data is fed into the network, and the output is computed by propagating the input through the network layer by layer.

2. Backward Propagation: In this phase, the error between the actual output and the desired output is computed, and this error is propagated backwards through the network to update the weights of the connections between the neurons.

The back propagation algorithm uses the gradient descent optimization algorithm to update the weights of the connections between the neurons. The gradient of the error with respect to the weights is computed, and the weights are updated in the direction of the negative gradient.

### Advantages and Limitations of Back Propagation Networks

Advantages:

1. Back propagation networks can learn to recognize complex patterns in data.

2. They can be used for a wide range of tasks, including classification, regression, and prediction.

3. They can handle large amounts of data and can be used for real-time applications.

Limitations:

1. They are computationally expensive and require large amounts of memory.

2. They can be prone to overfitting if the number of neurons in the hidden layers is too high.

3. They can get stuck in local minima during training, which can result in suboptimal solutions.

In conclusion, back propagation networks are a powerful class of machine learning algorithms that can learn to recognize complex patterns in data. By understanding the architecture and working of these networks, we can use them to solve a wide range of problems.