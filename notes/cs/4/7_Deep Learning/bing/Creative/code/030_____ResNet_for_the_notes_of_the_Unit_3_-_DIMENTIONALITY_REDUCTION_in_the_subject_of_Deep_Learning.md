### ResNet

ResNet is a deep learning architecture that stands for **Residual Neural Network**. It was proposed by He et al. in 2015 to address the problem of **vanishing gradients** in very deep neural networks. ResNet introduces the concept of **residual connections** or **skip connections** that allow the network to learn the **identity function** when needed. ResNet can achieve very high accuracy on image recognition tasks, such as ImageNet, and can be used as a feature extractor for other tasks, such as object detection and segmentation .

Some of the main points about ResNet are:

- ResNet consists of several **residual blocks**, each of which has two or more convolutional layers and a shortcut connection that bypasses some layers.
- The shortcut connection can be either **identity** or **projection**, depending on the dimensionality of the input and output of the residual block. Identity means that the input is directly added to the output, while projection means that the input is linearly transformed to match the output dimension.
- The output of a residual block is the element-wise sum of the input and the output of the convolutional layers, followed by a non-linear activation function, such as ReLU.
- ResNet can be divided into different variants, such as ResNet-18, ResNet-34, ResNet-50, ResNet-101, and ResNet-152, based on the number and type of residual blocks. ResNet-50 and above use **bottleneck blocks**, which have a 1x1 convolution layer before and after the 3x3 convolution layer, to reduce the number of parameters and computational cost.
- ResNet can be trained using standard techniques, such as stochastic gradient descent, batch normalization, and weight decay. ResNet can also benefit from **pre-training** on large-scale datasets, such as ImageNet, and **fine-tuning** on specific tasks or domains.

Here is a diagram of a residual block with identity shortcut connection:

![Residual block with identity shortcut connection](https://miro.medium.com/max/1400/1*ByrVJspW-TefwlH7OLxNkg.png)

: He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778).
: Babina, B. (2020). Deep Residual Learning for Image Recognition (ResNet Explained). Medium. Retrieved from https://medium.com/@bbabina/deep-residual-learning-for-image-recognition-resnet-explained-d2b3c06f7c0a
: Residual Neural Networks - ResNets: Paper Explanation - DebuggerCafe. (2020). Retrieved from https://debuggercafe.com/residual-neural-networks-resnets-paper-explanation/
: Residual Networks (ResNet) - Deep Learning - GeeksforGeeks. (2020). Retrieved from https://www.geeksforgeeks.org/residual-networks-resnet-deep-learning/