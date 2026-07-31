Hello, I am Sydney, your AI assistant. I can help you with your topic of change of order of integration. Here is some content that you can use for your notes:

### Change of order of integration

- Sometimes, it is easier or more convenient to evaluate a double integral by changing the order of integration.
- The order of integration is the order in which the variables are integrated with respect to their limits.
- The order of integration can be changed by using the following steps:

  1. Sketch the region of integration in the xy-plane and identify the limits of integration for each variable.
  2. Rewrite the limits of integration in terms of the other variable, using the equation of the boundary curve or line.
  3. Swap the order of integration and the corresponding limits of integration.
  4. Evaluate the new double integral.

- For example, consider the following double integral:

  $$\int_0^1 \int_{y^2}^y f(x,y) dx dy$$

  - The order of integration is dx dy, which means we integrate first with respect to x and then with respect to y.
  - The region of integration in the xy-plane is bounded by the lines y = 0, y = 1, and the parabola x = y^2, as shown below:

    ![Region of integration](https://i.imgur.com/4lZ0xZy.png)

  - To change the order of integration to dy dx, we need to rewrite the limits of integration for y in terms of x, using the equation x = y^2. This means that y = $\sqrt{x}$ or y = $-\sqrt{x}$, depending on the sign of x.
  - The new limits of integration for y are from $-\sqrt{x}$ to $\sqrt{x}$, and the limits of integration for x are from 0 to 1, as shown below:

    ![New limits of integration](https://i.imgur.com/0X9Q2fW.png)

  - The new double integral is:

    $$\int_0^1 \int_{-\sqrt{x}}^{\sqrt{x}} f(x,y) dy dx$$

  - This double integral may be easier to evaluate than the original one, depending on the function f(x,y).