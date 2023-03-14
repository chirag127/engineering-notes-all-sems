The following is a detailed ASCII diagram for neural networks as universal function approximators for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning.

The diagram illustrates the basic architecture of a feed-forward neural network with a single hidden layer containing a finite number of neurons. The network can approximate any continuous function on a compact subset of Rn, under mild assumptions on the activation function.

The network takes an input vector x of dimension n and produces an output vector y of dimension m. The input vector is multiplied by a weight matrix W1 of size n x k, where k is the number of neurons in the hidden layer. The result is then passed through an activation function f, which is usually a nonlinear function such as sigmoid, tanh, or ReLU. The output of the activation function is a vector h of dimension k, which represents the hidden layer. The vector h is then multiplied by another weight matrix W2 of size k x m, and the result is the output vector y.

The network can be trained by adjusting the weights W1 and W2 to minimize the error between the output y and the desired output y*. The error can be measured by a loss function L, such as mean squared error or cross entropy. The weights can be updated by using a gradient descent algorithm, which computes the partial derivatives of the loss function with respect to the weights and subtracts a small fraction of them from the weights.

The network can approximate any continuous function on a compact subset of Rn by choosing an appropriate activation function f and a sufficiently large number of neurons k. This is the essence of the universal approximation theorem, which was proven by Cybenko (1989) for sigmoid activation functions and by Hornik et al. (1989) for general activation functions.

The diagram is shown below using ASCII characters. The input vector x is represented by x1, x2, ..., xn. The output vector y is represented by y1, y2, ..., ym. The hidden layer h is represented by h1, h2, ..., hk. The weight matrices W1 and W2 are represented by w11, w12, ..., wnm. The activation function f is represented by f(.). The loss function L is represented by L(.,.).

```
    y1    y2    ...    ym
    |     |           |
    |     |           |
    v     v           v
w11 *  w12 *  ...  w1m *
    \  /    \     /    \
     \/      \   /      \
      \       \ /        \
       \       *          \
        \     / \          \
         \   /   \          \
          \ /     \          \
           *       *          *
          / \     / \        / \
         /   \   /   \      /   \
        /     \ /     \    /     \
       /       *       \  /       \
      /       / \       \/        \
     /       /   \      /\         \
    /       /     \    /  \         \
   /       /       \  /    \         \
  /       /         \/      \         \
 /       /          /\       \         \
/       /          /  \       \         \
*      *          *    *       *        *
|     |          |    |       |        |
|     |          |    |       |        |
v     v          v    v       v        v
h1    h2         ...  hk-1    hk
|     |          |    |       |        |
|     |          |    |       |        |
v     v          v    v       v        v
f(.)  f(.)       ...  f(.)    f(.)
|     |          |    |       |        |
|     |          |    |       |        |
v     v          v    v       v        v
w11 * w12 *     ...  wk-1n * wkn *
    \  /    \     /    \     /    \
     \/      \   /      \   /      \
      \       \ /        \ /        \
       \       *          *          \
        \     / \        / \         \
         \   /   \      /   \         \
          \ /     \    /     \         \
           *       *  *       *        *
          / \     / \/       / \       / \
         /   \   /  /\