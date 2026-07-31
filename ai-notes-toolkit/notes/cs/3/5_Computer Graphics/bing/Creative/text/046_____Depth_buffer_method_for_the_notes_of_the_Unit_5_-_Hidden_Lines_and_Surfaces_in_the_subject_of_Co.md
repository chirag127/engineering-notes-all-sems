### Depth buffer method

- Depth buffer method, also known as z-buffer method, is an image-space technique for hidden surface removal in computer graphics  .
- It is based on the idea of storing the depth (or z-coordinate) of the closest object at each pixel in a buffer, and comparing the depth of new objects with the existing depth to determine visibility  .
- The depth buffer method has the following steps :
  - Initialize the depth buffer and the frame buffer for each pixel to some predefined values, such as the maximum depth and the background color.
  - For each polygon in the scene, project it onto the view plane and scan-convert it to find the pixels that it covers.
  - For each pixel, calculate the depth of the polygon at that pixel using the plane equation.
  - Compare the depth of the polygon with the depth stored in the depth buffer for that pixel. If the polygon depth is smaller, it means the polygon is closer to the viewer and should be visible. In that case, update the depth buffer and the frame buffer with the new depth and color values. Otherwise, ignore the polygon and move on to the next pixel.
  - Repeat the above steps for all the polygons in the scene.
  - Display the frame buffer as the final image.
- The depth buffer method has some advantages and disadvantages :
  - Advantages:
    - It is easy to implement and can be done in hardware or software.
    - It can handle any number of polygons and any polygon shape, including concave and intersecting polygons.
    - It does not require sorting or clipping of polygons, which can be costly and complex.
  - Disadvantages:
    - It requires a large amount of memory to store the depth buffer, which can be a bottleneck for high-resolution images.
    - It can cause aliasing artifacts, such as jagged edges and popping, due to the discrete nature of pixels and depth values.
    - It does not handle transparency or anti-aliasing well, which may require additional techniques such as alpha blending or A-buffer method.