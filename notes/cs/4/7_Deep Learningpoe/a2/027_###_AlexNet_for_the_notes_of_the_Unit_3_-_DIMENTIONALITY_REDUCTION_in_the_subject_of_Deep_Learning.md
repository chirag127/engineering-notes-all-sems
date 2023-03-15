 Here is the markdown content for ### AlexNet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning:

### AlexNet

- AlexNet was developed by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton in 2012.
- It was the first CNN to win the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC) in 2012, reducing the top-5 error rate to 15.4% (a large improvement over the 26.2% achieved in 2011).
- AlexNet has 8 layers - 5 convolutional layers and 3 fully connected layers.
- It uses ReLU activation functions and max pooling to introduce non-linearity and reduce computational complexity respectively.
- Data augmentation techniques like cropping, flipping, and color jittering are used to expand the training dataset and reduce overfitting.
- The model is trained on two GPUs with dropout regularization to reduce overfitting.
- Applications: Image classification, Object detection, Semantic segmentation, etc.

Advantages:

- Achieved a significant improvement in accuracy over previous approaches.
- Paved the way for modern CNN architectures.
- Made training deep neural networks feasible due to the use of GPUs and some optimizations.

Disadvantages:

- Comparatively slow due to the use of GPUs.
- Not very efficient due to heavy usage of parameters and computational resources.
- Prone to overfitting due to the large number of parameters.

Mnemonics:

- AlexNet has 8 layers: 5 conv, 3 fc
- Uses ReLU and max pool
- Augments data (crop, flip, color jitter)
- Trains on 2 GPUs with dropout

Learning Tricks:

- Remember the layer arrangement and types of layers.
- Note the nonlinear and pooling layers with their purposes.
- Recognize data augmentation techniques and regularization used.
- Recall the advantages, disadvantages, and applications.