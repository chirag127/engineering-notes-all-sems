### Batch Normalization

Batch normalization is a technique used in deep learning to improve the training of neural networks. It is a form of normalization that operates on batches of data, rather than individual examples. Here are some key points to understand about batch normalization:

- Batch normalization is performed on the output of a layer in a neural network. Specifically, it normalizes the activations of the layer, so that they have zero mean and unit variance. This is done by subtracting the batch mean and dividing by the batch standard deviation.
- Normalizing the activations in this way can help to alleviate the problem of vanishing or exploding gradients, which can occur when training deep networks.
- Batch normalization can also help to regularize the network, by reducing the dependence of the activations on the specific values of the weights in the network. This can help to prevent overfitting.
- Batch normalization can be applied at different points in the network. It can be applied before or after the activation function, or even within the activation function.
- When using batch normalization, it is important to recompute the mean and standard deviation for each batch during training, rather than using a fixed estimate from the entire dataset. This is because the statistics of the activations can change as the network trains, and the batch statistics provide a more accurate estimate of the true statistics.
- During inference, the batch statistics are typically replaced by population statistics, which are estimated from the entire dataset. This is because the network is no longer being trained, and so there is no need to estimate the statistics on a batch-by-batch basis.
- Batch normalization can be implemented using a variety of techniques, including using a separate normalization layer, incorporating normalization into the activation function, or using a running average of the batch statistics.

Overall, batch normalization is a powerful technique for improving the training of deep neural networks. By normalizing the activations of each layer, it can help to improve the stability and performance of the network. However, it is important to use the technique correctly, by computing the batch statistics during training and using population statistics during inference.