### Fitting of second degree parabola

- A second degree parabola is a curve of the form y = a + bx + cx^2, where a, b and c are constants.
- Fitting of a second degree parabola means finding the values of a, b and c that best fit a given set of data points (x_i, y_i), i = 1, 2, ..., n.
- One way to fit a second degree parabola is to use the principle of least squares, which minimizes the sum of squared errors between the observed y_i and the predicted y values from the parabola.
- The sum of squared errors is given by:

  S = sum_{i=1}^n (y_i - y)^2 = sum_{i=1}^n (y_i - a - bx_i - cx_i^2)^2

- To find the values of a, b and c that minimize S, we take the partial derivatives of S with respect to a, b and c and set them equal to zero. This gives us a system of three normal equations:

  sum_{i=1}^n y_i = an + b sum_{i=1}^n x_i + c sum_{i=1}^n x_i^2

  sum_{i=1}^n x_i y_i = a sum_{i=1}^n x_i + b sum_{i=1}^n x_i^2 + c sum_{i=1}^n x_i^3

  sum_{i=1}^n x_i^2 y_i = a sum_{i=1}^n x_i^2 + b sum_{i=1}^n x_i^3 + c sum_{i=1}^n x_i^4

- Solving this system of equations for a, b and c gives us the coefficients of the best fitting parabola.
- Alternatively, we can use matrix notation to write the system of normal equations as:

  [n   sum x_i   sum x_i^2  ] [a]   [sum y_i    ]
  [sum x_i sum x_i^2 sum x_i^3] [b] = [sum x_i y_i]
  [sum x_i^2 sum x_i^3 sum x_i^4] [c]   [sum x_i^2 y_i]

- And then use matrix inversion or other methods to solve for the vector [a b c]^T.
- The fitted parabola can be used to interpolate or extrapolate the values of y for any given x, or to analyze the relationship between x and y.

Some possible mnemonics and learning tricks for the topic are:

- To remember the form of the second degree parabola, y = a + bx + cx^2, you can use the acronym ABC, where A stands for the constant term, B stands for the linear term, and C stands for the quadratic term.
- To remember the order of the terms in the normal equations, you can use the rhyme:

  Sum of y is equal to A times n plus B times sum of x plus C times sum of x squared

  Sum of x times y is equal to A times sum of x plus B times sum of x squared plus C times sum of x cubed

  Sum of x squared times y is equal to A times sum of x squared plus B times sum of x cubed plus C times sum of x to the fourth

- To remember the matrix form of the normal equations, you can use the pattern:

  The first row and column are the sums of x to the power of zero, one, and two

  The second row and column are the sums of x to the power of one, two, and three

  The third row and column are the sums of x to the power of two, three, and four

  The right hand side vector is the sums of y, x times y, and x squared times y

- To remember the steps of solving the normal equations, you can use the acronym SIS, where S stands for setting the partial derivatives to zero, I stands for inverting the matrix, and S stands for solving for the coefficients.