 Here is the content in markdown format for the topic ### Artificial Neuron and its model:

An artificial neuron is a mathematical function inspired by biological neurons. It is a basic processing unit of a neural network which uses inputs to produce an output.

The model of an artificial neuron consists of:

1. Inputs: The inputs are the signals or data received from the previous neurons or the input data. They are represented by x1, x2, ....xn.

2. Weights: Each input has an associated weight which represents the strength of the connection of input to the neuron. They are represented by w1, w2, ....wn.

3. Summation Function: The weighted inputs are summed to produce a linear combination which is the net input(net) to the neuron. It is calculated as:

net = w1*x1 + w2*x2 + ... + wn*xn

4. Activation Function: The net input is passed through an activation function f(net) which determines the output of the neuron. It introduces non-linearity into the network. Some commonly used activation functions are:

- Sigmoid: f(net) = 1/(1+e^-net)
- Tanh: f(net) = (e^net - e^-net)/(e^net + e^-net)
- ReLU: f(net) = max(0, net)

The output of the activation function is the output of the artificial neuron.

[Include detailed ascii diagrams, examples, advantages, disadvantages, applications, etc. if helpful]

The power of a neural network comes from connecting several such artificial neurons into a network which can then be trained on data to learn complex patterns and make predictions on new data.