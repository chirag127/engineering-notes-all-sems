### Back Face Detection algorithm

- Back face detection (or back face culling) is a technique to eliminate hidden surfaces or faces that are not visible to the viewer.
- It is based on the assumption that the object is a convex polyhedron, meaning that any line segment joining two points on the object lies entirely inside or on the boundary of the object.
- A face of a convex polyhedron is called a back face if it is oriented away from the viewer, meaning that the angle between the face normal and the viewing direction is greater than 90 degrees.
- A face of a convex polyhedron is called a front face if it is oriented towards the viewer, meaning that the angle between the face normal and the viewing direction is less than 90 degrees.
- The back face detection algorithm can be summarized as follows:

  - For each face of the object, compute the face normal vector by taking the cross product of two adjacent edges.
  - For each face of the object, compute the dot product of the face normal vector and the viewing direction vector.
  - If the dot product is negative, the face is a back face and can be eliminated from further processing.
  - If the dot product is positive, the face is a front face and should be retained for further processing.

- The back face detection algorithm can reduce the number of faces to be processed by up to 50%, depending on the shape and orientation of the object.
- The back face detection algorithm can be applied before or after the projection transformation, as long as the viewing direction vector is consistent with the projection type.