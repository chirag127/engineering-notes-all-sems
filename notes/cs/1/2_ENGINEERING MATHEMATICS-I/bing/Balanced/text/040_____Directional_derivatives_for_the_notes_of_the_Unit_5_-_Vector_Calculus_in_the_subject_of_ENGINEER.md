### Directional derivatives

- A directional derivative is a measure of the rate of change of a function in a given direction at a given point.
- It generalizes the concept of partial derivatives, which are the rates of change of a function in the coordinate directions.
- The directional derivative of a function $f(x,y,z)$ at a point $(x_0,y_0,z_0)$ in the direction of a unit vector $\vec{u}$ is denoted by $\nabla_uf(x_0,y_0,z_0)$ and defined as:

$$\nabla_uf(x_0,y_0,z_0) = \lim_{h\to 0} \frac{f(x_0+hu_x,y_0+hu_y,z_0+hu_z) - f(x_0,y_0,z_0)}{h}$$

- Alternatively, the directional derivative can be expressed using the gradient vector of $f$, which is $\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$. The formula is:

$$\nabla_uf(x_0,y_0,z_0) = \nabla f(x_0,y_0,z_0) \cdot \vec{u}$$

- The directional derivative has the following properties:

  - It is linear: $\nabla_u(af+bg) = a\nabla_uf + b\nabla_ug$ for any scalar functions $f$ and $g$ and any constants $a$ and $b$.
  - It is invariant under scalar multiplication of $\vec{u}$: $\nabla_{c\vec{u}}f = \nabla_{\vec{u}}f$ for any constant $c$.
  - It is zero if $\vec{u}$ is perpendicular to $\nabla f$: $\nabla_uf = 0$ if $\nabla f \cdot \vec{u} = 0$.
  - It is maximal if $\vec{u}$ is parallel to $\nabla f$: $\nabla_uf = |\nabla f|$ if $\vec{u} = \frac{\nabla f}{|\nabla f|}$.

- An example of finding the directional derivative is:

  - Find the directional derivative of $f(x,y) = x^2y$ at $(1,2)$ in the direction of $\vec{v} = (3,-4)$.

  - Solution: First, we need to find the unit vector in the direction of $\vec{v}$. This is given by:

    $$\vec{u} = \frac{\vec{v}}{|\vec{v}|} = \frac{(3,-4)}{\sqrt{3^2+(-4)^2}} = \left(\frac{3}{5},-\frac{4}{5}\right)$$

  - Next, we need to find the gradient vector of $f$ at $(1,2)$. This is given by:

    $$\nabla f(x,y) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right) = (2xy, x^2)$$

    $$\nabla f(1,2) = (2(1)(2), (1)^2) = (4,1)$$

  - Finally, we can use the formula to find the directional derivative:

    $$\nabla_uf(1,2) = \nabla f(1,2) \cdot \vec{u} = (4,1) \cdot \left(\frac{3}{5},-\frac{4}{5}\right) = \frac{12}{5} - \frac{4}{5} = \frac{8}{5}$$

  - Therefore, the directional derivative of $f$ at $(1,2)$ in the direction of $\vec{v}$ is $\frac{8}{5}$. This means that the function $f$ increases at a rate of $\frac{8}{5}$ units per unit distance along the direction of $\vec{v}$ at the point $(1,2)$.