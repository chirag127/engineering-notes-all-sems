# Directional derivatives

- A directional derivative is a measure of how a function changes in a given direction at a given point.
- It is a generalization of the concept of partial derivatives, which measure the change of a function along the coordinate axes.
- The directional derivative of a function $f(x,y,z)$ at a point $(x_0,y_0,z_0)$ in the direction of a unit vector $\vec{u}$ is denoted by $\nabla_uf(x_0,y_0,z_0)$ and is defined as the limit

$$\nabla_uf(x_0,y_0,z_0) = \lim_{h\to 0} \frac{f(x_0+hu_x,y_0+hu_y,z_0+hu_z) - f(x_0,y_0,z_0)}{h}$$

- The directional derivative can also be expressed using the gradient vector of the function, which is a vector that points in the direction of the greatest rate of increase of the function. The gradient vector is denoted by $\nabla f$ and is defined as

$$\nabla f = \frac{\partial f}{\partial x}\vec{i} + \frac{\partial f}{\partial y}\vec{j} + \frac{\partial f}{\partial z}\vec{k}$$

- The directional derivative can then be written as the dot product of the gradient vector and the unit vector:

$$\nabla_uf(x_0,y_0,z_0) = \nabla f(x_0,y_0,z_0) \cdot \vec{u}$$

- This formula shows that the directional derivative is the projection of the gradient vector onto the direction of $\vec{u}$, and that it is maximized when $\vec{u}$ is parallel to $\nabla f$.

- Some properties of the directional derivative are:

  - If $\vec{u}$ is the zero vector, then $\nabla_uf(x_0,y_0,z_0) = 0$.
  - If $\vec{u}$ is perpendicular to $\nabla f$, then $\nabla_uf(x_0,y_0,z_0) = 0$.
  - If $\vec{u}$ is parallel to $\nabla f$, then $\nabla_uf(x_0,y_0,z_0) = |\nabla f(x_0,y_0,z_0)|$.

- An example of finding the directional derivative of a function is:

  - Find the directional derivative of the function $f(x,y) = x^2 + y^2$ at the point $(1,1)$ in the direction of $\vec{v} = 2\vec{i} - \vec{j}$.

  - Solution:

    - First, we need to find the unit vector in the direction of $\vec{v}$. We can do this by dividing $\vec{v}$ by its magnitude:

    $$\vec{u} = \frac{\vec{v}}{|\vec{v}|} = \frac{2\vec{i} - \vec{j}}{\sqrt{2^2 + (-1)^2}} = \frac{2}{\sqrt{5}}\vec{i} - \frac{1}{\sqrt{5}}\vec{j}$$

    - Next, we need to find the gradient vector of the function at the point $(1,1)$. We can do this by taking the partial derivatives of the function with respect to $x$ and $y$ and plugging in the point:

    $$\nabla f = \frac{\partial f}{\partial x}\vec{i} + \frac{\partial f}{\partial y}\vec{j} = (2x)\vec{i} + (2y)\vec{j}$$

    $$\nabla f(1,1) = (2)\vec{i} + (2)\vec{j}$$

    - Finally, we can find the directional derivative by taking the dot product of the gradient vector and the unit vector:

    $$\nabla_uf(1,1) = \nabla f(1,1) \cdot \vec{u} = (2\vec{i} + 2\vec{j}) \cdot \left(\frac{2}{\sqrt{5}}\vec{i} - \frac{1}{\sqrt{