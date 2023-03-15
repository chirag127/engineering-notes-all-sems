## Unit 1 - Introduction and Line Generation

- Computer graphics is the field of study that deals with the creation, manipulation, and display of images using computers.
- Computer graphics can be used for various applications, such as entertainment, education, simulation, design, and visualization.
- Computer graphics can be classified into two types: raster graphics and vector graphics.
  - Raster graphics are composed of pixels, which are discrete units of color that form a grid on the screen. Raster graphics are also called bitmap graphics or pixel graphics.
  - Vector graphics are composed of geometric primitives, such as points, lines, curves, and polygons, that are defined by mathematical equations. Vector graphics are also called object-oriented graphics or geometric graphics.
- A line is one of the simplest and most fundamental geometric primitives in computer graphics. A line can be defined by two endpoints, or by a point and a direction, or by a slope and an intercept.
- Line generation is the process of determining the pixels that approximate a line on a raster display. Line generation algorithms should be efficient, accurate, and consistent.
- There are various line generation algorithms, such as:
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the x and y coordinates of the pixels along the line. It is simple, but it may cause rounding errors and it requires floating-point arithmetic.
  - Bresenham's algorithm: This algorithm uses an error term to decide whether to increment the x or y coordinate of the pixel along the line. It is faster, more accurate, and more consistent than the DDA algorithm, and it only requires integer arithmetic.
  - Midpoint algorithm: This algorithm uses the midpoint of the two possible pixels along the line to decide which one to choose. It is similar to Bresenham's algorithm, but it can be generalized to draw other geometric primitives, such as circles and ellipses.