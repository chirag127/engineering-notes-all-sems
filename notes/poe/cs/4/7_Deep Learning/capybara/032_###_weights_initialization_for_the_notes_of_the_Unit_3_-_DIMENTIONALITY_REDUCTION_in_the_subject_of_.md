### Weights Initialization for the Notes of the Unit 3 - Dimensionality Reduction in the Subject of Deep Learning

In deep learning, weights initialization is an important step as it can greatly affect the performance of the model. A good initialization can help the model converge faster and achieve better accuracy. In this section, we will discuss different methods of weights initialization.

#### 1. Zero Initialization

In this method, all the weights are initialized to zero. This method can be used for shallow networks but it is not recommended for deep networks as it results in all the neurons in a layer learning the same features. This can lead to the model being unable to learn complex features.

#### 2. Random Initialization

In this method, the weights are randomly initialized using a normal distribution or a uniform distribution. This method is commonly used and can work well for shallow networks. However, for deep networks, it can result in the vanishing or exploding gradient problem.

#### 3. Xavier Initialization

Xavier initialization is a method that takes into account the number of input and output neurons in a layer. It initializes the weights using a normal distribution with mean 0 and variance sqrt(2/(n_in + n_out)), where n_in is the number of input neurons and n_out is the number of output neurons. This method works well for sigmoid and tanh activation functions.

#### 4. He Initialization

He initialization is similar to Xavier initialization but it takes into account the activation function being used. It initializes the weights using a normal distribution with mean 0 and variance sqrt(2/n_in), where n_in is the number of input neurons. This method works well for ReLU activation function.

#### 5. Orthogonal Initialization

In this method, the weights are initialized using an orthogonal matrix. This method works well for recurrent neural networks.

#### 6. Glorot Initialization

Glorot initialization is a combination of Xavier and He initialization. It takes into account the activation function being used and the number of input and output neurons. It initializes the weights using a normal distribution with mean 0 and variance sqrt(2/(n_in + n_out)), where n_in is the number of input neurons and n_out is the number of output neurons. This method works well for both sigmoid and ReLU activation functions.

#### Mnemonics and Learning Tricks

Unfortunately, there are no easy-to-remember mnemonics or learning tricks for weights initialization. However, it is important to understand the different methods and their advantages and disadvantages. It is recommended to experiment with different initialization methods and choose the one that works best for the specific problem you are trying to solve.

In conclusion, weights initialization is an important step in deep learning and can greatly affect the performance of the model. It is recommended to experiment with different initialization methods and choose the one that works best for the specific problem you are trying to solve.