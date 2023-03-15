### Cauchy-Riemann equations (Cartesian and Polar form)

- The Cauchy-Riemann equations are a system of two partial differential equations that form a necessary and sufficient condition for a complex function to be holomorphic (complex differentiable) .
- If f(z) = u(x, y) + iv(x, y) is a complex function, where u and v are real functions of x and y, then the Cauchy-Riemann equations in Cartesian form are:

    (1a) `u_x = v_y`

    (1b) `u_y = -v_x`

    where `u_x` and `u_y` denote the partial derivatives of u with respect to x and y, and similarly for v  .

- The Cauchy-Riemann equations can also be written in polar form, if we use the polar coordinates `z = r(cos θ + i sin θ)`, where `r = sqrt(x^2 + y^2)` and `θ = tan^-1(y/x)`. Then the Cauchy-Riemann equations in polar form are:

    (2a) `r u_r = v_θ`

    (2b) `r v_r = -u_θ`

    where `u_r` and `u_θ` denote the partial derivatives of u with respect to r and θ, and similarly for v  .

- The Cauchy-Riemann equations can be used to check if a complex function is analytic (holomorphic) and to compute its complex derivative. If f(z) satisfies the Cauchy-Riemann equations and u and v are continuous and differentiable, then f(z) is analytic and its derivative is given by:

    (3) `f'(z) = u_x + i v_x = v_y - i u_y`

    in Cartesian form, or

    (4) `f'(z) = u_r + i v_r = (1/r) v_θ - i (1/r) u_θ`

    in polar form  .