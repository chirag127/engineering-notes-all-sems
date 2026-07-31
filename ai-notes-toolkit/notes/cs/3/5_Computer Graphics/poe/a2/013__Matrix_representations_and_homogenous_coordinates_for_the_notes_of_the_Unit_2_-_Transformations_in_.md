 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Matrix representations and homogenous coordinates

1. A transformation in 2D can be represented using a 3x3 transformation matrix. The first two columns represent the scaling and rotation components while the third column represents the translation component.
2. A 3D transformation can be represented using a 4x4 transformation matrix. The first three columns represent the scaling, rotation and shear components while the fourth column represents the translation component.
3. Homogenous coordinates are used to represent points in transformations. A point (x, y) in 2D is represented as (x, y, 1) in homogenous coordinates. Similarly, a point (x, y, z) in 3D is represented as (x, y, z, 1) in homogenous coordinates.
4. Matrix multiplication is used to transform points from one coordinate system to another. The transformation matrix is multiplied with the point in homogenous coordinates to get the new coordinate values.
5. Care must be taken to normalize the results after matrix multiplication by dividing the first three terms by the fourth term to get the Cartesian coordinates.

The above points cover the key aspects of matrix representations and homogenous coordinates required to understand 2D and 3D transformations in Computer Graphics. Let me know if you would like me to elaborate on any of the points or add additional details.