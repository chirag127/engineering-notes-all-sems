### Neural networks as universal function approximators for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- A neural network is a computational model that consists of layers of artificial neurons that can process and learn from data.
- A neural network can be seen as a function approximator that maps inputs to outputs, such as images to labels, texts to sentiments, or board states to moves.
- A function approximator is a model that can learn to approximate any target function from a given set of functions, such as continuous functions, differentiable functions, or polynomial functions.
- A universal function approximator is a model that can learn to approximate any target function from a very large or infinite set of functions, such as all continuous functions on a compact subset of the Euclidean space.
- The universal approximation theorem is a mathematical result that states that a feed-forward neural network with a single hidden layer containing a finite number of neurons can approximate any continuous function on a compact subset of the Euclidean space, under mild assumptions on the activation function .
- The universal approximation theorem implies that neural networks have a kind of universality, i.e., no matter what the target function is, there is a network that can approximately approach the result and do the job.
- The universal approximation theorem does not provide a construction for the weights of the network, but merely states that such a construction is possible.
- The universal approximation theorem also does not guarantee that the network can be trained efficiently or generalize well to new data, as these depend on other factors such as the optimization algorithm, the regularization technique, and the data distribution.
- There are also other versions of the universal approximation theorem that consider different architectures, such as networks with arbitrary depth, networks with bounded depth and bounded width, or networks with graph input.
- There are also other types of function approximators that are universal, such as radial basis functions or convolutional neural networks .

#### Mnemonics and learning tricks

- A possible mnemonic to remember the universal approximation theorem is: **U**niversal **A**pproximation **T**heorem: **U**nlimited **A**ctivation **T**ypes.
- A possible learning trick to understand the universal approximation theorem is to visualize how a neural network can approximate a simple function, such as a sine wave, by adjusting the weights and biases of the neurons. A tool that can help with this is: https://playground.tensorflow.org/