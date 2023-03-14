### VGG for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- VGG stands for Visual Geometry Group, which is the name of the research group at the University of Oxford that developed the VGG models .
- VGG models are deep convolutional neural networks (CNNs) that use small 3x3 filters and multiple layers to achieve high performance on image recognition tasks  .
- VGG models are simple and elegant in their design, and they only use convolutional layers, pooling layers, and fully connected layers as their components .
- VGG models are also widely used as feature extractors for other tasks, such as object detection, semantic segmentation, and super-resolution.
- VGG models have two main variants: VGG-16 and VGG-19, which have 16 and 19 weight layers (convolutional and fully connected) respectively  .
- VGG-16 and VGG-19 have the same architecture except for the number of convolutional layers in the last three blocks  .
- The following table shows the architecture of VGG-16 and VGG-19, where C denotes a convolutional layer, P denotes a max pooling layer, and F denotes a fully connected layer  .

| Layer | VGG-16 | VGG-19 |
| ----- | ------ | ------ |
| 1     | C(64)  | C(64)  |
| 2     | C(64)  | C(64)  |
| 3     | P      | P      |
| 4     | C(128) | C(128) |
| 5     | C(128) | C(128) |
| 6     | P      | P      |
| 7     | C(256) | C(256) |
| 8     | C(256) | C(256) |
| 9     | C(256) | C(256) |
| 10    | C(256) | C(256) |
| 11    | P      | P      |
| 12    | C(512) | C(512) |
| 13    | C(512) | C(512) |
| 14    | C(512) | C(512) |
| 15    | C(512) | C(512) |
| 16    | P      | P      |
| 17    | C(512) | C(512) |
| 18    | C(512) | C(512) |
| 19    | C(512) | C(512) |
| 20    | C(512) | C(512) |
| 21    | P      | P      |
| 22    | F(4096)| F(4096)|
| 23    | F(4096)| F(4096)|
| 24    | F(1000)| F(1000)|
| 25    | Softmax| Softmax|

- VGG models were trained on the ImageNet dataset, which contains over 14 million images belonging to 1000 classes  .
- VGG models achieved state-of-the-art results on the ImageNet challenge in 2014, with VGG-16 and VGG-19 achieving 92.7% and 92.5% top-5 test accuracy respectively  .
- VGG models are also very easy to implement using deep learning frameworks such as Keras and PyTorch .
- VGG models have some drawbacks, such as being very large in size (over 500MB), requiring a lot of memory and computation, and being prone to overfitting  .
- VGG models can be improved by using techniques such as batch normalization, dropout, data augmentation, and transfer learning  .
- VGG models can also be replaced by smaller and more efficient architectures, such as SqueezeNet, MobileNet,