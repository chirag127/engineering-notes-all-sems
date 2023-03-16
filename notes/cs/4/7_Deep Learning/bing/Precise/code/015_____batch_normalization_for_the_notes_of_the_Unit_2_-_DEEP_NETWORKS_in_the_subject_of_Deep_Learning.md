### Batch Normalization

Batch normalization is a technique used to enhance the stability of deep learning networks. It is applied to the output of the previous activation layer by subtracting the batch mean and then dividing by the batch’s standard deviation. This technique converts interlayer outputs into a standard format, called normalizing, effectively 'resetting' the distribution of the output of the previous layer to be more efficiently processed by the subsequent layer.

Batch normalization has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks. It accelerates training, in some cases by halving the epochs or better, and provides some regularization.