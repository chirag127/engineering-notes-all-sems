# Matrix representations and homogenous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling and perspective projection in computer graphics .
- Homogenous coordinates are a way to represent points and vectors in a higher-dimensional space using an extra coordinate, usually denoted by w.
- Homogenous coordinates allow all geometric transformation equations to be represented as matrix multiplication, which simplifies the computation and the combination of multiple transformations .
- Homogenous coordinates also enable the representation of points at infinity, which are useful for perspective projection and parallel lines.
- To convert a point (x, y) in Cartesian coordinates to a point (x, y, w) in homogenous coordinates, we can use any value of w except zero, and divide the coordinates by w to get the original point. For example, (2, 3) can be represented as (4, 6, 2) or (6, 9, 3) in homogenous coordinates .
- To convert a point (x, y, w) in homogenous coordinates to a point (x, y) in Cartesian coordinates, we divide the coordinates by w, as long as w is not zero. For example, (4, 6, 2) can be converted to (2, 3) by dividing by 2 .
- To represent a vector (x, y) in homogenous coordinates, we use w = 0, which indicates that the vector does not have a position. For example, (2, 3) can be represented as (2, 3, 0) in homogenous coordinates .
- To represent a matrix transformation in homogenous coordinates, we use a square matrix of size one greater than the dimension of the space. For example, a 2D transformation can be represented by a 3x3 matrix, and a 3D transformation can be represented by a 4x4 matrix .
- The matrix representation for translation in homogenous coordinates is:

![translation matrix](https://www.geeksforgeeks.org/wp-content/uploads/translation-matrix.png)

where tx and ty are the translation distances along the x and y axes, respectively .

- The matrix representation for rotation in homogenous coordinates is:

![rotation matrix](https://www.geeksforgeeks.org/wp-content/uploads/rotation-matrix.png)

where θ is the angle of rotation in the counterclockwise direction .

- The matrix representation for scaling in homogenous coordinates is:

![scaling matrix](https://www.geeksforgeeks.org/wp-content/uploads/scaling-matrix.png)

where sx and sy are the scaling factors along the x and y axes, respectively .

- The matrix representation for perspective projection in homogenous coordinates is:

![perspective projection matrix](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Perspective_projection_matrix.svg/512px-Perspective_projection_matrix.svg.png)

where f is the focal length of the camera, and n and f are the near and far clipping planes, respectively .

- To apply a matrix transformation to a point or a vector in homogenous coordinates, we multiply the matrix by the column vector of the coordinates. For example, to translate the point (2, 3) by (4, 5), we multiply the translation matrix by the column vector of the point:

![matrix multiplication example](https://www.geeksforgeeks.org/wp-content/uploads/matrix-multiplication.png)

which gives the result (6, 8, 1), which can be converted to (6, 8) in Cartesian coordinates .

- To combine multiple matrix transformations, we multiply the matrices in the reverse order of the transformations. For example, to first translate the point (2, 3) by (4, 5) and then rotate it by 90 degrees, we multiply the rotation matrix by the translation matrix and then by the column vector of the point:

![matrix combination example](https://www.geeksforgeeks.org/wp-content/uploads/matrix-combination.png)

which gives the result (-8, 6, 1), which can be converted to (-8, 6) in Cartesian coordinates [^3