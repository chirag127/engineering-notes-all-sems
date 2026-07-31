 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Backpropagation Learning Methods

1. Feedforward Propagation: In this step, the input is fed to the neural network and its effect propagates through the network layer by layer. The output is then calculated.
2. Backpropagation: It is a method used to determine the error in the output and calculate the changes required in the weights of the connections to minimize the error. It happens in two passes:
- Forward pass: The input is fed forward to calculate the output.
- Backward pass: The output error is propagated back and the changes in weights are calculated.
3. Weight Update: In this step, the weights of the connections are updated by applying the changes calculated in the backpropagation step. This step makes the neural network learn from the input data.
4. Repeat: The above three steps are repeated multiple times for all the training examples until the network learns the patterns in the data.

The key steps in backpropagation are:
1. Compute the output activation values for each layer
2. Compute the error at the output layer. The error is the difference between the actual output and the expected output.
3. Compute the error terms for the hidden layers. This is done by propagating the error from the output layer back to the hidden layers.
4. Update the weights. Use the error terms to determine how to change the weights to reduce the error.

The backpropagation algorithm allows the neural network to be trained using examples, making it a popular learning technique for training multilayer perceptrons.