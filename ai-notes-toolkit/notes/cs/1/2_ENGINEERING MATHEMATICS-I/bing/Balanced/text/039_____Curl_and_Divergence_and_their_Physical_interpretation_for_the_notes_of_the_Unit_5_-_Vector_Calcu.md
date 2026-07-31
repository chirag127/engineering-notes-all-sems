### Curl and Divergence and their Physical interpretation

- Curl and divergence are two operators that can be applied to vector fields in three-dimensional Euclidean space.
- Vector fields can be used to model the velocity of a fluid flow at each point in space.
- Curl and divergence measure different aspects of the behavior of the fluid flow around a point.

#### Divergence

- Divergence of a vector field $\vec{F}$ at a point $P$ is denoted by $\nabla \cdot \vec{F}(P)$ and is defined as the limit of the net outward flux of $\vec{F}$ per unit volume as the volume shrinks to $P$.
- Divergence can be calculated using the formula $\nabla \cdot \vec{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$, where $F_x, F_y, F_z$ are the components of $\vec{F}$.
- Physically, divergence measures the tendency of the fluid to collect or disperse at a point. A positive divergence means that the fluid is expanding or diverging from the point, while a negative divergence means that the fluid is contracting or converging to the point. A zero divergence means that the fluid is neither expanding nor contracting, but maintaining a constant density around the point.
- Examples of vector fields with positive, negative, and zero divergence are:

  - $\vec{F}(x,y,z) = (x,y,z)$, which has divergence $\nabla \cdot \vec{F} = 3$. This vector field represents a fluid that is moving away from the origin in all directions, creating a source of fluid at the origin.
  - $\vec{F}(x,y,z) = (-x,-y,-z)$, which has divergence $\nabla \cdot \vec{F} = -3$. This vector field represents a fluid that is moving toward the origin in all directions, creating a sink of fluid at the origin.
  - $\vec{F}(x,y,z) = (y,-x,0)$, which has divergence $\nabla \cdot \vec{F} = 0$. This vector field represents a fluid that is rotating around the $z$-axis, creating a vortex of fluid with no net change in density.

#### Curl

- Curl of a vector field $\vec{F}$ at a point $P$ is denoted by $\nabla \times \vec{F}(P)$ and is defined as the vector whose magnitude is the maximum circulation of $\vec{F}$ per unit area as the area shrinks to $P$ and whose direction is the normal to the plane of the circulation.
- Curl can be calculated using the formula $\nabla \times \vec{F} = \left( \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z} \right) \hat{i} + \left( \frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x} \right) \hat{j} + \left( \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \right) \hat{k}$, where $F_x, F_y, F_z$ are the components of $\vec{F}$ and $\hat{i}, \hat{j}, \hat{k}$ are the unit vectors along the $x, y, z$ axes respectively.
- Physically, curl measures the tendency of the fluid to swirl or rotate around a point. A nonzero curl means that the fluid is spinning or curling around the point, while a zero curl means that the fluid is not spinning or curling, but moving in a straight line or not moving at all.
- Examples of vector fields with nonzero and zero curl are:

  - $\vec{F}(x,y,z) = (y,-x,0)$, which has curl $\nabla \times \vec{F} = 2 \hat{k}$. This vector field represents a fluid that is rotating around the $z$-axis with a constant angular speed of 2 radians per unit time.
  - $\vec{F}(x,y,z) = (x,y,z)$, which has curl $\nabla \times \vec{F} = \vec{0}$. This vector field represents a fluid that is moving away