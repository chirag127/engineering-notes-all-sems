### Basic Transformation for the Notes of the Unit 2 - Transformations in the Subject of Computer Graphics

In the field of Computer Graphics, transformations play a significant role in creating and manipulating images. Transformations are applied to objects to change their position, size, and orientation. In this section, we will discuss the basic transformations used in Computer Graphics.

#### Translation
Translation is a transformation that moves an object from one position to another. It involves moving each point of the object by a specified distance in the x, y, and z-axis. The formula for translation is as follows:

```
T(x,y,z) = | 1 0 0 x |
           | 0 1 0 y |
           | 0 0 1 z |
           | 0 0 0 1 |
```

#### Scaling
Scaling is a transformation that changes the size of an object. It involves changing the distance between each point of the object. The formula for scaling is as follows:

```
S(x,y,z) = | x 0 0 0 |
           | 0 y 0 0 |
           | 0 0 z 0 |
           | 0 0 0 1 |
```

#### Rotation
Rotation is a transformation that changes the orientation of an object. It involves rotating each point of the object by a specified angle around an axis. The formula for rotation is as follows:

```
R(x,y,z) = | cosθ+(1-cosθ)x^2  (1-cosθ)xy-sinθz  (1-cosθ)xz+sinθy  0 |
           | (1-cosθ)xy+sinθz  cosθ+(1-cosθ)y^2   (1-cosθ)yz-sinθx  0 |
           | (1-cosθ)xz-sinθy  (1-cosθ)yz+sinθx  cosθ+(1-cosθ)z^2   0 |
           |         0                  0                  0         1 |
```

#### Reflection
Reflection is a transformation that reflects an object across a plane. It involves changing the sign of one coordinate of each point of the object. The formula for reflection is as follows:

```
M(x,y,z) = | -1  0  0  0 |
           |  0 -1  0  0 |
           |  0  0 -1  0 |
           |  0  0  0  1 |
```

In conclusion, these basic transformations are fundamental to Computer Graphics. They can be used to create complex images by combining them in different ways. It is essential to understand these transformations to create visually appealing and realistic graphics.