# Cauchy-Riemann Equations (Cartesian and Polar Form)

The Cauchy-Riemann equations are a set of partial differential equations that provide a necessary and sufficient condition for a function to be analytic. These equations are used in the study of complex variable differentiation, which is a topic in the subject of Engineering Mathematics-II.

## Cartesian Form

In the Cartesian coordinate system, the Cauchy-Riemann equations are given by:

```
∂u/∂x = ∂v/∂y
∂u/∂y = -∂v/∂x
```

where `u` and `v` are the real and imaginary parts of a complex function `f(z) = u(x,y) + iv(x,y)` and `x` and `y` are the real and imaginary parts of the complex variable `z = x + iy`.

## Polar Form

In the polar coordinate system, the Cauchy-Riemann equations are given by:

```
∂u/∂r = (1/r) ∂v/∂θ
∂v/∂r = -(1/r) ∂u/∂θ
```

where `u` and `v` are the real and imaginary parts of a complex function `f(z) = u(r,θ) + iv(r,θ)` and `r` and `θ` are the magnitude and argument of the complex variable `z = r(cosθ + isinθ)`.

These equations are useful for determining whether a function is analytic and for finding the derivative of a complex function. They are an important tool in the study of complex variable differentiation.