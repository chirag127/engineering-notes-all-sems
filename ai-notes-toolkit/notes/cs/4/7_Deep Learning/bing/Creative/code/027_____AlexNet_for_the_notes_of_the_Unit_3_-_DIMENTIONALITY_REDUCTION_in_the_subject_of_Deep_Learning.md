# AlexNet

AlexNet is a convolutional neural network (CNN) architecture that was designed by Alex Krizhevsky in collaboration with Ilya Sutskever and Geoffrey Hinton. It competed and won the ImageNet Large Scale Visual Recognition Challenge in 2012 , achieving a top-5 error rate of 15.3%, which was 10.8 percentage points lower than the runner-up. AlexNet is considered one of the most influential papers published in computer vision, having spurred many more papers employing CNNs and GPUs to accelerate deep learning.

Some of the main features of AlexNet are:

- It consists of eight layers: five convolutional layers, three max-pooling layers, two normalization layers, two fully connected layers, and one softmax layer .
- It uses rectified linear units (ReLU) as the activation function for the hidden layers, which helps to avoid the vanishing gradient problem and speed up the training.
- It uses dropout as a regularization technique to reduce overfitting and improve generalization.
- It uses data augmentation techniques such as random cropping, flipping, and color alterations to increase the size and diversity of the training set.
- It uses grouped convolutions to split the model across two GPUs, which allows for larger models and faster training .
- It uses a large learning rate with a polynomial decay schedule and a momentum term to optimize the model parameters.

AlexNet is a milestone in the development of deep learning and computer vision, as it demonstrated the power and potential of CNNs for image recognition tasks. It also inspired many subsequent works that improved and extended the CNN architecture, such as VGGNet, GoogLeNet, ResNet, and DenseNet. AlexNet is still widely used as a baseline and a reference model for image classification and other vision tasks.