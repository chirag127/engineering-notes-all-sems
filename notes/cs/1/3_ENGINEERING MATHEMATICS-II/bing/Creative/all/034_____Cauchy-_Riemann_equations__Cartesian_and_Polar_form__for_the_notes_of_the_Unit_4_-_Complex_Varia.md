# Cauchy-Riemann equations (Cartesian and Polar form)

- The Cauchy-Riemann equations are a system of two partial differential equations that form a necessary and sufficient condition for a complex function to be holomorphic (complex differentiable) .
- A complex function f(z) = u(x,y) + iv(x,y) is holomorphic at a point z = x + iy if and only if the partial derivatives of u and v satisfy the following equations   :

  - Cartesian form:

    - (1a) `@u/@x = @v/@y`
    - (1b) `@u/@y = -@v/@x`

  - Polar form:

    - (2a) `@u/@r = (1/r) @v/@theta`
    - (2b) `@v/@r = -(1/r) @u/@theta`

- The Cartesian form can be derived by applying the limit definition of the complex derivative to f(z) and equating the real and imaginary parts .
- The polar form can be derived by applying the chain rule to the Cartesian form and using the relations `x = r cos(theta)` and `y = r sin(theta)` .
- The Cauchy-Riemann equations can be used to check if a complex function is analytic and to compute its derivative .
- The Cauchy-Riemann equations also imply some important properties of holomorphic functions, such as the harmonic nature of u and v, the Cauchy integral formula, and the maximum modulus principle .