# Locally Weighted Regression

- Locally weighted regression (LWR) is a nonparametric regression method that combines k-nearest neighbor based machine learning  .
- It is called locally weighted because for a query point, the function is approximated on the basis of data near that point and weighted by its distance from the query point .
- It is a supervised learning algorithm that does not have a training phase. All the work is done during the testing phase or while making predictions .
- The main idea of LWR is to fit a linear model to a subset of data points that are close to the query point, and then use the model to make a prediction for the query point .
- The subset of data points is selected by using a weighting function that assigns higher weights to points that are closer to the query point and lower weights to points that are farther away .
- The weighting function is usually a Gaussian function with a bandwidth parameter that controls the size of the subset .
- The linear model is fitted by minimizing the weighted least squares error, which is the sum of the squared errors multiplied by the weights .
- The linear model can be expressed as h(x) = theta^T x, where theta is the vector of coefficients that minimizes the weighted least squares error .
- The advantage of LWR is that it can adapt to the local shape of the data and capture nonlinear patterns without having to choose features carefully.
- The disadvantage of LWR is that it is computationally expensive, as it requires fitting a new model for each query point, and it is sensitive to the choice of the bandwidth parameter .