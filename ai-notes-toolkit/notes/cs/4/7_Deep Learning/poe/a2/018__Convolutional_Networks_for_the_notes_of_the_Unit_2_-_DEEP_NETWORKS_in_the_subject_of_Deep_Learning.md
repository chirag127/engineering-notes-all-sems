 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Convolutional Networks

1. Convolutional networks are a type of feed-forward artificial neural network. They have three main components:
- Convolutional layers: Apply filters or kernels to the input data and pass the convolved feature maps to the next layer.
- Activation layers: Apply an activation function to the output of the convolutional layers. ReLU is commonly used.
- Pooling layers: Perform downsampling on the convolved feature maps to reduce dimensionality and capture the dominant features.

2. The convolutional layers apply filters to the input data to detect spatial patterns and pass these as feature maps to the next layer. Multiple filters are used and stacked as channels in the feature maps. The filters are slid over the input and convolved to produce a feature map.

3. The downsampling or pooling layers reduce the dimensionality of the convolved feature maps and keep the dominant features. Max pooling and average pooling are two common types. They take the maximum or average value in a window slid over the feature map to produce a downsampled feature map.

4. The activation layers apply an activation function to the output of the convolutional and pooling layers. ReLU is a popular choice as it has a non-linear activation and introduces sparsity. The final activation layer uses a softmax function to produce normalized probability values for classification.

5. The overall effect of stacking the convolutional, pooling, and activation layers is a hierarchical extraction of features and pattern learning at multiple levels of abstraction. The fully connected layers at the end perform final classification.