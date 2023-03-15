### Method of least squares

- The method of least squares is a statistical method for determining the best fit line or curve for a given set of data points  .
- The best fit line or curve is the one that minimizes the sum of the squares of the errors or residuals, which are the differences between the observed values and the fitted values  .
- The method of least squares can be used to find the equation of the best fit line or curve of the form y = mx + b, where m is the slope and b is the y-intercept .
- The method of least squares can also be used to find the coefficients of higher degree polynomials or other functions that fit the data points.
- The method of least squares can be applied to linear or nonlinear systems of equations, and can handle overdetermined or underdetermined cases .
- The method of least squares can be performed using various techniques, such as matrix algebra, calculus, or numerical methods .

#### Steps to perform the method of least squares for a linear equation y = mx + b

- Given a set of n data points (x1, y1), (x2, y2), ..., (xn, yn), we want to find the values of m and b that minimize the sum of the squared errors, which is given by:

![Sum of squared errors](https://latex.codecogs.com/png.latex?S%28m%2C%20b%29%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28y_i%20-%20mx_i%20-%20b%29%5E2)

- To find the minimum of S(m, b), we take the partial derivatives of S(m, b) with respect to m and b, and set them equal to zero:

![Partial derivatives](https://latex.codecogs.com/png.latex?%5Cfrac%7B%5Cpartial%20S%7D%7B%5Cpartial%20m%7D%20%3D%20-2%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20x_i%28y_i%20-%20mx_i%20-%20b%29%20%3D%200%2C%20%5Cquad%20%5Cfrac%7B%5Cpartial%20S%7D%7B%5Cpartial%20b%7D%20%3D%20-2%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28y_i%20-%20mx_i%20-%20b%29%20%3D%200)

- Solving these equations simultaneously, we get the normal equations for m and b:

![Normal equations](https://latex.codecogs.com/png.latex?m%20%3D%20%5Cfrac%7Bn%5Csum%20x_iy_i%20-%20%5Csum%20x_i%5Csum%20y_i%7D%7Bn%5Csum%20x_i%5E2%20-%20%28%5Csum%20x_i%29%5E2%7D%2C%20%5Cquad%20b%20%3D%20%5Cfrac%7B%5Csum%20y_i%20-%20m%5Csum%20x_i%7D%7Bn%7D)

- Substituting the values of x and y from the data points into these equations, we can find the values of m and b that minimize the sum of the squared errors.
- The equation of the best fit line is then given by y = mx + b, where m and b are the values obtained from the normal equations.