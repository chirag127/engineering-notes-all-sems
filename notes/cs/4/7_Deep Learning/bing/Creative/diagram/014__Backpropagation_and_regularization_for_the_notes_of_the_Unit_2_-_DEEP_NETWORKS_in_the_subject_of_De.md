Backpropagation and regularization are two important concepts in deep learning. Backpropagation is an algorithm for computing the gradients of the loss function with respect to the parameters of a neural network. Regularization is a technique for reducing overfitting and improving generalization of the neural network.

One way to draw a detailed ASCII diagram for backpropagation and regularization is to use a computation graph, which is a graphical representation of the operations and functions involved in the neural network. A computation graph can show the forward pass, where the inputs are propagated through the network to produce the outputs, and the backward pass, where the gradients are computed using the chain rule.

Here is an example of a computation graph for a simple neural network with one hidden layer and L2 regularization. The network has two inputs x1 and x2, one hidden layer with two units h1 and h2, and one output unit y. The activation functions are sigmoid for the hidden layer and linear for the output layer. The loss function is mean squared error (MSE) plus L2 regularization.

The diagram uses the following symbols:

- `*` for multiplication
- `+` for addition
- `-` for subtraction
- `/` for division
- `^` for exponentiation
- `|` for absolute value
- `()` for grouping
- `[]` for indexing
- `<>` for partial derivatives
- `=` for assignment
- `->` for forward pass
- `<-` for backward pass
- `#` for comments

The diagram also shows the values of the parameters and the gradients for a sample input-output pair (x1, x2) = (0.5, 0.2) and y = 0.8. The regularization parameter is 0.1.

The diagram is as follows:

```
# Forward pass
x1 = 0.5 -> x2 = 0.2 ->

# Hidden layer
w11 = 0.1 -> w12 = 0.2 -> w21 = 0.3 -> w22 = 0.4 -> b1 = 0.5 -> b2 = 0.6 ->
z1 = w11 * x1 + w21 * x2 + b1 = 0.25 -> z2 = w12 * x1 + w22 * x2 + b2 = 0.34 ->
h1 = sigmoid(z1) = 0.562 -> h2 = sigmoid(z2) = 0.584 ->

# Output layer
v1 = 0.7 -> v2 = 0.8 -> c = 0.9 ->
y_hat = v1 * h1 + v2 * h2 + c = 1.507 ->

# Loss function
y = 0.8 ->
L = 0.5 * (y_hat - y)^2 + 0.5 * 0.1 * (w11^2 + w12^2 + w21^2 + w22^2 + v1^2 + v2^2) = 0.271 ->

# Backward pass
<- dL/dy_hat = (y_hat - y) + 0.1 * (v1 + v2) = 0.757 <-
<- dL/dv1 = dL/dy_hat * h1 + 0.1 * v1 = 0.526 <-
<- dL/dv2 = dL/dy_hat * h2 + 0.1 * v2 = 0.548 <-
<- dL/dc = dL/dy_hat = 0.757 <-
<- dL/dh1 = dL/dy_hat * v1 = 0.530 <-
<- dL/dh2 = dL/dy_hat * v2 = 0.606 <-
<- dL/dz1 = dL/dh1 * h1 * (1 - h1) = 0.131 <-
<- dL/dz2 = dL/dh2 * h2 * (1 - h2) = 0.146 <-
<- dL/dw11 = dL/dz1 * x1 + 0.1 * w11 = 0.076 <-
<- dL/dw12 = dL/dz2 * x1 + 0.1 * w12 = 0.083 <-
<- dL/dw21 = dL/dz1 * x2 + 0.1 * w21 = 0.