# Locally Weighted Regression

- Locally weighted regression (LWR) is a nonparametric regression method that combines k-nearest neighbor based machine learning with linear regression .
- LWR is also known as locally weighted learning, kernel regression, or lazy learning .
- LWR does not have a training phase, but rather fits a linear model to the data points near the query point at the time of prediction .
- LWR assigns higher weights to the data points that are closer to the query point, and lower weights to the ones that are farther away  .
- LWR can capture nonlinear patterns in the data by using a local linear approximation .
- LWR has a parameter called the bandwidth or smoothing parameter, which controls the size of the neighborhood around the query point  .
- LWR can be generalized to higher dimensions and nonlinear models.
- LWR can be used for control problems, such as robot learning, by adapting the model parameters online based on the feedback from the environment.