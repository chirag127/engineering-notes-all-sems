### Directional derivatives

- A directional derivative is a measure of how a multivariable function changes in a given direction at a given point.
- It is a generalization of the concept of partial derivatives, which measure the change of a function along the coordinate axes.
- The formula for the directional derivative of a function f(x,y) along a unit vector u = (a,b) is:

  D_u f(x,y) = lim_{h -> 0} (f(x + ah, y + bh) - f(x,y))/h

- Alternatively, the directional derivative can be expressed using the gradient vector of f, denoted by ∇f, which is a vector that points in the direction of the greatest increase of f. The formula is:

  D_u f(x,y) = ∇f(x,y) ⋅ u

- The directional derivative has the following properties:

  - It is a linear function of the direction vector u, meaning that D_(cu) f = c D_u f for any scalar c, and D_(u+v) f = D_u f + D_v f for any vectors u and v.
  - It is zero when u is perpendicular to ∇f, meaning that the function does not change in that direction.
  - It is equal to the magnitude of ∇f when u is parallel to ∇f, meaning that the function changes the most in that direction.