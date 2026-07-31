### AlexNet

AlexNet is a deep convolutional neural network (CNN) that was proposed by Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton in 2012. It won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) by a large margin, achieving a top-5 error rate of 15.3%, compared to 26.2% by the second-best entry. AlexNet is considered one of the most influential papers published in computer vision, having spurred many more papers employing CNNs and GPUs to accelerate deep learning.

Some of the main features of AlexNet are:

- It consists of eight layers: five convolutional layers, two fully connected hidden layers, and one fully connected output layer.
- It used the rectified linear unit (ReLU) as its activation function, instead of the sigmoid or tanh, which improved the training speed and reduced the problem of vanishing gradients.
- It used dropout, a regularization technique, to reduce overfitting and improve generalization.
- It used data augmentation, such as random cropping, flipping and color jittering, to increase the size and diversity of the training set.
- It used local response normalization (LRN), a form of lateral inhibition, to enhance the contrast of the feature maps and reduce the correlation between adjacent neurons.
- It used overlapping max pooling, which reduced the size of the feature maps and introduced some translation invariance.
- It used a parallel architecture with two GPUs, which allowed it to train on larger batches and use more parameters.
- It used a softmax classifier at the output layer, which predicted the probability of each of the 1000 classes in the ImageNet dataset.

AlexNet is not a complicated architecture when compared with some state-of-the-art CNN architectures that have emerged in the more recent years, but it was a breakthrough in the field of deep learning, showing that CNNs can achieve remarkable results on large-scale image recognition tasks. AlexNet also demonstrated the importance of having a large and diverse dataset, such as ImageNet, to train deep neural networks. AlexNet is still widely used as a baseline or a reference model for various computer vision applications.