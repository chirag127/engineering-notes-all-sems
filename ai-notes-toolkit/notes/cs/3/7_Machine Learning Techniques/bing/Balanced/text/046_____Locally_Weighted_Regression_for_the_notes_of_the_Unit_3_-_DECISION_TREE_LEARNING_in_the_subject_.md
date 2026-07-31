### Locally Weighted Regression

- Locally weighted regression (LWR) is a nonparametric regression method that combines k-nearest neighbor based machine learning with linear regression .
- It is called locally weighted because for a query point, the function is approximated on the basis of data near that point and weighted by its distance from the query point .
- It is a nonparametric algorithm because it does not assume any specific form of the function, such as a polynomial or a linear function .
- There is no training phase in LWR. All the work is done during the testing phase or while making predictions .
- The steps of LWR are as follows :
  - Given a dataset X, y, and a query point x, find the k nearest neighbors of x in X.
  - Assign weights to each neighbor based on its distance from x, using a kernel function such as the Gaussian kernel.
  - Fit a linear regression model to the weighted neighbors, using the weights as the coefficients.
  - Predict the value of y for x using the fitted model.
- The advantages of LWR are that it can fit complex and nonlinear functions, and that it can adapt to local variations in the data.
- The disadvantages of LWR are that it is computationally expensive, as it requires finding the nearest neighbors and fitting a model for each query point, and that it is sensitive to the choice of the kernel function and the bandwidth parameter.