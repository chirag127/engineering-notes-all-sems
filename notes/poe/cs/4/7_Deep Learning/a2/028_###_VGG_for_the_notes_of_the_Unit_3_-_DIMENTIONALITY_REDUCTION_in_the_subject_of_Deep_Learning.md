 Here is the content in markdown format:

### VGG for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- VGG is a convolutional neural network architecture proposed by K. Simonyan and A. Zisserman from the University of Oxford in the ILSVRC-2014.
- The name VGG is derived from the Visual Geometry Group of the University of Oxford.
- The architecture has 16-19 layers with the configurations like VGG-11, VGG-13, VGG-16 and VGG-19 where the first two digits denote the number of convolutional layers and the last digit denotes the number of fully connected layers.
- The characteristic feature of the VGG network is the use of small 3x3 convolutional filters in the initial convolutional layers followed by max-pooling layers for dimensionality reduction.
- The small 3x3 filters capture the notions of left/right, up/down, center which help in extracting spatial relationships from input and the max-pooling layers progressively reduce the spatial size of the feature maps to decrease the number of parameters and computations in the network.
- The use of only 3x3 convolutions and max-pooling enables the network to be very deep with lesser parameters.
- The VGG network achieves state-of-the-art performance in the ImageNet database and is used as a base architecture in many modern CNNs.

Mnemonics:
Very Good and Very Great CNN! 16-19 layers with only 3x3 convolutions and max-pooling.

Learning tricks:
- Understand the importance of 3x3 convolutions and max-pooling in extracting spatial features and reducing dimensionality.
- Note the configuration numbers of the VGG network to remember the depth and fully connected layers.
- Know that VGG achieves SOTA performance and is used as a base in many modern CNNs.

[Detailed diagrams and examples can be included here if required.]