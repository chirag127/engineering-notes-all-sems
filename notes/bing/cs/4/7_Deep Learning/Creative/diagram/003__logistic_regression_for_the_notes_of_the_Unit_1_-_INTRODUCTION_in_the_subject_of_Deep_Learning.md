Logistic regression is a regression model that predicts the probability of a binary outcome (0 or 1) based on one or more input variables (features). It uses a sigmoid function to map the input variables to a value between 0 and 1, which represents the probability of the outcome being 1. The sigmoid function has the following formula:

![sigmoid function](https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Csigma%28z%29%20%3D%20%5Cfrac%7B1%7D%7B1%20&plus;%20e%5E%7B-z%7D%7D)

where z is a linear combination of the input variables and the model parameters:

![linear combination](https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20z%20%3D%20%5Cbeta_0%20&plus;%20%5Cbeta_1x_1%20&plus;%20%5Cbeta_2x_2%20&plus;%20...%20&plus;%20%5Cbeta_nx_n)

The model parameters are estimated by maximizing the likelihood function, which measures how well the model fits the data. The likelihood function is given by:

![likelihood function](https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20L%28%5Cbeta%29%20%3D%20%5Cprod_%7Bi%3D1%7D%5E%7Bn%7D%20%5Csigma%28z_i%29%5Ey_i%281-%5Csigma%28z_i%29%29%5E%7B1-y_i%7D)

where y_i is the actual outcome of the i-th observation, and z_i is the linear combination of the input variables and the model parameters for the i-th observation.

The following diagram illustrates the basic architecture of a logistic regression model:

![logistic regression diagram](https://i.imgur.com/6xX0Z0R.png)

The diagram shows how the input variables (x_1, x_2, ..., x_n) are multiplied by the model parameters (beta_0, beta_1, ..., beta_n) and summed up to form the linear combination (z). Then, the sigmoid function (sigma) is applied to z to produce the probability of the outcome being 1 (p). The predicted outcome (y_hat) is then obtained by comparing p with a threshold value (usually 0.5). If p is greater than or equal to the threshold, y_hat is 1; otherwise, y_hat is 0. The predicted outcome is then compared with the actual outcome (y) to calculate the error and update the model parameters. This process is repeated for all the observations in the data set until the model converges to the optimal parameters.