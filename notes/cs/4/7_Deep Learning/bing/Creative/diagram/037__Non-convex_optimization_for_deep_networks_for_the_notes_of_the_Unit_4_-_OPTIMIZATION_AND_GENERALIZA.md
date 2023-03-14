Non-convex optimization for deep networks is a challenging problem that involves finding the optimal parameters of a non-linear and non-convex function that represents the neural network. A non-convex function may have multiple local minima, saddle points, and flat regions that make it difficult to find the global minimum. However, non-convex optimization techniques have been shown to be effective in training deep neural networks and achieving state-of-the-art results in various domains .

The following diagram illustrates the basic architecture of a deep neural network and the non-convex optimization problem:

```
    Input layer            Hidden layers            Output layer
    x1 x2 ... xn           h1 h2 ... hm             y1 y2 ... yk
    |  |   |               |  |   |                 |  |   |
    v  v   v               v  v   v                 v  v   v
    o--o---o--- ... ---o---o--o---o--- ... ---o---o--o---o---o
    |  |   |   |   |   |   |  |   |   |   |   |   |  |   |   |
    W1 W2  W3  ...  Wl  Wl+1 Wl+2 Wl+3 ... Wl+m Wl+m+1 Wl+m+2 Wl+m+k
    |  |   |   |   |   |   |  |   |   |   |   |   |  |   |   |
    o--o---o--- ... ---o---o--o---o--- ... ---o---o--o---o---o
    ^  ^   ^               ^  ^   ^                 ^  ^   ^
    |  |   |               |  |   |                 |  |   |
    b1 b2  b3              bl bl+1 bl+2             bl+m bl+m+1 bl+m+k
```

The input layer consists of n nodes that represent the features of the input data. The output layer consists of k nodes that represent the predictions of the network. The hidden layers consist of m nodes each that represent the intermediate representations of the data. Each node in the network is connected to the nodes in the previous and next layers by weights W that represent the strength of the connections. Each node also has a bias b that represents the offset of the node. The network can be seen as a function f(x; W, b) that maps the input x to the output y.

The non-convex optimization problem is to find the optimal values of W and b that minimize a loss function L(y, f(x; W, b)) that measures the discrepancy between the true labels y and the predicted labels f(x; W, b). The loss function is a non-convex function of W and b, and may have multiple local minima, saddle points, and flat regions. The optimization problem can be written as:

```
    min_{W, b} L(y, f(x; W, b))
```

There are various methods to solve this non-convex optimization problem, such as gradient descent, stochastic gradient descent, momentum, Adam, etc. These methods rely on computing the gradient of the loss function with respect to W and b, and updating the parameters in the opposite direction of the gradient. However, these methods are not guaranteed to find the global minimum, and may get stuck in a suboptimal solution. Therefore, various techniques have been proposed to improve the convergence and performance of these methods, such as initialization, regularization, learning rate scheduling, batch normalization, etc. These techniques aim to avoid or escape the local minima, saddle points, and flat regions, and to find a good solution that generalizes well to unseen data  .