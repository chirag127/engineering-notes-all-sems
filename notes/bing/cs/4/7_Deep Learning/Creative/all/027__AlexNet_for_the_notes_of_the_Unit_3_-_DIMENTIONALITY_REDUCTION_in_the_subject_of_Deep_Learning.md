### AlexNet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- AlexNet is a deep convolutional neural network (CNN) that was introduced in 2012 by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton .
- AlexNet won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) in 2012, achieving a top-5 error rate of 15.3%, which was much lower than the previous best of 26.2% .
- AlexNet is considered one of the most influential papers published in computer vision, having spurred many more papers published employing CNNs and GPUs to accelerate deep learning.
- AlexNet consists of eight layers: five convolutional layers, two fully connected hidden layers, and one fully connected output layer .
- AlexNet used the rectified linear unit (ReLU) instead of the sigmoid as its activation function, which improved the training speed and reduced the problem of vanishing gradients .
- AlexNet used dropout as a regularization technique to reduce overfitting and improve generalization .
- AlexNet used data augmentation techniques such as image cropping, flipping, and color alterations to increase the size and diversity of the training set .
- AlexNet used local response normalization (LRN) to enhance the contrast of the feature maps and reduce the correlation between adjacent neurons .
- AlexNet used overlapping max pooling to reduce the size of the feature maps and introduce some translation invariance .
- AlexNet used two parallel GPUs to train the network, which reduced the training time and allowed for larger models and batches .
- AlexNet can classify images into 1000 object categories, such as keyboard, mouse, pencil, and many animals.
- AlexNet is a popular benchmark for evaluating the performance of other deep learning models on image classification tasks .

Some possible mnemonics and learning tricks for AlexNet are:

- Remember the number of layers as 5-2-1: five convolutional layers, two fully connected hidden layers, and one fully connected output layer.
- Remember the activation function as ReLU: rectified linear unit.
- Remember the regularization technique as dropout: dropping out some neurons randomly during training.
- Remember the data augmentation techniques as CFC: cropping, flipping, and color alterations.
- Remember the normalization technique as LRN: local response normalization.
- Remember the pooling technique as OMP: overlapping max pooling.
- Remember the parallelization technique as 2GPUs: two graphics processing units.