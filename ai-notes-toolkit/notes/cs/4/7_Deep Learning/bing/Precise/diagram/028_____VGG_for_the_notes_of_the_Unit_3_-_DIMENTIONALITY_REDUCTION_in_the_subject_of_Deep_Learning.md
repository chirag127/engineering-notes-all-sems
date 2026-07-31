### VGG
- VGG is a convolutional neural network model proposed by K. Simonyan and A. Zisserman from the University of Oxford in the paper "Very Deep Convolutional Networks for Large-Scale Image Recognition".
- The model achieves 92.7% top-5 test accuracy in ImageNet, which is a dataset of over 14 million images belonging to 1000 classes.
- VGG is characterized by its simplicity, using only 3x3 convolutional layers stacked on top of each other in increasing depth.
- Reducing volume size is handled by max pooling.
- Two fully-connected (FC) layers, each with 4096 nodes are then followed by a softmax classifier.
- There are other variants of VGG like VGG16 (16 weight layers) and VGG19 (19 weight layers).
- The architecture of VGG is visualized below:
```
Input
Conv3-64
Conv3-64
MaxPool
Conv3-128
Conv3-128
MaxPool
Conv3-256
Conv3-256
Conv3-256
MaxPool
Conv3-512
Conv3-512
Conv3-512
MaxPool
Conv3-512
Conv3-512
Conv3-512
MaxPool
FC-4096
FC-4096
FC-1000
Softmax
```
- VGG is a great example of how the depth of the network is a critical component for good performance.
- VGG is very appealing because it is very uniform - the only hyperparameter to select is the depth of the network, and all the other hyperparameters were fixed.
- VGG is also very expensive to evaluate, and it is not as good as more recent architectures like ResNet.
- VGG is a good choice for extracting features from images, and it is often used as a pre-trained model for transfer learning.