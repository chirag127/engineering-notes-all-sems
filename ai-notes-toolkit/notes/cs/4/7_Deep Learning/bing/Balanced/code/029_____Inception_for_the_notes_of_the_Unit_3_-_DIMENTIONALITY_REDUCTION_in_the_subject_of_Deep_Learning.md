# Inception

- Inception is a deep learning model based on convolutional neural networks (CNNs) that was introduced by Google in 2014 .
- Inception aims to improve the accuracy and efficiency of image classification and object detection tasks by using a novel architecture that combines multiple types of convolutions and pooling layers in parallel.
- Inception consists of several modules, each of which has a different number and size of filters, and performs different operations on the input feature maps.
- The main idea of Inception is to use a **1x1 convolution** layer before applying a larger convolution or pooling layer, to reduce the dimensionality and computational cost of the network.
- The 1x1 convolution layer acts as a **bottleneck** that compresses the input feature maps into a lower-dimensional representation, which can then be processed by a larger convolution or pooling layer more efficiently.
- The 1x1 convolution layer can also be used to increase the depth of the network by applying more filters, which can capture more complex and diverse features.
- The Inception module also uses a **concatenation** layer to combine the outputs of different convolutions and pooling layers, which increases the diversity and richness of the feature maps.
- The Inception module can be repeated several times in the network, forming a **deep** and **wide** architecture that can learn from multiple scales and perspectives of the input image.
- The Inception model has been improved and refined over the years, resulting in different versions such as Inception V2, Inception V3, and Inception V4, which incorporate various techniques such as batch normalization, factorization, residual connections, and label smoothing.
- The Inception model has achieved state-of-the-art results on several image classification and object detection benchmarks, such as ImageNet, COCO, and PASCAL VOC.

: Going deeper with convolutions. Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, and Andrew Rabinovich. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 1–9, 2015.

: Rethinking the inception architecture for computer vision. Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 2818–2826, 2016.