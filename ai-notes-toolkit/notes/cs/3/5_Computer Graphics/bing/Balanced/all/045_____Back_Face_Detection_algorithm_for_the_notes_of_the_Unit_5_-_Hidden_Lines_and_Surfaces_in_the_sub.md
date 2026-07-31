# Back Face Detection Algorithm

- Back face detection (or back face culling) is a technique to eliminate hidden surfaces or lines in computer graphics.
- It is based on the assumption that a polygonal model of a solid object is represented by a set of faces that are oriented outward from the object's interior.
- A face is said to be back facing if it is oriented away from the viewer, i.e., its normal vector points in the opposite direction of the viewing vector.
- Back facing faces are not visible to the viewer and can be discarded from the rendering process, saving computation time and memory.
- The algorithm to determine whether a face is back facing or not is as follows:

  - For each face F in the polygonal model, compute its normal vector N by taking the cross product of two non-parallel edges of F.
  - For each face F, compute its centroid C by taking the average of its vertices.
  - For each face F, compute the viewing vector V by subtracting the viewer's position P from the centroid C, i.e., V = C - P.
  - For each face F, compute the dot product of N and V, i.e., D = N.V.
  - If D is positive, then F is back facing and can be discarded. If D is negative or zero, then F is front facing and should be rendered.