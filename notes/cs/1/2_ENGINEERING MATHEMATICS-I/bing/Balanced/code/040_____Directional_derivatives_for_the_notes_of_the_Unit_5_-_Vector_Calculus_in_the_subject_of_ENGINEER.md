### Directional derivatives

- A directional derivative is a measure of the rate of change of a function in a given direction at a given point.
- It generalizes the concept of partial derivatives, which are the rates of change of a function in the coordinate directions.
- The directional derivative of a function $f(x,y,z)$ at a point $P$ in the direction of a unit vector $\vec{u}$ is denoted by $\nabla_{\vec{u}}f(P)$ and is defined as:

$$\nabla_{\vec{u}}f(P) = \lim_{h\to 0} \frac{f(P+h\vec{u})-f(P)}{h}$$

- Alternatively, the directional derivative can be expressed using the gradient vector of the function, which is a vector that points in the direction of the greatest rate of increase of the function. The gradient vector of $f(x,y,z)$ is denoted by $\nabla f$ and is defined as:

$$\nabla f = \frac{\partial f}{\partial x}\vec{i} + \frac{\partial f}{\partial y}\vec{j} + \frac{\partial f}{\partial z}\vec{k}$$

- The directional derivative can then be computed as the dot product of the gradient vector and the unit vector:

$$\nabla_{\vec{u}}f(P) = \nabla f(P) \cdot \vec{u}$$

- This formula shows that the directional derivative is the projection of the gradient vector onto the direction of $\vec{u}$, and that it is maximized when $\vec{u}$ is parallel to $\nabla f$.

- Example: Find the directional derivative of the function $f(x,y) = x^2 + y^2$ at the point $(1,1)$ in the direction of $\vec{v} = \frac{1}{\sqrt{2}}(\vec{i}+\vec{j})$.

- Solution: First, we find the gradient vector of the function:

$$\nabla f = \frac{\partial f}{\partial x}\vec{i} + \frac{\partial f}{\partial y}\vec{j} = 2x\vec{i} + 2y\vec{j}$$

- Then, we evaluate the gradient vector at the point $(1,1)$:

$$\nabla f(1,1) = 2\vec{i} + 2\vec{j}$$

- Next, we normalize the vector $\vec{v}$ to get a unit vector $\vec{u}$ in the same direction:

$$\vec{u} = \frac{\vec{v}}{|\vec{v}|} = \frac{1}{\sqrt{2}}(\vec{i}+\vec{j})$$

- Finally, we use the formula for the directional derivative:

$$\nabla_{\vec{u}}f(1,1) = \nabla f(1,1) \cdot \vec{u} = (2\vec{i} + 2\vec{j}) \cdot \frac{1}{\sqrt{2}}(\vec{i}+\vec{j}) = \frac{4}{\sqrt{2}}$$

- Therefore, the directional derivative of the function at the point $(1,1)$ in the direction of $\vec{v}$ is $\frac{4}{\sqrt{2}}$.