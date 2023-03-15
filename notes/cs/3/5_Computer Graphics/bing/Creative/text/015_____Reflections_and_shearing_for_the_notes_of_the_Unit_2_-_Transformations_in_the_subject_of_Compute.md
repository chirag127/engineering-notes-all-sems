### Reflections and Shearing

- Reflections and shearing are two types of transformations in computer graphics that change the position, orientation, or shape of an object.
- A reflection is a transformation that flips an object over a line or a plane, creating a mirror image of the original object. The line or plane is called the axis of reflection or the mirror.
- A shearing is a transformation that slants an object in one or more directions, changing its shape but not its area or volume. The amount of slanting is called the shear factor or the shear angle.
- Some properties and examples of reflections and shearing are:

#### Reflections

- A reflection preserves the size, shape, and orientation of the object, but reverses its handedness (left-right or clockwise-counterclockwise).
- A reflection can be performed in 2D or 3D space, depending on the dimension of the axis of reflection. For example, a 2D reflection can be done over a line, while a 3D reflection can be done over a plane.
- A reflection can be represented by a matrix multiplication, where the matrix depends on the axis of reflection. For example, a reflection over the x-axis can be represented by the matrix:

```
[1  0]
[0 -1]
```

- A reflection can be composed with other transformations, such as rotations, translations, or scaling. For example, a reflection over the line y = x can be obtained by rotating the object by 90 degrees clockwise, then reflecting it over the x-axis, then rotating it by 90 degrees counterclockwise.
- A reflection can be used to create symmetrical patterns, such as kaleidoscopes, snowflakes, or logos.

#### Shearing

- A shearing preserves the area or volume of the object, but changes its shape and orientation.
- A shearing can be performed in 2D or 3D space, depending on the direction of the slanting. For example, a 2D shearing can be done along the x-axis or the y-axis, while a 3D shearing can be done along the x-axis, the y-axis, or the z-axis.
- A shearing can be represented by a matrix multiplication, where the matrix depends on the direction and the shear factor of the slanting. For example, a shearing along the x-axis by a factor of k can be represented by the matrix:

```
[1 k]
[0 1]
```

- A shearing can be composed with other transformations, such as rotations, translations, or scaling. For example, a shearing along the x-axis by a factor of k can be obtained by rotating the object by an angle of arctan(k), then scaling it by a factor of 1/sqrt(1 + k^2), then rotating it by an angle of -arctan(k).
- A shearing can be used to create perspective effects, such as foreshortening, distortion, or skewing.