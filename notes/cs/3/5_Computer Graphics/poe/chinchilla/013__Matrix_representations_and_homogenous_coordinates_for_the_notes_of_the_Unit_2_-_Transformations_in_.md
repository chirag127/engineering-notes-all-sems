### Matrix representations and homogenous coordinates for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

In the field of computer graphics, matrix representations are widely used to perform various types of transformations on objects. These transformations can include translations, rotations, scaling, and shearing. Matrix representations allow us to apply these transformations to objects in a simple and efficient way. In this section, we will discuss matrix representations and homogenous coordinates in detail.

#### Matrix Representations

A matrix is a rectangular array of numbers. In computer graphics, matrices are used to represent transformations. A transformation matrix is a square matrix that describes how to transform points in space. The transformation matrix can be used to perform various types of transformations such as translations, rotations, scaling, and shearing.

The transformation matrix for a translation in two dimensions is given as follows:

```
[1 0 tx]
[0 1 ty]
[0 0 1]
```

where `tx` and `ty` are the translation values in the x and y direction, respectively. 

The transformation matrix for a rotation in two dimensions is given as follows:

```
[cos(theta) -sin(theta) 0]
[sin(theta) cos(theta)  0]
[0           0           1]
```

where `theta` is the angle of rotation in radians.

The transformation matrix for a scaling in two dimensions is given as follows:

```
[sx 0   0]
[0  sy  0]
[0  0  1]
```

where `sx` and `sy` are the scaling values in the x and y direction, respectively.

#### Homogenous Coordinates

In computer graphics, homogenous coordinates are used to represent points in space. Homogenous coordinates allow us to represent points with four values instead of three. The fourth value is often referred to as the `w` coordinate. Homogenous coordinates are useful because they allow us to represent translations as matrix multiplications.

To convert a point in Cartesian coordinates to homogenous coordinates, we can add a `w` coordinate of 1. The resulting homogenous coordinate is given as `[x, y, z, 1]`.

To convert a point in homogenous coordinates back to Cartesian coordinates, we can divide the first three coordinates by the `w` coordinate. The resulting Cartesian coordinate is given as `[x/w, y/w, z/w]`.

Homogenous coordinates are also useful for representing points at infinity. In homogenous coordinates, a point at infinity can be represented as `[x, y, z, 0]`.

#### Conclusion

Matrix representations and homogenous coordinates are important concepts in computer graphics. Matrix representations allow us to perform various types of transformations on objects, while homogenous coordinates allow us to represent points in space and perform translations as matrix multiplications. Understanding these concepts is essential for developing computer graphics applications.