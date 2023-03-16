# Deep Convolutional Neural Networks for Image Pattern Classification

- Deep convolutional neural networks (DCNNs) are a type of artificial neural networks that can learn from image samples and extract features for image pattern classification .
- DCNNs consist of multiple layers of processing units, each of which performs a specific operation on the input data, such as convolution, pooling, activation, normalization, or dropout .
- Convolution is the process of applying a filter (also called a kernel) to the input image, sliding it over the image, and computing the dot product of the filter and the image patch at each position. This produces a feature map that captures the presence of the filter pattern in the input image .
- Pooling is the process of reducing the size of the feature map by applying a function (such as max, average, or min) to a local region of the feature map. This reduces the computational cost and the number of parameters, and also introduces some invariance to translation, rotation, and scaling .
- Activation is the process of applying a nonlinear function (such as sigmoid, tanh, or ReLU) to the feature map, to introduce some nonlinearity and increase the expressive power of the network .
- Normalization is the process of scaling and shifting the feature map, to reduce the internal covariate shift and improve the convergence and generalization of the network .
- Dropout is the process of randomly dropping out some units of the feature map, to prevent overfitting and improve the robustness of the network .
- DCNNs typically have several convolutional layers, followed by pooling layers, activation layers, normalization layers, and dropout layers, and end with one or more fully connected layers that perform the final classification task  .
- DCNNs can learn complex and hierarchical features from the input images, by applying multiple filters of different sizes and depths, and by combining the outputs of different layers  .
- DCNNs have achieved state-of-the-art results in various image pattern classification tasks, such as object detection, face recognition, scene understanding, and image segmentation     .
- DCNNs can also be trained using small training sample sizes, by using data augmentation techniques, transfer learning methods, or very deep architectures.

: Deep Convolution Neural Networks for Image Classification, https://www.academia.edu/89390146/Deep_Convolution_Neural_Networks_for_Image_Classification
: The Complete Beginner’s Guide to Deep Learning: Convolutional Neural Networks, https://towardsdatascience.com/wtf-is-image-classification-8e78a8235acb
: Deep Convolutional Neural Networks, https://www.run.ai/guides/deep-learning-for-computer-vision/deep-convolutional-neural-networks
: Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps, https://arxiv.org/abs/1312.6034
: ImageNet classification with deep convolutional neural networks, https://dl.acm.org/doi/10.1145/3065386
: Very deep convolutional neural network based image classification using small training sample size, https://ieeexplore.ieee.org/document/7486599/