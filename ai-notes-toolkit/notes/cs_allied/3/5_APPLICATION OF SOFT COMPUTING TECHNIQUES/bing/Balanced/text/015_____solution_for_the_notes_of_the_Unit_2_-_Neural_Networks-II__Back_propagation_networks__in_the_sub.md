### Solution for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- Back propagation networks are a type of artificial neural networks that use a supervised learning algorithm to produce a desired output .
- The algorithm adjusts the weights of the connections between the nodes in the network according to a feedback signal that measures the error rate of a forward propagation .
- The goal of back propagation is to minimize the error or loss function of the network by updating the weights in the opposite direction of the gradient .
- The steps of the back propagation algorithm are as follows:
  - Initialize the network with random weights and biases.
  - For each training example, perform the following substeps:
    - Feed the input forward through the network and compute the output of each node.
    - Compare the output of the network with the desired output and calculate the error for each output node.
    - Propagate the error backward through the network and compute the error for each hidden node.
    - Update the weights and biases of each connection using the gradient descent rule.
  - Repeat the above steps until the error of the network is sufficiently low or a maximum number of iterations is reached.
- Back propagation networks can be used for various applications, such as classification, regression, pattern recognition, image processing, natural language processing, etc .