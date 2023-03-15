### Solution for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of Application of Soft Computing

- A back propagation network is a type of artificial neural network that uses a supervised learning algorithm to produce a desired output .
- The algorithm adjusts the weights of the connections between the nodes in the network according to a feedback signal that indicates the error rate of a forward propagation .
- The goal of back propagation is to minimize the error or loss function by updating the weights in the opposite direction of the gradient of the error function with respect to the weights .
- The steps of the back propagation algorithm are as follows:
  - Initialize the network with random weights and biases.
  - For each training example, perform the following substeps:
    - Feed the input forward through the network and compute the output of each node.
    - Compare the output of the network with the desired output and calculate the error for each output node.
    - Propagate the error backward through the network and compute the error gradient for each weight and bias.
    - Update the weights and biases by subtracting a fraction of the error gradient from the current values.
  - Repeat the above steps until the error is sufficiently low or a maximum number of iterations is reached.
- Back propagation networks can be used for various applications, such as classification, regression, pattern recognition, image processing, natural language processing, etc .