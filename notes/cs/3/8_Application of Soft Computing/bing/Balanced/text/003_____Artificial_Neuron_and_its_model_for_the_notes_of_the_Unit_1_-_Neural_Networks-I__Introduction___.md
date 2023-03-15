### Artificial Neuron and its Model

- An artificial neuron is a mathematical function that simulates the basic functionality of a biological neuron, which is the basic unit of a neural network.
- An artificial neuron receives one or more inputs, usually weighted, and sums them to produce an output. The output is then passed through a non-linear function, called an activation function or transfer function, that determines the final output of the neuron .
- The activation function can have different shapes, such as sigmoid, linear, step, or hyperbolic tangent, depending on the desired properties of the neuron.
- The artificial neuron can be represented by a simple diagram, as shown below:

![Artificial neuron diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/ArtificialNeuronModel_english.png/220px-ArtificialNeuronModel_english.png)

- The diagram shows the inputs x1, x2, ..., xn, the weights w1, w2, ..., wn, the bias b, the sum function Σ, the activation function f, and the output y.
- The mathematical model of the artificial neuron can be expressed by the following equation:

y = f(Σ(wi * xi) + b)

- where y is the output, f is the activation function, wi is the weight of the ith input, xi is the ith input, and b is the bias.
- The weights and the bias are the parameters of the artificial neuron that can be adjusted during the learning process to optimize the performance of the neural network .
- The artificial neuron can perform various computations, such as logical operations, linear regression, or classification, depending on the choice of the activation function and the values of the weights and the bias .