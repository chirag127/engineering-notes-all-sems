### Intro to Neural Nets for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

- Neural networks are flexible and powerful data-processing tools that can learn from data and make predictions or decisions.
- Neural networks are inspired by the structure and function of the human brain, which consists of billions of interconnected neurons.
- Neural networks are composed of artificial neurons, which are simple computational units that receive and process input data.
- Each artificial neuron has a set of weights and a bias that determine how the input data is transformed and an activation function that determines the output of the neuron.
- The output of one neuron can be the input of another neuron, forming a network of connections.
- Neural networks can have multiple layers of neurons, such as an input layer, one or more hidden layers, and an output layer.
- The input layer receives the raw data, the hidden layer(s) perform intermediate computations, and the output layer produces the final prediction or decision.
- The hidden layer(s) can have different architectures and functions, such as convolutional, recurrent, or attention-based layers.
- Neural networks can learn from data by adjusting their weights and biases through a process called training.
- Training involves feeding data to the network, comparing the network output with the desired output, and updating the weights and biases using a learning algorithm, such as gradient descent.
- Neural networks can perform various tasks, such as classification, regression, clustering, dimensionality reduction, image recognition, natural language processing, and more.
- Neural networks have some advantages, such as being able to handle nonlinear and complex relationships, being able to generalize to new data, and being able to learn from large amounts of data.
- Neural networks also have some disadvantages, such as being prone to overfitting, being computationally expensive, being difficult to interpret, and being sensitive to the choice of hyperparameters.

#### Mnemonics and learning tricks

- A possible mnemonic to remember the components of a neural network is **WABO**:

  - **W**eights: the parameters that multiply the input data
  - **A**ctivation: the function that determines the output of a neuron
  - **B**ias: the parameter that adds to the input data
  - **O**utput: the result of the neuron computation

- A possible learning trick to understand the concept of activation functions is to think of them as **switches** that turn on or off the neurons depending on the input data. For example, a binary step function can be seen as a switch that turns on the neuron if the input is above a certain threshold and turns it off otherwise. Other activation functions, such as sigmoid, tanh, or ReLU, can be seen as switches that have different degrees of sensitivity or smoothness.