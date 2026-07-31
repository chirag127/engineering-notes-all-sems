## Unit 5 - Hidden Lines and Surfaces

- Hidden lines and surfaces are used to represent the parts of an object that are not visible from a given viewpoint.
- Hidden lines are usually drawn as dashed or dotted lines on a 2D drawing or a 3D model.
- Hidden surfaces are usually removed or shaded differently on a 3D model or a rendering.
- The purpose of hidden lines and surfaces is to show the shape and structure of an object more clearly and completely, and to avoid ambiguity or confusion.
- There are different methods and algorithms to determine and draw hidden lines and surfaces, such as:
  - Ray casting: tracing rays from the viewpoint to the object and finding the nearest visible surface along each ray.
  - Z-buffering: storing the depth or distance of each pixel on the screen and comparing it with the depth of the object at that pixel.
  - Painter's algorithm: sorting the surfaces of the object from back to front and drawing them in that order, overwriting the previous surfaces.
  - Scan-line algorithm: dividing the screen into horizontal scan lines and finding the visible segments of each surface along each scan line.
  - BSP trees: partitioning the space and the object into convex regions using binary space partitioning trees and traversing the tree in a back-to-front or front-to-back order.
- Some advantages and disadvantages of these methods are:
  - Ray casting: simple and easy to implement, but slow and inefficient for complex objects and scenes.
  - Z-buffering: fast and efficient, but requires a lot of memory and does not handle transparency or overlapping surfaces well.
  - Painter's algorithm: handles transparency and overlapping surfaces well, but requires sorting and may cause artifacts or errors if the surfaces are not properly ordered.
  - Scan-line algorithm: faster than ray casting and does not require sorting, but does not handle transparency or overlapping surfaces well.
  - BSP trees: handles transparency and overlapping surfaces well, and does not require sorting or depth comparison, but requires a lot of preprocessing and may cause artifacts or errors if the surfaces are not properly partitioned.