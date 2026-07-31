### Matrix representations and homogenous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling and perspective projection in computer graphics.
- Matrix representations allow us to perform multiple transformations by multiplying the corresponding matrices, and to apply the transformations to vectors by multiplying them by the matrix.
- Homogenous coordinates are a way to represent points and vectors in a higher-dimensional space, such that the original coordinates can be recovered by dividing by the last coordinate.
- Homogenous coordinates have the advantage of being able to represent affine and projective transformations as matrices, and to handle points at infinity without special cases.
- Homogenous coordinates are also useful for clipping and culling operations, as they can be used to test whether a point is inside or outside a viewing volume.
- To convert a point (x, y) in Cartesian coordinates to a point (x', y', w) in homogenous coordinates, we can use the formula:

    ```
    x' = x * w
    y' = y * w
    ```

    where w is any non-zero scalar. Usually, we choose w = 1 for convenience.

- To convert a point (x', y', w) in homogenous coordinates to a point (x, y) in Cartesian coordinates, we can use the formula:

    ```
    x = x' / w
    y = y' / w
    ```

    provided that w is not zero. If w is zero, then the point is at infinity and has no Cartesian equivalent.

- To convert a vector (x, y) in Cartesian coordinates to a vector (x', y', w) in homogenous coordinates, we can use the formula:

    ```
    x' = x
    y' = y
    w = 0
    ```

    This ensures that the vector is invariant under translation, as it should be.

- To convert a vector (x', y', w) in homogenous coordinates to a vector (x, y) in Cartesian coordinates, we can use the formula:

    ```
    x = x'
    y = y'
    ```

    provided that w is zero. If w is not zero, then the vector is not a valid homogenous vector.

- The matrix representation for translation by (tx, ty) in homogenous coordinates is:

    ```
    | 1  0  tx |
    | 0  1  ty |
    | 0  0  1  |
    ```

- The matrix representation for rotation by an angle θ in homogenous coordinates is:

    ```
    | cosθ  -sinθ  0 |
    | sinθ   cosθ  0 |
    | 0      0     1 |
    ```

- The matrix representation for scaling by (sx, sy) in homogenous coordinates is:

    ```
    | sx  0   0 |
    | 0   sy  0 |
    | 0   0   1 |
    ```

- The matrix representation for perspective projection with a focal length f in homogenous coordinates is:

    ```
    | f  0  0  0 |
    | 0  f  0  0 |
    | 0  0  1  0 |
    | 0  0  1  0 |
    ```

    This matrix maps a point (x, y, z) in 3D space to a point (x', y', w) in homogenous coordinates, such that the projected point on the image plane is (x'/w, y'/w).