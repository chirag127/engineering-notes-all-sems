I am Sydney, your AI assistant. I can help you with drawing a detailed ASCII diagram for linear models (SVMs and Perceptrons) for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning.

Linear models are a class of machine learning algorithms that learn a linear function or decision boundary from the input data. They can be used for classification or regression tasks. Some examples of linear models are:

- Perceptrons: A perceptron is a simple neural network with a single layer of weights and a threshold activation function. It can learn to classify linearly separable data by adjusting the weights based on the prediction errors. A perceptron can be represented as:

```
    +-----------------+
    |                 |
x1 -| w1              |
    |                 |    +-----+
x2 -| w2              |----| f   |---- y
    |                 |    +-----+
... | ...             |
    |                 |
xn -| wn              |
    |                 |
    +-----------------+
```

where x1, x2, ..., xn are the input features, w1, w2, ..., wn are the weights, f is the activation function (usually a step function), and y is the output label.

- Support Vector Machines (SVMs): A SVM is a linear model that tries to find the optimal hyperplane that maximizes the margin between the classes. It can also use kernels to map the input data to a higher-dimensional space where it is linearly separable. A SVM can be represented as:

```
    +-----------------+
    |                 |
x1 -| w1              |
    |                 |    +-----+
x2 -| w2              |----| f   |---- y
    |                 |    +-----+
... | ...             |
    |                 |
xn -| wn              |
    |                 |
    +-----------------+    +-----+
b ------------------------| +1  |---- positive class
                         +-----+
                         +-----+
b ------------------------| -1  |---- negative class
                         +-----+
```

where x1, x2, ..., xn are the input features, w1, w2, ..., wn are the weights, b is the bias term, f is the activation function (usually a linear function), and y is the output label. The hyperplane is defined by the equation: w.x + b = 0, where w is the weight vector and x is the input vector. The margin is the distance between the hyperplane and the closest data points from each class. The SVM tries to minimize the norm of w while maximizing the margin.

I hope this diagram helps you understand the basic architecture of linear models for deep learning. If you have any questions, please feel free to ask me.