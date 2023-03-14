### Convolutional Networks for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- A convolutional neural network (CNN) is a type of deep learning algorithm that is most commonly applied to analyze and learn visual features from large amounts of data.  
- CNNs are also known as shift invariant or space invariant artificial neural networks (SIANN), based on the shared-weight architecture of the convolution kernels or filters that slide along input features and provide translation-equivariant responses known as feature maps.  
- CNNs are regularized versions of multilayer perceptrons (MLPs), which are fully connected networks where each neuron in one layer is connected to all neurons in the next layer. The full connectivity of MLPs makes them prone to overfitting data. 
- CNNs reduce the number of parameters and improve the generalization ability of the network by using local connections, weight sharing, and pooling operations. 
- CNNs are composed of multiple layers, each of which performs a specific function on the input data. The layers are typically convolutional layers, activation layers, pooling layers, and fully connected layers.  
- A convolutional layer applies a set of filters to the input data, producing a set of feature maps that capture the local patterns in the data. The filters are learned during the training process and can be interpreted as feature detectors.  
- An activation layer applies a nonlinear function to the output of the convolutional layer, introducing nonlinearity to the network and allowing it to learn complex functions. The most common activation functions are ReLU, sigmoid, and tanh.  
- A pooling layer reduces the spatial dimension of the feature maps, making the network more robust to small variations in the input and reducing the computational cost. The most common pooling operations are max pooling, average pooling, and global pooling.  
- A fully connected layer connects every neuron in the previous layer to every neuron in the next layer, performing a linear transformation followed by an activation function. The fully connected layer is usually the last layer of the network and produces the output of the network, such as a class label or a score.  
- CNNs can be trained using gradient-based optimization methods, such as stochastic gradient descent (SGD), Adam, or RMSprop. The gradients are computed using the backpropagation algorithm, which propagates the error from the output layer to the input layer, updating the weights of the network accordingly.  
- CNNs are widely used in computer vision and have become the state of the art for many visual applications, such as image classification, object detection, face recognition, semantic segmentation, and image generation.  
- CNNs can also be used for other AI tasks, such as natural language processing, speech recognition, recommender systems, and financial time series.  

Some mnemonics and learning tricks for convolutional networks are:

- CNN: Convolutional Neural Network
- SIANN: Shift Invariant Artificial Neural Network
- MLP: Multilayer Perceptron
- ReLU: Rectified Linear Unit
- SGD: Stochastic Gradient Descent
- Adam: Adaptive Moment Estimation
- RMSprop: Root Mean Square Propagation
- Remember the order of the layers: Convolution -> Activation -> Pooling -> Fully Connected
- Remember the functions of the layers: Convolution -> Detect features, Activation -> Introduce nonlinearity, Pooling -> Reduce dimensionality, Fully Connected -> Produce output
- Remember the types of pooling: Max -> Take the maximum value, Average -> Take the average value, Global -> Take the global value
- Remember the types of activation: ReLU -> Max(0, x), Sigmoid -> 1 / (1 + exp(-x)), Tanh -> (exp(x) - exp(-x)) / (exp(x) + exp(-x))