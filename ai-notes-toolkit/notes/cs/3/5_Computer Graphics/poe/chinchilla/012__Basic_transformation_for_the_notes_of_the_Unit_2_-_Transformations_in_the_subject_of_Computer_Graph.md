### Basic Transformations for the Notes of Unit 2 - Transformations in the Subject of Computer Graphics

In computer graphics, transformations are used to manipulate the position, orientation, and size of objects in a scene. Basic transformations include translation, rotation, scaling, and reflection, which are essential for creating and manipulating 2D and 3D graphics.

#### Translation
Translation is used to move an object from one position to another in a scene. It involves adding a constant value to the object's coordinates in either the X, Y, or Z axis. The formula for translation is as follows:

```
[x' y' z' 1] = [x y z 1] [1 0 0 tx]
                            [0 1 0 ty]
                            [0 0 1 tz]
```

Where (x, y, z) are the coordinates of the original point, (x', y', z') are the coordinates of the translated point, and (tx, ty, tz) are the translation factors in the X, Y, and Z axis, respectively.

#### Rotation
Rotation is used to change the orientation of an object in a scene. It involves rotating the object around an axis by a given angle. The formula for rotation is as follows:

```
[x' y' z' 1] = [x y z 1] R(theta)
```

Where (x, y, z) are the coordinates of the original point, (x', y', z') are the coordinates of the rotated point, and R(theta) is the rotation matrix that rotates the object by an angle of theta around a given axis.

#### Scaling
Scaling is used to change the size of an object in a scene. It involves multiplying the object's coordinates by a scaling factor in either the X, Y, or Z axis. The formula for scaling is as follows:

```
[x' y' z' 1] = [x y z 1] [sx 0 0 0]
                            [0 sy 0 0]
                            [0 0 sz 0]
                            [0 0 0 1]
```

Where (x, y, z) are the coordinates of the original point, (x', y', z') are the coordinates of the scaled point, and (sx, sy, sz) are the scaling factors in the X, Y, and Z axis, respectively.

#### Reflection
Reflection is used to mirror an object in a scene. It involves reflecting the object across a plane defined by an axis. The formula for reflection is as follows:

```
[x' y' z' 1] = [x y z 1] [1 0 0 0]
                            [0 1 0 0]
                            [0 0 -1 0]
                            [0 0 0 1]
```

Where (x, y, z) are the coordinates of the original point, (x', y', z') are the coordinates of the reflected point, and the reflection matrix reflects the object across the Z axis.

In conclusion, understanding basic transformations is crucial for creating and manipulating computer graphics. These transformations are the building blocks for more complex operations such as animation and rendering. Mastery of these transformations is an important skill for any aspiring computer graphics artist or programmer.