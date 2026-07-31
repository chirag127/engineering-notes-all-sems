### 3-D Transformation for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

In Computer Graphics, 3-D transformation refers to the process of changing the position, orientation, and size of a 3-dimensional object. It is a fundamental concept in Computer Graphics, and is widely used in creating 3-D models, animations, and simulations. In this unit, we will learn about various types of 3-D transformations and their mathematical representation.

Here are some key points to keep in mind while studying 3-D transformation:

1. **Translation:** Translation is the process of moving an object from one position to another in 3-D space. The translation of an object is performed using a translation matrix that specifies the amount of displacement in each of the three dimensions. The translation matrix can be represented as:

```
[1 0 0 Tx]
[0 1 0 Ty]
[0 0 1 Tz]
[0 0 0 1 ]
```

where `Tx`, `Ty`, and `Tz` are the amounts of displacement in the x, y, and z directions, respectively.

2. **Scaling:** Scaling is the process of changing the size of an object in 3-D space. The scaling of an object is performed using a scaling matrix that specifies the amount of scaling in each of the three dimensions. The scaling matrix can be represented as:

```
[Sx 0  0  0]
[0  Sy 0  0]
[0  0  Sz 0]
[0  0  0  1]
```

where `Sx`, `Sy`, and `Sz` are the scaling factors in the x, y, and z directions, respectively.

3. **Rotation:** Rotation is the process of changing the orientation of an object in 3-D space. The rotation of an object is performed using a rotation matrix that specifies the amount of rotation around a particular axis. There are three types of rotation: Rotation about x-axis, rotation about y-axis, and rotation about z-axis. The rotation matrices for these types of rotation can be represented as:

```
Rotation about x-axis:
[1      0       0       0]
[0   cosθ  -sinθ  0]
[0   sinθ   cosθ  0]
[0      0       0       1]

Rotation about y-axis:
[cosθ  0   sinθ   0]
[0      1       0       0]
[-sinθ  0   cosθ  0]
[0      0       0       1]

Rotation about z-axis:
[cosθ  -sinθ  0   0]
[sinθ  cosθ   0   0]
[0         0       1   0]
[0         0       0   1]
```

where `θ` is the angle of rotation around the particular axis.

4. **Composite Transformation:** Composite transformation is the process of applying multiple transformations to an object in a specific order. The order of applying the transformations is important and can affect the final output. The composite transformation matrix can be obtained by multiplying the individual transformation matrices in the reverse order of their application.

5. **Homogeneous Coordinates:** Homogeneous coordinates are used to represent 3-D points and vectors in a 4-dimensional space. The homogeneous coordinates of a point in 3-D space can be represented as (`x`, `y`, `z`, `1`), and the homogeneous coordinates of a vector in 3-D space can be represented as (`x`, `y`, `z`, `0`). Homogeneous coordinates are useful in performing 3-D transformations using matrix multiplication.

In conclusion, 3-D transformation is a critical concept in Computer Graphics, and its understanding is essential in creating and manipulating 3-D objects. By understanding the mathematical representation of various types of 3-D transformations, we can apply them to create complex 3-D models and animations.