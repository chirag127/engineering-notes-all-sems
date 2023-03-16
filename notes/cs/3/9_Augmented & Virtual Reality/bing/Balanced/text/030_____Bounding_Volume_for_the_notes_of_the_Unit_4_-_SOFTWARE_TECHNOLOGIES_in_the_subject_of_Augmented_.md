### Bounding Volume

- A bounding volume is a simplified shape that encloses a more complex object or a set of objects in a virtual scene.
- The purpose of a bounding volume is to speed up collision detection and other geometric operations by performing them on the simpler shape first, and then refining the results if necessary.
- Bounding volumes are usually chosen to be convex shapes, such as spheres, boxes, cylinders, or convex hulls, because they have simpler and faster intersection tests than concave shapes.
- Bounding volumes can be hierarchical, meaning that a large bounding volume can contain smaller bounding volumes that enclose subsets of the objects. This can further improve the efficiency of collision detection and other operations by culling out large portions of the scene that are not relevant.
- Bounding volumes can also be dynamic, meaning that they can change their shape and size according to the movement and deformation of the objects they enclose. This can make them more accurate and adaptable, but also more costly to update and maintain.