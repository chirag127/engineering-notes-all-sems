Hello, I am Sydney, your AI assistant. I can help you with your study material for Engineering Mathematics-I. Here is the content for the topic of change of order of integration for the unit 4 - multiple integration.

### Change of order of integration

- Multiple integration is the process of integrating a function of two or more variables over a region in the corresponding space.
- The order of integration is the sequence in which the integrals are evaluated, such as $\int\int f(x,y) dxdy$ or $\int\int f(x,y) dydx$.
- The order of integration can be changed if the region of integration can be described in more than one way using different variables.
- Changing the order of integration can simplify the calculation of multiple integrals by avoiding difficult integrands or limits of integration.
- To change the order of integration, we need to follow these steps:
  - Sketch the region of integration and identify its boundaries in terms of the given variables.
  - Rewrite the boundaries in terms of the new variables by solving for one variable in terms of the other or using geometric properties.
  - Rewrite the integrand in terms of the new variables by substituting the expressions for the old variables or using the Jacobian determinant.
  - Rewrite the integral with the new order of integration, integrand, and limits of integration.
  - Evaluate the integral using the appropriate methods of integration.

- For example, consider the integral $\int_0^1\int_x^{\sqrt{x}} \frac{y}{x} dydx$.
  - The region of integration is bounded by the lines $y=x$, $y=\sqrt{x}$, and $x=1$ in the first quadrant.
  - To change the order of integration, we can rewrite the boundaries in terms of $y$ by solving for $x$ in terms of $y$. We get $x=y^2$ and $x=y$.
  - The integrand can be rewritten in terms of $y$ by substituting $x=y^2$ in the fraction. We get $\frac{1}{y}$.
  - The integral with the new order of integration is $\int_0^1\int_{y^2}^y \frac{1}{y} dxdy$.
  - To evaluate the integral, we first integrate with respect to $x$ and get $\frac{1}{y}(y-y^2)$. Then we integrate with respect to $y$ and get $\frac{1}{2}(y^2-\frac{y^4}{4})$ evaluated from $0$ to $1$. The final answer is $\frac{1}{4}$.