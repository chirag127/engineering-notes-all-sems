Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on 3-D Transformation for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics. Here is the content in markdown format:

# 3-D Transformation

## Introduction

- A 3-D transformation is a process of changing the position, orientation, size, or shape of a 3-D object in a 3-D space.
- A 3-D transformation can be represented by a 4x4 matrix that operates on a 3-D point or vector in homogeneous coordinates.
- A 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve parallelism, ratios of distances, and angles between lines, but not lengths or areas. Examples of affine transformations are translation, rotation, scaling, and shear.
- Non-affine transformations do not preserve any of the properties of affine transformations. Examples of non-affine transformations are perspective and curved transformations.

## Translation

- Translation is a 3-D transformation that moves a 3-D object by a given displacement vector.
- Translation can be represented by the following matrix:

```
| 1  0  0  tx |
| 0  1  0  ty |
| 0  0  1  tz |
| 0  0  0  1  |
```

- Where tx, ty, and tz are the components of the displacement vector along the x, y, and z axes, respectively.
- To translate a 3-D point (x, y, z, 1) by the displacement vector (tx, ty, tz), we multiply the point by the translation matrix:

```
| 1  0  0  tx |   | x |   | x + tx |
| 0  1  0  ty | * | y | = | y + ty |
| 0  0  1  tz |   | z |   | z + tz |
| 0  0  0  1  |   | 1 |   |   1    |
```

- Translation is a commutative operation, meaning that the order of applying multiple translations does not matter.

## Rotation

- Rotation is a 3-D transformation that rotates a 3-D object around a given axis by a given angle.
- Rotation can be represented by the following matrix:

```
| r11 r12 r13 0 |
| r21 r22 r23 0 |
| r31 r32 r33 0 |
| 0   0   0   1 |
```

- Where r11, r12, r13, r21, r22, r23, r31, r32, and r33 are the elements of the rotation matrix, which depend on the axis and angle of rotation.
- To rotate a 3-D point (x, y, z, 1) around an axis by an angle, we multiply the point by the rotation matrix:

```
| r11 r12 r13 0 |   | x |   | r11*x + r12*y + r13*z |
| r21 r22 r23 0 | * | y | = | r21*x + r22*y + r23*z |
| r31 r32 r33 0 |   | z |   | r31*x + r32*y + r33*z |
| 0   0   0   1 |   | 1 |   |          1            |
```

- Rotation is not a commutative operation, meaning that the order of applying multiple rotations matters.
- There are three common axes of rotation in 3-D space: x-axis, y-axis, and z-axis. The rotation matrices for each axis are:

```
Rotation around x-axis by angle θ:

| 1   0    0   0 |
| 0  cosθ -sinθ 0 |
| 0  sinθ  cosθ 0 |
| 0   0    0   1 |

Rotation around y-axis by angle θ:

|  cosθ 0  sinθ 0 |
|   0   1   0   0 |
| -sinθ 0  cosθ 0 |
|   0   0   0   1 |

Rotation around z-axis by angle θ:

| cosθ -sinθ 0 0 |
| sinθ  cosθ 0 0 |
|  0

```
