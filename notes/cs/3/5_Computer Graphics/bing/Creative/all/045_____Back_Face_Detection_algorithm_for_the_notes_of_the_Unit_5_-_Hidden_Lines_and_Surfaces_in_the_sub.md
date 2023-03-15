# Back Face Detection Algorithm

- Back face detection, also known as plane equation method, is an object space method for identifying the visible surfaces of a polyhedron .
- A polyhedron is a solid object bounded by flat polygonal faces. Each face has a normal vector that points outward from the object.
- A face is called a back face if its normal vector points away from the viewer, or equivalently, if the angle between the normal vector and the viewing direction is greater than 90 degrees .
- Back face detection algorithm works as follows :
  - For each face of the polyhedron, compute its normal vector by taking the cross product of two adjacent edges.
  - For each face of the polyhedron, compute its plane equation by substituting any vertex into the equation Ax + By + Cz + D = 0, where A, B, C are the components of the normal vector.
  - For each face of the polyhedron, test whether it is a back face by substituting the viewing point into the plane equation and checking the sign of the result. If the result is positive, the face is a back face and can be eliminated. If the result is negative or zero, the face is a front face and should be retained.
- Back face detection algorithm can reduce the number of faces to be processed by the hidden surface removal algorithms, such as Z-buffer, scan-line, or painter's algorithm .
- Back face detection algorithm is also known as back-face culling in computer graphics, and it is a common optimization technique for rendering 3D scenes.