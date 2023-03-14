 Here is the content in markdown format for the topic ### Convolutional Networks for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning:

### Convolutional Networks

- Convolutional Networks or ConvNets are a type of feed-forward neural network designed for processing grid-structured data like images.
- They have convolutional layers which act as feature extractors from the input data and pooling layers which downsample the extracted features.
- These layers enable ConvNets to automatically learn spatial hierarchies of features through backpropagation.
- Some key points to remember:

**Convolutional Layer:**

- Applies convolution operation on the input using filters/kernels to produce a feature map.
- Each filter is slid over the width and height of the input and a dot product is taken between the filter and input at that region to produce a activation.
- Multiple filters are applied to generate multiple feature maps.
- The filters/kernels are the learnable parameters which get adjusted during training.

**Pooling Layer:**

- Downsamples the feature maps by taking the max or average of the region of the feature map it slides over.
- This helps in removing redundancy and also controls overfitting.
- The most common types are max pooling and average pooling.

**Advantages:**

- Shifts the computational burden from the amount of input data to the number of parameters in the network, making them efficient even for large images.
- The features are learned automatically suited for the task, eliminating the need for manual feature engineering.
- Hierarchical feature extraction enables them to capture both low and high-level features of the data.

**Applications:**

- Image Classification
- Object Detection
- Semantic Segmentation
- Video Analysis

**Additional tips/Mnemonics:**

- "Border openings" - Feature maps have depth(channels) but shrink in width and height after each Conv and Pool layer.
- "Cats sliding on Max/Average windows" - Imagine cats (filters) sliding over and taking Max/Average in windows (pooling region) to understand Conv and Pool layers.
- "Parameter sharing" - Same filter is applied across the whole volume in Conv layers which enables efficient learning of features.