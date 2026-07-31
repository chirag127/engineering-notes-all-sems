# Double integral

- A double integral is a way to integrate over a two-dimensional area. It can be used to find the volume under a surface, the area of a region, the average value of a function, and other applications.
- A double integral of a function of two variables, say f(x,y), over a region R in the xy-plane, is denoted by:

$$\iint_R f(x,y) \, dA$$

where dA is a small element of area in the region R.

- A double integral can be evaluated by iterated integration, which means integrating first with respect to one variable, then with respect to the other variable. For example, if R is a rectangular region with boundaries a ≤ x ≤ b and c ≤ y ≤ d, then the double integral can be written as:

$$\iint_R f(x,y) \, dA = \int_a^b \int_c^d f(x,y) \, dy \, dx = \int_c^d \int_a^b f(x,y) \, dx \, dy$$

- The order of integration can be changed if the region R is simple enough, and the limits of integration are adjusted accordingly. For example, if R is a triangular region with vertices (0,0), (1,0), and (0,1), then the double integral can be written as:

$$\iint_R f(x,y) \, dA = \int_0^1 \int_0^{1-x} f(x,y) \, dy \, dx = \int_0^1 \int_y^1 f(x,y) \, dx \, dy$$

- A double integral can also be evaluated by changing to polar coordinates, if the region R and the function f(x,y) are more convenient in terms of r and θ. For example, if R is a circular region with radius 1 and center at the origin, then the double integral can be written as:

$$\iint_R f(x,y) \, dA = \int_0^{2\pi} \int_0^1 f(r \cos \theta, r \sin \theta) \, r \, dr \, d\theta$$

where r is the distance from the origin and θ is the angle from the positive x-axis.

- A double integral has some properties that are similar to those of a single integral, such as linearity, additivity, and comparison. For example, if f(x,y) and g(x,y) are two functions defined on a region R, and k is a constant, then:

$$\iint_R (f(x,y) + g(x,y)) \, dA = \iint_R f(x,y) \, dA + \iint_R g(x,y) \, dA$$

$$\iint_R k f(x,y) \, dA = k \iint_R f(x,y) \, dA$$

$$\iint_R f(x,y) \, dA \leq \iint_R g(x,y) \, dA \quad \text{if} \quad f(x,y) \leq g(x,y) \quad \text{for all} \quad (x,y) \in R$$