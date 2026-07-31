# Jacobians

- A Jacobian matrix is a matrix that contains the first-order partial derivatives of a vector-valued function of several variables .
- A Jacobian matrix can be used to convert surface and volume integrals from one coordinate system to another.
- A Jacobian matrix can also be used to linearize a nonlinear function near a given point.
- A Jacobian matrix can be rectangular or square, depending on the number of input and output variables of the function.
- A Jacobian determinant is the determinant of a square Jacobian matrix.
- A Jacobian determinant can be used to measure the local change of volume or area induced by a transformation.
- A Jacobian determinant can also be used to determine whether a transformation is invertible or not.

## Example

- Consider the function `f(x,y) = (x^2 + y^2, x + y)` that maps from `R^2` to `R^2`.
- The Jacobian matrix of `f` is given by:

```
J(x,y) = | 2x  2y |
         | 1   1  |
```

- The Jacobian determinant of `f` is given by:

```
det(J(x,y)) = 2x - 2y
```

- The Jacobian matrix can be used to approximate the function near a point, for example, `(1,1)`. The linearization of `f` at `(1,1)` is given by:

```
f(x,y) ≈ f(1,1) + J(1,1)(x-1,y-1)
       = (2,2) + | 2  2 |(x-1,y-1)
                | 1  1 |
       = (2,2) + (2x + 2y - 4, x + y - 2)
       = (2x - 2, x + y)
```

- The Jacobian determinant can be used to measure the change of area induced by `f`. For example, if we consider a unit square with vertices `(0,0), (1,0), (1,1), (0,1)`, the image of this square under `f` is a parallelogram with vertices `(0,0), (1,1), (2,2), (1,1)`. The area of the parallelogram is given by the absolute value of the Jacobian determinant at any point in the square, for example, `(0.5,0.5)`:

```
Area = |det(J(0.5,0.5))|
     = |2(0.5) - 2(0.5)|
     = |0|
     = 0
```

- The Jacobian determinant can also be used to determine whether `f` is invertible or not. If the Jacobian determinant is nonzero at a point, then `f` is locally invertible at that point. If the Jacobian determinant is zero at a point, then `f` is not locally invertible at that point. For example, `f` is not invertible at `(0,0)` because `det(J(0,0)) = 0`. However, `f` is invertible at `(1,0)` because `det(J(1,0)) = 2`.