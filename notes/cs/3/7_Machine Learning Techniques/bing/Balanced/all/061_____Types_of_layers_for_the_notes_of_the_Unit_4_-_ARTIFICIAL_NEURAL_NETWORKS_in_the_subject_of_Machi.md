# Types of layers for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- A layer in an artificial neural network is a group of neurons that perform a specific function on the input or output data.
- Based on the position in a neural network, there are three types of layers:
  - Input layer – responsible for receiving input data and passing it on to the next layer. This is the first layer in a neural network.
  - Hidden layers – can be found in almost every type of neural network except some single-layer types like perceptron. They perform various transformations on the input data to extract features or patterns that are useful for the output layer.
  - Output layer – the last layer in a neural network which produces the final output or prediction.
- Based on the function or structure of the neurons in a layer, there are several types of layers  :
  - Fully connected (or dense) layers – connect every neuron in one layer to every neuron in the next layer. They are the most common type of layer and can be used for various tasks such as classification, regression, or dimensionality reduction.
  - Convolutional layers – apply a set of filters or kernels to the input data to create feature maps that capture spatial information or patterns. They are widely used for image processing, computer vision, or natural language processing tasks.
  - Pooling layers – reduce the size or dimensionality of the feature maps by applying a pooling operation such as max, average, or sum. They help to reduce the computational cost and prevent overfitting.
  - Deconvolutional (or transposed convolutional) layers – perform the inverse operation of convolutional layers by upsampling the input data to create larger feature maps. They are often used for image generation, segmentation, or super-resolution tasks.
  - Recurrent layers – have a feedback loop that allows them to store and process sequential or temporal data. They can handle variable-length inputs and outputs and are suitable for time series analysis, natural language processing, or speech recognition tasks.
  - Normalization layers – normalize the input data or the activations of the neurons to improve the stability and performance of the neural network. They can help to avoid problems such as vanishing or exploding gradients, covariate shift, or internal covariate shift.
  - Other types of layers – include dropout layers, attention layers, embedding layers, etc. that perform specific functions or operations on the input or output data. They can enhance the performance, generalization, or interpretability of the neural network.