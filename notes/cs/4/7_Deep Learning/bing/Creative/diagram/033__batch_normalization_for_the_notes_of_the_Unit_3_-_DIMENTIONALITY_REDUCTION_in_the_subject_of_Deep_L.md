Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch. This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks .

The following diagram illustrates the basic architecture of a batch normalization layer:

```
Input: x = [x1, x2, ..., xn] (n-dimensional vector)

Output: y = [y1, y2, ..., yn] (n-dimensional vector)

Parameters: gamma = [gamma1, gamma2, ..., gamman] (n-dimensional vector)
            beta = [beta1, beta2, ..., betan] (n-dimensional vector)

Step 1: Calculate the mean and variance of x over the mini-batch

mean = (1/m) * sum(x)  (scalar)
var = (1/m) * sum((x - mean)^2)  (scalar)

Step 2: Normalize x by subtracting the mean and dividing by the square root of the variance

x_hat = (x - mean) / sqrt(var + epsilon)  (n-dimensional vector)

Step 3: Scale and shift x_hat by multiplying by gamma and adding beta

y = gamma * x_hat + beta  (n-dimensional vector)
```

The epsilon term is a small constant (e.g. 1e-5) added to the variance to avoid division by zero. The gamma and beta parameters are learnable and allow the model to adjust the normalized output to the optimal scale and location for the next layer. The batch normalization layer also keeps track of the running mean and variance of the inputs during training, which are used to normalize the inputs during inference. This ensures that the distribution of the inputs does not change drastically between training and testing.