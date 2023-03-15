### Surface integral

- A surface integral is a generalization of a line integral to account for surfaces in three dimensions.
- A surface integral is used to add a bunch of values associated with points on a surface, such as the flux of a vector field or the mass of a thin sheet.
- A surface integral can be defined for scalar fields or vector fields, depending on whether the integrand is a scalar or a vector.
- A surface integral of a scalar field over a surface S is denoted by

$$\iint_S f(x,y,z) \, dS$$

where f(x,y,z) is the scalar field and dS is the differential element of surface area.
- A surface integral of a vector field over a surface S is denoted by

$$\iint_S \mathbf{F} \cdot \, d\mathbf{S}$$

where $\mathbf{F}$ is the vector field and d$\mathbf{S}$ is the differential element of surface area with a direction normal to the surface.
- A surface integral can be computed by parametrizing the surface S with a function $\mathbf{r}(u,v)$ and using the formula

$$\iint_S f(x,y,z) \, dS = \iint_D f(\mathbf{r}(u,v)) \, \left\lvert \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right\rvert \, du \, dv$$

where D is the domain of the parametrization and $\frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v}$ is the cross product of the partial derivatives of $\mathbf{r}$ with respect to u and v, which gives a normal vector to the surface.
- A surface integral can also be computed by using a projection onto a coordinate plane and using the formula

$$\iint_S f(x,y,z) \, dS = \iint_R f(x,y,g(x,y)) \, \sqrt{1 + \left(\frac{\partial g}{\partial x}\right)^2 + \left(\frac{\partial g}{\partial y}\right)^2} \, dx \, dy$$

where R is the projection of S onto the xy-plane and g(x,y) is the function that gives the z-coordinate of the surface S.

- A surface integral can be used to calculate the surface area of a surface by setting f(x,y,z) = 1 in the formula.
- A surface integral can be used to calculate the flux of a vector field through a surface by using the dot product of the vector field and the normal vector to the surface in the formula.
- A surface integral can be used to calculate the mass of a thin sheet by using the density function as the scalar field in the formula.