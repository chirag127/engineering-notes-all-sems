 Here is the content in markdown format without any emojis or external links and in formal tone:

### Maxima and Minima of functions of several variables

- A function of several variables has a maximum or minimum value when its partial derivatives are all zero.
- The resulting equations are called the `equations of critical points`. Solving these equations gives the critical points of the function.
- The second partial derivatives are then evaluated at these critical points to classify them:
    - If all second partial derivatives are positive, it is a minimum.
    - If all second partial derivatives are negative, it is a maximum.
    - If some second partial derivative is zero or if they have different signs, the point is a saddle point or neither a maximum nor a minimum.
- Example: Consider the function $f(x, y) = x^2 - 2xy + 3y^2$.
    - Take partial derivatives: $\\frac{\\partial f}{\\partial x} = 2x - 2y$ and $\\frac{\\partial f}{\\partial y} = -2x + 6y$
    - Setting them equal to zero gives $x = y$ and $3y^2 - 2y - 2x + 2 = 0$
    - Solving the second equation gives $y = 1$ or $y = -2$
    - Evaluating second partial derivatives at $x = 1, y = 1$ gives $4 > 0$ and $6 > 0$. Therefore, $f$ has a minimum at $(x, y) = (1, 1)$.
- This method can be extended to functions of three or more variables by taking partial derivatives with respect to each variable and solving the equations simultaneously. The second partial derivatives are then evaluated to classify the critical point.