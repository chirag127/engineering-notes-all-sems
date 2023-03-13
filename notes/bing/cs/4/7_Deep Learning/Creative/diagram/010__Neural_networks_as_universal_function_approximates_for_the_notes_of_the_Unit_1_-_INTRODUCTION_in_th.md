A neural network is a universal function approximator if it can approximate any continuous function on a compact subset of the input space, given enough hidden units and a suitable activation function. The following diagram illustrates the basic architecture of a neural network as a universal function approximator:

```
Input layer: x1, x2, ..., xn
Hidden layer: h1, h2, ..., hm
Output layer: y
Activation function: f
Weights: w
Bias: b

x1 ---w11---> h1 ---w1---> y
|             |             |
w21          f             f
|             |             |
x2 ---w22---> h2 ---w2---> y
|             |             |
w31          f             f
|             |             |
...   ...     ...   ...     ...
|             |             |
wn1          f             f
|             |             |
xn ---wn2---> hm ---wm---> y
              |             |
              b             b
```

The output of the neural network is given by the following formula:

y = f(w1 * f(w11 * x1 + w21 * x2 + ... + wn1 * xn + b) + w2 * f(w22 * x1 + w22 * x2 + ... + wn2 * xn + b) + ... + wm * f(wm1 * x1 + wm2 * x2 + ... + wmn * xn + b) + b)

The universal approximation theorem states that for any continuous function g on a compact subset of the input space, there exists a neural network with one hidden layer and a finite number of hidden units that can approximate g with arbitrary accuracy. This means that neural networks can learn to represent any complex nonlinear function, given enough data and training. However, the theorem does not provide a practical way to find the optimal weights and biases for the neural network, nor does it guarantee that the neural network will generalize well to unseen data. Therefore, neural networks are powerful but challenging tools for function approximation.