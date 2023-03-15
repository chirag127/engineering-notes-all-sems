### Method of least squares

- The method of least squares is a statistical method for determining the best fit line or curve for a given set of data points  .
- The best fit line or curve is the one that minimizes the sum of the squared errors (SSE) between the observed values (y) and the predicted values (ŷ) of the dependent variable    .
- The SSE is also called the variance or the residual sum of squares (RSS)   .
- The method of least squares can be used to find linear, polynomial, exponential, logarithmic, or other types of regression models   .
- The method of least squares can be applied to overdetermined systems, which are sets of equations that have more equations than unknowns .
- The method of least squares can be computed by using matrix algebra, calculus, or numerical methods    .

#### Example

- Suppose we have the following data points:

| x | y |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |
| 4 | 7 |

- We want to find the best fit line of the form y = mx + b for this data.
- Using the method of least squares, we need to minimize the SSE, which is given by:

SSE = ∑(y - ŷ)² = ∑(y - (mx + b))²

- To find the values of m and b that minimize the SSE, we can use calculus and set the partial derivatives of SSE with respect to m and b equal to zero:

∂SSE/∂m = -2∑(y - (mx + b))x = 0

∂SSE/∂b = -2∑(y - (mx + b)) = 0

- Solving these equations simultaneously, we get:

m = (∑xy - n̅x̅y)/(∑x² - n̅x²)

b = y̅ - mx̅

where n is the number of data points, and x̅ and y̅ are the means of x and y, respectively.

- Plugging in the values from the data, we get:

m = (56 - 4*2.5*4.5)/(30 - 4*6.25) = 0.8

b = 4.5 - 0.8*2.5 = 2.5

- Therefore, the best fit line is:

y = 0.8x + 2.5

- The SSE for this line is:

SSE = (2 - (0.8*1 + 2.5))² + (4 - (0.8*2 + 2.5))² + (5 - (0.8*3 + 2.5))² + (7 - (0.8*4 + 2.5))²

SSE = 0.4 + 0.4 + 0.4 + 0.4

SSE = 1.6

- The graph of the data points and the best fit line is shown below:

![Graph of data points and best fit line](https://i.imgur.com/7wM6g0u.png)