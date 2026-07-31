### Back Face Detection Algorithm

- Back face detection, also known as plane equation method, is an object space method for identifying the visible surfaces of a polyhedron .
- A polyhedron is a solid object bounded by flat polygonal faces. Each face has a normal vector that points outward from the polyhedron.
- The normal vector of a face can be computed by taking the cross product of two non-parallel edges of the face.
- The back face detection algorithm works as follows :
  - For each face of the polyhedron, compute its normal vector and its plane parameters A, B, C, and D.
  - For a left-handed coordinate system, if the Z component of the normal vector is positive, then the face is a back face and can be discarded. If the Z component is negative, then the face is a front face and can be drawn.
  - For a right-handed coordinate system, the opposite is true: if the Z component of the normal vector is negative, then the face is a back face and can be discarded. If the Z component is positive, then the face is a front face and can be drawn.
  - Alternatively, for any coordinate system, a point (x, y, z) is inside a face with plane parameters A, B, C, and D if Ax + By + Cz + D < 0. If the point is along the line of sight to the face, then the face is a back face and can be discarded. If the point is not along the line of sight to the face, then the face is a front face and can be drawn.
- The back face detection algorithm is fast and simple, but it has some limitations:
  - It only works for convex polyhedra, where every face is visible from the outside. For concave polyhedra, some faces may be hidden by other faces, even if they are front faces.
  - It does not account for the perspective projection, where the orientation of the faces may change depending on the viewpoint. For example, a face that is a back face from one viewpoint may become a front face from another viewpoint.
  - It does not account for the occlusion of faces by other objects in the scene. For example, a face that is a front face may be hidden by another object that is closer to the viewer.

Here is a diagram that illustrates the back face detection algorithm for a left-handed coordinate system:

```
    y
    |
    |   /\
    |  /  \
    | /    \  N
    |/      \  \
    +--------+   \
   /|       /|    \
  / |      / |     \
 /  |     /  |      \
+---+----+   +-------+----> x
|  /|   /|  /|      /|
| / |  / | / |     / |
|/  |/  |/  |/    /  |
+---+---+   +----+   |
|  /    |  /    |   /
| /     | /     |  /
|/      |/      | /
+-------+-------+/
    /
   /
  /
 z
```

The face with normal vector N is a back face because its Z component is positive. The other faces are front faces because their Z components are negative.