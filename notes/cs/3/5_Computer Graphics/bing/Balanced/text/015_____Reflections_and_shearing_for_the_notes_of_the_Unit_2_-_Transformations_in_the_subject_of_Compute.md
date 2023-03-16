### Reflections and Shearing

- Reflections and shearing are two types of transformations in computer graphics that change the position and shape of an object respectively.
- A transformation is a process of mapping the coordinates of an object from one coordinate system to another.
- Reflection is a transformation that produces a mirror image of an object with respect to a plane, called the mirror plane or the reflection plane.
- Shearing is a transformation that slants the shape of an object by displacing its points along a fixed direction, called the shearing direction.

#### Reflection

- Reflection can be seen as a special case of rotation, where the angle of rotation is 180 degrees.
- The reflection of an object can be obtained by multiplying its coordinates by a reflection matrix, which depends on the orientation of the mirror plane.
- For example, if the mirror plane is parallel to the x-axis, the reflection matrix is:

```
R_x = | 1  0 |
      | 0 -1 |
```

- This matrix negates the y-coordinate of every point, while keeping the x-coordinate unchanged.
- Similarly, if the mirror plane is parallel to the y-axis, the reflection matrix is:

```
R_y = |-1  0 |
      | 0  1 |
```

- This matrix negates the x-coordinate of every point, while keeping the y-coordinate unchanged.
- If the mirror plane is parallel to the origin, the reflection matrix is:

```
R_o = |-1  0 |
      | 0 -1 |
```

- This matrix negates both the x-coordinate and the y-coordinate of every point, producing the inverse image of the object.
- In general, the reflection matrix for any mirror plane can be derived using the normal vector of the plane and some trigonometric formulas.
- The following figure shows some examples of reflection in 2D:

![Reflection in 2D](https://www.includehelp.com/computer-graphics/images/reflection.jpg)

#### Shearing

- Shearing is a transformation that changes the shape of an object by sliding its layers along a fixed direction, without changing its area or volume.
- Shearing can be done in one direction or two directions, depending on the number of shearing factors involved.
- A shearing factor is a constant that determines the amount of displacement of a point along the shearing direction.
- The shearing of an object can be obtained by multiplying its coordinates by a shearing matrix, which depends on the shearing factors and the shearing direction.
- For example, if the shearing is done along the x-axis, the shearing matrix is:

```
S_x = | 1  sh_x |
      | 0    1  |
```

- This matrix adds the product of the y-coordinate and the shearing factor sh_x to the x-coordinate of every point, while keeping the y-coordinate unchanged.
- Similarly, if the shearing is done along the y-axis, the shearing matrix is:

```
S_y = | 1    0  |
      | sh_y 1 |
```

- This matrix adds the product of the x-coordinate and the shearing factor sh_y to the y-coordinate of every point, while keeping the x-coordinate unchanged.
- If the shearing is done along both the x-axis and the y-axis, the shearing matrix is:

```
S_xy = | 1  sh_x |
       | sh_y 1  |
```

- This matrix adds the product of the y-coordinate and the shearing factor sh_x to the x-coordinate, and the product of the x-coordinate and the shearing factor sh_y to the y-coordinate of every point.
- In general, the shearing matrix for any shearing direction can be derived using the angle of the direction and some trigonometric formulas.
- The following figure shows some examples of shearing in 2D:

![Shearing in 2D](https://www.includehelp.com/computer-graphics/images/shearing.jpg)