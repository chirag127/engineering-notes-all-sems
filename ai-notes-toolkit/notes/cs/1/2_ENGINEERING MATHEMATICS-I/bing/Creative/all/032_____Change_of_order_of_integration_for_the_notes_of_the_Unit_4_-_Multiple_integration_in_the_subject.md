Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of change of order of integration for the notes of the Unit 4 - Multiple integration in the subject of ENGINEERING MATHEMATICS-I.

# Change of order of integration

- Sometimes, it is easier to evaluate a double integral by changing the order of integration.
- The order of integration is the order in which the integrals are performed.
- The order of integration can be changed by using the following steps:

  1. Sketch the region of integration and identify the limits of integration for each variable.
  2. Rewrite the limits of integration by interchanging the roles of the variables and the functions that define the region.
  3. Evaluate the new double integral by performing the integrals in the reversed order.

- Example: Evaluate the double integral $\int_0^1 \int_x^{\sqrt{x}} f(x,y) dy dx$ by changing the order of integration.

  - Solution: The region of integration is bounded by the curves $y=x$, $y=\sqrt{x}$, and $x=1$. The limits of integration for $x$ are $0$ and $1$, and the limits of integration for $y$ are $x$ and $\sqrt{x}$.
  - To change the order of integration, we interchange the roles of $x$ and $y$. The limits of integration for $y$ are $0$ and $1$, and the limits of integration for $x$ are $y^2$ and $y$. The new double integral is $\int_0^1 \int_{y^2}^y f(x,y) dx dy$.
  - To evaluate the new double integral, we perform the integrals in the reversed order. First, we integrate with respect to $x$, then with respect to $y$. The result is $\int_0^1 \left[ F(y,y) - F(y^2,y) \right] dy$, where $F(x,y)$ is an antiderivative of $f(x,y)$ with respect to $x$.