### Locally Weighted Regression

Locally Weighted Regression (LWR) is a non-parametric method for fitting a regression model to data. It is used when the relationship between the independent and dependent variables is not well-defined by a linear or polynomial equation. LWR is particularly useful when the data has a high degree of non-linearity or when the relationship between the variables changes over the range of the data.

Here are some key points to remember about LWR:

1. LWR fits a separate model to each data point, using only nearby data points to make the fit. This is in contrast to global regression methods, which use all the data points to fit a single model.
2. The weight given to each data point in the fit is determined by a kernel function, which assigns higher weights to data points that are closer to the point being fitted.
3. The bandwidth parameter controls the width of the kernel function and determines how much influence nearby data points have on the fit. A small bandwidth will result in a more flexible fit, while a large bandwidth will result in a smoother fit.
4. LWR can be computationally expensive, as a separate model must be fit for each data point. However, there are efficient algorithms available for performing LWR, such as the LOWESS algorithm.
5. LWR can be sensitive to the choice of bandwidth parameter, and it is important to choose an appropriate value for the bandwidth to achieve a good fit.

LWR is a powerful tool for modeling complex relationships between variables, and is widely used in machine learning and data analysis. It is an important technique to understand and master for anyone working in these fields.