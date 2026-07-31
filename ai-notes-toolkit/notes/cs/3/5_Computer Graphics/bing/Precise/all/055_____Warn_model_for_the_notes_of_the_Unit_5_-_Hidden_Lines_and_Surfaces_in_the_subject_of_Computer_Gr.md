# Unit 5 - Hidden Lines and Surfaces

The Warn model is a technique used in computer graphics to remove hidden lines and surfaces from a 3D model. This technique is also known as hidden surface removal or visible surface determination. Here are some key points to remember about the Warn model:

1. The Warn model is an image-space algorithm, meaning that it operates on the 2D projection of the 3D model.
2. The algorithm works by dividing the image into a grid of small rectangular cells, called pixels.
3. For each pixel, the algorithm determines which object or surface is closest to the viewer and should be visible.
4. The algorithm uses a depth buffer, also known as a z-buffer, to store the depth information for each pixel.
5. The depth buffer is initialized with the maximum possible depth value for each pixel.
6. As the algorithm processes each object or surface, it updates the depth buffer with the depth of the visible surface at each pixel.
7. Once all objects and surfaces have been processed, the depth buffer contains the final image, with hidden lines and surfaces removed.

The Warn model is a simple and efficient technique for hidden surface removal, but it has some limitations. For example, it can only handle opaque objects and does not support transparency or reflections. Additionally, the algorithm can suffer from aliasing artifacts, where jagged edges appear on the final image due to the limited resolution of the depth buffer. Despite these limitations, the Warn model remains a popular technique for hidden surface removal in computer graphics.