# Backpropagation Algorithm

- Backpropagation is an algorithm for supervised learning of artificial neural networks using gradient descent.
- It is based on generalizing the Widrow-Hoff learning rule, which adjusts the weights of the network according to the error between the desired and actual output.
- It works by propagating the error backwards from the output layer to the input layer, and updating the weights of the network accordingly.
- The steps of the backpropagation algorithm are as follows  :

  1. Initialize the weights of the network randomly.
  2. For each training example, perform the following steps:
     - Feed the input forward through the network and compute the output of each layer.
     - Calculate the error of the output layer by comparing it with the desired output.
     - For each layer, starting from the output layer and moving backwards, compute the error term of each node, which is the product of the node's output error and the derivative of its activation function.
     - For each weight in the network, calculate the gradient of the error function with respect to the weight, which is the product of the error term of the node that the weight connects to and the output of the node that the weight comes from.
     - Update the weight by subtracting a fraction of the gradient, called the learning rate, from the weight.
  3. Repeat step 2 until the error of the network is sufficiently small or a maximum number of iterations is reached.