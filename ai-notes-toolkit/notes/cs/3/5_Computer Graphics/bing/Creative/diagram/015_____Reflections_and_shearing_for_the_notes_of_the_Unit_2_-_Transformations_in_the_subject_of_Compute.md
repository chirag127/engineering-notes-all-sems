### Reflections and Shearing

Reflections and shearing are two types of transformations in computer graphics that change the position and shape of an object.

#### Reflection

- Reflection is a kind of rotation where the angle of rotation is 180 degrees.
- The reflected object is always formed on the other side of the mirror, which can be a line, a plane, or an axis.
- The mirror is also called the reflection line, reflection plane, or reflection axis, depending on the dimension of the object and the mirror.
- The reflection of an object can be obtained by multiplying its coordinates by a reflection matrix, which depends on the orientation and position of the mirror.
- For example, the reflection matrix for a 2D object about the x-axis is:

```
[1  0]
[0 -1]
```

- And the reflection matrix for a 3D object about the xy-plane is:

```
[1  0  0]
[0  1  0]
[0  0 -1]
```

- Reflection preserves the size and shape of the object, but reverses its orientation.

#### Shearing

- Shearing is the process of slanting an object in 2D or 3D space either in x, y, or z direction.
- Shearing changes the shape of the object, but not its size or area.
- The shearing of an object can be obtained by adding a constant factor to its coordinates, which depends on the direction and amount of shearing.
- For example, the shearing matrix for a 2D object in the x-direction by a factor of k is:

```
[1 k]
[0 1]
```

- And the shearing matrix for a 3D object in the z-direction by a factor of k is:

```
[1 0 k]
[0 1 k]
[0 0 1]
```

- Shearing can be done in one direction or two directions, depending on the application and the desired effect.