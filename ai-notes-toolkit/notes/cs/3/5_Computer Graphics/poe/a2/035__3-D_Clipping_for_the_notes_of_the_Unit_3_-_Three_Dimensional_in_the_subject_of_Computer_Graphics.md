 Here is the content in markdown format without any emojis or external links and in a formal tone:

### 3-D Clipping for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

1. Clipping: Clipping is a technique to remove portions of a 3D model that lie outside a defined volume. This volume can be a view frustrum or any other volume defined by additional clipping planes. Clipping is done to increase rendering efficiency by not drawing portions of the scene that will not be visible in the final image.
2. View Frustrum Clipping: The view frustrum is the pyramid shaped volume defined by the camera’s position and viewing direction. Any object lying completely outside this volume need not be drawn. This clipping discards objects behind the camera and those which are outside the field of view.
3. Additional Clipping Planes: Additional clipping planes can be defined to clip away portions of the scene for other purposes. For example, to clip away objects behind a wall to simulate a shadow effect or to clip faraway objects to simulate fog. The clipping planes are defined by a point on the plane and the plane normal. Any vertex or primitive lying on the negative side of the plane is clipped.
4. Clipping Algorithms: The basic clipping algorithms are:
- Sutherland-Hodgman Algorithm: Clips a polygon against a plane.
- Cyrus-Beck Algorithm: Clips a polygon against an arbitrarily oriented plane.
These algorithms can be extended to clip entire polygonal models by recursively applying them on newly exposed edges and triangles.

The content summarizes key points about 3-D Clipping used in Computer Graphics in a formal manner with points and without any external links or emojis. Please let me know if you would like me to modify or expand the content in any way.