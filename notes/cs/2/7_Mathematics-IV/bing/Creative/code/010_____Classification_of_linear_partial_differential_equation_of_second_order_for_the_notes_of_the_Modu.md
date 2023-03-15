Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information that I found from the web:

### Classification of linear partial differential equation of second order

- A linear partial differential equation of second order is an equation of the form:

`L[u] = a(x,y)u_xx + 2b(x,y)u_xy + c(x,y)u_yy + d(x,y)u_x + e(x,y)u_y + f(x,y)u = g(x,y)`

where `u` is the unknown function of `x` and `y`, and `a`, `b`, `c`, `d`, `e`, `f`, and `g` are given functions of `x` and `y`.

- The classification of such equations depends on the sign of the discriminant `D(x,y) = b(x,y)^2 - a(x,y)c(x,y)`. The discriminant determines the nature of the characteristic curves of the equation, which are the curves along which the equation reduces to an ordinary differential equation.

- The classification is as follows:

  - If `D(x,y) > 0` for all `(x,y)`, the equation is **hyperbolic**. The characteristic curves are real and distinct. An example of a hyperbolic equation is the wave equation:

  `u_tt - c^2u_xx = 0`

  - If `D(x,y) = 0` for all `(x,y)`, the equation is **parabolic**. The characteristic curves are real and coincident. An example of a parabolic equation is the heat equation:

  `u_t - k u_xx = 0`

  - If `D(x,y) < 0` for all `(x,y)`, the equation is **elliptic**. The characteristic curves are complex and conjugate. An example of an elliptic equation is the Laplace equation:

  `u_xx + u_yy = 0`

- The classification may vary depending on the point `(x,y)`. For example, the Tricomi equation:

`u_xx + x u_yy = 0`

is elliptic when `x < 0`, parabolic when `x = 0`, and hyperbolic when `x > 0`.

- The classification can be changed by applying a suitable change of variables that transforms the equation into a canonical form. The canonical forms are:

  - For hyperbolic equations:

  `L[u] = u_xy`

  - For parabolic equations:

  `L[u] = u_yy`

  - For elliptic equations:

  `L[u] = u_xx + u_yy`

- The change of variables can be found by solving the characteristic equation:

`a(x,y) dy^2 - 2b(x,y) dx dy + c(x,y) dx^2 = 0`

which gives the slopes of the characteristic curves at each point `(x,y)`. The new variables are chosen to be along and across the characteristic curves.

- The classification and the canonical forms are useful for finding the general solution of the equation, or the solution that satisfies certain boundary or initial conditions. Different methods can be applied depending on the type of the equation, such as separation of variables, Fourier series, integral transforms, Green's functions, etc.