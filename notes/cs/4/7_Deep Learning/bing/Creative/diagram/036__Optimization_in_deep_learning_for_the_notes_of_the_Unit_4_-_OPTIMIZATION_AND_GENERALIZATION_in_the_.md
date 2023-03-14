Optimization in deep learning is the process of finding the optimal values of the parameters (such as weights and biases) of a deep neural network that minimize a loss function (such as cross-entropy or mean squared error) and maximize the performance (such as accuracy or recall) on a given dataset. Optimization methods in deep learning can be classified into two categories: first-order methods and second-order methods. First-order methods only use the gradient information of the loss function, while second-order methods also use the Hessian matrix or its approximation. First-order methods are more widely used in deep learning because they are simpler, faster, and more scalable than second-order methods.

The following diagram illustrates the basic architecture of a deep neural network and the optimization process:

```
+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|    Input       |    |    Hidden      |    |    Hidden      |    |    Output      |
|    layer       |    |    layer       |    |    layer       |    |    layer       |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |----|                |----|                |----|                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+

    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    V                 V                 V                 V                 V

+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|    Weights     |    |    Weights     |    |    Weights     |    |    Weights     |
|    matrix      |    |    matrix      |    |    matrix      |    |    matrix      |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
+----------------+    +----------------+    +----------------+    +----------------+

    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    |                 |                 |                 |                 |
    V                 V                 V                 V                 V

+----------------+    +----------------+    +----------------+    +----------------+
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|                |    |                |    |                |    |                |
|    Biases      |    |    Biases      |