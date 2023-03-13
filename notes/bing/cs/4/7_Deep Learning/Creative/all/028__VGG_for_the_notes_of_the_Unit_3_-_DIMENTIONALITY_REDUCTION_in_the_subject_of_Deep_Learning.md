### VGG for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- VGG stands for **Visual Geometry Group**, which is the name of the research group at Oxford University that proposed the VGG models in 2014.
- VGG models are **deep convolutional neural networks** that consist of multiple layers of **3x3 convolutional filters** followed by **max pooling layers** and **fully connected layers** at the end .
- VGG models are designed to **increase the depth** of the network by using **small filters** and **reducing the feature map size** after each convolutional layer .
- VGG models have two variants: **VGG-16** and **VGG-19**, which have **16** and **19** convolutional layers respectively .
- VGG models are **pre-trained** on a large-scale image recognition dataset called **ImageNet**, which contains over 14 million images of 1000 classes .
- VGG models can be **loaded and used** in the **Keras** deep learning library, which provides an **Applications** interface for accessing pre-trained models.
- VGG models can be used to **classify objects** in photographs by passing the image through the network and getting the **output probabilities** of the 1000 classes.
- VGG models can also be used as **feature extractors** for other tasks, such as **object detection**, **face recognition**, or **image segmentation**, by removing the fully connected layers and using the **output feature maps** of the convolutional layers .
- VGG models are **simple and elegant** in their architecture, but they are also **very large and computationally expensive** due to their depth and number of parameters .
- VGG models are often **outperformed** by newer and more efficient architectures, such as **SqueezeNet**, **GoogleNet**, or **ResNet**, which use techniques such as **bottleneck layers**, **inception modules**, or **skip connections** to reduce the complexity and improve the accuracy of the network .

Some possible mnemonics and learning tricks for VGG are:

- VGG = Very Good Group (to remember the name of the research group)
- VGG = Very Good at Going deep (to remember the main idea of increasing the depth)
- VGG = 3x3 filters, 2x2 pooling, 16 or 19 layers (to remember the basic structure of the network)
- VGG = Pre-trained on ImageNet, used in Keras (to remember the dataset and the library)
- VGG = Large and Slow, but Simple and Elegant (to remember the pros and cons of the network)