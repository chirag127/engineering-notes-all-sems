### Cauchy-Riemann equations (Cartesian and Polar form)

- The Cauchy-Riemann equations are a system of two partial differential equations that form a necessary and sufficient condition for a complex function to be holomorphic (complex differentiable) .
- If f(z) = u(x, y) + iv(x, y) is a complex function of a single complex variable z = x + iy, where u and v are real-valued functions of two real variables x and y, then the Cauchy-Riemann equations are:

  - (1a) `@u/@x = @v/@y`
  - (1b) `@u/@y = -@v/@x`

- These equations state that the partial derivatives of u and v must be continuous and satisfy the above equalities at every point in the domain of f .
- If f is holomorphic, then it has a complex derivative given by:

  - (2) `f'(z) = @u/@x + i@v/@x = @v/@y - i@u/@y`

- This derivative is independent of the direction of approach to z, as long as the limit exists .
- The Cauchy-Riemann equations can also be written in polar form, using the transformation:

  - (3) `x = r cos(theta), y = r sin(theta), z = re^(i theta)`

- where r and theta are the polar coordinates of z. Then, if f(z) = u(r, theta) + iv(r, theta), the Cauchy-Riemann equations in polar form are:

  - (4a) `@u/@r = (1/r) @v/@theta`
  - (4b) `@v/@r = -(1/r) @u/@theta`

- These equations state that the partial derivatives of u and v with respect to r and theta must be continuous and satisfy the above equalities at every point in the domain of f .
- If f is holomorphic, then it has a complex derivative given by:

  - (5) `f'(z) = e^(-i theta) (@u/@r + i@v/@r) = (1/r) e^(-i theta) (@v/@theta - i@u/@theta)`

- This derivative is independent of the direction of approach to z, as long as the limit exists .
- The Cauchy-Riemann equations are useful for checking if a complex function is holomorphic, and for computing its complex derivative. They also imply some important properties of holomorphic functions, such as the harmonic nature of u and v, and the conformal mapping of f .

: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations
: https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/02%3A_Analytic_Functions/2.06%3A_Cauchy-Riemann_Equations
: https://sites.math.washington.edu/~hart/m427/Lecture10.pdf