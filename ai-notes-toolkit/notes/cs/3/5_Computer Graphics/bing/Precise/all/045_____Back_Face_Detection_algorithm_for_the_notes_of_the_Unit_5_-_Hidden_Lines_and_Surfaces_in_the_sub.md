### Back Face Detection Algorithm

Back Face Detection, also known as the Plane Equation method, is an object space method used to identify hidden surfaces in a scene that contain non-overlapping convex polyhedra . The idea is to check if the polygon surface will be facing away from the viewer or not .

- The polygon surface equation is given by: Ax + By + Cz + D < 0 .
- While determining whether a surface is a back-face or front-face, the viewing direction must also be considered .
- The normal of the surface is given by: N = (A, B, C) .
- A fast and simple object-space method used to remove hidden surfaces from a 3D object is called the plane equation method .
- It is based on the "inside-outside" tests .
- A point (x, y, z) is "inside" a polygon surface with plane parameters A, B, C, and D if .
- The dot product can be used for Back Face Culling .
- To determine if a polygon is a front face or a back face, generate a vector C connecting the COP and a vertex of the polygon .
- Take the dot product C•N of the vector C and the polygon’s normal N .
- If C•N > 0, it’s a back face. If C•N < 0, it’s a front face .
