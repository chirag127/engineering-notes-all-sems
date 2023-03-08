 Here is the content in markdown format for the topic -

### Activation function

An activation function is a function applied at each node of a neural network which decides whether a node's output signal should be sent to the next layer or not. It introduces non-linearity into the network and allows the network to learn complex patterns in the data. Some common types of activation functions are:

1. Sigmoid function - It outputs a value between 0 and 1, which represents a probability. It is differentiable everywhere and outputs a smooth curve. However, it saturates and kills gradients for large positive/negative values.
$$
\sigma(x) = \frac{1}{1+e^{-x}}
$$

2. Tanh function - It outputs a value between -1 and 1. It is differentiable everywhere and outputs a smooth curve. However, it also saturates but to a lesser degree than sigmoid.
$$
\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$

3. ReLU function - It outputs 0 if input is negative and the input itself if input is positive. It solves the saturation problem and allows nodes to be more easily activated. However, it is not differentiable at 0 and can lead to 'dying ReLU' problem.
$$
f(x) = \max(0, x)
$$

Advantages - Introduces non-linearity, avoids saturation to some extent, allows complex patterns to be learned.
Disadvantages - May lead to vanishing gradient problem if not chosen properly.

Applications - Used in the hidden layers of artificial neural networks to introduce non-linearity. The output layer activation depends on the problem, for example, sigmoid for probability outputs and softmax for multi-class classification.

[Diagrams and codes can be added here]