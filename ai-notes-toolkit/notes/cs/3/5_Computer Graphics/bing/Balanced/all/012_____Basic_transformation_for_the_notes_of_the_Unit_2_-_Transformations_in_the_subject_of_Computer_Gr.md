# Basic Transformation for the Notes of the Unit 2 - Transformations in the Subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- Transformations are useful for repositioning and resizing graphics on the screen, as well as for creating animations and effects.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another on the plane. It can be described by a vector that specifies the displacement in the x and y directions. Translation can be performed by adding the displacement vector to the original coordinates of the object.
- Rotation is the turning of an object around a fixed point on the plane. It can be described by an angle that specifies the amount of rotation in the clockwise or counterclockwise direction. Rotation can be performed by multiplying the original coordinates of the object by a rotation matrix that depends on the angle and the point of rotation.
- Scaling is the change of size of an object on the plane. It can be described by a factor that specifies the ratio of the new size to the original size. Scaling can be performed by multiplying the original coordinates of the object by a scaling matrix that depends on the factor and the point of scaling.
- Transformations can be combined to create more complex effects. For example, a rotation followed by a translation is equivalent to a rotation around a different point. A scaling followed by a rotation is equivalent to a rotation followed by a scaling with a different factor. The order of transformations matters, as different orders may produce different results.
- Transformations can be represented by matrices and vectors, which are convenient for performing calculations and storing information. A 2D object can be represented by a vector of its coordinates, such as (x, y). A 2D transformation can be represented by a 2x2 matrix that operates on the vector, such as [[a, b], [c, d]]. The result of the transformation is another vector, such as (x', y').
- The following are some examples of matrices that represent common transformations:

  - Translation by (tx, ty): [[1, 0], [0, 1]] + (tx, ty)
  - Rotation by θ around the origin: [[cos θ, -sin θ], [sin θ, cos θ]]
  - Scaling by sx and sy around the origin: [[sx, 0], [0, sy]]
  - Reflection across the x-axis: [[1, 0], [0, -1]]
  - Reflection across the y-axis: [[-1, 0], [0, 1]]
  - Shearing along the x-axis by shx: [[1, shx], [0, 1]]
  - Shearing along the y-axis by shy: [[1, 0], [shy, 1]]

- To apply a transformation to an object, we need to multiply the matrix of the transformation by the vector of the object. For example, to rotate an object by 90 degrees around the origin, we need to multiply the matrix [[0, -1], [1, 0]] by the vector (x, y) to get the vector (-y, x).
- To apply multiple transformations to an object, we need to multiply the matrices of the transformations in the reverse order of the transformations. For example, to translate an object by (tx, ty) and then rotate it by θ around the origin, we need to multiply the matrix [[cos θ, -sin θ], [sin θ, cos θ]] by the matrix [[1, 0], [0, 1]] + (tx, ty) and then by the vector (x, y) to get the vector (x'cos θ - y'sin θ, x'sin θ + y'cos θ), where x' = x + tx and y' = y + ty.