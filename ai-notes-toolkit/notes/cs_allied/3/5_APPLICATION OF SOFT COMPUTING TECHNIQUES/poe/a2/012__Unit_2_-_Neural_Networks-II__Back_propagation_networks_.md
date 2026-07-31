 Here is the content in Markdown format without any emojis or external links as per your instructions:

## Unit 2 - Neural Networks-II (Back propagation networks)

1. Backpropagation is a method used to train multi-layered neural networks. It is done layer by layer, starting from the output layer and moving backwards towards the input layer.
2. The training process involves two steps for each layer:
    1. Forward propagation: The input is propagated forward through the network to generate an output. The error between the actual output and expected output is calculated.
    2. Backward propagation: The error is propagated backwards through the network. The weights are adjusted to minimize the error. This process is repeated until the error is minimized.
3. The benefits of backpropagation are:
    1. It is computationally efficient as it uses the calculations from forward propagation.
    2. It can train networks with multiple layers as it calculates gradients layer by layer.
    3. It has been successfully used to train complex neural networks in various applications.
4. The limitations of backpropagation are:
    1. Choosing the right learning rate is critical. If the learning rate is too high, the algorithm can oscillate and diverge. If it is too low, the training can take a long time to converge.
    2. Getting stuck in local minima - Backpropagation may get stuck in local minima and not find the global minimum.
    3. Requirement of differentiable activation functions - Backpropagation requires the use of activation functions that are differentiable, limiting the options.

The above content summarizes the key points about backpropagation in neural networks in a formal manner as instructed, without any emojis or external links. Please let me know if you would like me to modify or expand the content.