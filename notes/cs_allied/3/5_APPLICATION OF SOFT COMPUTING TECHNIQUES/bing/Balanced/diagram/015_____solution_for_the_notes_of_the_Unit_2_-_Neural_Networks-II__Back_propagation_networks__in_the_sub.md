### Solution for the notes of the Unit 2 - Neural Networks-II (Back propagation networks) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- Back propagation networks are a type of artificial neural networks that use a supervised learning algorithm to produce a desired output .
- The algorithm adjusts the weights of the connections between the nodes in the network according to a feedback signal that indicates the error rate of a forward propagation .
- The goal of back propagation is to minimize the error or loss function, which measures the difference between the actual output and the desired output .
- The steps of back propagation are as follows :
  - Initialize the network with random weights and biases.
  - For each input-output pair in the training data, perform the following sub-steps:
    - Feed the input forward through the network and compute the output at each layer.
    - Compare the output of the network with the desired output and calculate the error.
    - Propagate the error backward through the network and compute the gradient of the error with respect to each weight and bias.
    - Update the weights and biases by subtracting a fraction of the gradient, called the learning rate.
  - Repeat the above steps until the error is sufficiently small or a maximum number of iterations is reached.
- Back propagation networks can be used for various applications, such as classification, regression, pattern recognition, image processing, natural language processing, etc .