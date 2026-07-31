### Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A composite transformation is a combination of two or more transformations into a single one that is equivalent to the transformations that are performed one after another over a 2D or 3D object  .
- The resulting matrix of a composite transformation is called a composite matrix. The process of combining the matrices is called concatenation.
- The order of concatenation matters, as different orders may produce different results. For example, a translation followed by a rotation is not the same as a rotation followed by a translation .
- A common example of a composite transformation is a rotation about an arbitrary point. This can be achieved by the following steps:
  - Translate the object so that the arbitrary point coincides with the origin.
  - Rotate the object about the origin by the desired angle.
  - Translate the object back to the original position of the arbitrary point.
- The composite matrix for this example is given by:

![Composite matrix for rotation about an arbitrary point](https://www.javatpoint.com/computer-graphics/images/composite-transformation1.jpg)

- Another example of a composite transformation is a reflection about an arbitrary line. This can be achieved by the following steps:
  - Translate the object so that the arbitrary line passes through the origin.
  - Rotate the object so that the arbitrary line coincides with the x-axis.
  - Reflect the object about the x-axis.
  - Rotate the object back to the original orientation of the arbitrary line.
  - Translate the object back to the original position of the arbitrary line.
- The composite matrix for this example is given by:

![Composite matrix for reflection about an arbitrary line](https://www.javatpoint.com/computer-graphics/images/composite-transformation2.jpg)

- Composite transformations can be used to create complex effects and animations in computer graphics, such as scaling, shearing, and perspective transformations .
- Composite transformations can also be applied to coordinate systems, such as the world, view, and projection coordinate systems, to transform the objects from one system to another.