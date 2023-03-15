# Transformation of Projections

- A projection is a method of representing a three-dimensional (3D) object on a two-dimensional (2D) plane, such as a sheet of paper or a computer screen.
- A projection is obtained by drawing lines of sight from an observer's eye to the points on the object and marking where these lines intersect a plane of projection.
- A plane of projection is an imaginary flat surface that the object is projected onto.
- The type of projection depends on the relative position and orientation of the observer, the object, and the plane of projection.
- There are two main types of projections: parallel and perspective.
- In a parallel projection, the lines of sight are assumed to be parallel to each other and perpendicular to the plane of projection. This means that the distance from the observer to the object is infinite, and the size and shape of the object are preserved in the projection.
- In a perspective projection, the lines of sight converge at a single point, called the center of projection or the vanishing point. This means that the distance from the observer to the object is finite, and the size and shape of the object are distorted in the projection, depending on the distance and angle.
- A transformation of projections is a change in the type, position, or orientation of the projection, resulting in a different view of the object.
- A transformation of projections can be performed by applying a matrix multiplication to the coordinates of the object, using a specific projection matrix that corresponds to the desired projection.
- A projection matrix is a 4x4 matrix that maps the 3D coordinates of the object to the 2D coordinates of the projection plane, by adding a fourth dimension called the homogeneous coordinate.
- The homogeneous coordinate is used to distinguish between parallel and perspective projections, and to allow for translation and scaling of the object in the projection plane.
- A projection matrix can be decomposed into three components: a perspective division, a projection transformation, and a viewport transformation.
- A perspective division is a division by the homogeneous coordinate, which normalizes the coordinates and makes them independent of the distance from the observer.
- A projection transformation is a transformation that changes the type of projection, such as orthographic, oblique, or perspective.
- An orthographic projection is a parallel projection where the plane of projection is parallel to one of the principal planes of the object, such as the front, top, or side view.
- An oblique projection is a parallel projection where the plane of projection is inclined to one of the principal planes of the object, such as the isometric, dimetric, or trimetric view.
- A perspective projection is a projection where the lines of sight converge at a single point, such as the one-point, two-point, or three-point view.
- A viewport transformation is a transformation that maps the coordinates of the projection plane to the coordinates of the display device, such as a screen or a printer, by scaling, translating, and clipping the projection.