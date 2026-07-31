# Surface Integral

- A surface integral is a generalization of a line integral to account for surfaces in three dimensions.
- A surface integral is used to add a bunch of values associated with points on a surface, such as the area, the flux, the mass, the electric field, etc.
- A surface integral can be of two types: scalar or vector.
- A scalar surface integral is the integral of a scalar function over a surface, such as the area of the surface or the mass of a thin sheet.
- A vector surface integral is the integral of a vector field over a surface, such as the flux of the field through the surface or the work done by the field along the surface.
- A surface integral can be computed using various techniques, such as parametrization, projection, or divergence theorem, depending on the type of the surface and the function.
- A surface integral can be expressed in different notations, such as $\iint_S f(x,y,z) dS$ or $\iint_S \vec{F} \cdot d\vec{S}$, where $S$ is the surface, $f$ is the scalar function, $\vec{F}$ is the vector field, and $dS$ or $d\vec{S}$ is the differential element of the surface.
- A surface integral can be applied to various problems in physics, engineering, and mathematics, such as calculating the heat transfer, the electric potential, the surface area, the center of mass, etc.

## Example

- Find the surface integral of the function $f(x,y,z) = x^2 + y^2 + z^2$ over the sphere $x^2 + y^2 + z^2 = 4$.

- Solution:

- We can use the parametrization technique to compute the surface integral. We can parametrize the sphere using spherical coordinates as follows:

$$x = 2 \sin \theta \cos \phi$$
$$y = 2 \sin \theta \sin \phi$$
$$z = 2 \cos \theta$$
$$0 \leq \theta \leq \pi, 0 \leq \phi \leq 2\pi$$

- The differential element of the surface is given by:

$$d\vec{S} = \frac{\partial \vec{r}}{\partial \theta} \times \frac{\partial \vec{r}}{\partial \phi} d\theta d\phi$$

- where $\vec{r} = (x,y,z)$ is the position vector of a point on the surface. We can compute the cross product as follows:

$$\frac{\partial \vec{r}}{\partial \theta} = (2 \cos \theta \cos \phi, 2 \cos \theta \sin \phi, -2 \sin \theta)$$
$$\frac{\partial \vec{r}}{\partial \phi} = (-2 \sin \theta \sin \phi, 2 \sin \theta \cos \phi, 0)$$
$$\frac{\partial \vec{r}}{\partial \theta} \times \frac{\partial \vec{r}}{\partial \phi} = (4 \sin^2 \theta \cos \phi, 4 \sin^2 \theta \sin \phi, 4 \sin \theta \cos \theta)$$

- The magnitude of the cross product is:

$$|\frac{\partial \vec{r}}{\partial \theta} \times \frac{\partial \vec{r}}{\partial \phi}| = 4 \sin \theta$$

- Therefore, the differential element of the surface is:

$$dS = 4 \sin \theta d\theta d\phi$$

- The surface integral is then:

$$\iint_S f(x,y,z) dS = \int_0^{2\pi} \int_0^{\pi} f(2 \sin \theta \cos \phi, 2 \sin \theta \sin \phi, 2 \cos \theta) 4 \sin \theta d\theta d\phi$$
$$= \int_0^{2\pi} \int_0^{\pi} (4 \sin^2 \theta \cos^2 \phi + 4 \sin^2 \theta \sin^2 \phi + 4 \cos^2 \theta) 4 \sin \theta d\theta d\phi$$
$$= \int_0^{