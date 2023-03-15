### Functions of complex variable

- A complex function is a function that maps complex numbers to complex numbers.
- A complex function can be written as w(z) = u(x, y) + iv(x, y), where z = x + iy is the complex variable, w = u + iv is the complex value, and u and v are real functions of x and y.
- A complex function is said to be differentiable at a point z0 if the limit

`lim_(z->z0) (w(z) - w(z0))/(z - z0)`

exists and is independent of the direction of approach of z to z0.
- The limit, if it exists, is called the derivative of w(z) at z0 and is denoted by w'(z0) or dw/dz.
- A complex function is said to be analytic or holomorphic at a point z0 if it is differentiable at z0 and at every point in some neighborhood of z0.
- A complex function is said to be entire if it is analytic at every point in the complex plane.
- A complex function is said to be harmonic if it satisfies Laplace's equation, that is,

`del^2 u = (d^2 u)/(dx^2) + (d^2 u)/(dy^2) = 0`

and

`del^2 v = (d^2 v)/(dx^2) + (d^2 v)/(dy^2) = 0`

where u and v are the real and imaginary parts of the complex function.
- A complex function that is analytic in a domain D satisfies the Cauchy-Riemann equations, that is,

`(du)/(dx) = (dv)/(dy)`

and

`(du)/(dy) = -(dv)/(dx)`

where u and v are the real and imaginary parts of the complex function.
- A complex function that is analytic in a domain D also satisfies the following properties:

  - It has a continuous derivative of any order in D.
  - It has an antiderivative or primitive function in D, that is, a function F(z) such that F'(z) = w(z) for all z in D.
  - It has a Taylor series expansion around any point z0 in D, that is, w(z) = sum_(n=0)^infty a_n (z - z0)^n, where a_n = w^(n)(z0)/n! and w^(n)(z0) is the nth derivative of w(z) at z0.
  - It has a Laurent series expansion around any isolated singularity z0 in D, that is, w(z) = sum_(n=-infty)^infty a_n (z - z0)^n, where a_n = (1/(2pi i)) int_C (w(z))/(z - z0)^(n+1) dz and C is a simple closed contour around z0 in D.
  - It satisfies the Cauchy integral formula, that is, w(z0) = (1/(2pi i)) int_C (w(z))/(z - z0) dz, where C is a simple closed contour around z0 in D and z0 is any point inside C.
  - It satisfies the Cauchy integral theorem, that is, int_C w(z) dz = 0, where C is a simple closed contour in D and w(z) is analytic in D and on C.
  - It satisfies the maximum modulus principle, that is, if w(z) is analytic and non-constant in a domain D, then |w(z)| cannot attain a maximum value in D.