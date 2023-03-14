### ResNet for the notes of the Unit 3 - DIMENSIONALITY REDUCTION in the subject of Deep Learning

ResNet is short for "Residual Network," which is a type of deep neural network that is used for image recognition and classification. It was introduced in 2015 by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. ResNet is known for its ability to train very deep neural networks, which was previously a challenge due to the problem of vanishing gradients.

Here are some important points to remember about ResNet:

- ResNet uses a skip connection, also known as a shortcut connection, to allow the input to be added to the output of one or more layers. This helps to mitigate the problem of vanishing gradients by allowing the gradient to flow directly from the output to the input.
- The skip connection is implemented as an identity function, which means that the input is simply added to the output without any transformation.
- ResNet uses a building block called a residual block, which consists of two convolutional layers with batch normalization and ReLU activation, followed by the skip connection. The output of the residual block is the sum of the input and the output of the second convolutional layer.
- ResNet comes in different versions, which vary in the number of layers and the architecture of the residual blocks. The most common versions are ResNet-18, ResNet-34, ResNet-50, ResNet-101, and ResNet-152. The number after the name indicates the number of layers in the network.
- ResNet has achieved state-of-the-art performance on various image recognition and classification tasks, such as ImageNet and CIFAR-10.

Mnemonics and learning tricks:
- Remember that ResNet is all about adding the input to the output, so you can think of it as "rescuing" the gradient from vanishing by allowing it to flow directly through the skip connection.
- You can also remember the different versions of ResNet by associating them with their number of layers. For example, ResNet-18 has 18 layers, ResNet-50 has 50 layers, and so on.