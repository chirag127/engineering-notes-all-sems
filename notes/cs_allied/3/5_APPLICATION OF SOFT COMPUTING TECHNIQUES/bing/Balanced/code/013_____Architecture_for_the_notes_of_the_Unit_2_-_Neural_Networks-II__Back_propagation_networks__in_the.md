# Architecture for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- A back propagation network is a type of artificial neural network that uses a supervised learning algorithm to train the network weights based on the error between the actual output and the desired output .
- A back propagation network consists of three main components: an input layer, one or more hidden layers, and an output layer .
- The input layer receives the input data and passes it to the first hidden layer. The hidden layers perform nonlinear transformations on the input data and pass it to the next layer. The output layer produces the final output of the network .
- The network weights are initialized randomly and then adjusted iteratively using the back propagation algorithm .
- The back propagation algorithm consists of two phases: forward propagation and backward propagation .
- In forward propagation, the input data is fed into the network and the output is computed. The output is then compared with the desired output and the error is calculated .
- In backward propagation, the error is propagated back through the network layers and the weights are updated according to a learning rule that minimizes the error .
- The learning rule is based on the gradient descent method, which moves the weights in the opposite direction of the gradient of the error function.
- The back propagation algorithm is repeated until the error is reduced below a certain threshold or a maximum number of iterations is reached .
- The back propagation network can learn complex nonlinear functions and generalize well to unseen data .
- The back propagation network can be applied to various problems such as classification, regression, pattern recognition, image processing, natural language processing, etc  .