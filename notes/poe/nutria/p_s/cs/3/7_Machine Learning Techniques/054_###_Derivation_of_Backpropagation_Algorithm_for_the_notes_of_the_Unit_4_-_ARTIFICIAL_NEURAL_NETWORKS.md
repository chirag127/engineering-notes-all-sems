
### Derivation of Backpropagation Algorithm for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

Backpropagation is a supervised learning algorithm used to train neural networks. It is used to adjust the weights of the neurons in the network to minimize the error between the predicted output and the actual output.

The basic idea behind backpropagation is to propagate the error back through the network and adjust the weights accordingly. This is done by calculating the gradient of the error with respect to the weights and then updating the weights in the opposite direction of the gradient.

The process of backpropagation consists of two steps. First, the forward pass is done where the output of the network is calculated given the input. Second, the backward pass is done where the error is calculated and the weights are adjusted accordingly.

The forward pass of backpropagation is done by propagating the inputs through the network and calculating the output of each neuron. The output of each neuron is calculated using the activation function which is usually a sigmoid or tanh function.

The backward pass of backpropagation is done by calculating the error of the network and then propagating the error back through the network and adjusting the weights accordingly. The error is calculated by comparing the predicted output with the actual output. The error is then propagated back through the network using the chain rule. The chain rule is used to calculate the gradients of the error with respect to the weights. The gradients are then used to update the weights in the opposite direction of the gradient.

The backpropagation algorithm is an important algorithm used in artificial neural networks. It is used to adjust the weights of the neurons in the network to minimize the error between the predicted output and the actual output. The backpropagation algorithm is used in many applications such as image recognition, speech recognition, and natural language processing.