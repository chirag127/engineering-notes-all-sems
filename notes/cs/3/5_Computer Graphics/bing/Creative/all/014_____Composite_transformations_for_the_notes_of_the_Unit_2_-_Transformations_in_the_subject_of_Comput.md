# Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A composite transformation is a combination of two or more transformations into a single one that is equivalent to the transformations that are performed one after another over a 2D or 3D object  .
- The process of combining the transformations is called concatenation, and the resulting matrix is called the composite matrix.
- The order of the transformations matters, as different orders may produce different results. Some transformations are commutative, meaning that the order does not affect the outcome, while others are non-commutative, meaning that the order does affect the outcome.
- For example, translation and scaling are commutative, as translating and then scaling an object is the same as scaling and then translating it. However, rotation and scaling are non-commutative, as rotating and then scaling an object is not the same as scaling and then rotating it.
- To perform a composite transformation, we need to multiply the matrices of the individual transformations in the reverse order of the desired sequence. For example, if we want to translate an object by (tx, ty) and then rotate it by an angle θ, we need to multiply the rotation matrix by the translation matrix, and then multiply the result by the object's coordinates.
- The general formula for a composite transformation matrix is:

  M = Mn * Mn-1 * ... * M2 * M1

  where M is the composite matrix, Mn is the last transformation matrix, and M1 is the first transformation matrix.
- Some common composite transformations are:

  - Rotation about an arbitrary point: This can be achieved by translating the object to the origin, rotating it by the desired angle, and then translating it back to the original position  .
  - Scaling about an arbitrary point: This can be achieved by translating the object to the origin, scaling it by the desired factors, and then translating it back to the original position  .
  - Reflection about an arbitrary line: This can be achieved by translating the object to the origin, rotating it to align the line with the x-axis, reflecting it about the x-axis, and then reversing the previous steps  .
  - Shearing about an arbitrary line: This can be achieved by translating the object to the origin, rotating it to align the line with the x-axis, shearing it along the x-axis, and then reversing the previous steps  .

- Composite transformations are useful for creating complex effects and animations in computer graphics, such as scaling and rotating a scene, or transforming a character's pose.