### Surface integral

- A surface integral is a generalization of double integrals to integration over surfaces.
- It can be thought of as the double integral analogue of the line integral.
- Surface integrals are used to calculate the area approximation of all points present on the surface, or to add a bunch of values associated with points on a surface.
- The definition of surface integral relies on splitting the surface into small surface elements, and taking the limit of the sum of products formed by multiplying the area of a portion of a surface by the value of a function at any point in this area, as the area of the largest portion approaches zero .
- There are two types of surface integrals: scalar surface integrals and vector surface integrals.
- A scalar surface integral is used to integrate a scalar function over a surface, such as the temperature or density of a surface.
- A vector surface integral is used to integrate a vector field over a surface, such as the flux or circulation of a vector field.
- The formula for a scalar surface integral is:

$$\iint_S f(x,y,z) \, dS$$

where $f(x,y,z)$ is the scalar function, $S$ is the surface, and $dS$ is the surface element.
- The formula for a vector surface integral is:

$$\iint_S \mathbf{F} \cdot \, d\mathbf{S}$$

where $\mathbf{F}$ is the vector field, $S$ is the surface, and $d\mathbf{S}$ is the vector surface element.
- To evaluate a surface integral, one needs to parameterize the surface using two variables, such as $u$ and $v$, and express the surface element in terms of these variables.
- For example, if the surface $S$ is given by the equation $z = g(x,y)$, then one possible parameterization is:

$$x = u, \quad y = v, \quad z = g(u,v)$$

and the surface element is:

$$dS = \sqrt{1 + \left(\frac{\partial g}{\partial u}\right)^2 + \left(\frac{\partial g}{\partial v}\right)^2} \, du \, dv$$

- Then the scalar surface integral becomes:

$$\iint_S f(x,y,z) \, dS = \iint_D f(u,v,g(u,v)) \sqrt{1 + \left(\frac{\partial g}{\partial u}\right)^2 + \left(\frac{\partial g}{\partial v}\right)^2} \, du \, dv$$

where $D$ is the projection of $S$ onto the $xy$-plane.
- Similarly, the vector surface integral becomes:

$$\iint_S \mathbf{F} \cdot \, d\mathbf{S} = \iint_D \mathbf{F}(u,v,g(u,v)) \cdot \left(\frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v}\right) \, du \, dv$$

where $\mathbf{r}(u,v) = (u,v,g(u,v))$ is the position vector of the surface, and $\times$ denotes the cross product of two vectors.