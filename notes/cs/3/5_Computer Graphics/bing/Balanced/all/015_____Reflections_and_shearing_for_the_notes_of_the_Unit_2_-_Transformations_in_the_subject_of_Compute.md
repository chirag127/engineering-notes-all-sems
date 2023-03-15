# Reflections and Shearing

Reflections and shearing are two types of transformations in computer graphics that change the position and shape of an object.

## Reflection

Reflection is a transformation that flips an object over a line or a plane, creating a mirror image of the original object. The line or plane is called the mirror line or the mirror plane. The angle of reflection is equal to the angle of incidence, and the distance of the reflected point from the mirror is equal to the distance of the original point from the mirror.

Reflection can be performed in two dimensions or three dimensions. In two dimensions, the mirror line can be horizontal, vertical, or diagonal. In three dimensions, the mirror plane can be xy-plane, yz-plane, xz-plane, or any arbitrary plane.

Reflection can be represented by a matrix multiplication, where the matrix depends on the mirror line or plane. For example, the matrix for reflection over the x-axis in two dimensions is:

```
| 1  0 |
| 0 -1 |
```

The matrix for reflection over the yz-plane in three dimensions is:

```
|-1  0  0 |
| 0  1  0 |
| 0  0  1 |
```

## Shearing

Shearing is a transformation that slants an object in one or two directions, changing the shape of the object. The object is distorted by sliding the layers of the object parallel to a fixed direction. The fixed direction is called the shear direction, and the amount of sliding is called the shear factor.

Shearing can be performed in two dimensions or three dimensions. In two dimensions, the shear direction can be horizontal or vertical, and the shear factor can be positive or negative. In three dimensions, the shear direction can be x, y, or z, and the shear factor can be a pair of values corresponding to the other two axes.

Shearing can also be represented by a matrix multiplication, where the matrix depends on the shear direction and factor. For example, the matrix for shearing in the x-direction with a factor of k in two dimensions is:

```
| 1  k |
| 0  1 |
```

The matrix for shearing in the z-direction with factors of kx and ky in three dimensions is:

```
| 1  0  kx |
| 0  1  ky |
| 0  0  1  |
```