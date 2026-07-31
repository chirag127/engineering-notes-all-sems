### Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A transformation is a process of changing the position, size, shape, or orientation of an object in a coordinate system.
- A composite transformation is a combination of two or more transformations into a single one that is equivalent to applying them one after another.
- A composite transformation can be represented by a matrix that is obtained by multiplying the matrices of the individual transformations in the order of their application.
- The order of the transformations matters, as some transformations are not commutative, meaning that changing the order will change the result.
- For example, rotation and translation are not commutative, as rotating an object and then translating it will produce a different result than translating it and then rotating it.
- However, some transformations are commutative, such as scaling and reflection, meaning that changing the order will not change the result.
- For example, scaling an object and then reflecting it will produce the same result as reflecting it and then scaling it.
- The most common types of transformations in computer graphics are translation, scaling, rotation, and shear.
- Translation is the process of moving an object by a given distance along a given direction.
- Scaling is the process of changing the size of an object by a given factor along a given axis.
- Rotation is the process of rotating an object by a given angle around a given point or axis.
- Shear is the process of distorting an object by a given factor along a given direction.
- Each type of transformation has a corresponding matrix that can be used to perform the transformation on the coordinates of an object.
- For example, the matrix for translation by (tx, ty) is:

```
| 1  0  tx |
| 0  1  ty |
| 0  0  1  |
```

- The matrix for scaling by (sx, sy) is:

```
| sx  0  0 |
| 0  sy  0 |
| 0  0  1  |
```

- The matrix for rotation by θ degrees around the origin is:

```
| cosθ  -sinθ  0 |
| sinθ  cosθ   0 |
| 0     0      1 |
```

- The matrix for shear by (shx, shy) is:

```
| 1  shx  0 |
| shy  1  0 |
| 0   0  1  |
```

- To perform a composite transformation on an object, we multiply the matrices of the individual transformations in the order of their application, and then multiply the resulting matrix with the coordinates of the object.
- For example, to perform a translation by (tx, ty) followed by a rotation by θ degrees around the origin, we multiply the matrices as follows:

```
| 1  0  tx |   | cosθ  -sinθ  0 |   | cosθ  -sinθ  tx |
| 0  1  ty | x | sinθ  cosθ   0 | = | sinθ  cosθ   ty |
| 0  0  1  |   | 0     0      1 |   | 0     0      1  |
```

- Then, we multiply the resulting matrix with the coordinates of the object, such as (x, y, 1), to obtain the transformed coordinates, such as (x', y', 1).
- For example, if x = 2, y = 3, tx = 4, ty = 5, and θ = 90 degrees, then the transformed coordinates are:

```
| cosθ  -sinθ  tx |   | x |   | -3 + 4 |   | 1 |
| sinθ  cosθ   ty | x | y | = |  2 + 5 | = | 7 |
| 0     0      1  |   | 1 |   |    1   |   | 1 |
```

- Therefore, the point (2, 3) is translated by (4, 5) and then rotated by 90 degrees around the origin, resulting in the point (1, 7).