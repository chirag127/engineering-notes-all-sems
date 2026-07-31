### Back Face Detection Algorithm

Back Face Detection, also known as the Plane Equation method, is an object space method used in computer graphics to determine the visible surfaces of objects  . This method compares objects and parts of objects to find out which surfaces are visible  .

- Back-face detection can identify all the hidden surfaces in a scene that contain non-overlapping convex polyhedra .
- The polygon surface equation is used in this method: Ax + By + Cz + D < 0 .
- The idea is to check if the triangle will be facing away from the viewer or not .
- Back-face culling is a preprocessing step for hidden surface removal .
- It is very powerful in that almost half of the polygons of an object are discarded as back faces .
- Especially, for a single convex polyhedron, back-face culling does the entire job of hidden-surface removal .
- Hidden-surface removal is applied only to the remaining front faces .
