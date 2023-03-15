Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of change of order of integration for the notes of the Unit 4 - Multiple integration in the subject of ENGINEERING MATHEMATICS-I.

### Change of order of integration

- Sometimes, it is easier to evaluate a double integral by changing the order of integration.
- The order of integration is the sequence in which we integrate with respect to the variables.
- For example, the order of integration for $\int_{a}^{b}\int_{c}^{d}f(x,y)dydx$ is $dydx$, which means we integrate first with respect to $y$ and then with respect to $x$.
- The order of integration for $\int_{c}^{d}\int_{a}^{b}f(x,y)dxdy$ is $dxdy$, which means we integrate first with respect to $x$ and then with respect to $y$.
- To change the order of integration, we need to find the new limits of integration for the variables.
- The new limits of integration should describe the same region of integration as the original ones, but in a different way.
- One way to find the new limits of integration is to sketch the region of integration and label the boundaries with the corresponding equations.
- Then, we can read off the new limits of integration by looking at the horizontal and vertical projections of the region.
- For example, consider the double integral $\int_{0}^{1}\int_{y}^{2y}f(x,y)dxdy$.
- The region of integration is bounded by the lines $y=0$, $y=1$, $x=y$, and $x=2y$.
- To change the order of integration to $dydx$, we need to find the new limits of integration for $y$ in terms of $x$.
- We can sketch the region of integration and label the boundaries as shown below.

![Region of integration](https://i.imgur.com/6w7lZ0A.png)

- The horizontal projection of the region is the interval $[0,2]$ on the $x$-axis.
- The vertical projection of the region is the interval $[0,1]$ on the $y$-axis.
- The lower limit of integration for $y$ is the line $y=x/2$, which is the lower boundary of the region.
- The upper limit of integration for $y$ is the line $y=x$, which is the upper boundary of the region.
- Therefore, the new limits of integration for $y$ are $x/2$ and $x$.
- The new order of integration is $\int_{0}^{2}\int_{x/2}^{x}f(x,y)dydx$.
- This means we integrate first with respect to $y$ from $x/2$ to $x$, and then with respect to $x$ from $0$ to $2$.
- Note that changing the order of integration does not change the value of the double integral, as long as the region of integration is the same.