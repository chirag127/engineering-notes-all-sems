# Unit 4 - Complex Variable–Differentiation

- Complex differentiation is the study of how complex functions change with respect to complex variables.
- A complex function is a function that maps complex numbers to complex numbers, such as f(z) = z^2 + 2z + 1, where z is a complex variable.
- A complex variable is a variable that can take on complex values, such as z = x + iy, where x and y are real variables and i is the imaginary unit.
- A complex function can be written in terms of its real and imaginary parts, such as f(z) = u(x,y) + iv(x,y), where u and v are real functions of two real variables.
- A complex function is said to be differentiable at a point z if the limit

  `f'(z) = lim_(h->0) (f(z+h) - f(z))/h`

  exists and is independent of the direction of h, where h is a complex number.
- A complex function is said to be analytic or holomorphic at a point z if it is differentiable at z and at every point in some neighborhood of z.
- A complex function is said to be entire if it is analytic at every point in the complex plane.
- A complex function is said to be meromorphic if it is analytic except at isolated points, called poles, where it has a certain type of singularity.
- A key result in complex differentiation is the Cauchy-Riemann equations, which state that a complex function f(z) = u(x,y) + iv(x,y) is differentiable at a point z = x + iy if and only if

  `u_x = v_y` and `u_y = -v_x`

  where the subscripts denote partial derivatives.
- The Cauchy-Riemann equations link the real and imaginary parts of a complex function and show that complex differentiation is more restrictive than real differentiation.
- Another important result in complex differentiation is the Cauchy integral formula, which states that if f is a holomorphic function inside and on a simple closed contour C, and z is any point inside C, then

  `f(z) = (1/(2pi i)) int_C (f(w)/(w-z)) dw`

  where i is the imaginary unit and dw is the differential along C.
- The Cauchy integral formula allows us to compute the value of a holomorphic function at any point inside a contour by using the values of the function on the contour and the complex variable w.
- The Cauchy integral formula also implies that a holomorphic function is infinitely differentiable and equal to its own Taylor series, which is a power series expansion of the form

  `f(z) = sum_(n=0)^infty a_n (z-z_0)^n`

  where z_0 is a fixed point and a_n are the coefficients given by

  `a_n = (f^(n)(z_0))/(n!)`

  where f^(n) denotes the nth derivative of f.
- Complex differentiation is the basis of complex analysis, which is the study of the properties and applications of complex functions. Complex analysis has many applications in mathematics, physics, engineering, and other fields.