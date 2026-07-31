### Batch Normalization

Batch normalization is a technique used to improve the training of deep neural networks. It involves normalizing the input values of each layer to have zero mean and unit variance. Here are some key points to understand about batch normalization:

- Batch normalization is typically applied to the outputs of fully connected layers or convolutional layers in a neural network.
- The normalization step involves subtracting the mean of the batch and dividing by the standard deviation of the batch.
- The normalized values are then scaled and shifted by learnable parameters called gamma and beta, respectively.
- The gamma and beta parameters allow the network to learn to undo the normalization if it is not helpful for a particular layer.
- Batch normalization can help to reduce the effects of internal covariate shift, which is the phenomenon of changing internal distributions of features during training.
- By stabilizing the input values to each layer, batch normalization can help to speed up training and improve the accuracy of the model.
- During inference, batch normalization uses the population statistics of the training data to normalize the input values.

Overall, batch normalization is a powerful technique for improving the training of deep neural networks. It can help to reduce the effects of internal covariate shift, speed up training, and improve accuracy.