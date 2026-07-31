## Unit 1 - Introduction and Line Generation

- This unit introduces the basic concepts and techniques of computer graphics, such as pixels, coordinates, primitives, rasterization, and interpolation.
- It also covers the algorithms for generating lines, circles, and other curves on a raster display, such as DDA, Bresenham's, and Midpoint algorithms.
- The objectives of this unit are to:
  - Understand the fundamentals of computer graphics and its applications.
  - Learn how to represent and manipulate graphical objects using pixels and coordinates.
  - Learn how to draw lines, circles, and curves using different algorithms and compare their advantages and disadvantages.
  - Implement the line generation algorithms in a programming language of your choice.

### Pixels and Coordinates
- A pixel (short for picture element) is the smallest unit of a digital image that can be displayed on a screen or printed on a paper.
- A pixel has a color and a position on a two-dimensional grid called the raster.
- The raster is composed of rows and columns of pixels, and each pixel has a unique address given by its row and column numbers, or coordinates.
- The coordinates of a pixel are usually denoted by (x, y), where x is the column number and y is the row number, starting from the top-left corner of the raster.
- The size of the raster is determined by the resolution of the display device, which is the number of pixels per unit length, such as pixels per inch (ppi) or dots per inch (dpi).
- The higher the resolution, the more pixels can be displayed, and the sharper and smoother the image will appear.
- However, higher resolution also requires more memory and processing power to store and manipulate the pixels.

### Primitives and Rasterization
- A primitive is a basic graphical object that can be used to create more complex shapes and images, such as points, lines, circles, polygons, etc.
- Rasterization is the process of converting a primitive from its mathematical representation (such as an equation or a set of vertices) to a set of pixels on the raster that approximate its shape and color.
- Rasterization is also known as scan conversion, because it involves scanning the primitive and determining which pixels are inside or on the boundary of the primitive, and assigning them appropriate colors.
- Rasterization is one of the most fundamental and important tasks in computer graphics, because it allows us to display any graphical object on a screen or a printer.
- However, rasterization also introduces some challenges and limitations, such as aliasing, sampling, and quantization errors.

### Interpolation
- Interpolation is a technique of estimating the values of a function at intermediate points, given the values of the function at some known points.
- Interpolation is useful for rasterization, because it allows us to calculate the color and position of the pixels that lie between the known points of a primitive, such as the endpoints of a line or the vertices of a polygon.
- Interpolation can be done using different methods, such as linear, polynomial, or spline interpolation, depending on the degree and smoothness of the function.
- Interpolation can also be done in different dimensions, such as one-dimensional (1D) interpolation for lines, two-dimensional (2D) interpolation for polygons, or three-dimensional (3D) interpolation for surfaces.

### Line Generation Algorithms
- A line is one of the simplest and most common primitives in computer graphics, and it can be defined by two endpoints, or by a slope and an intercept, or by a parametric equation.
- A line can also be represented by a linear function, such as y = mx + b, where m is the slope and b is the intercept, or by a vector equation, such as P = P0 + tD, where P0 is the starting point, D is the direction vector, and t is the parameter.
- To rasterize a line, we need to find the pixels that are closest to the ideal line, and assign them the color of the line.
- There are several algorithms for generating lines on a raster display, such as the Digital Differential Analyzer (DDA) algorithm, the Bresenham's algorithm, and the Midpoint algorithm.
- These algorithms differ in their accuracy, efficiency, and simplicity, and they have different advantages and disadvantages for different types of lines, such as horizontal, vertical, diagonal, or arbitrary lines.