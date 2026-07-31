### Directional derivatives

- A directional derivative is a measure of the rate of change of a function in a given direction at a given point.
- It generalizes the concept of partial derivatives, which are the rates of change of a function in the x, y and z directions.
- The directional derivative of a function f(x,y,z) at a point P in the direction of a unit vector **u** is denoted by ∇<sub>u</sub>f(P) and is defined as:

∇<sub>u</sub>f(P) = lim<sub>h→0</sub> [f(P + h**u**) - f(P)] / h

- Alternatively, the directional derivative can be computed using the gradient of f, which is a vector that points in the direction of the greatest increase of f. The gradient of f is denoted by ∇f and is defined as:

∇f = (∂f/∂x)**i** + (∂f/∂y)**j** + (∂f/∂z)**k**

- The directional derivative can then be expressed as the dot product of the gradient and the unit vector:

∇<sub>u</sub>f(P) = ∇f(P) · **u**

- The directional derivative has the following properties:

  - It is zero if **u** is perpendicular to ∇f(P), meaning that f does not change in that direction.
  - It is positive if **u** has an acute angle with ∇f(P), meaning that f increases in that direction.
  - It is negative if **u** has an obtuse angle with ∇f(P), meaning that f decreases in that direction.
  - It is equal to the magnitude of ∇f(P) if **u** is parallel to ∇f(P), meaning that f changes at the maximum rate in that direction.

- Example: Find the directional derivative of f(x,y) = x<sup>2</sup> + y<sup>2</sup> at the point (1,1) in the direction of **v** = 2**i** - **j**.

  - Solution: First, we need to find the unit vector in the direction of **v**. This is given by:

    **u** = **v** / |**v**| = (2**i** - **j**) / √(2<sup>2</sup> + 1<sup>2</sup>) = (2/√5)**i** - (1/√5)**j**

  - Next, we need to find the gradient of f at the point (1,1). This is given by:

    ∇f(1,1) = (∂f/∂x)**i** + (∂f/∂y)**j** = (2x)**i** + (2y)**j** |<sub>x=1,y=1</sub> = 2**i** + 2**j**

  - Finally, we can find the directional derivative by taking the dot product of the gradient and the unit vector:

    ∇<sub>u</sub>f(1,1) = ∇f(1,1) · **u** = (2**i** + 2**j**) · ((2/√5)**i** - (1/√5)**j**) = (4/√5) - (2/√5) = 2/√5

  - Therefore, the directional derivative of f at the point (1,1) in the direction of **v** is 2/√5.