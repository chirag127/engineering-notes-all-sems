# Method of Least Squares

- The method of least squares is a statistical method for determining the line of best fit for a set of data, providing a visual demonstration of the relationship between the data points.
- Each point of data represents the relationship between a known independent variable and an unknown dependent variable.
- The line of best fit is of the form y = mx + b, where m is the slope and b is the y-intercept.
- The goal of this method is to minimize the sum of the squared errors as much as possible, where an error is the difference between an observed value and the fitted value provided by the line.
- The sum of the squared errors is also called the variance, and it measures how well the line fits the data.
- To find the line of best fit, we need to solve the normal equations, which are derived from the condition that the partial derivatives of the variance with respect to m and b are zero.
- The normal equations are:

  - m ∑x^2 + b ∑x = ∑xy
  - m ∑x + b n = ∑y

  where n is the number of data points, and ∑ denotes the summation notation.
- To solve the normal equations, we can use matrix algebra and write them in the form of Ax = b, where A is a 2x2 matrix, x is a 2x1 vector, and b is a 2x1 vector.
- The matrix equation is:

  - [∑x^2 ∑x; ∑x n] [m; b] = [∑xy; ∑y]

- To find the solution x, we can multiply both sides by the inverse of A, which is given by:

  - A^-1 = 1/(n ∑x^2 - (∑x)^2) [n -∑x; -∑x ∑x^2]

- The solution x is then:

  - x = A^-1 b = 1/(n ∑x^2 - (∑x)^2) [n -∑x; -∑x ∑x^2] [∑xy; ∑y]

- The solution x contains the values of m and b that minimize the variance and give the line of best fit.