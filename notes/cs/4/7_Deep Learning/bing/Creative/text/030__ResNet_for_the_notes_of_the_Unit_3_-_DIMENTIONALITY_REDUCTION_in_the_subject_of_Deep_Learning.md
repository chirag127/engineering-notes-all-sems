### ResNet

- ResNet stands for **Residual Network**, a deep learning architecture that can achieve state-of-the-art performance on various computer vision tasks, such as image classification, object detection, and image segmentation.
- ResNet was proposed by **Kaiming He et al.** from Microsoft Research in 2015, in their paper titled "Deep Residual Learning for Image Recognition" .
- ResNet introduces the concept of **residual blocks**, which are composed of two or more convolutional layers and a **skip connection** that bypasses some layers and adds the input to the output of the block.
- ResNet solves the problem of **vanishing/exploding gradients**, which occurs when training very deep neural networks. The gradients tend to become very small or very large, making the optimization process difficult and unstable.
- ResNet allows the network to learn **residual functions**, which are the difference between the desired output and the input, instead of learning the output directly. This makes the network easier to optimize and more expressive.
- ResNet can be built with different numbers of layers, depending on the complexity of the task and the dataset. The authors of the paper experimented with ResNet architectures with up to **152 layers**, which achieved the best results on the ImageNet dataset at the time .
- ResNet can also be used as a **feature extractor** for many deep learning tasks, by using the pre-trained weights from the ImageNet dataset and fine-tuning the network on a specific task or dataset   .