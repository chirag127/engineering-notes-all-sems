### Artificial Neuron and its Model

- An artificial neuron is a mathematical function that simulates the basic functionality of a biological neuron, which is the basic unit of a neural network.
- An artificial neuron receives one or more inputs, usually weighted, and sums them to produce an output. The output is then passed through a non-linear function called an activation function or transfer function.
- The activation function determines the output of the artificial neuron based on the input sum. It can have different shapes, such as sigmoid, step, linear, or hyperbolic tangent.
- The artificial neuron can be represented by a simple diagram as shown below:

```
  w1     w2     wn
x1 ----> O  x2 ----> O  ... xn ----> O
          |            |           |
          |            |           |
          +-----+------+-----+-----+
                |
                | net
                v
             f(net) ----> y
```

- In this diagram, x1, x2, ..., xn are the inputs, w1, w2, ..., wn are the weights, net is the weighted sum of the inputs, f(net) is the activation function, and y is the output of the artificial neuron.
- The artificial neuron can be modeled by a mathematical equation as follows:

```
net = w1 * x1 + w2 * x2 + ... + wn * xn
y = f(net)
```

- The artificial neuron can perform different tasks depending on the choice of the activation function and the weights. For example, it can act as a linear regressor, a classifier, a logic gate, or a memory unit.
- The artificial neuron can be combined with other artificial neurons to form an artificial neural network, which is a system of interconnected artificial neurons that can learn from data and perform complex tasks.
- The artificial neural network can have different architectures, such as feedforward, recurrent, convolutional, or deep neural networks, depending on the arrangement and connection of the artificial neurons.