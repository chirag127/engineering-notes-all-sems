 Here is the formal notes in Markdown format without any emojis or external links:

### Training a Convnet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION

1. Gather the data: Collect the training data which is the images in the required categories. The convnet will learn the features from the training images.

2. Design the architecture: Decide the number of layers (convolution, pooling, fully connected), filters, kernel size, activation functions, etc. The architecture is designed based on the type of task. For an image classification task, a standard convnet architecture can be used.

3. Define the loss function: The loss function is defined based on the task. For an image classification task, categorical cross-entropy loss is used. It measures the difference between the predicted and actual probability distributions.

4. Choose the optimization algorithm: An optimization algorithm is chosen to minimize the loss function. Common choices include SGD, Adam, RMSprop, etc. The learning rate is also specified.

5. Train the convnet: The convnet is trained for a fixed number of epochs or until the validation loss stops decreasing. The weights are updated using the gradients calculated from the loss function in each iteration. Various techniques like data augmentation, dropout, etc can be used to improve training.

6. Evaluate the performance: The trained convnet is evaluated using metrics like accuracy that compare the predictions with the ground truth labels. The performance on the training and validation set can give an estimate of how well the convnet has learned the features and patterns in the data.

7. Make inferences on new data: The trained convnet can now be used to make predictions on new images. It can classify unseen images into the appropriate categories based on the features it has learned from the training data.