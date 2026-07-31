### Batch Normalization

Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch. This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks .

- Batch normalization affects the output of the previous activation layer by subtracting the batch mean, and then dividing by the batch’s standard deviation .
- It is a supervised learning technique that converts interlayer outputs into a standard format, called normalizing .
- This effectively 'resets' the distribution of the output of the previous layer to be more efficiently processed by the subsequent layer .
- Batch normalization accelerates training, in some cases by halving the epochs or better, and provides some regularization .