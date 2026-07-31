Hello, I am Sydney, your AI assistant. I can help you with your study material for Unit 3 - Three Dimensional in the subject of Computer Graphics. Here are some notes on the topic of projections:

### Projections

- A projection is a process of transforming a 3D object into a 2D image on a plane, called the projection plane or view plane.
- The projection plane can be parallel or perpendicular to one of the coordinate axes, or it can be arbitrarily oriented in 3D space.
- The projection of a point P(x, y, z) onto the projection plane is the intersection of the line passing through P and perpendicular to the projection plane with the projection plane.
- There are two main types of projections: parallel and perspective.

#### Parallel Projections

- In parallel projections, the lines of projection are parallel to each other and perpendicular to the projection plane.
- Parallel projections preserve the relative proportions and angles of the 3D object, but they do not show the depth or distance of the object.
- Parallel projections can be classified into orthographic and oblique projections.

##### Orthographic Projections

- In orthographic projections, the projection plane is parallel to one of the principal planes (xy, yz, or xz) of the 3D object.
- Orthographic projections can be further classified into three types: front, top, and side views.
- The front view is obtained by projecting the 3D object onto the xy-plane, the top view is obtained by projecting the 3D object onto the xz-plane, and the side view is obtained by projecting the 3D object onto the yz-plane.
- The front, top, and side views are also called the standard views or the principal views of the 3D object.
- The standard views can be arranged in different ways to form a multiview projection, which shows the 3D object from different angles.
- The most common arrangement of the standard views is the first-angle projection, which is used in Europe and Asia, and the third-angle projection, which is used in North America and Australia.
- In the first-angle projection, the 3D object is placed in the first quadrant, and the standard views are arranged as follows:

```
    +-----------------+
    |                 |
    |      Top        |
    |                 |
    +-----------------+
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    +-----------------+
    |                 |
    |      Front      |
    |                 |
    +-----------------+
```

- In the third-angle projection, the 3D object is placed in the third quadrant, and the standard views are arranged as follows:

```
    +-----------------+
    |                 |
    |      Front      |
    |                 |
    +-----------------+
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    +-----------------+
    |                 |
    |      Top        |
    |                 |
    +-----------------+
```

- The side view can be placed on either the left or the right of the front view, depending on the orientation of the 3D object.

##### Oblique Projections

- In oblique projections, the projection plane is still parallel to one of the principal planes of the 3D object, but the lines of projection are not perpendicular to the projection plane.
- Oblique projections show more of the 3D object than orthographic projections, but they distort the shape and size of the object.
- Oblique projections can be further classified into three types: cavalier, cabinet, and general oblique projections.
- In cavalier projections, the lines of projection are at a 45-degree angle to the projection plane, and the length of the projected lines is equal to the length of the original lines.
- In cabinet projections, the lines of projection are at a 63.4-degree angle to the projection plane, and the length of the projected lines is half of the length of the original lines.
- In general oblique projections, the lines of projection are at an arbitrary angle to the projection plane, and the length of the projected lines is scaled by a factor called the foreshortening factor.
- The foreshortening factor can be calculated by the formula:

```
foreshortening factor = cos(alpha) / cos(beta)

where alpha is the angle between the line of projection and the projection plane, and beta is the angle between the line of projection and the original line.

```
