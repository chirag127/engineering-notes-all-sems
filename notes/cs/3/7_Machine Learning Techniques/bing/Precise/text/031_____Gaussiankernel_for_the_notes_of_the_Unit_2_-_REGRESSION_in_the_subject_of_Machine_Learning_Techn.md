### Gaussian Kernel

Gaussian Kernel Regression is a regression technique that does not require any iterative learning, such as gradient descent in linear regression. It can be thought of as fitting a line to a scatter plot.

An important parameter of Gaussian Kernel Regression is the variance, sigma^2. This parameter controls the smoothness of the approximated function. Smaller values of sigma will cause the function to overfit the data points, while larger values will cause it to underfit.

In the context of Gaussian Kernel Regression, each constructed kernel can also be viewed as a normal distribution with mean value xᵢ and standard deviation b.