### Fitting of second degree parabola

- A second degree parabola is a curve of the form `y = a + bx + cx^2`, where `a`, `b`, and `c` are constants.
- Fitting a second degree parabola to a given set of data points means finding the values of `a`, `b`, and `c` that minimize the sum of squared errors between the observed `y` values and the predicted `y` values from the parabola.
- The method of least squares is a common technique for finding the best-fitting curve. It involves solving a system of normal equations that are derived from the partial derivatives of the error function with respect to `a`, `b`, and `c`.
- The normal equations for fitting a second degree parabola are:

  - `∑y = an + b∑x + c∑x^2`
  - `∑xy = a∑x + b∑x^2 + c∑x^3`
  - `∑x^2y = a∑x^2 + b∑x^3 + c∑x^4`

  where `n` is the number of data points and `∑` denotes the summation over all data points.

- To solve the normal equations, one can use matrix methods, such as Gaussian elimination or Cramer's rule, or numerical methods, such as Newton-Raphson or gradient descent.
- Once the values of `a`, `b`, and `c` are obtained, the fitted parabola can be plotted and the goodness of fit can be assessed by measures such as the coefficient of determination (`R^2`) or the root mean square error (RMSE).
- Fitting a second degree parabola can be useful for modeling nonlinear trends or relationships in data, such as quadratic growth or decay, or for interpolation or extrapolation of data.