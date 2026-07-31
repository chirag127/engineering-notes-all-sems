### Depth buffer method

- Depth buffer method, also known as z-buffer method, is an image-space technique for hidden surface removal in computer graphics  .
- It is based on the idea of storing the depth (or z-coordinate) of the closest object at each pixel in a buffer, and comparing the depth of new objects with the existing depth to determine visibility  .
- The depth buffer method has the following steps :
  - Initialize the depth buffer and the frame buffer for each pixel to some predefined values, such as the farthest depth and the background color.
  - For each polygon in the scene, project it onto the view plane and scan-convert it to find the pixels that it covers.
  - For each pixel, calculate the depth of the polygon at that pixel using the plane equation of the polygon.
  - Compare the depth of the polygon with the depth stored in the depth buffer for that pixel. If the polygon depth is smaller (closer to the viewer), then update the depth buffer and the frame buffer with the new depth and color values. Otherwise, discard the pixel.
  - Repeat the above steps for all the polygons in the scene.
  - Display the frame buffer as the final image.
- The depth buffer method has the following advantages  :
  - It is easy to implement, especially in hardware.
  - It can handle any number and type of polygons, including intersecting and transparent ones.
  - It does not require sorting or clipping of polygons.
- The depth buffer method has the following disadvantages  :
  - It requires a large amount of memory to store the depth buffer, which may limit the resolution or precision of the depth values.
  - It may suffer from aliasing or jagged edges, due to the discrete nature of pixels and depth values.
  - It may produce incorrect results for some cases, such as coplanar polygons or self-intersecting polygons.