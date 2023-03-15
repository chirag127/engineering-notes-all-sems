### Concept of Convolution for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- Convolution is a mathematical operation that mixes two functions to produce a third function.
- In machine learning, convolution is often used to apply a filter (also called a kernel or a feature detector) to an input matrix (such as an image) to produce an output matrix (also called a feature map or an activation map).
- Convolution can be seen as a sliding window operation, where the filter is moved over the input matrix and multiplied element-wise with the corresponding sub-matrix, and the result is summed up and stored in the output matrix.
- Convolution can be used to extract features from the input matrix, such as edges, shapes, patterns, etc., that are useful for the learning task.
- Convolution can also be used to reduce the dimensionality of the input matrix, by using a smaller filter size or a stride (the number of steps the filter moves over the input matrix).
- A convolutional neural network (CNN or convnet) is a type of artificial neural network that uses convolution as one of its main operations.
- A CNN consists of three types of layers: a convolutional layer, a pooling layer and a fully connected layer.
- A convolutional layer applies one or more filters to the input matrix and produces one or more output matrices.
- A pooling layer reduces the size of the output matrices by applying a function (such as max, average or sum) to a region of the matrix (such as 2x2 or 3x3) and outputting the result.
- A fully connected layer connects every neuron in the previous layer to every neuron in the next layer, and performs a linear transformation followed by a non-linear activation function.
- A CNN can have multiple convolutional and pooling layers, followed by one or more fully connected layers at the end.
- A CNN can learn to recognize complex patterns and features from the input matrix, such as faces, objects, scenes, etc., by adjusting the weights of the filters and the neurons through backpropagation.
- A CNN can be used for various applications and data types, such as image classification, object detection, face recognition, natural language processing, etc..

: https://www.techtarget.com/searchenterpriseai/definition/convolutional-neural-network
: https://datamodelling.org/what-is-convolution-in-machine-learning/
: https://en.wikipedia.org/wiki/Convolutional_neural_network
: https://timdettmers.com/2015/03/26/convolution-deep-learning/