### Total derivative

- The total derivative of a function of several variables means the total change in the dependent variable due to the changes in all the independent variables.
- The total derivative is the derivative with respect to a variable that depends on the function not only directly but also via the intermediate variables.
- The formula for a total derivative is a direct result of the chain rule.
- The total derivative can be used to approximate the change in the function value given small changes in the independent variables.
- The total derivative can also be used to analyze the sensitivity or error propagation of the function value due to the errors in the independent variables.

#### Example

- Suppose z = f(x, y) = x^2 + y^2 is a function of two variables, where z is the dependent variable and x and y are the independent variables.
- The total derivative of z with respect to t is given by

dz/dt = (dz/dx)(dx/dt) + (dz/dy)(dy/dt)

- where dz/dx and dz/dy are the partial derivatives of z with respect to x and y, and dx/dt and dy/dt are the derivatives of x and y with respect to t.
- If x = t and y = 2t, then

dx/dt = 1 and dy/dt = 2

- and

dz/dx = 2x and dz/dy = 2y

- Therefore,

dz/dt = (2x)(1) + (2y)(2) = 2t + 4t = 6t

- This means that the rate of change of z with respect to t is 6t.