## Unit 1 - Introduction and Line Generation

- Computer graphics is the field of study that deals with the creation, manipulation, and display of images using computers.
- Computer graphics can be used for various applications, such as entertainment, education, simulation, visualization, design, and communication.
- Computer graphics can be classified into two types: raster graphics and vector graphics.
  - Raster graphics are composed of pixels, which are small dots of color arranged in a grid. Each pixel has a specific color and location on the screen. Raster graphics are commonly used for digital photos, videos, and games.
  - Vector graphics are composed of geometric primitives, such as points, lines, curves, and polygons. Each primitive has a mathematical description and can be transformed, scaled, rotated, and colored. Vector graphics are commonly used for logos, fonts, diagrams, and illustrations.
- Line generation is one of the basic tasks in computer graphics, as lines are used to draw other shapes and objects.
- Line generation algorithms are methods to determine which pixels should be turned on to display a line segment on a raster screen.
- Line generation algorithms should be efficient, accurate, and consistent. They should also avoid aliasing, which is the jagged appearance of lines due to the discrete nature of pixels.
- Some of the common line generation algorithms are:
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the next pixel along the line. It is simple, but can be slow and inaccurate due to rounding errors.
  - Bresenham's algorithm: This algorithm uses integer arithmetic and decision variables to determine the next pixel along the line. It is faster and more accurate than DDA, but can only handle lines with slopes between 0 and 1.
  - Midpoint algorithm: This algorithm uses the midpoint of the line segment to decide which pixel to turn on next. It is similar to Bresenham's algorithm, but can handle lines with any slope and can be extended to draw circles and ellipses.