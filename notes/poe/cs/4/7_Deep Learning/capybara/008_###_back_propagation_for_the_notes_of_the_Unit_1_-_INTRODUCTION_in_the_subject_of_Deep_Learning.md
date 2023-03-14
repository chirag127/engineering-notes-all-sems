### Back Propagation for the Notes of Unit 1 - Introduction in the Subject of Deep Learning

Back propagation is an essential algorithm for supervised learning in deep neural networks. It is used to adjust the weights of the network to minimize the error between the predicted output and the actual output. 

Below are some key points to remember about back propagation:

- Back propagation is a method to calculate the gradients of the error function with respect to the weights of the network. The gradients are used to update the weights to minimize the error.
- The back propagation algorithm consists of two phases: the forward phase and the backward phase. In the forward phase, the input is propagated through the network, and the output is calculated. In the backward phase, the error is propagated backwards through the network, and the gradients are calculated.
- Back propagation uses the chain rule of calculus to calculate the gradients. The chain rule states that the derivative of a composite function is equal to the product of the derivatives of the individual functions.
- The back propagation algorithm can be sensitive to the choice of the activation function used in the network. The most commonly used activation functions are sigmoid, ReLU, and tanh.
- There are variants of the back propagation algorithm, such as stochastic gradient descent (SGD), mini-batch gradient descent, and batch gradient descent. SGD updates the weights after each training example, while batch gradient descent updates the weights after processing the entire training set. Mini-batch gradient descent is a compromise between the two, where the weights are updated after processing a small batch of training examples.
- Back propagation can be computationally expensive, especially for deep networks with many layers. To speed up the training process, several techniques can be used, such as weight initialization, regularization, and dropout.
- One mnemonic to remember the steps of back propagation is "feed-forward, backpropagate, update weights". This reminds us that we first propagate the input forward through the network, then backpropagate the error backwards, and finally update the weights to minimize the error.

In summary, back propagation is a crucial algorithm for training deep neural networks. Understanding its principles and variants is essential for achieving good performance in deep learning tasks.