A shallow network is a type of neural network that has only one or two hidden layers between the input and output layers. A shallow network computes a function that maps the input to the output by applying a series of linear and nonlinear transformations. The following diagram illustrates the basic architecture of a shallow network with one hidden layer:

```
    Input layer      Hidden layer     Output layer
    +---------+      +---------+      +---------+
    | x1      |----->| z1      |----->| y1      |
    +---------+      +---------+      +---------+
    | x2      |----->| z2      |----->| y2      |
    +---------+      +---------+      +---------+
    | x3      |----->| z3      |----->| y3      |
    +---------+      +---------+      +---------+
```

Each node in the hidden layer computes a weighted sum of the inputs and adds a bias term, then applies a nonlinear activation function to produce an output. For example, the node z1 computes:

```
z1 = f(w11 * x1 + w21 * x2 + w31 * x3 + b1)
```

where f is the activation function, w are the weights, and b is the bias. The output layer computes a similar function, but with different weights and biases. For example, the node y1 computes:

```
y1 = g(v11 * z1 + v21 * z2 + v31 * z3 + c1)
```

where g is the activation function, v are the weights, and c is the bias. The activation functions f and g can be different, depending on the task and the network design. Some common choices are sigmoid, tanh, relu, softmax, etc.

The goal of training a shallow network is to find the optimal values of the weights and biases that minimize a loss function that measures the difference between the network output and the desired output. This is usually done by using a gradient-based optimization algorithm, such as gradient descent, that updates the parameters in the direction of the negative gradient of the loss function with respect to the parameters. The gradient is computed by using a technique called backpropagation, which propagates the errors from the output layer to the hidden layer and the input layer.