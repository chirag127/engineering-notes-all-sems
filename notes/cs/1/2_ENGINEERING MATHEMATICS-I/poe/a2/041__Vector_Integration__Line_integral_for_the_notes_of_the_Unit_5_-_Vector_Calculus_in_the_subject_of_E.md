 Here is the content in markdown format without any emojis or external links:

### Vector Integration: Line integral

- A line integral is a integral where the function to be integrated is evaluated along a curve.
- The line integral of a vector field F along a curve C is defined as the limit of the sum of the products of the magnitudes of the field and the corresponding elements of arc as the norm of elements tends to zero.
- Mathematically, if C is the parametric curve r(t) = (x(t), y(t), z(t)), then the line integral is:
`[; \int_C \mathbf{F} \cdot \mathbf{dr} = \lim_{ \Delta t \to 0 } \sum_{i=0}^{n-1} F(r(t_i)) \Delta r_i ;]`
- Here, `Δr_i` is the element of arc length and `r(t_i)` is the position vector at `t = t_i`.
- The line integral depends on the curve taken and the direction of integration. It gives the work done by the field F in taking a particle around the curve.
- Some properties of line integrals are:
- Linearity: ` `[; \int_{C_1 + C_2} \mathbf{F} \cdot d\mathbf{r} = \int_{C_1} \mathbf{F} \cdot d\mathbf{r} + \int_{C_2} \mathbf{F} \cdot d\mathbf{r} ;]`
- Positive and negative integrands: ` `[; \int_C (-\mathbf{F}) \cdot d\mathbf{r} = - \int_C \mathbf{F} \cdot d\mathbf{r} ;]`
- Parametrization independence: If C and C' represent the same curve with different parametrizations, then ` `[; \int_C \mathbf{F} \cdot d\mathbf{r} = \int_{C'} \mathbf{F} \cdot d\mathbf{r} ;]`