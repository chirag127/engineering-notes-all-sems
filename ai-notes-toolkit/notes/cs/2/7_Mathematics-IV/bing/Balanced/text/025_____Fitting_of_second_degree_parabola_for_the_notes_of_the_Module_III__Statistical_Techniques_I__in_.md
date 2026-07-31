### Fitting of second degree parabola

- A second degree parabola is a curve of the form y = a + bx + cx^2, where a, b and c are constants.
- Fitting a second degree parabola to a given set of data points means finding the values of a, b and c that minimize the sum of squared errors (SSE) between the observed y values and the predicted y values from the parabola.
- The SSE is given by SSE = sum((y_i - (a + bx_i + cx_i^2))^2), where y_i and x_i are the observed values of y and x for the i-th data point, and the sum is taken over all n data points.
- To find the values of a, b and c that minimize the SSE, we can use the method of normal equations, which involves solving a system of three linear equations in three unknowns.
- The normal equations are obtained by taking the partial derivatives of the SSE with respect to a, b and c and setting them equal to zero. This gives:

  - sum(y_i) = na + b sum(x_i) + c sum(x_i^2)
  - sum(x_i y_i) = a sum(x_i) + b sum(x_i^2) + c sum(x_i^3)
  - sum(x_i^2 y_i) = a sum(x_i^2) + b sum(x_i^3) + c sum(x_i^4)

- Solving this system of equations gives the values of a, b and c that minimize the SSE and fit the second degree parabola to the data points.
- The coefficient of determination (R^2) is a measure of how well the fitted parabola explains the variation in the observed y values. It is given by R^2 = 1 - SSE/SST, where SST = sum((y_i - y_bar)^2) is the total sum of squares and y_bar = sum(y_i)/n is the mean of the observed y values.
- The R^2 value ranges from 0 to 1, with higher values indicating a better fit. A value of 1 means that the fitted parabola passes through all the data points exactly. A value of 0 means that the fitted parabola has no relation to the data points.