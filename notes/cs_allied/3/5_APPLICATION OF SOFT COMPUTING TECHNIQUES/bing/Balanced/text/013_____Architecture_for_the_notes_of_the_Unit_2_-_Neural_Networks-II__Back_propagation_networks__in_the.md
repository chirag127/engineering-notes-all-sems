### Architecture for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- A back propagation neural network is a multilayer, feed-forward neural network consisting of an input layer, hidden layer and an output layer.
- The neurons present in the hidden and output layers have biases, which are the connections from the units whose activation is always 1.
- The input layer receives the input data and passes it to the hidden layer. The hidden layer performs some computations and transfers the results to the output layer. The output layer produces the final output.
- The number of neurons in the input and output layers depends on the problem domain, while the number of neurons in the hidden layer is usually determined by trial and error.
- The network structure is one input layer, one hidden layer, and one output layer is a standard network structure, but more hidden layers can be added for complex problems.
- The network learns by adjusting the weights of the connections between the layers using a learning algorithm called backpropagation.
- Backpropagation is a method for training the weights in a multilayer feed-forward neural network by propagating the error rate of a forward propagation backward through the neural network layers.
- Backpropagation involves two phases: a forward pass and a backward pass.
- In the forward pass, the input data is fed to the input layer and the output is computed by passing it through the hidden and output layers. The output is then compared with the desired output to calculate the error.
- In the backward pass, the error is propagated back to the hidden and output layers, and the weights are updated according to a gradient descent rule that minimizes the error.
- The process of forward and backward pass is repeated until the error is reduced to an acceptable level or a maximum number of iterations is reached.
- The backpropagation algorithm can be applied to different types of activation functions, such as sigmoid, tanh, or ReLU.
- The backpropagation algorithm can also be modified by using different learning methods, such as momentum, adaptive learning rate, or regularization.
- The backpropagation network is a powerful and widely used model for solving various problems, such as classification, regression, pattern recognition, image processing, natural language processing, etc.