## Unit 2 - DEEP NETWORKS

- A deep neural network (DNN) is an artificial neural network (ANN) with multiple layers between the input and output layers.
- A layer is a set of units (also called neurons or nodes) that perform some computation on the inputs they receive from the previous layer or the data source.
- A unit is a function that takes a weighted sum of its inputs, adds a bias term, and applies a non-linear activation function to produce an output.
- A weight is a numerical value that determines the strength of the connection between two units. A bias is a constant term that shifts the input of the activation function.
- An activation function is a function that introduces non-linearity into the network, allowing it to learn complex patterns and functions. Some common activation functions are sigmoid, tanh, ReLU, softmax, etc.
- A deep network can have different types of layers, such as fully connected, convolutional, recurrent, attention, etc., depending on the nature and structure of the data and the task to be performed.
- A fully connected layer is a layer where each unit is connected to every unit in the previous layer. It is also called a dense layer. It is often used as the final layer of a network to produce the output.
- A convolutional layer is a layer where each unit is connected to a local region of the previous layer, defined by a filter or a kernel. It is often used to process image data, as it can capture spatial features and patterns.
- A recurrent layer is a layer where each unit has a connection to itself, allowing it to store some information from the previous time step. It is often used to process sequential data, such as text or speech, as it can capture temporal dependencies and context.
- An attention layer is a layer where each unit can learn to focus on a subset of the previous layer, based on some query or context. It is often used to enhance the performance of recurrent or convolutional layers, as it can capture long-range dependencies and relevance.
- A deep network can be trained using gradient descent, an optimization algorithm that iteratively updates the weights and biases of the network to minimize a loss function, which measures the difference between the network output and the desired output.
- A loss function is a function that quantifies how well the network performs on a given data point or a batch of data points. Some common loss functions are mean squared error, cross entropy, hinge loss, etc.
- Gradient descent requires the computation of the gradient of the loss function with respect to the weights and biases of the network, which is done using the backpropagation algorithm, a technique that applies the chain rule of calculus to propagate the error signals from the output layer to the input layer.
- Gradient descent can have different variants, such as stochastic gradient descent, mini-batch gradient descent, momentum, Nesterov accelerated gradient, AdaGrad, RMSProp, Adam, etc., depending on how the learning rate and the direction of the update are determined.
- A learning rate is a hyperparameter that controls how much the weights and biases are changed in each iteration of gradient descent. A high learning rate can lead to faster convergence, but also to instability and divergence. A low learning rate can lead to slower convergence, but also to better accuracy and generalization.
- A deep network can be evaluated using different metrics, such as accuracy, precision, recall, F1-score, ROC curve, AUC, etc., depending on the type and objective of the task. These metrics measure how well the network can classify, predict, or generate the output given the input.
- A deep network can have different applications, such as image recognition, natural language processing, speech recognition, machine translation, computer vision, natural language generation, etc., depending on the domain and problem to be solved.
- A deep network can also have different challenges, such as overfitting, underfitting, vanishing gradient, exploding gradient, adversarial examples, etc., depending on the architecture, data, and training of the network. These challenges can affect the performance and robustness of the network.

Some mnemonics and learning tricks for Unit 2 - DEEP NETWORKS are:

- DNN: Deep Neural Network, a network with multiple layers between input and output.
- LAYER: A set of units that perform some computation on the inputs.
- UNIT: A function that takes a weighted sum of inputs, adds a bias, and applies an activation function.
- WEIGHT: A numerical value that determines the strength of the connection between two units.
- BIAS: A constant term that shifts the input of the