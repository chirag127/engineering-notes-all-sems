### Concept of Convolutional Neural Network

- A convolutional neural network (CNN) is a type of artificial neural network that uses a mathematical operation called convolution to extract features from the input data, such as images or videos .
- A convolution is a process of sliding a small filter (also called a kernel) over the input data and computing the dot product of the filter and the input at each position. The result is a feature map that represents the presence of certain patterns or features in the input .
- A CNN consists of three main types of layers: convolutional layers, pooling layers, and fully-connected layers  .
- A convolutional layer applies one or more filters to the input data and produces one or more feature maps. The filters can have different sizes, shapes, and numbers of channels, depending on the desired output. The filters are learned during the training process, and they can capture different aspects of the input data, such as edges, shapes, colors, textures, etc  .
- A pooling layer reduces the size of the feature maps by applying a downsampling operation, such as max pooling or average pooling. This reduces the computational cost and the number of parameters, and also introduces some invariance to small translations or distortions in the input data  .
- A fully-connected layer connects every node in the previous layer to every node in the next layer, and performs a linear transformation followed by a non-linear activation function. This layer is similar to a regular feed-forward neural network, and it can perform classification or regression tasks on the extracted features  .
- A CNN can have multiple convolutional and pooling layers, stacked on top of each other, to form a deep architecture. The deeper layers can learn more abstract and complex features from the input data, and the final layer can produce the desired output, such as a class label or a score  .
- A CNN is trained using backpropagation and gradient descent, similar to other neural networks. The loss function measures the difference between the predicted output and the actual output, and the gradients are computed and propagated backwards through the network, updating the weights of the filters and the fully-connected layers  .
- A CNN is a powerful and versatile model that can handle various types of data and tasks, such as image recognition, object detection, face recognition, natural language processing, etc. It can learn features automatically from the data, without requiring manual feature engineering or domain knowledge  .

: https://deepai.org/machine-learning-glossary-and-terms/convolutional-neural-network
: https://en.wikipedia.org/wiki/Convolutional_neural_network
: https://www.ibm.com/topics/convolutional-neural-networks