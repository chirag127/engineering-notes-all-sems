### Locally Weighted Regression

Locally Weighted Regression (LWR) is a non-parametric method for fitting a regression model to a dataset. It is used when the relationship between the independent and dependent variables is not linear or when the data is noisy. LWR is also known as the memory-based method or instance-based learning.

Here are some key points to remember about LWR:

1. LWR fits a separate model for each query point, using only the training examples that are close to the query point.
2. The model is typically a linear regression model, but other models can also be used.
3. The training examples are weighted according to their distance from the query point, with closer examples receiving higher weights.
4. The weights are typically computed using a kernel function, such as the Gaussian kernel.
5. LWR can be computationally expensive, as it requires fitting a separate model for each query point.
6. LWR can be sensitive to the choice of the kernel function and its parameters.
7. LWR can be used for both regression and classification problems.

LWR is a powerful method for modeling complex relationships between variables, and can be particularly useful when the data is noisy or the relationship between the variables is not linear. However, it can be computationally expensive and sensitive to the choice of the kernel function and its parameters. As with any machine learning technique, it is important to carefully evaluate the performance of LWR on a given dataset before using it in practice.