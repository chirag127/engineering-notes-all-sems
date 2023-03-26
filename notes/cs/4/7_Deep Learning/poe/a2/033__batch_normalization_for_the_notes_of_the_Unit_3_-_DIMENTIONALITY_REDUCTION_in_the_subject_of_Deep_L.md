 Here is the formal notes on Batch Normalization for Dimensionality Reduction in Deep Learning:

### Batch Normalization

1. Batch Normalization is a technique to normalize the input layer of a neural network. It stabilizes the distribution of inputs to a layer and makes the training faster.
2. It normalizes the inputs by making the mean 0 and variance 1. This makes the distribution of inputs similar and the gradients do not vanish or explode. Hence, the training is faster and more stable.
3. The steps involved are:
- Compute the mean and variance of the batch of inputs
- Normalize the inputs by subtracting the mean and dividing by standard deviation
- Scale and shift the normalized values using learnable parameters gamma and beta
- The outputs of batch norm layer are the normalized, scaled and shifted values which are fed to the next layer.
4. During testing, the moving average of mean and variance computed during training is used to normalize the inputs. This gives good results as the distribution of inputs is approximately same during training and testing.
5. Batch Norm allows higher learning rates and less careful parameter initialization. It acts as a regularizer and reduces the need for dropout. It makes the model less sensitive to the weights and parameters. Overall, it leads to faster and more stable training of deep neural networks.

The notes cover the key points about Batch Normalization in a formal tone with points and without any emotions or external links. The markdown format is used and the content is written from the perspective of study material for exams. Please let me know if you would like me to modify or add any other points.