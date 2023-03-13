### Backpropagation for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- Backpropagation is a method of training a neural network by adjusting the weights of the connections between the nodes based on the error of the output layer compared to the desired output  .
- Backpropagation consists of two phases: forward propagation and backward propagation .
  - In forward propagation, the input data is fed into the network and the activation of each node is computed until the output layer is reached .
  - In backward propagation, the error of the output layer is calculated and propagated back to the previous layers, using the chain rule of calculus to compute the gradients of the weights with respect to the error .
  - The weights are then updated by subtracting a fraction of the gradients, called the learning rate, from the current weights .
- Backpropagation is sensitive to the initial conditions of the weights, which can affect the convergence and the quality of the solution .
  - A common practice is to initialize the weights randomly with small values close to zero, to avoid symmetry and saturation problems .
  - Another technique is to use a pre-training phase, where the network is trained in an unsupervised manner to learn useful features from the data, before fine-tuning it with backpropagation.
- Backpropagation is a fundamental component of deep learning, as it enables the training of complex and non-linear models that can learn from large amounts of data  .
  - However, backpropagation also has some limitations and challenges, such as the vanishing gradient problem, the exploding gradient problem, the local minima problem, the overfitting problem, and the computational cost .
  - Various techniques have been proposed to overcome or mitigate these issues, such as regularization, normalization, optimization algorithms, activation functions, and network architectures .

#### Mnemonics and learning tricks

- One possible mnemonic to remember the steps of backpropagation is **FEBRU**:
  - **F**orward propagation: compute the activations of each node from input to output
  - **E**rror calculation: compute the difference between the output layer and the desired output
  - **B**ackward propagation: compute the gradients of the weights with respect to the error using the chain rule
  - **R**ate of learning: choose a fraction of the gradients to update the weights
  - **U**pdate the weights: subtract the learning rate times the gradients from the current weights
- Another possible mnemonic to remember the formula for updating the weights is **WAG**:
  - **W**eight: the current value of the weight
  - **A**lpha: the learning rate
  - **G**radient: the partial derivative of the error with respect to the weight
  - The formula is: W = W - alpha * G
- A possible learning trick to understand the chain rule in backpropagation is to use a graphical representation of the network and the error, and draw arrows to indicate the direction and the magnitude of the gradients .
  - For example, see the figure below for a simple network with one hidden layer and one output node:

```
    x1  x2
     \  /
      h
     / \
    y   e
```

  - The error e is computed as the difference between the output y and the desired output t: e = y - t
  - The output y is computed as the activation of the node h, which is a function of the weighted sum of the inputs x1 and x2: y = f(w1 * x1 + w2 * x2)
  - The gradient of the error with respect to the weight w1 is computed as the product of the gradients along the path from e to w1: d(e)/d(w1) = d(e)/d(y) * d(y)/d(w1)
  - The gradient of the error with respect to the weight w2 is computed similarly: d(e)/d(w2) = d(e)/d(y) * d(y)/d(w2)
  - The gradients