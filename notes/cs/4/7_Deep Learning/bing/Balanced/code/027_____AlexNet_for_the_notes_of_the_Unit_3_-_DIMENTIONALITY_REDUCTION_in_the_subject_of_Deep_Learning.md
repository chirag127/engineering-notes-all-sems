# AlexNet

AlexNet is a deep convolutional neural network (CNN) that was designed for image classification and won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) in 2012. It is considered one of the most influential papers in computer vision and deep learning, as it demonstrated the power and potential of CNNs and GPUs for large-scale visual recognition tasks. 

Some of the main features of AlexNet are:

- It consists of eight layers: five convolutional layers, two fully connected hidden layers, and one fully connected output layer. The first convolutional layer uses 11x11 filters with a stride of 4, followed by max pooling and normalization. The second convolutional layer uses 5x5 filters with a stride of 1, followed by max pooling and normalization. The third, fourth, and fifth convolutional layers use 3x3 filters with a stride of 1, and are connected without pooling or normalization. The last three layers are fully connected, with the final layer having 1000 output units corresponding to the 1000 ImageNet classes. 
- It uses rectified linear units (ReLU) as the activation function, instead of the sigmoid or tanh functions that were commonly used before. ReLU is faster and more effective for training deep networks, as it avoids the problem of vanishing gradients and allows for sparse activations. 
- It uses dropout as a regularization technique, which randomly drops out units and their connections during training to prevent overfitting. Dropout reduces the number of parameters and co-adaptations in the network, and improves the generalization performance. 
- It uses data augmentation as another regularization technique, which artificially increases the size and diversity of the training data by applying random transformations, such as cropping, flipping, rotating, and changing the brightness and contrast. Data augmentation reduces the risk of overfitting and improves the robustness of the network to variations in the input. 
- It uses stochastic gradient descent (SGD) with momentum as the optimization algorithm, which updates the network parameters based on the gradient of the loss function and a fraction of the previous update. Momentum helps the network escape from local minima and converge faster. 
- It uses a learning rate schedule, which gradually decreases the learning rate as the training progresses. This helps the network find a good solution and avoid oscillations or divergence. 
- It uses a weight decay, which adds a penalty term to the loss function that is proportional to the squared magnitude of the network parameters. Weight decay prevents the network from learning large weights that may cause overfitting or numerical instability. 
- It uses a softmax function as the output layer, which normalizes the output scores to probabilities that sum to one. The softmax function is suitable for multi-class classification problems, as it allows the network to assign a confidence score to each class. 
- It uses a cross-entropy loss function, which measures the difference between the predicted probabilities and the true labels. The cross-entropy loss function encourages the network to assign high probabilities to the correct classes and low probabilities to the incorrect classes. 
- It uses a distributed training scheme, which splits the network across two GPUs and communicates the gradients between them. This allows the network to use more memory and computational resources, and train faster and more efficiently. 

AlexNet is an important milestone in the history of deep learning, as it showed that CNNs can achieve state-of-the-art results on challenging visual recognition tasks, and inspired many subsequent research and applications in the field. 

: https://towardsdatascience.com/what-alexnet-brought-to-the-world-of-deep-learning-46c7974b46fc
: https://towardsdatascience.com/implementing-alexnet-cnn-architecture-using-tensorflow-2-0-and-keras-2113e090ad98
: https://www.pinecone.io/learn/imagenet/
: https://en.wikipedia.org/wiki/AlexNet
: https://d2l.ai/chapter_convolutional-modern/alexnet.html
: https://www.mathworks.com/help/deeplearning/ref/alexnet.html