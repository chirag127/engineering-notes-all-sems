### Basic Transformations for the notes of Unit 2 - Transformations in Computer Graphics

Transformations are an essential aspect of Computer Graphics, as they help us modify and manipulate objects in 2D and 3D space. In this section, we will discuss the basics of transformations and their application in graphics.

1. **Translation**

Translation is the process of moving an object from one position to another. In 2D graphics, it involves moving an object along the X and Y axes. In 3D graphics, we move objects along the X, Y, and Z axes. Translation is performed using the following formula:

```
T(x,y) = [1 0 x]
         [0 1 y]
         [0 0 1]
```

Where `x` and `y` are the distances to be moved along the X and Y axes, respectively.

2. **Scaling**

Scaling is the process of resizing an object. In 2D graphics, it involves increasing or decreasing the size of an object along the X and Y axes. In 3D graphics, we can also scale along the Z axis. Scaling is performed using the following formula:

```
S(x,y) = [x 0 0]
         [0 y 0]
         [0 0 1]
```

Where `x` and `y` are the scaling factors along the X and Y axes, respectively.

3. **Rotation**

Rotation is the process of rotating an object around a given point. In 2D graphics, it involves rotating an object along the Z-axis. In 3D graphics, we can also rotate around the X and Y axes. Rotation is performed using the following formula:

```
R(θ) = [cosθ -sinθ 0]
       [sinθ cosθ  0]
       [0     0     1]
```

Where `θ` is the angle of rotation in radians.

4. **Reflection**

Reflection is the process of flipping an object along a line. In 2D graphics, it involves reflecting an object along the X or Y axis. In 3D graphics, we can also reflect along the XZ, YZ, or XY planes. Reflection is performed using the following formula:

```
Rx = [1  0  0]
     [0 -1  0]
     [0  0  1]

Ry = [-1 0  0]
     [0  1  0]
     [0  0  1]
```

Where `Rx` and `Ry` are the reflection matrices along the X and Y axes, respectively.

By applying these basic transformations, we can create complex graphics and animations. These transformations form the backbone of computer graphics and animation software, and are used extensively in video games, films, and other visual media.