## Unit 1 - Introduction and Line Generation

- Computer graphics is the field of study that deals with the creation, manipulation, and display of images using computers.
- Computer graphics can be used for various applications, such as entertainment, education, simulation, visualization, design, and communication.
- Computer graphics can be classified into two types: raster graphics and vector graphics.
  - Raster graphics are composed of pixels, which are discrete units of color information arranged in a grid. Raster graphics are commonly used for digital images, such as photographs and paintings.
  - Vector graphics are composed of geometric primitives, such as points, lines, curves, and polygons, which are defined by mathematical equations. Vector graphics are commonly used for diagrams, logos, fonts, and animations.
- A line is one of the basic geometric primitives in computer graphics. A line can be defined by two endpoints, or by a point and a direction, or by a slope and an intercept.
- A line can be drawn on a raster display using various algorithms, such as DDA, Bresenham's, and Xiaolin Wu's.
  - DDA (Digital Differential Analyzer) is a simple algorithm that uses incremental calculations to determine the pixel coordinates of a line. It can handle any slope, but it may produce gaps or jagged edges due to rounding errors.
  - Bresenham's algorithm is an improvement over DDA that uses integer arithmetic and error terms to eliminate rounding errors and gaps. It can handle slopes between 0 and 1, but it needs to be modified for other slopes.
  - Xiaolin Wu's algorithm is a more advanced algorithm that uses subpixel accuracy and antialiasing techniques to produce smooth and realistic lines. It can handle any slope, but it is more complex and computationally expensive than DDA and Bresenham's.