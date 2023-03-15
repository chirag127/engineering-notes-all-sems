 Here is the content in markdown format for the topic ### batch normalization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning:

### Batch Normalization

- Batch Normalization is a technique to normalize the input layer of a neural network.
- It helps to stabilize the distribution of inputs to a layer and makes the training faster.
- It calculates the mean and variance of the inputs and normalizes them.
- The means and variances are learnable parameters and are adjusted during training.
- Formula:
```
x_norm = (x - E[x]) / √Var[x]
```
Where E[x] is the mean and Var[x] is the variance.
- During training, the means and variances are calculated from the batch of inputs. During inference, they are calculated from the whole training data.
- Advantages:
-- Faster training due to reduced internal covariate shift.
-- Reduces sensitivity to initialization and scales gradients.
-- Acts as a regularizer.
- Disadvantages:
-- Additional hyperparameter to tune - decay rate for moving average of mean and variance.
-- May not work well for small batch sizes.

[Detailed diagrams and examples can be added here if required.]

Batch Normalization is commonly applied after fully connected layers and convolutional layers in Convolutional Neural Networks and generally leads to better performance. It is a crucial technique for training deep neural networks.