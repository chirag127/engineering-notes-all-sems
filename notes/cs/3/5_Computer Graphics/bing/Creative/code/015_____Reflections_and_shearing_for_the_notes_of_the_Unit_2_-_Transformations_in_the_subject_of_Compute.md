### Reflections and Shearing

- Reflections and shearing are two types of transformations in computer graphics that change the position, orientation, or shape of an object.
- A reflection is a transformation that flips an object over a line or a plane, creating a mirror image of the original object. The line or plane is called the axis or plane of reflection.
- A shearing is a transformation that slants an object in one or more directions, changing the shape of the object. The amount of slanting is called the shear factor.
- Both reflections and shearing can be performed in two-dimensional or three-dimensional space, depending on the number of coordinates involved.

#### Reflections in 2D

- A reflection in 2D is a transformation that flips an object over a line, creating a mirror image of the original object. The line is called the axis of reflection.
- The axis of reflection can be horizontal, vertical, or diagonal, depending on the orientation of the line.
- To perform a reflection in 2D, we need to find the new coordinates of each point of the object after the transformation. This can be done by using the following formulas, depending on the axis of reflection:

  - If the axis of reflection is the x-axis, then the new coordinates of a point (x, y) are (x, -y).
  - If the axis of reflection is the y-axis, then the new coordinates of a point (x, y) are (-x, y).
  - If the axis of reflection is the line y = x, then the new coordinates of a point (x, y) are (y, x).
  - If the axis of reflection is the line y = -x, then the new coordinates of a point (x, y) are (-y, -x).

- For example, consider the following figure, where a triangle ABC is reflected over the x-axis, the y-axis, the line y = x, and the line y = -x.

![Reflection in 2D](https://www.includehelp.com/computer-graphics/images/reflection-in-2d.jpg)

- The new coordinates of the vertices of the triangle after each reflection are:

  - Over the x-axis: A'(-2, -1), B'(1, -3), C'(4, -2)
  - Over the y-axis: A'(-2, 1), B'(-1, 3), C'(-4, 2)
  - Over the line y = x: A'(1, -2), B'(3, 1), C'(2, 4)
  - Over the line y = -x: A'(-1, 2), B'(-3, -1), C'(-2, -4)

#### Reflections in 3D

- A reflection in 3D is a transformation that flips an object over a plane, creating a mirror image of the original object. The plane is called the plane of reflection.
- The plane of reflection can be any plane that passes through the origin, such as the xy-plane, the yz-plane, or the xz-plane, or any other plane defined by a normal vector.
- To perform a reflection in 3D, we need to find the new coordinates of each point of the object after the transformation. This can be done by using the following formulas, depending on the plane of reflection:

  - If the plane of reflection is the xy-plane, then the new coordinates of a point (x, y, z) are (x, y, -z).
  - If the plane of reflection is the yz-plane, then the new coordinates of a point (x, y, z) are (-x, y, z).
  - If the plane of reflection is the xz-plane, then the new coordinates of a point (x, y, z) are (x, -y, z).
  - If the plane of reflection is defined by a normal vector (a, b, c), then the new coordinates of a point (x, y, z) are (x - 2a(xa + yb + zc) / (a^2 + b^2 + c^2), y - 2b(xa + yb + zc) / (a^2 + b^2 + c^2), z - 2c(xa + yb + zc) / (a^2 + b^2 + c^2)).

- For example, consider the following figure, where a cube ABCDEFG