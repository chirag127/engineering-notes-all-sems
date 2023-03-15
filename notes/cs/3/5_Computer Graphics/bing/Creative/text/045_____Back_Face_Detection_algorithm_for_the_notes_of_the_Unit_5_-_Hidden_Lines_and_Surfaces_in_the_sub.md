### Back Face Detection Algorithm

- Back face detection, also known as plane equation method, is an object space method for visible surface detection .
- It is based on the idea that a polygon is a back face if it is oriented away from the viewer, and hence can be eliminated from the rendering process.
- It can be applied to convex polyhedra, such as cubes, pyramids, and prisms, but not to concave polyhedra, such as tori, or objects with holes.
- The algorithm works as follows :
  - For each polygon in the object, compute its normal vector using the cross product of two adjacent edges.
  - For a right-handed coordinate system, if the z-component of the normal vector is positive, then the polygon is a back face. If the z-component is negative, then the polygon is a front face.
  - For a left-handed coordinate system, the opposite is true: if the z-component of the normal vector is negative, then the polygon is a back face. If the z-component is positive, then the polygon is a front face.
  - Alternatively, the dot product of the normal vector and the view vector can be used to determine the orientation of the polygon. If the dot product is positive, then the polygon is a back face. If the dot product is negative, then the polygon is a front face.
  - Discard all the back faces from the rendering process, and only draw the front faces.
- The advantages of back face detection are:
  - It is simple and fast to implement, as it only requires a few arithmetic operations per polygon.
  - It can eliminate up to 50% of the polygons in a typical scene, reducing the computational load for the subsequent stages of the rendering pipeline.
- The disadvantages of back face detection are:
  - It cannot handle concave polyhedra or objects with holes, as some of their back faces may be visible to the viewer.
  - It cannot handle transparent or translucent objects, as their back faces may contribute to the final image.
  - It cannot handle self-intersecting objects, as some of their back faces may be in front of their front faces.