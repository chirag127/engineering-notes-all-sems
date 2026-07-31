### Reflections and Shearing

Reflections and shearing are two types of transformations in computer graphics that change the position and shape of an object.

#### Reflection

- Reflection is a kind of rotation where the angle of rotation is 180 degrees.
- The reflected object is always formed on the other side of a mirror plane, which can be any plane in 3D space.
- The mirror plane can be defined by its normal vector and a point on the plane.
- To reflect an object, we need to find the mirror image of each vertex of the object with respect to the mirror plane.
- The mirror image of a point P can be found by subtracting twice the projection of P onto the normal vector from P.
- The formula for the mirror image of P is:

    P' = P - 2(P.N)N

    where P' is the mirror image, P is the original point, N is the normal vector, and . is the dot product.

- The reflection matrix for a given mirror plane can be derived by applying the formula to the standard basis vectors.
- The reflection matrix for the xy-plane is:

    R = | -1  0  0  0 |
        |  0 -1  0  0 |
        |  0  0  1  0 |
        |  0  0  0  1 |

- The reflection matrix for the xz-plane is:

    R = | -1  0  0  0 |
        |  0  1  0  0 |
        |  0  0 -1  0 |
        |  0  0  0  1 |

- The reflection matrix for the yz-plane is:

    R = |  1  0  0  0 |
        |  0 -1  0  0 |
        |  0  0 -1  0 |
        |  0  0  0  1 |

- To reflect an object, we need to multiply each vertex by the reflection matrix and then redraw the object.

- An example of reflection in the xy-plane is shown below:

    ![Reflection in the xy-plane](https://www.gatevidyalay.com/wp-content/uploads/2018/12/3D-Reflection-in-Computer-Graphics-Example-1.png)

#### Shearing

- Shearing is the process of slanting an object in 3D space either in x, y, or in the z-direction.
- Shearing changes (or deforms) the shape of the object, but not its volume or area.
- Shearing can be done in one direction or two directions, depending on the number of parameters used.
- The shearing parameters are the factors by which the coordinates of the object are shifted along a given axis.
- The shearing matrix for a given direction can be derived by adding the shearing parameters to the corresponding elements of the identity matrix.
- The shearing matrix for the x-direction is:

    S = |  1  shx  0  0 |
        |  0   1   0  0 |
        |  0   0   1  0 |
        |  0   0   0  1 |

    where shx is the shearing parameter along the x-axis.

- The shearing matrix for the y-direction is:

    S = |  1   0   0  0 |
        | shy  1   0  0 |
        |  0   0   1  0 |
        |  0   0   0  1 |

    where shy is the shearing parameter along the y-axis.

- The shearing matrix for the z-direction is:

    S = |  1   0   0  0 |
        |  0   1   0  0 |
        | shz  0   1  0 |
        |  0   0   0  1 |

    where shz is the shearing parameter along the z-axis.

- To shear an object, we need to multiply each vertex by the shearing matrix and then redraw the object.

- An example of shearing in the x-direction is shown below:

    ![Shearing in the x-direction](https://www.geeksforgeeks.org/wp-content