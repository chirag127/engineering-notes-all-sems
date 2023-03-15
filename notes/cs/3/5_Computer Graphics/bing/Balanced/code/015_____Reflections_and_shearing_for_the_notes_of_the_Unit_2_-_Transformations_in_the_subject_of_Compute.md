### Reflections and Shearing

Reflection and shearing are two types of transformations in computer graphics that change the position and shape of an object.

#### Reflection

- Reflection is a kind of rotation where the angle of rotation is 180 degrees.
- The reflected object is always formed on the other side of the mirror, which can be a line or a plane.
- The mirror line or plane is also called the axis of reflection or the plane of reflection.
- The distance of the original object and the reflected object from the mirror is equal.
- The reflection can be done in 2D or 3D space, depending on the dimension of the mirror.
- The reflection matrix is used to calculate the coordinates of the reflected object from the original object.
- The reflection matrix depends on the orientation of the mirror. For example, if the mirror is parallel to the x-axis, the reflection matrix is:

```
R_x = | 1  0 |
      | 0 -1 |
```

- Similarly, if the mirror is parallel to the y-axis, the reflection matrix is:

```
R_y = |-1  0 |
      | 0  1 |
```

- If the mirror is at an arbitrary angle, the reflection matrix is:

```
R = | cos(2θ)  sin(2θ) |
    | sin(2θ) -cos(2θ) |
```

- Where θ is the angle between the mirror and the x-axis.
- The reflection matrix for 3D space is more complex and depends on the equation of the plane of reflection.

#### Shearing

- Shearing is the process of slanting an object in 2D or 3D space either in x, y, or z direction.
- Shearing changes the shape of the object, but not its area or volume.
- The shearing can be done in one direction or two directions. It is an ideal technique to change the shape of an existing object.
- The sliding of layers of the object occurs while doing the shearing. The layers are parallel to the direction of shearing.
- The shearing matrix is used to calculate the coordinates of the sheared object from the original object.
- The shearing matrix depends on the direction and the amount of shearing. For example, if the shearing is done in x direction by a factor of sh_x, the shearing matrix is:

```
S_x = | 1  sh_x |
      | 0    1  |
```

- Similarly, if the shearing is done in y direction by a factor of sh_y, the shearing matrix is:

```
S_y = | 1    0  |
      | sh_y 1 |
```

- If the shearing is done in both x and y directions by factors of sh_x and sh_y, the shearing matrix is:

```
S_xy = | 1  sh_x |
       | sh_y 1  |
```

- The shearing matrix for 3D space is more complex and depends on the direction and the amount of shearing in x, y, and z axes.