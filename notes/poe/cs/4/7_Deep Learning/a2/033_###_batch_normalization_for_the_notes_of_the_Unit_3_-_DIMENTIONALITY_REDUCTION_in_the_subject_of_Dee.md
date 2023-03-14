 Here is the content in markdown format for the topic ### batch normalization for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning:

### Batch Normalization

- Batch Normalization is a technique to normalize the input layer of a neural network.
- It makes the distribution of the input data remain consistent throughout the training process. This helps in faster training and more accurate predictions.
- The key steps in Batch Normalization are:

1. Compute the mean and variance of the input data.
2. Normalize the data by subtracting the mean from each input and dividing by the variance.
3. Scale and shift the normalized values using two parameters gamma and beta.
4. The normalized values are then fed as input to the next layer of the network.

- Advantages:

- Faster training due to reduced internal covariate shift.
- Networks train with higher learning rates and are less sensitive to initialization.
- Acts as a regularizer and controls overfitting.

- Disadvantages:

- Additional hyper-parameters gamma and beta need to be tuned.
- May not work well with small batch sizes.

- Examples: Image classification, Speech recognition, etc.

- Batch Normalization is placed after the input layer and before the activation function. It makes the distribution of input data to the next layer more consistent and stable, which helps in training deep neural networks effectively.

- Mnemonics: Think of Batch Normalization as a way to normalize and standardize the input data to a neural network to make training more efficient and robust. The mean is subtracted and the data is divided by variance to normalize, then gamma and beta parameters scale and shift the values to the desired range.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.