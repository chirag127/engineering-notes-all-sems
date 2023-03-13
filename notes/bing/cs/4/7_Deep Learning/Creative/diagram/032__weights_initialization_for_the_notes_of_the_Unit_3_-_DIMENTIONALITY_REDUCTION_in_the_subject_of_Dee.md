Weight initialization is a procedure to set the weights of a neural network to small random values that define the starting point for the optimization (learning or training) of the neural network model. Different weight initialization techniques can have a significant impact on the performance and convergence of the model, especially for deep neural networks.

One of the common weight initialization techniques is the **Xavier initialization**, also known as **Glorot initialization**, which is suitable for layers that use the **sigmoid** or **tanh** activation functions. The idea is to initialize the weights with a uniform or normal distribution that has a zero mean and a variance of 1 / n_in, where n_in is the number of inputs to the layer. This helps to keep the variance of the activations and gradients consistent across the layers and prevent vanishing or exploding gradients.

Another weight initialization technique is the **He initialization**, also known as **Kaiming initialization**, which is suitable for layers that use the **ReLU** or **Leaky ReLU** activation functions. The idea is to initialize the weights with a normal distribution that has a zero mean and a variance of 2 / n_in, where n_in is the number of inputs to the layer. This helps to overcome the problem of dying ReLU units, where some neurons become inactive and stop learning.

The following diagram illustrates the basic architecture of a deep neural network with three hidden layers and two output units, and shows how the weights are initialized using the Xavier and He techniques:

```
Input layer (n_in = 4)             Hidden layer 1 (n_h1 = 3)        Hidden layer 2 (n_h2 = 2)        Hidden layer 3 (n_h3 = 2)        Output layer (n_out = 2)

x1 ------------------------------> h1 ----------------------------> h5 ----------------------------> h7 ----------------------------> y1
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
x2 ------------------------------> h2 ----------------------------> h6 ----------------------------> h8 ----------------------------> y2
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
|                                 |                               |                               |                               |
x3 ------------------------------> h3
|                                 |
|                                 |
|                                 |
|                                 |
|                                 |
|                                 |
x4 ------------------------------> h4

Weights initialization:

Xavier: W ~ U[-sqrt(1/n_in), sqrt(1/n_in)] or N(0, 1/n_in)

He: W ~ N(0, 2/n_in)

Examples:

W1_11 ~ U[-sqrt(1/4), sqrt(1/4)] or N(0, 1/4) for Xavier
W1_11 ~ N(0, 2/4) for He

W2_12 ~ U[-sqrt(1/3), sqrt(1/3)] or N(0, 1/3) for Xavier
W2_12 ~ N(0, 2/3) for He

W3_21 ~ U[-sqrt(1/2), sqrt(1/2)] or N(0, 1/2) for Xavier
W3_21 ~ N(0, 2/2) for He

W4_22 ~ U[-sqrt(1/2), sqrt(1/2)] or N(0, 1/2) for Xavier
W4_22 ~ N(0, 2/2) for He

W5_11 ~ U[-sqrt(1/2), sqrt(1/2)] or N(0, 1/2) for Xavier
W5_11 ~ N(0, 2/2) for He

W6_12 ~ U[-sqrt(1/2), sqrt(1/2)] or N(0, 1/2) for Xavier
W6_12 ~ N(0, 2/2) for He
```