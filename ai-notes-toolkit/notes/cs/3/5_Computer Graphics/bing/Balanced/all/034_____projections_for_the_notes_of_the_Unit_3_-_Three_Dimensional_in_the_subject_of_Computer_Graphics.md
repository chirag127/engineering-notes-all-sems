# Projections in Computer Graphics

- Projection is a technique or process which is used to transform a 3D object into a 2D plane.
- Projection is necessary to display a 3D object on a 2D screen or paper.
- Projection can be classified into two types: parallel projection and perspective projection.

## Parallel Projection

- Parallel projection discards z-coordinate and parallel lines from each vertex on the object are extended until they intersect the view plane.
- Parallel projection preserves the relative proportions and angles of the object, but not the true distances or sizes.
- Parallel projection can be further divided into orthographic projection, oblique projection and isometric projection.

### Orthographic Projection

- Orthographic projection is a type of parallel projection where the direction of projection is normal to the projection plane .
- Orthographic projection shows only one face of the object, and the hidden lines are removed or dashed.
- Orthographic projection can be defined by a 6-tuple, (left, right, bottom, top, near, far), which defines the clipping planes.
- Orthographic projection is commonly used in engineering and technical drawings.

### Oblique Projection

- Oblique projection is a type of parallel projection where the direction of projection is not normal to the projection plane .
- Oblique projection shows more than one face of the object, and the hidden lines are usually visible.
- Oblique projection can be classified into cavalier projection and cabinet projection, depending on the angle between the projection direction and the projection plane.
- Oblique projection is often used to create a 3D effect in 2D drawings.

### Isometric Projection

- Isometric projection is a special case of oblique projection where the direction of projection makes equal angles with the three principal axes of the object .
- Isometric projection shows three faces of the object, and the angles between them are 120 degrees.
- Isometric projection preserves the lengths of the edges of the object, but not the angles or areas.
- Isometric projection is widely used in video games, technical illustrations and architectural drawings.

## Perspective Projection

- Perspective projection simulates the way a human eye perceives a 3D scene.
- Perspective projection preserves the relative sizes and distances of the object, but not the parallelism or angles.
- Perspective projection can be defined by a center of projection (or eye point), a view plane (or image plane), and a view reference point (or look-at point).
- Perspective projection can be classified into one-point, two-point and three-point perspective, depending on the number of vanishing points on the view plane.
- Perspective projection is commonly used in art, photography and computer graphics.