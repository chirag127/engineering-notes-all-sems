 Here is the content in markdown format for the topic ### Back Face Detection algorithm for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics:

## Back Face Detection algorithm

- Back face detection is an algorithm to detect and cull the back faces of a polygon which are not visible to the viewer.
- It is done to optimize the rendering process by not wasting time and resources to render the back faces which are not visible.
- The algorithm works on these steps:

1. Find the normal to each polygon face using the coordinates of its vertices. The normal points outwards from the face.
2. Find the view direction vector from the viewpoint to the polygon face.
3. Take the dot product of the normal and view direction vector.
- If the dot product is negative, the face is facing away from the viewer. Hence, it is a back face and can be culled.
- If the dot product is positive, the face is facing towards the viewer. Hence, it should be rendered.

- advantages: Optimized rendering by not rendering invisible back faces.
- disadvantages: Additional computation required to find normals and dot product.
- applications: Used in 3D graphics for rendering optimization.

- Here is an ascii diagram to understand the concept:

View point -->         View direction vector
↕
┌───────────────────┐
│       │            Polygon
│       │            face
│       │    Normal
└───────────────────┘

The dot product of normal and view direction vector will be negative here,
marking this as a back face to cull.