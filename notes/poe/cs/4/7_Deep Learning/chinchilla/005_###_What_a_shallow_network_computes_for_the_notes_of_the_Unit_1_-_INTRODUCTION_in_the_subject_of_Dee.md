### What a shallow network computes for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

Deep Learning is a subfield of machine learning that focuses on building and training artificial neural networks to model and solve complex problems. Shallow networks, on the other hand, are neural networks with only one hidden layer, making them simpler and easier to train.

In this section, we will discuss what a shallow network computes and how it works.

#### Computational Model of a Shallow Network

A shallow network consists of an input layer, a hidden layer, and an output layer. The input layer receives the input data, and the output layer produces the predictions or classifications based on the input data. The hidden layer performs computations on the input data and generates a set of intermediate representations, also known as features. These features are then fed into the output layer for the final prediction.

The computations performed by a shallow network can be represented mathematically using matrix operations. The input data is first multiplied by a weight matrix, which is a matrix of parameters that the network learns during training. The result of this multiplication is then passed through an activation function, which introduces non-linearity into the network and allows it to model complex relationships between the input and output.

#### Learning in Shallow Networks

Training a shallow network involves adjusting the parameters of the weight matrix so that the network can make accurate predictions on the training data. This is done using an optimization algorithm that minimizes a loss function, which measures the difference between the predicted output and the actual output.

The most commonly used optimization algorithm for shallow networks is called backpropagation, which involves computing the gradient of the loss function with respect to the parameters of the weight matrix and using it to update the parameters in the opposite direction of the gradient.

#### Mnemonic and Learning Tricks

One mnemonic to remember the computational model of a shallow network is "I have a hunch". This stands for Input, Hidden layer, Activation function, and Output.

Another trick to remember the learning process in shallow networks is "backpropagation is the way to go". This emphasizes the importance of backpropagation in adjusting the parameters of the weight matrix during training.

#### Advantages and Disadvantages of Shallow Networks

Some advantages of shallow networks include:

- Simplicity: Shallow networks are simpler and easier to understand than deep networks, making them a good starting point for beginners.
- Faster Training: Shallow networks train faster than deep networks, making them more suitable for tasks that require quick results.
- Less Overfitting: Shallow networks are less prone to overfitting than deep networks, especially when the amount of training data is limited.

Some disadvantages of shallow networks include:

- Limited Representation: Shallow networks have limited representation power and may not be able to model complex relationships between the input and output as effectively as deep networks.
- Tendency to Get Stuck in Local Minima: Shallow networks are more likely to get stuck in local minima during training, which can affect the accuracy of the predictions.
- Lack of Contextual Information: Shallow networks do not take into account contextual information, such as the order of the input data, which can be important for some tasks.

#### Examples and Applications

Shallow networks are commonly used in various applications, including:

- Image classification and object recognition
- Speech recognition and natural language processing
- Financial forecasting and stock market analysis
- Fraud detection and anomaly detection
- Recommendation systems and personalized marketing

Some popular examples of shallow networks include logistic regression, support vector machines, and single-layer perceptrons.