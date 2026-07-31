### Back Face Detection Algorithm

- Back Face Detection, also known as the Plane Equation method, is an object space method used to determine the visible surfaces of objects  .
- The algorithm compares objects and parts of objects to find out which surfaces are visible  .
- For example, consider a triangular surface whose visibility needs to be decided. The idea is to check if the triangle will be facing away from the viewer or not  .
- In the left-handed system, if the Z component of the normal vector is positive, then it is a back face. If the Z component of the vector is negative, then it is a front face .
- Back-face culling is a step in the graphical pipeline that tests whether the points in a polygon appear in clockwise or counter-clockwise order when projected onto the screen .