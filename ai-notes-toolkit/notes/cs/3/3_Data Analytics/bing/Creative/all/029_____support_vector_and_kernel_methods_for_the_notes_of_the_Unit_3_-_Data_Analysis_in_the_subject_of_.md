# Support Vector and Kernel Methods

## Support Vector Machines (SVMs)

- SVMs are a type of supervised learning algorithm that can perform classification and regression tasks.
- SVMs aim to find the optimal hyperplane that separates the data into different classes or predicts the output value for a given input.
- SVMs use a technique called the **margin maximization** to find the hyperplane that has the largest distance to the nearest data points of any class. This ensures that the hyperplane is robust and generalizable.
- The data points that are closest to the hyperplane are called the **support vectors**, and they determine the position and orientation of the hyperplane.
- SVMs can handle linearly separable and non-linearly separable data by using different types of **kernels**.

## Kernel Methods

- Kernel methods are a way of mapping the data into a higher-dimensional feature space, where the data may become linearly separable or more suitable for linear analysis.
- Kernel methods use a function called the **kernel function** to compute the inner product or similarity between two data points in the feature space, without explicitly transforming the data.
- Kernel methods are also known as the **kernel trick**, because they allow us to use linear algorithms in non-linear problems, by implicitly transforming the data with the kernel function.
- Kernel methods can be applied to various algorithms, such as SVMs, Gaussian processes, principal component analysis, ridge regression, and many others.
- Kernel methods can use different types of kernel functions, such as linear, polynomial, radial basis function (RBF), sigmoid, and others. The choice of the kernel function depends on the data and the task.