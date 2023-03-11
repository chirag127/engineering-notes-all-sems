### Basic Transformation for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

In Computer Graphics, transformation refers to the process of changing the position, orientation, or size of an object. The transformation can be applied to both 2D and 3D objects, and there are various basic transformations that can be performed to achieve this goal. The following are some of the basic transformations that are commonly used in Computer Graphics:

1. Translation: It is a process of moving an object from one position to another. In translation, the object is moved along the x, y, or z-axis by a certain distance. The translation matrix can be represented as:

```
[1 0 0 dx]
[0 1 0 dy]
[0 0 1 dz]
[0 0 0 1 ]
```

2. Rotation: It is a process of rotating an object by a certain angle around an axis. The axis of rotation can be the x, y, or z-axis. The rotation matrix can be represented as:

```
[cosθ    -sinθ   0   0]
[sinθ    cosθ    0   0]
[0       0       1   0]
[0       0       0   1]
```

3. Scaling: It is a process of changing the size of an object. The scaling matrix can be represented as:

```
[sx  0   0   0]
[0   sy  0   0]
[0   0   sz  0]
[0   0   0   1]
```

4. Shearing: It is a process of distorting the shape of an object. The shearing matrix can be represented as:

```
[1   shx 0   0]
[shy 1   0   0]
[0   0   1   0]
[0   0   0   1]
```

All these basic transformations can be performed using matrix multiplication. The order of the multiplication of the matrices is important as it affects the final result. The order of the matrices is as follows:

```
final_matrix = T * R * S * H * P
```

where T, R, S, H, and P represent translation, rotation, scaling, shearing, and projection matrices, respectively.

Advantages of Basic Transformations:
- Basic transformations are easy to perform and understand.
- They can be used to create complex transformations by combining them.
- They are helpful in creating animations and special effects in Computer Graphics.

Disadvantages of Basic Transformations:
- They can lead to loss of information if not performed carefully.
- They can be time-consuming if a large number of objects need to be transformed at the same time.

Examples of Basic Transformations:
- Translation: Moving an object from one position to another in a video game.
- Rotation: Rotating a 3D model of a car in a car designing software.
- Scaling: Zooming in or out of an image in an image editing software.
- Shearing: Distorting the shape of a text in a graphic designing software.

Applications of Basic Transformations:
- Computer Graphics
- Video games
- Animation
- Virtual Reality
- Augmented Reality

In conclusion, basic transformations are an essential part of Computer Graphics. They provide a way to change the position, orientation, or size of an object. By combining them, complex transformations can be created, which are helpful in creating animations and special effects.