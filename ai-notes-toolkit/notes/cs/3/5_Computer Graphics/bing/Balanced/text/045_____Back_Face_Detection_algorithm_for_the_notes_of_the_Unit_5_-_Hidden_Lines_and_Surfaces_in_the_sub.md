### Back Face Detection algorithm for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Back face detection (or back face culling) is a technique to eliminate hidden surfaces or faces that are not visible to the viewer.
- It is based on the assumption that the object is a convex polyhedron, which means that any line segment joining two points on the surface of the object lies entirely within the object.
- A face of a convex polyhedron is said to be back facing if it is oriented away from the viewer, or equivalently, if its surface normal is pointing away from the viewer.
- The back face detection algorithm can be summarized as follows:

  1. For each face of the polyhedron, compute its surface normal vector by taking the cross product of two adjacent edges.
  2. Transform the surface normal vector to the view coordinate system using the model-view matrix.
  3. If the z-component of the transformed surface normal vector is positive, then the face is back facing and can be discarded. Otherwise, the face is front facing and should be rendered.

- The back face detection algorithm can improve the rendering efficiency by reducing the number of faces that need to be processed by the hidden surface removal algorithm, such as the z-buffer algorithm or the painter's algorithm.
- However, the back face detection algorithm is not applicable to non-convex polyhedra, such as a torus or a concave cube, because some of their faces may be partially visible and partially hidden. In such cases, a more sophisticated hidden surface removal algorithm is needed.