### Functions of complex variable

- A complex function is a function that maps complex numbers to complex numbers.
- A complex function can be written as w(z) = u(x, y) + iv(x, y), where z = x + iy is the complex variable, w = u + iv is the complex value, and u and v are real functions of x and y.
- A complex function is said to be differentiable at a point z0 if the limit

$$\lim_{z \to z_0} \frac{w(z) - w(z_0)}{z - z_0}$$

exists and is finite. This limit is called the derivative of w(z) at z0 and is denoted by w'(z0).
- A complex function is said to be analytic or holomorphic at a point z0 if it is differentiable at z0 and at every point in some neighborhood of z0.
- A complex function is said to be entire if it is analytic at every point in the complex plane.
- A complex function is said to be harmonic if its real and imaginary parts satisfy Laplace's equation, i.e.,

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

and

$$\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$$

- A complex function that is analytic in a domain D satisfies the Cauchy-Riemann equations, i.e.,

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

and

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

- The Cauchy-Riemann equations are necessary but not sufficient conditions for a complex function to be analytic. A sufficient condition is that the partial derivatives of u and v are continuous and satisfy the Cauchy-Riemann equations.
- A complex function that is analytic in a domain D has a power series expansion at any point z0 in D, i.e.,

$$w(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$

where the coefficients an are given by

$$a_n = \frac{w^{(n)}(z_0)}{n!}$$

- A complex function that is analytic in a domain D has an antiderivative or primitive in D, i.e., there exists a function F(z) such that F'(z) = w(z) for all z in D.