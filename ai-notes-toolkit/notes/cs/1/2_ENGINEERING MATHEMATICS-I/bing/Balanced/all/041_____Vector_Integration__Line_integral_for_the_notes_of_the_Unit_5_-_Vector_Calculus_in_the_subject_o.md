# Vector Integration: Line integral

- A line integral is an integral in which a function is integrated along some curve in the coordinate system.
- The function which is to be integrated can either be represented as a scalar field or vector field. We can integrate both scalar-valued function and vector-valued function along a curve.
- A line integral of a scalar field is thus a line integral of a vector field, where the vectors are always tangential to the line of the integration.
- A line integral of a vector field can be thought of as a measure of the total effect of a given tensor field along a given curve. For example, the line integral over a scalar field can be interpreted as the area under the field carved out by a particular curve.
- Line integrals are useful in physics for computing the work done by a force on a moving object.
- The line integral of a vector field on a curve is defined by:

$$\int_C \mathbf{F} \cdot d\mathbf{r}$$

where $\mathbf{F}$ is the vector field, $C$ is the curve, and $\cdot$ denotes a dot product.
- In Cartesian coordinates, the line integral can be written as:

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) dt$$

where $\mathbf{r}(t)$ is a parametrization of the curve $C$ from $t=a$ to $t=b$, and $\mathbf{r}'(t)$ is the derivative of $\mathbf{r}(t)$ with respect to $t$.
- We can also write line integrals of vector fields as a line integral with respect to arc length as follows:

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C \mathbf{F} \cdot \mathbf{T} ds$$

where $\mathbf{T}(t)$ is the unit tangent vector and is given by:

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$$

and $ds$ is the differential arc length, given by:

$$ds = \|\mathbf{r}'(t)\| dt$$

- The value of the line integral depends on the orientation of the curve $C$. If we parameterize the curve such that we move in the opposite direction as $t$ increases, the value of the line integral is multiplied by $-1$.
- The line integral of a vector field is independent of the parametrization $\mathbf{r}(t)$ in absolute value, but they do depend on its orientation.