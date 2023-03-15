# Total derivative

- The total derivative of a function of several variables means the total change in the dependent variable due to the changes in all the independent variables.
- The total derivative is the derivative with respect to a variable that depends on the function not only directly but also via the intermediate variables.
- The formula for a total derivative is a direct result of the chain rule.
- The total derivative can be used to approximate the change in a function given small changes in the variables, or to analyze the sensitivity or error propagation of a function.

## Definition and formula

- Suppose z = f(x, y) be a function of two variables, where z is the dependent variable and x and y are the independent variables.
- The total derivative of z with respect to t is denoted by dz/dt and is defined as

dz/dt = ∂z/∂x * dx/dt + ∂z/∂y * dy/dt

- where ∂z/∂x and ∂z/∂y are the partial derivatives of z with respect to x and y, and dx/dt and dy/dt are the derivatives of x and y with respect to t.
- The total differential of z is denoted by dz and is defined as

dz = ∂z/∂x * dx + ∂z/∂y * dy

- where dx and dy are the increments or changes in x and y.
- The total differential gives an approximation of the change in z given small changes in x and y, that is,

Δz ≈ dz

## Example

- Suppose z = x^2 + y^3, where x = t + 1 and y = t^2 - 1 are functions of t.
- Find the total derivative of z with respect to t.

Solution:

- First, we find the partial derivatives of z with respect to x and y.

∂z/∂x = 2x

∂z/∂y = 3y^2

- Next, we find the derivatives of x and y with respect to t.

dx/dt = 1

dy/dt = 2t

- Then, we use the formula for the total derivative to get

dz/dt = ∂z/∂x * dx/dt + ∂z/∂y * dy/dt

= 2x * 1 + 3y^2 * 2t

= 2(t + 1) + 6(t^2 - 1)t

= 8t^3 - 4t + 2

- This is the total derivative of z with respect to t.