### Architecture for the notes of the Unit 2 - Neural Networks-II (Back propagation networks)

- A back propagation neural network is a **multilayer, feed-forward neural network** consisting of an input layer, hidden layer and an output layer .
- The neurons present in the hidden and output layers have **biases**, which are the connections from the units whose activation is always 1.
- The input layer receives the input data and passes it to the hidden layer. The hidden layer performs some computations and transfers the result to the output layer. The output layer produces the final output.
- The network is trained by adjusting the weights and biases of the neurons using the **back propagation algorithm**, which is a method for minimizing the error between the desired and actual output .
- The back propagation algorithm involves two phases: **forward propagation** and **backward propagation** .
- In forward propagation, the input data is fed to the input layer and the output is computed by passing it through the hidden and output layers. The output is then compared with the desired output to calculate the error .
- In backward propagation, the error is propagated back through the network, starting from the output layer to the hidden layer and then to the input layer. The weights and biases are updated according to the gradient of the error with respect to each parameter .
- The process of forward and backward propagation is repeated until the error is minimized or a predefined number of iterations is reached .
- The back propagation algorithm can be applied to various types of neural networks, such as **spiking neural networks** (SNNs), which use spikes as the communication signals between neurons.
- The back propagation algorithm can also be modified to incorporate different learning rules, such as **momentum**, **adaptive learning rate**, **dropout**, **regularization**, etc., to improve the performance and generalization of the neural network .