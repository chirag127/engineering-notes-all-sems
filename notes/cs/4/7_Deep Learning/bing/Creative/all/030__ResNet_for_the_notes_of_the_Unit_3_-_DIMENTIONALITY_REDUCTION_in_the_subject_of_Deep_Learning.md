### ResNet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- ResNet stands for Residual Network, a deep learning architecture that can learn from very deep neural networks without suffering from the vanishing/exploding gradient problem.
- ResNet introduces the concept of residual blocks, which are composed of two or more convolutional layers and a skip connection that bypasses some layers and adds the input to the output of the block.
- The idea behind residual blocks is to learn the residual function F(x) = H(x) - x, where H(x) is the desired underlying mapping and x is the input. This way, the network can fit H(x) = F(x) + x, which is easier to optimize than H(x) directly.
- ResNet can achieve very high accuracy on image recognition tasks, such as ImageNet and COCO, by using very deep networks with hundreds or thousands of layers .
- ResNet can also be used as a feature extractor for other tasks, such as object detection, image segmentation, and face recognition, by fine-tuning the pre-trained ResNet models on different datasets .
- ResNet has several variants, such as ResNet-18, ResNet-34, ResNet-50, ResNet-101, and ResNet-152, which differ in the number and type of residual blocks used. ResNet-50, ResNet-101, and ResNet-152 use bottleneck blocks, which reduce the number of channels before and after the 3x3 convolution to save computation and memory.
- ResNet has inspired many other architectures that use skip connections, such as DenseNet, ResNeXt, and Wide ResNet.

Some mnemonics and learning tricks for ResNet are:

- ResNet is like a highway network, where some layers can be skipped if they are not helpful for the performance.
- ResNet learns the residual function, which is the difference between the desired output and the input, and adds it back to the input to get the final output.
- ResNet uses very deep networks, but avoids the vanishing/exploding gradient problem by using skip connections and batch normalization.
- ResNet can be used for many tasks, not just image recognition, by fine-tuning the pre-trained models on different datasets.