### Back Propagation Learning Methods

Back propagation is a supervised learning algorithm used for training artificial neural networks. It is a method of adjusting the weights of the connections between the neurons in the network to minimize the error between the desired output and the actual output. The algorithm is based on the chain rule of calculus and is used to compute the gradient of the error function with respect to the weights of the network.

The back propagation algorithm consists of the following steps:

1. Forward pass: The input is fed forward through the network to compute the output of each neuron.
2. Compute error: The error between the desired output and the actual output is computed.
3. Backward pass: The error is propagated backward through the network to compute the gradient of the error function with respect to the weights.
4. Update weights: The weights are updated using the computed gradient and a learning rate.

The back propagation algorithm is an iterative process and is repeated until the error between the desired output and the actual output is minimized. The learning rate is a hyperparameter that controls the step size of the weight updates and can be adjusted to improve the performance of the algorithm.

Back propagation is commonly used in training feedforward neural networks, but can also be applied to other types of neural networks such as recurrent neural networks. It is a powerful algorithm that has been widely used in many applications, including image recognition, speech recognition, and natural language processing. However, it is not the only learning algorithm for neural networks and other methods such as genetic algorithms and reinforcement learning can also be used.