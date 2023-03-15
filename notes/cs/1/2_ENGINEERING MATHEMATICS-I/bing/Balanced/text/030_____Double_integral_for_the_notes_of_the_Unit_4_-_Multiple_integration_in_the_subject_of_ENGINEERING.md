### Double integral

- A double integral is a way to integrate over a two-dimensional area. It can be used to find the volume under a surface, the area of a region, the average value of a function, and other applications.
- A double integral of a function of two variables, say f(x,y), over a region R in the xy-plane, is denoted by:

$$\iint_R f(x,y) \, dA$$

where dA is a small element of area in the region R.

- A double integral can be evaluated by iterated integration, which means integrating first with respect to one variable and then with respect to the other variable. For example, if R is a rectangular region with vertices (a,b), (a,d), (c,b), and (c,d), then the double integral can be written as:

$$\iint_R f(x,y) \, dA = \int_a^c \int_b^d f(x,y) \, dy \, dx = \int_b^d \int_a^c f(x,y) \, dx \, dy$$

- The order of integration can be changed if the region R can be described by two different sets of limits. For example, if R is a triangular region with vertices (0,0), (1,0), and (0,1), then the double integral can be written as:

$$\iint_R f(x,y) \, dA = \int_0^1 \int_0^{1-x} f(x,y) \, dy \, dx = \int_0^1 \int_0^{1-y} f(x,y) \, dx \, dy$$

- The value of the double integral does not depend on the order of integration, as long as the limits are consistent with the region R.

- A double integral can also be evaluated by changing to polar coordinates, if the region R is circular or has a simple description in terms of r and θ. For example, if R is a disk with center at the origin and radius 2, then the double integral can be written as:

$$\iint_R f(x,y) \, dA = \int_0^{2\pi} \int_0^2 f(r \cos \theta, r \sin \theta) \, r \, dr \, d\theta$$

where r is the distance from the origin and θ is the angle measured from the positive x-axis.

- The change of variables formula for double integrals states that if x = g(u,v) and y = h(u,v) are smooth functions that map a region S in the uv-plane to a region R in the xy-plane, then:

$$\iint_R f(x,y) \, dA = \iint_S f(g(u,v),h(u,v)) \, |J| \, du \, dv$$

where J is the Jacobian determinant given by:

$$J = \frac{\partial (x,y)}{\partial (u,v)} = \frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \frac{\partial y}{\partial u}$$

and |J| is the absolute value of J.

- The change of variables formula can be used to simplify the evaluation of double integrals by transforming the region R and the function f into a more convenient form. For example, if R is an ellipse with equation $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, then the change of variables x = au and y = bv transforms R into a unit circle and the double integral becomes:

$$\iint_R f(x,y) \, dA = \iint_{\text{unit circle}} f(au,bv) \, ab \, du \, dv$$

- Some examples of double integrals are:

  - To find the volume of a solid bounded by a surface z = f(x,y) and the xy-plane over a region R, use:

  $$V = \iint_R f(x,y) \, dA$$

  - To find the area of a region R in the xy-plane, use:

  $$A = \iint_R 1 \, dA$$

  - To find the average value of a function f(x,y) over a region R in the xy-plane, use:

  $$\bar{f} = \frac