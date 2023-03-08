### Fitting of straight lines

- Fitting of a straight line is the process of constructing a straight line that has the best fit to a series of data points.
- The equation of a straight line or least square line is `y = a + b x`, where `a` and `b` are constants or unknowns.
- The constants `a` and `b` can be estimated by the method of least squares, which minimizes the sum of the squares of the vertical distances from the data points to the fitting line .
- The method of least squares involves solving two normal equations: `n a + b ∑ x_i = ∑ y_i` and `a ∑ x_i + b ∑ x_i^2 = ∑ x_i y_i`, where `n` is the number of data points and `∑` denotes the summation.
- The solution of the normal equations gives the estimates of `a` and `b` as: `a = (∑ y_i ∑ x_i^2 - ∑ x_i ∑ x_i y_i) / (n ∑ x_i^2 - (∑ x_i)^2)` and `b = (n ∑ x_i y_i - ∑ x_i ∑ y_i) / (n ∑ x_i^2 - (∑ x_i)^2)`.
- The fitting line can be used to interpolate or extrapolate the values of `y` for given values of `x`, or to test the hypothesis of a linear relationship between `x` and `y`.
- The quality of the fit can be measured by the coefficient of determination `R^2`, which is the ratio of the explained variation to the total variation in the data.
- The coefficient of determination `R^2` ranges from 0 to 1, where 1 indicates a perfect fit and 0 indicates no linear relationship.
- The coefficient of determination `R^2` can be calculated as: `R^2 = 1 - SS_e / SS_t`, where `SS_e` is the sum of squares of the errors and `SS_t` is the total sum of squares.
- The sum of squares of the errors `SS_e` is given by: `SS_e = ∑ (y_i - y)^2`, where `y` is the estimated value of `y` from the fitting line.
- The total sum of squares `SS_t` is given by: `SS_t = ∑ (y_i - y_bar)^2`, where `y_bar` is the mean value of `y` in the data.

- An example of fitting a straight line to a set of data points is shown below:

| x | y |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |
| 4 | 7 |
| 5 | 8 |

- Using the method of least squares, we can calculate the estimates of `a` and `b` as:

`a = (∑ y_i ∑ x_i^2 - ∑ x_i ∑ x_i y_i) / (n ∑ x_i^2 - (∑ x_i)^2) = (26 * 55 - 15 * 100) / (5 * 55 - 15^2) = 0.6`

`b = (n ∑ x_i y_i - ∑ x_i ∑ y_i) / (n ∑ x_i^2 - (∑ x_i)^2) = (5 * 100 - 15 * 26) / (5 * 55 - 15^2) = 1.4`

- The equation of the fitting line is: `y = 0.6 + 1.4 x`
- The coefficient of determination `R^2` is:

`R^2 = 1 - SS_e / SS_t`

`SS_e = ∑ (y_i - y)^2 = (2 - 2)^2 + (4 - 3.4)^2 + (5 - 4.8)^2 + (7 - 6.2)^2 + (8 - 7.6)^2 = 1.2`

`SS_t = ∑ (y_i - y_bar)^2 = (2 - 5.2)^2 + (

Some possible mnemonics and learning tricks for the topic are:

- To remember the equation of a straight line, you can use the acronym SLAB: Straight Line = A + B x
- To remember the formula for the coefficient of determination, you can use the rhyme: R squared is one minus error over total squared
- To remember the normal equations, you can use the word NAB: N times A plus B times sum of x equals sum of y, and A times sum of x plus B times sum of x squared equals sum of x times y
- To remember the order of operations for solving the normal equations, you can use the acronym PEMDAS: Parentheses, Exponents, Multiplication and Division, Addition and Subtraction
- To remember the difference between interpolation and extrapolation, you can use the word INEX: INterpolation is INside the data range, EXtrapolation is EXtending beyond the data range