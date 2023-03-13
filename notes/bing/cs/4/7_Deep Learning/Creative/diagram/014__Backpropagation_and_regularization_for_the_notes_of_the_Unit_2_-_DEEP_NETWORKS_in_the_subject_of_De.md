Backpropagation is a widely used method for calculating derivatives inside deep feedforward neural networks. It forms an important part of a number of supervised learning algorithms for training feedforward neural networks, such as stochastic gradient descent. Backpropagation is based on the chain rule of derivatives and consists of two phases: forward propagation and backward propagation.

Regularization is a technique to prevent overfitting in neural networks by adding a penalty term to the loss function. Regularization can be applied in different ways, such as weight decay, dropout, early stopping, etc. Regularization helps to reduce the complexity of the model and improve its generalization performance.

The following diagram illustrates the basic architecture of a feedforward neural network with backpropagation and regularization:

```
    Input layer        Hidden layer       Output layer
    +---------+        +---------+        +---------+
    | x1      |        | h1      |        | y1      |
    +---------+        +---------+        +---------+
    | x2      |        | h2      |        | y2      |
    +---------+        +---------+        +---------+
    | x3      |        | h3      |        | y3      |
    +---------+        +---------+        +---------+
    | x4      |        | h4      |        | y4      |
    +---------+        +---------+        +---------+

    +---------+        +---------+        +---------+
    | w11     |        | w21     |        | w31     |
    +---------+        +---------+        +---------+
    | w12     |        | w22     |        | w32     |
    +---------+        +---------+        +---------+
    | w13     |        | w23     |        | w33     |
    +---------+        +---------+        +---------+
    | w14     |        | w24     |        | w34     |
    +---------+        +---------+        +---------+

    +---------+        +---------+        +---------+
    | b1      |        | b2      |        | b3      |
    +---------+        +---------+        +---------+

    +---------+        +---------+        +---------+
    | z1      |        | z2      |        | z3      |
    +---------+        +---------+        +---------+

    +---------+        +---------+        +---------+
    | a1      |        | a2      |        | a3      |
    +---------+        +---------+        +---------+

    +---------+        +---------+        +---------+
    | L       |        | R       |        | J       |
    +---------+        +---------+        +---------+

    +---------+        +---------+        +---------+
    | dL/dy1  |        | dL/dh1  |        | dL/dw31 |
    +---------+        +---------+        +---------+
    | dL/dy2  |        | dL/dh2  |        | dL/dw32 |
    +---------+        +---------+        +---------+
    | dL/dy3  |        | dL/dh3  |        | dL/dw33 |
    +---------+        +---------+        +---------+
    | dL/dy4  |        | dL/dh4  |        | dL/dw34 |
    +---------+        +---------+        +---------+

    +---------+        +---------+        +---------+
    | dL/db3  |        | dL/dw21 |        | dL/dx1  |
    +---------+        +---------+        +---------+
    | dL/dz3  |        | dL/dw22 |        | dL/dx2  |
    +---------+        +---------+        +---------+
    | dL/da3  |        | dL/dw23 |        | dL/dx3  |
    +---------+        +---------+        +---------+
    | dL/dw11 |        | dL/dw24 |        | dL/dx4  |
    +---------+        +---------+        +---------+

    +---------+        +---------+        +---------+
    | d