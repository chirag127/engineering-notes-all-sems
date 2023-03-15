Hello, I am Sydney, your AI assistant. I can help you with your study material for Computer Graphics. Here are some notes on the topic of composite transformations for the unit 2 - transformations.

### Composite transformations

- A composite transformation is a sequence of two or more transformations applied to a geometric object.
- The result of a composite transformation is equivalent to applying a single transformation that combines the effects of all the individual transformations in the sequence.
- The order of the transformations in the sequence matters, as different orders may produce different results.
- The most common transformations used in computer graphics are translation, rotation, scaling, and reflection.
- Translation moves an object by a given displacement vector.
- Rotation rotates an object by a given angle around a given axis.
- Scaling changes the size of an object by a given scale factor along each axis.
- Reflection flips an object over a given plane or line.
- To perform a composite transformation, we can use a transformation matrix that represents the combined effect of all the individual transformations.
- A transformation matrix is a square matrix that can be multiplied with the coordinates of an object to obtain the transformed coordinates.
- The transformation matrix for a composite transformation is obtained by multiplying the matrices for each individual transformation in the sequence, from right to left.
- For example, if we want to perform a composite transformation that first translates an object by (tx, ty, tz), then rotates it by angle θ around the z-axis, and then scales it by (sx, sy, sz), we can use the following transformation matrix:

```
| sx*cos(θ)  -sy*sin(θ)  0  tx |
| sx*sin(θ)   sy*cos(θ)  0  ty |
|    0           0       sz tz |
|    0           0       0   1 |
```

- To apply this matrix to an object with coordinates (x, y, z, 1), we simply multiply the matrix with the column vector:

```
| sx*cos(θ)  -sy*sin(θ)  0  tx |   | x |
| sx*sin(θ)   sy*cos(θ)  0  ty | x | y |
|    0           0       sz tz |   | z |
|    0           0       0   1 |   | 1 |
```

- The result is a column vector with the transformed coordinates (x', y', z', 1).
- Note that the last coordinate is always 1 for homogeneous coordinates, which are used to represent points in 3D space.
- Composite transformations can be used to model complex motions and transformations of objects in computer graphics, such as animation, camera movement, and projection.