# Functions of complex variable

- A complex function is a function that maps complex numbers to complex numbers.
- A complex number is a number of the form z = x + iy, where x and y are real numbers and i is the imaginary unit, such that i^2 = -1.
- A complex function can be written as w = u + iv, where u and v are real-valued functions of x and y.
- A complex function can also be written as w = f(z), where f is a rule that assigns a complex number w to each complex number z.
- A complex function is said to be differentiable at a point z0 if the limit

$$f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}$$

exists and is independent of the direction of approach of z to z0.
- A complex function is said to be analytic or holomorphic at a point z0 if it is differentiable at z0 and at every point in some neighborhood of z0.
- A complex function is said to be entire if it is analytic at every point in the complex plane.
- A complex function is said to be meromorphic if it is analytic at every point in the complex plane except for a set of isolated singularities.
- Some examples of complex functions are:

  - The exponential function: $$e^z = e^{x + iy} = e^x (\cos y + i \sin y)$$
  - The trigonometric functions: $$\sin z = \frac{e^{iz} - e^{-iz}}{2i}$$ $$\cos z = \frac{e^{iz} + e^{-iz}}{2}$$
  - The logarithmic function: $$\log z = \log |z| + i \arg z$$ where |z| is the modulus of z and arg z is the principal argument of z, such that -pi < arg z <= pi
  - The power function: $$z^a = |z|^a e^{ia \arg z}$$ where a is any complex number
  - The complex polynomials: $$p(z) = a_0 + a_1 z + a_2 z^2 + ... + a_n z^n$$ where a0, a1, ..., an are complex coefficients
  - The rational functions: $$r(z) = \frac{p(z)}{q(z)}$$ where p and q are complex polynomials and q(z) != 0 for all z in the domain of r
- Some properties of complex functions are:

  - The sum, difference, product, and quotient of two complex functions are also complex functions, provided that the quotient is well-defined.
  - The composition of two complex functions is also a complex function, provided that the domain and range of the functions are compatible.
  - The derivative of a complex function is also a complex function, provided that the function is differentiable.
  - The derivative of a complex function satisfies the Cauchy-Riemann equations, which are necessary and sufficient conditions for analyticity. The Cauchy-Riemann equations are:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

$$\frac{\partial u}{\partial y} = - \frac{\partial v}{\partial x}$$

  - The derivative of a complex function satisfies the chain rule, the product rule, and the quotient rule, which are similar to the rules for real functions. The chain rule is:

$$\frac{d}{dz} f(g(z)) = f'(g(z)) g'(z)$$

The product rule is:

$$\frac{d}{dz} (f(z) g(z)) = f'(z) g(z) + f(z) g'(z)$$

The quotient rule is:

$$\frac{d}{dz} \frac{f(z)}{g(z)} = \frac{f'(z) g(z) - f(z) g'(z)}{g(z)^2}$$

  - The derivative of a complex function satisfies the Cauchy integral formula, which relates the value of a function at a point to the values of the function on a closed contour around the point[^3