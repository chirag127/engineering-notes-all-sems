### Method of least squares

The method of least squares is a statistical method for finding the best fit line or curve for a given set of data points. The best fit line or curve is the one that minimizes the sum of the squared errors between the observed values and the predicted values of the dependent variable. The squared errors are also called the residuals.

The method of least squares can be used to model the relationship between a dependent variable and one or more independent variables, such as in linear regression or nonlinear regression. The method can also be used to solve overdetermined systems of linear equations, where there are more equations than unknowns.

Some basic concepts and formulas related to the method of least squares are:

- The equation of the best fit line for a set of data points (x<sub>i</sub>, y<sub>i</sub>) is y = mx + b, where m is the slope and b is the y-intercept. The values of m and b can be found by solving the normal equations:

  - m = (nΣx<sub>i</sub>y<sub>i</sub> - Σx<sub>i</sub>Σy<sub>i</sub>) / (nΣx<sub>i</sub><sup>2</sup> - (Σx<sub>i</sub>)<sup>2</sup>)
  - b = (Σy<sub>i</sub> - mΣx<sub>i</sub>) / n

  where n is the number of data points and Σ denotes the summation.

- The equation of the best fit curve for a set of data points (x<sub>i</sub>, y<sub>i</sub>) is y = f(x), where f(x) is a nonlinear function that depends on the type of curve. The values of the parameters of f(x) can be found by using numerical methods, such as the Gauss-Newton method or the Levenberg-Marquardt method, that iteratively minimize the sum of the squared errors.

- The sum of the squared errors (SSE) for a given set of data points (x<sub>i</sub>, y<sub>i</sub>) and a given function f(x) is:

  - SSE = Σ(y<sub>i</sub> - f(x<sub>i</sub>))<sup>2</sup>

  The smaller the SSE, the better the fit of the function to the data.

- The coefficient of determination (R<sup>2</sup>) is a measure of how well the function f(x) explains the variation in the dependent variable y. It is defined as:

  - R<sup>2</sup> = 1 - (SSE / SST)

  where SST is the total sum of squares, which is the sum of the squared deviations of y<sub>i</sub> from the mean of y. The value of R<sup>2</sup> ranges from 0 to 1, with 1 indicating a perfect fit and 0 indicating no fit.

- The method of least squares can be generalized to handle multiple independent variables, such as in multiple linear regression or multiple nonlinear regression. In this case, the equation of the best fit function is y = f(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>k</sub>), where x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>k</sub> are the independent variables and f(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>k</sub>) is a linear or nonlinear function of them. The values of the parameters of f(x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>k</sub>) can be found by solving the normal equations (for linear functions) or using numerical methods (for nonlinear functions) that minimize the SSE.

- The method of least squares can also be used to solve overdetermined systems of linear equations, such as Ax = b, where A is a matrix of coefficients, x is a vector of unknowns, and b is a vector of constants. If A has more rows than columns, then the system is overdetermined and has no exact solution. However, a least-squares solution can be found by multiplying both sides of the equation by A<sup>T</sup> (the transpose of A) and solving the resulting system:

  - A<sup>T</sup>Ax = A<sup>T</sup