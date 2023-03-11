### Pooling

Pooling is a technique used in Convolutional Neural Networks (CNNs) to reduce the spatial dimensions of the input feature maps. Pooling is usually applied after convolutional layers to progressively reduce the spatial size of the feature maps and control overfitting. In this section, we will discuss different types of pooling techniques used in CNNs.

#### Max Pooling

Max pooling is the most commonly used pooling technique in CNNs. In max pooling, we divide the input feature map into non-overlapping rectangles and take the maximum value of each rectangle as the output. Max pooling is useful in detecting the presence of a feature regardless of its position in the input image. Max pooling has the following advantages:

- It reduces the spatial dimensions of the feature map, making the network computationally efficient.
- It introduces translational invariance, which means that the network can detect features regardless of their position in the input image.

#### Average Pooling

Average pooling is another commonly used pooling technique in CNNs. In average pooling, we divide the input feature map into non-overlapping rectangles and take the average value of each rectangle as the output. Average pooling is useful in detecting the presence of a feature regardless of its position and intensity in the input image. Average pooling has the following advantages:

- It reduces the spatial dimensions of the feature map, making the network computationally efficient.
- It is less prone to overfitting than max pooling.

#### Global Pooling

Global pooling is a pooling technique used in the final layer of a CNN to produce a fixed-size output. In global pooling, we take the maximum or average value of the entire feature map as the output. Global pooling has the following advantages:

- It produces a fixed-size output, which is useful in tasks such as image classification.
- It reduces the spatial dimensions of the feature map, making the network computationally efficient.

In conclusion, pooling is an important technique used in CNNs to reduce the spatial dimensions of the input feature maps. Max pooling, average pooling, and global pooling are commonly used pooling techniques in CNNs. Each pooling technique has its own advantages and disadvantages, and the choice of pooling technique depends on the specific task at hand.