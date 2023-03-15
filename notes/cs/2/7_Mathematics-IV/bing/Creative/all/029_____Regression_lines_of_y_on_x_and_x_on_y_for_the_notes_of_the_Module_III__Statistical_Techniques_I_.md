# Regression lines of y on x and x on y

- Regression is a statistical method that measures the relationship between two or more variables.
- Regression line is a straight line that best fits the data points on a scatter plot and shows the direction and strength of the correlation between the variables.
- There are two types of regression lines: regression line of y on x and regression line of x on y.
- Regression line of y on x is the line that minimizes the sum of the squares of the vertical distances of the data points from the line. It is also called the line of best fit or the least squares line.
- Regression line of x on y is the line that minimizes the sum of the squares of the horizontal distances of the data points from the line. It is also called the inverse regression line or the orthogonal regression line.
- The equations of the regression lines are derived using the method of moments, which involves finding the mean and variance of both variables and the covariance between them.
- The equation of the regression line of y on x is given by:

  y = a + bx

  where a is the y-intercept, b is the slope, and x is the independent variable.

  The values of a and b are given by:

  b = cov(x, y) / var(x)

  a = mean(y) - b * mean(x)

- The equation of the regression line of x on y is given by:

  x = c + dy

  where c is the x-intercept, d is the slope, and y is the independent variable.

  The values of c and d are given by:

  d = cov(x, y) / var(y)

  c = mean(x) - d * mean(y)

- The regression lines of y on x and x on y are not the same, unless the correlation coefficient between x and y is either 1 or -1, which means the variables are perfectly linearly related.
- The regression lines of y on x and x on y intersect at the point (mean(x), mean(y)), which is the centroid of the data points.