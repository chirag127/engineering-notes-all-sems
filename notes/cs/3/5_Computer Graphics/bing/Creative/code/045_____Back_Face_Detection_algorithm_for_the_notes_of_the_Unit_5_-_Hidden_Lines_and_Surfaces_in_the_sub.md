# Back Face Detection Algorithm

- Back face detection, also known as plane equation method, is an object space method for identifying the visible surfaces of a polyhedron .
- A polyhedron is a solid object bounded by flat polygonal faces. Each face has a normal vector that points outward from the polyhedron.
- The normal vector of a face can be computed by taking the cross product of two non-parallel edges of the face.
- The back face detection algorithm is based on the assumption that the polyhedron is convex, meaning that any line segment joining two points inside or on the polyhedron is entirely contained within or on the polyhedron.
- The algorithm works as follows :
  - For each face of the polyhedron, compute its normal vector and its plane parameters (A, B, C, and D) using the equation Ax + By + Cz + D = 0.
  - For each face of the polyhedron, perform an inside-outside test on a reference point (x, y, z) that is known to be inside the polyhedron. This can be the centroid of the polyhedron or any other point that is guaranteed to be inside.
  - The inside-outside test is done by substituting the reference point into the plane equation and checking the sign of the result. If the result is positive, then the reference point is inside the face and the face is a back face. If the result is negative, then the reference point is outside the face and the face is a front face.
  - Discard all the back faces from the rendering process, as they are hidden by the front faces.
- The back face detection algorithm is a simple and fast way to eliminate hidden surfaces, but it has some limitations:
  - It only works for convex polyhedra. If the polyhedron is concave, some back faces may be visible and some front faces may be hidden.
  - It does not account for occlusion by other objects in the scene. If there are multiple polyhedra in the scene, some front faces may be hidden by other objects that are closer to the viewer.
  - It does not account for perspective projection. If the polyhedron is viewed from a perspective camera, some back faces may appear as front faces and vice versa, depending on the angle of view and the distance from the camera.