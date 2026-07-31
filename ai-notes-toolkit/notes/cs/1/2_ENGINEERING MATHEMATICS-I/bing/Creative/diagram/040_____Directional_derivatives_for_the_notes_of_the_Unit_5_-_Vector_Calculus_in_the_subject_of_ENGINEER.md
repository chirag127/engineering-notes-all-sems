### Directional derivatives

- A directional derivative is a measure of the rate of change of a function in a given direction at a given point.
- It generalizes the concept of partial derivatives, which are the rates of change of a function in the x, y and z directions.
- The directional derivative of a function f(x,y,z) at a point P in the direction of a unit vector **u** is denoted by ∇f(**u**) and is given by the formula:

∇f(**u**) = lim<sub>h→0</sub> [f(P + h**u**) - f(P)]/h

- Alternatively, the directional derivative can be expressed using the gradient of f, which is a vector that points in the direction of the greatest increase of f and has a magnitude equal to the rate of change in that direction. The gradient of f is denoted by ∇f and is given by the formula:

∇f = (∂f/∂x)**i** + (∂f/∂y)**j** + (∂f/∂z)**k**

- The directional derivative can then be computed by taking the dot product of the gradient and the unit vector:

∇f(**u**) = ∇f · **u**

- The directional derivative has the following properties:

  - It is zero if **u** is perpendicular to ∇f, meaning that f does not change in that direction.
  - It is positive if **u** has an acute angle with ∇f, meaning that f increases in that direction.
  - It is negative if **u** has an obtuse angle with ∇f, meaning that f decreases in that direction.
  - It is equal to the magnitude of ∇f if **u** is parallel to ∇f, meaning that f changes at the maximum rate in that direction.

- Example: Find the directional derivative of the function f(x,y) = x<sup>2</sup> + y<sup>2</sup> at the point (1,1) in the direction of the vector **v** = 2**i** - **j**.

  - Solution: First, we need to find the unit vector in the direction of **v** by dividing **v** by its magnitude:

    **u** = **v**/|**v**| = (2**i** - **j**)/√5

  - Next, we need to find the gradient of f at the point (1,1) by taking the partial derivatives and plugging in the values of x and y:

    ∇f = (∂f/∂x)**i** + (∂f/∂y)**j** = (2x**i** + 2y**j**)

    ∇f(1,1) = (2**i** + 2**j**)

  - Finally, we need to take the dot product of the gradient and the unit vector to get the directional derivative:

    ∇f(**u**) = ∇f(1,1) · **u** = (2**i** + 2**j**) · (2**i** - **j**)/√5

    ∇f(**u**) = (4 - 2)/√5 = 2/√5

  - Therefore, the directional derivative of f at (1,1) in the direction of **v** is 2/√5.