### Locally Weighted Regression

- Locally weighted regression (LWR) is a nonparametric regression method that combines k-nearest neighbor based machine learning  .
- It is called locally weighted because for a query point, the function is approximated on the basis of data near that point and weighted by its distance from the query point .
- It is a supervised learning algorithm that does not have a training phase. All the work is done during the testing phase or while making predictions .
- The main idea of LWR is to fit a linear model to a subset of data points that are close to the query point, using a weighted least squares method .
- The weights are determined by a kernel function, such as a Gaussian kernel, that assigns higher weights to points that are closer to the query point and lower weights to points that are farther away .
- The advantage of LWR is that it can capture complex nonlinear patterns in the data without having to choose features carefully or use high-degree polynomials.
- The disadvantage of LWR is that it is computationally expensive, as it requires solving a linear system for each query point, and it is sensitive to the choice of the kernel bandwidth parameter .