## Unit 1 - Introduction and Line Generation

- Computer graphics is the field of study that deals with the creation, manipulation, and display of images using computers.
- Computer graphics can be used for various applications, such as entertainment, education, engineering, medicine, art, and science.
- Computer graphics can be classified into two types: raster graphics and vector graphics.
- Raster graphics are composed of pixels, which are small dots of color arranged in a grid. Raster graphics are commonly used for digital photos, videos, and games.
- Vector graphics are composed of geometric primitives, such as points, lines, curves, and polygons. Vector graphics are commonly used for logos, diagrams, fonts, and illustrations.
- Line generation is one of the basic operations in computer graphics, as lines are used to draw other shapes and objects.
- Line generation algorithms are methods to determine which pixels should be turned on to display a line on a raster screen.
- Line generation algorithms should be efficient, accurate, and consistent. They should also avoid aliasing, which is the jagged appearance of lines due to pixelation.
- Some of the common line generation algorithms are:
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the next pixel position along the line. It is simple, but may be slow and inaccurate due to rounding errors.
  - Bresenham's algorithm: This algorithm uses integer arithmetic and decision variables to determine the next pixel position along the line. It is faster and more accurate than DDA, but may be more complex to implement.
  - Midpoint algorithm: This algorithm uses the midpoint of the line segment between two pixels to decide which pixel to turn on next. It is similar to Bresenham's algorithm, but may be easier to generalize to other shapes, such as circles and ellipses.