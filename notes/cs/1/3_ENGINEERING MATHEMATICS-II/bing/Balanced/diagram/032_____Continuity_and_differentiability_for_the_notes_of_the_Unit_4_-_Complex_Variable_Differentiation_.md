### Continuity and Differentiability of Complex Functions

- A complex function is a function that maps complex numbers to complex numbers, such as f(z) = z^2 + 1.
- A complex function is continuous at a point z_0 if the limit of the function as z approaches z_0 is equal to the value of the function at z_0, i.e., lim_(z->z_0) f(z) = f(z_0) .
- A complex function is differentiable at a point z_0 if the limit of the difference quotient as h approaches zero exists and is finite, i.e., lim_(h->0) (f(z_0 + h) - f(z_0))/h = f'(z_0) .
- The derivative of a complex function is also a complex function that gives the rate of change of the function at each point in its domain.
- A complex function is analytic at a point z_0 if it is differentiable at z_0 and in some neighborhood of z_0. A complex function that is analytic in the whole complex plane is called entire .
- Some examples of complex functions and their derivatives are:

  - f(z) = z^n, where n is any integer, f'(z) = n z^(n-1) .
  - f(z) = e^z, f'(z) = e^z .
  - f(z) = sin(z), f'(z) = cos(z) .
  - f(z) = log(z), f'(z) = 1/z .

- Some properties of complex derivatives are:

  - The sum rule: (f + g)'(z) = f'(z) + g'(z) .
  - The product rule: (f g)'(z) = f'(z) g(z) + f(z) g'(z) .
  - The quotient rule: (f/g)'(z) = (f'(z) g(z) - f(z) g'(z))/g(z)^2 .
  - The chain rule: (f o g)'(z) = f'(g(z)) g'(z) .

- Some theorems related to continuity and differentiability of complex functions are:

  - The Cauchy-Riemann equations: If f(z) = u(x, y) + i v(x, y), where u and v are real functions of x and y, then f(z) is differentiable at z = x + i y if and only if u_x = v_y and u_y = -v_x, where the subscripts denote partial derivatives .
  - The Cauchy integral formula: If f(z) is analytic in a simply connected domain D and C is a simple closed contour in D, then for any z_0 inside C, f(z_0) = (1/2 pi i) ∮_(C) f(z)/(z - z_0) dz, where the integral is taken in the positive (counterclockwise) sense .
  - The Liouville's theorem: If f(z) is entire and bounded, then f(z) is constant .