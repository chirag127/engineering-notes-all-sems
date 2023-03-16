# Weights Initialization

- Weights initialization is the process of assigning initial values to the parameters of a neural network before training.
- It is important to choose appropriate initial values for the weights, as they can affect the speed of convergence, the quality of the local minima, and the generalization performance of the network.
- There are different methods for weights initialization, such as random, zero, constant, Xavier, He, and orthogonal initialization.
- Random initialization assigns random values to the weights, usually from a uniform or normal distribution. This method can break the symmetry between the units in the same layer, but it can also cause problems such as vanishing or exploding gradients, poor conditioning, and slow convergence.
- Zero initialization assigns zero values to all the weights. This method can avoid the problems of random initialization, but it can also cause the network to learn nothing, as all the units in the same layer will have the same output and gradient.
- Constant initialization assigns a fixed value to all the weights, such as 1 or -1. This method can also avoid the problems of random initialization, but it can also cause the network to learn nothing, as all the units in the same layer will have the same output and gradient.
- Xavier initialization assigns values to the weights according to the formula:

$$
w_{ij} \sim \mathcal{N}(0, \frac{2}{n_{in} + n_{out}})
$$

where $w_{ij}$ is the weight between the $i$-th unit in the previous layer and the $j$-th unit in the current layer, $n_{in}$ is the number of units in the previous layer, and $n_{out}$ is the number of units in the current layer. This method can preserve the variance of the inputs and outputs across the layers, and prevent the gradients from vanishing or exploding.
- He initialization is a variation of Xavier initialization, which assigns values to the weights according to the formula:

$$
w_{ij} \sim \mathcal{N}(0, \frac{2}{n_{in}})
$$

This method is suitable for networks with rectified linear units (ReLU) as activation functions, as it can account for the non-linearity of ReLU and prevent the variance from shrinking.
- Orthogonal initialization assigns values to the weights such that the weight matrix of each layer is orthogonal, i.e., $W^TW = I$, where $W$ is the weight matrix and $I$ is the identity matrix. This method can preserve the norm of the inputs and outputs across the layers, and prevent the gradients from vanishing or exploding.