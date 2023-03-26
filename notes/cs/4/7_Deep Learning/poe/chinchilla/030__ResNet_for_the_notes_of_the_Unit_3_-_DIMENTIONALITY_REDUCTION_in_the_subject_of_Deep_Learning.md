### ResNet for the notes of the Unit 3 - DIMENSIONALITY REDUCTION in the subject of Deep Learning

Residual Networks, also known as ResNets, are a type of neural network architecture that has been widely used in deep learning for image recognition and computer vision tasks. ResNets were introduced in 2015 by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.

Here are some key points to understand about ResNets:

- ResNets are designed to overcome the problem of vanishing gradients, which is a common issue in deep neural networks. Vanishing gradients occur when the gradient signal becomes very small as it propagates through the layers of a neural network, making it difficult to train the network effectively.
- ResNets use skip connections or shortcut connections to bypass one or more layers in a neural network. This allows the gradient signal to flow more easily through the network, making it easier to train deeper networks. 
- The skip connections in ResNets can be implemented in different ways, including identity mappings, which simply pass the input directly to the output, and projection shortcuts, which use a learned projection to match the dimensions of the input and output.
- ResNets have achieved state-of-the-art performance on a wide range of computer vision tasks, including image classification, object detection, and semantic segmentation. 
- ResNets have also inspired many other neural network architectures, including DenseNets, which use dense connections between layers, and Inception-ResNet, which combines the Inception architecture with ResNet-style skip connections.

In summary, ResNets are a powerful type of neural network architecture that can help overcome the problem of vanishing gradients and enable the training of much deeper networks. They have achieved impressive results on a wide range of computer vision tasks and have inspired many other neural network architectures.