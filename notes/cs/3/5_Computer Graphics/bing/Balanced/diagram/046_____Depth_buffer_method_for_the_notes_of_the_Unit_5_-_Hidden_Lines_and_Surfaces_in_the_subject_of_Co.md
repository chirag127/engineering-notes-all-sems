### Depth buffer method

- Depth buffer method, also known as z-buffer method, is an image-space technique for hidden surface removal in computer graphics  .
- It is based on the idea of storing the depth or z-coordinate of each pixel in a buffer, and comparing it with the depth of the incoming polygon fragment  .
- If the depth of the fragment is less than or equal to the depth of the pixel, it means the fragment is closer to the viewer and should be visible. In that case, the pixel color and depth are updated with the fragment color and depth  .
- If the depth of the fragment is greater than the depth of the pixel, it means the fragment is behind the pixel and should be occluded. In that case, the pixel color and depth are not changed  .
- The depth buffer method is simple, fast, and easy to implement in hardware. It can handle any number of polygons and any polygon shape  .
- However, the depth buffer method also has some limitations, such as:
  - It requires a large amount of memory to store the depth buffer, which may not be available on some devices  .
  - It may suffer from aliasing or jagged edges, due to the discrete nature of the pixel grid  .
  - It may not handle transparency or overlapping polygons correctly, as it only stores one depth value per pixel  .
  - It may not work well with perspective projection, as the depth values are not linearly distributed in the image space  .

The following diagram illustrates the depth buffer method:

![Depth buffer method diagram](https://www.geeksforgeeks.org/wp-content/uploads/Depth-Buffer-Method.png)

: Z-Buffer or Depth-Buffer method - GeeksforGeeks
: Z-buffering - Wikipedia
: Computer Graphics Z-Buffer Algorithm - javatpoint