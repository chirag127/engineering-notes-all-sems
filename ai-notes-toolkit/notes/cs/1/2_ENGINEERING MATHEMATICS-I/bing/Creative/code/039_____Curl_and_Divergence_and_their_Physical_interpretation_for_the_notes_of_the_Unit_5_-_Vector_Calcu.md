# Curl and Divergence and their Physical Interpretation

- Curl and divergence are two operators that can be applied to vector fields in three-dimensional Euclidean space.
- Vector fields can be used to model the velocity of a fluid flow at each point in space.
- Curl and divergence measure different aspects of the behavior of the fluid flow around a point.

## Curl

- The curl of a vector field $\vec{F}$, denoted by $\nabla \times \vec{F}$, is a vector field that points in the direction of the axis of rotation of the fluid flow, and has a magnitude equal to the angular speed of the rotation.
- The curl can be computed using the formula:

$$\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_x & F_y & F_z \end{vmatrix}$$

- The curl can also be interpreted as the circulation of the vector field per unit area, where circulation is the line integral of the vector field along a closed curve.
- The curl can be used to test if a vector field is conservative, that is, if it is the gradient of some scalar function. A vector field is conservative if and only if its curl is zero everywhere.
- The curl can also be used to find the magnetic field induced by an electric current, according to Ampere's law.

## Divergence

- The divergence of a vector field $\vec{F}$, denoted by $\nabla \cdot \vec{F}$, is a scalar field that measures the net outward flux of the vector field per unit volume.
- The divergence can be computed using the formula:

$$\nabla \cdot \vec{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$$

- The divergence can also be interpreted as the rate of change of density of the fluid flow at a point. A positive divergence means that the fluid is expanding or diverging from the point, while a negative divergence means that the fluid is contracting or converging to the point.
- The divergence can be used to test if a vector field is solenoidal, that is, if it has no sources or sinks. A vector field is solenoidal if and only if its divergence is zero everywhere.
- The divergence can also be used to find the electric field due to a charge distribution, according to Gauss's law.