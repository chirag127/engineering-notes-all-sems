Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch. This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks .

The following diagram illustrates the basic architecture of a batch normalization layer in a deep neural network. The diagram is drawn using ASCII characters.

```
Input layer: x1, x2, ..., xn
|
|  W1
|  |
|  v
|  z1
|  |
|  v
|  a1
|  |
|  v
Batch normalization layer: y1, y2, ..., yn
|  |
|  v
|  u1
|  |
|  v
|  b1
|  |
|  v
Output layer: y_hat1, y_hat2, ..., y_hatn

Legend:
W1: weight matrix of the first layer
z1: linear combination of the input layer and the weight matrix
a1: activation function applied to z1
y1, y2, ..., yn: normalized inputs for each mini-batch
u1: linear combination of the normalized inputs and a scale parameter gamma
b1: bias term added to u1
y_hat1, y_hat2, ..., y_hatn: output of the batch normalization layer
```