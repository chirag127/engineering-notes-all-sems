# Concept of Convolutional Neural Network

- A convolutional neural network (CNN) is a type of artificial neural network that uses a mathematical operation called convolution in one or more of its layers.
- Convolution is a process of applying a filter (also called a kernel) to an input, such as an image, and producing an output, such as a feature map.
- The filter slides over the input and performs element-wise multiplication and summation, resulting in a single value in the output.
- The filter can be seen as a way of extracting features from the input, such as edges, shapes, colors, etc.
- A CNN typically consists of three types of layers: convolutional layers, pooling layers, and fully-connected layers.
- A convolutional layer applies one or more filters to the input and produces one or more feature maps as the output.
- A pooling layer reduces the size of the feature maps by applying a function, such as max or average, to a region of the input and producing a single value as the output.
- A fully-connected layer connects every node in the input to every node in the output and performs a linear transformation followed by a non-linear activation function.
- A CNN can have multiple convolutional and pooling layers, followed by one or more fully-connected layers at the end.
- The final output of a CNN is usually a vector of probabilities, representing the likelihood of the input belonging to different classes.
- A CNN can be trained using backpropagation and gradient descent, similar to other neural networks.
- A CNN can be used for various tasks, such as image classification, object detection, face recognition, natural language processing, etc.