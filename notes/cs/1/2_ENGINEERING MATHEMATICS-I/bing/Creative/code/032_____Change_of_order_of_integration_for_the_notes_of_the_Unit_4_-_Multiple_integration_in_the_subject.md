Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of change of order of integration for the notes of the Unit 4 - Multiple integration in the subject of ENGINEERING MATHEMATICS-I.

```markdown
### Change of order of integration

- Sometimes, it is easier to evaluate a double integral by changing the order of integration.
- The order of integration is the order in which the variables are integrated with respect to their limits.
- The order of integration can be changed by using the following steps:

  1. Sketch the region of integration in the xy-plane and identify the limits of integration for each variable.
  2. Rewrite the limits of integration in terms of the other variable by solving the equations that define the boundaries of the region.
  3. Swap the order of integration and the corresponding limits of integration.
  4. Evaluate the new double integral.

- For example, consider the following double integral:

  $$\int_{0}^{1} \int_{y}^{2y} f(x,y) dx dy$$

  The region of integration is shown below:

  ![Region of integration](https://i.imgur.com/8T0Zz0n.png)

  The limits of integration for x are given by y and 2y, and the limits of integration for y are given by 0 and 1.
  To change the order of integration, we need to rewrite the limits of integration for y in terms of x by solving the equations y = x and y = x/2.

  $$y = x \implies x = y$$
  $$y = x/2 \implies x = 2y$$

  The new limits of integration for y are x and x/2, and the new limits of integration for x are 0 and 1.
  The order of integration is swapped, and the new double integral is:

  $$\int_{0}^{1} \int_{x/2}^{x} f(x,y) dy dx$$

  This double integral may be easier to evaluate than the original one, depending on the function f(x,y).
```