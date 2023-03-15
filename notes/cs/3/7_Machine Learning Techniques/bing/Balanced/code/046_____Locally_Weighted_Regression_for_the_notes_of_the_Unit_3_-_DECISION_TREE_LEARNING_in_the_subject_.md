### Locally Weighted Regression

- Locally weighted regression (LWR) is a nonparametric regression method that combines k-nearest neighbor based machine learning  .
- It is called locally weighted because for a query point, the function is approximated on the basis of data near that point and weighted because the contribution of each data point is weighted by its distance from the query point  .
- LWR does not have a training phase. All the work is done during the testing phase or while making predictions  .
- LWR can be seen as a generalization of linear regression, where instead of fitting a single line to the entire data, it fits a different line to each query point using a subset of the data near that point  .
- LWR can be formulated as follows  :

  - Given a dataset X, y, we want to find a model parameter β (x) that minimizes the residual sum of weighted squared errors:

    ![equation](https://latex.codecogs.com/png.latex?%5Cbeta%28x%29%20%3D%20%5Carg%5Cmin_%7B%5Cbeta%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20w_i%28x%29%28y_i%20-%20%5Cbeta%5ETx_i%29%5E2)

  - where w_i (x) is the weight assigned to the i-th data point for the query point x. A common choice of weight function is the Gaussian kernel:

    ![equation](https://latex.codecogs.com/png.latex?w_i%28x%29%20%3D%20%5Cexp%5Cleft%28-%5Cfrac%7B%28x%20-%20x_i%29%5ET%28x%20-%20x_i%29%7D%7B2%5Ctau%5E2%7D%5Cright%29)

  - where τ is a bandwidth parameter that controls how fast the weight decays with distance. A larger τ means a smoother fit, while a smaller τ means a more flexible fit.

  - The solution for β (x) can be obtained by solving the normal equation:

    ![equation](https://latex.codecogs.com/png.latex?%5Cbeta%28x%29%20%3D%20%28X%5ETW%28x%29X%29%5E%7B-1%7DX%5ETW%28x%29y)

  - where W (x) is a diagonal matrix with w_i (x) as the i-th diagonal element.

  - The prediction for the query point x can be obtained by:

    ![equation](https://latex.codecogs.com/png.latex?h%28x%29%20%3D%20%5Cbeta%28x%29%5ETx)

- LWR has the advantage of being able to fit complex nonlinear functions without explicitly choosing the features or the form of the function  .
- LWR has the disadvantage of being computationally expensive, as it requires solving a linear system for each query point, and being sensitive to the choice of the bandwidth parameter  .