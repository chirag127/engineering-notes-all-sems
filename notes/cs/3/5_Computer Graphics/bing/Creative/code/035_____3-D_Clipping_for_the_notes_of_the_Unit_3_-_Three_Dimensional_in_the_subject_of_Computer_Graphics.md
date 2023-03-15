Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on 3-D Clipping for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics.

### 3-D Clipping
- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene.
- The purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects.
- 3-D clipping can be done in two basic steps:
  - Discard objects that cannot be viewed, such as objects that are behind the camera, outside the field of view, or too far away. This can be done by comparing the object's bounding box or sphere against the dimensions of the view volume, either before or after projection.
  - Clip objects that intersect with any clipping plane, such as the near and far planes, or the left, right, top and bottom planes of the view volume. This can be done by using algorithms such as Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman, or Cyrus-Beck, which are extensions of the 2-D clipping algorithms to 3-D space.
- 3-D clipping can also be applied to higher dimensions, such as 4-D or 5-D, by using hyperplanes or hyperspheres as clipping regions.
- 3-D clipping can also be used to create effects such as fog, depth of field, or shadows, by modifying the clipping planes or the color and intensity of the clipped fragments.