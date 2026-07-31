### Matrix Representations and Homogenous Coordinates for the Notes of Unit 2 - Transformations in the Subject of Computer Graphics

In the field of computer graphics, transformations are a crucial concept that allows us to manipulate and modify the position, orientation, and size of objects in a virtual space. To represent these transformations, we use matrices and homogenous coordinates. In this unit, we will explore these concepts in detail.

Here are some key points to keep in mind:

- A matrix is a rectangular array of numbers that can be used to represent a variety of geometric transformations, including translation, rotation, scaling, and skewing.
- Homogenous coordinates are a way of representing points in space that allows us to perform these transformations using matrices.
- Homogenous coordinates use a fourth coordinate, called the "w" coordinate, to represent the scale factor of a point. This allows us to perform translation and other transformations without changing the position of the point in space.
- To transform a point using a matrix, we multiply the matrix by the homogenous coordinate of the point. This gives us a new homogenous coordinate that represents the transformed point.
- To transform an object, we apply the same transformation matrix to all of its vertices. This allows us to modify the position, orientation, and size of the object in a consistent and predictable way.
- We can also use matrices to perform composite transformations, which are combinations of multiple individual transformations. To do this, we simply multiply the matrices of the individual transformations together.
- In addition to representing transformations, matrices and homogenous coordinates can also be used for other tasks in computer graphics, such as projection and lighting calculations.

By understanding matrix representations and homogenous coordinates, you will have the tools you need to create complex and realistic virtual environments. Keep these key points in mind as you continue to explore the exciting field of computer graphics.