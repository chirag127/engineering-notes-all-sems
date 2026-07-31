# AlexNet

- AlexNet is a convolutional neural network (CNN) architecture that was proposed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton in 2012.
- AlexNet won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) in 2012, achieving a top-5 error rate of 15.3%, which was significantly lower than the previous best result of 26.2%.
- AlexNet is considered to be a milestone in the development of deep learning, as it demonstrated the power and scalability of CNNs for image recognition tasks.
- AlexNet consists of eight layers: five convolutional layers and three fully connected layers. The network has about 60 million parameters and 650,000 neurons.
- AlexNet uses rectified linear units (ReLU) as the activation function, which helps to avoid the problem of vanishing gradients and speeds up the training process.
- AlexNet also employs dropout, a regularization technique that randomly drops out some neurons during training, to reduce overfitting and improve generalization.
- AlexNet uses max pooling, a downsampling technique that reduces the spatial dimensions of the feature maps, to reduce the computational complexity and the number of parameters.
- AlexNet uses local response normalization (LRN), a normalization technique that enhances the contrast of the feature maps, to improve the generalization performance.
- AlexNet uses data augmentation, a technique that artificially increases the size and diversity of the training data, to reduce overfitting and improve generalization.
- AlexNet uses stochastic gradient descent (SGD) with momentum, a optimization technique that updates the network parameters based on the gradient of the loss function and a fraction of the previous update, to train the network.
- AlexNet is trained on a dataset of 1.2 million images from 1000 classes, which is a subset of the ImageNet dataset.
- AlexNet is implemented using two Nvidia GTX 580 GPUs, which allows for faster training and larger models. The network is split across the two GPUs, with some layers communicating between them.
- AlexNet takes about five to six days to train on the ImageNet dataset, which is much faster than previous models that took weeks or months.