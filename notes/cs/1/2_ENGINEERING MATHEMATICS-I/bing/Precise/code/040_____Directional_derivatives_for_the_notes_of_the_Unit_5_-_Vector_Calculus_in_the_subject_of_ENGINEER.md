### Directional Derivatives

- Directional derivatives are a way to measure the rate of change of a multivariable function in a specific direction.
- The directional derivative of a function `f(x,y)` at a point `(x0,y0)` in the direction of a unit vector `u=<a,b>` is given by the dot product of the gradient of `f` at `(x0,y0)` and the unit vector `u`.
- The formula for the directional derivative is `Duf(x0,y0) = f_x(x0,y0)a + f_y(x0,y0)b`, where `f_x` and `f_y` are the partial derivatives of `f` with respect to `x` and `y`, respectively.
- The directional derivative can also be calculated using the chain rule. If `r(t) = <x0 + at, y0 + bt>` is a parametric equation for a line in the direction of `u`, then `Duf(x0,y0) = (d/dt)(f(r(t)))|_(t=0)`.
- The directional derivative is positive if the function is increasing in the direction of `u`, negative if the function is decreasing in the direction of `u`, and zero if the function is constant in the direction of `u`.
- The gradient vector of a function `f(x,y)` at a point `(x0,y0)` points in the direction of the greatest increase of the function at that point, and its magnitude is equal to the rate of increase in that direction.
- The directional derivative can be used to find the equation of the tangent plane to a surface `z=f(x,y)` at a point `(x0,y0,z0)`. The equation of the tangent plane is `z-z0 = f_x(x0,y0)(x-x0) + f_y(x0,y0)(y-y0)`.