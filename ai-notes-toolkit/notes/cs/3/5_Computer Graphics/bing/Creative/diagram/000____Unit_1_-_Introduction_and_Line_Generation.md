## Unit 1 - Introduction and Line Generation

- This unit introduces the basic concepts and techniques of computer graphics, such as pixels, coordinates, primitives, rasterization, and interpolation.
- It also covers the algorithms for generating lines, circles, and other curves on a raster display, such as DDA, Bresenham's, and Midpoint algorithms.
- The objectives of this unit are to:
  - Understand the fundamentals of computer graphics and its applications.
  - Learn how to represent and manipulate graphical objects using pixels and coordinates.
  - Learn how to draw lines, circles, and curves using various algorithms and compare their advantages and disadvantages.
  - Implement the line and circle generation algorithms in a programming language of your choice.

### Pixels and Coordinates

- A pixel (short for picture element) is the smallest unit of a digital image that can be displayed on a screen. It is usually a square or a rectangle with a single color.
- A coordinate system is a way of assigning numerical values to the position of a pixel on the screen. The most common coordinate system is the Cartesian system, where the origin (0,0) is at the lower-left corner of the screen, and the x-axis and y-axis are horizontal and vertical, respectively.
- A graphical object, such as a line, a circle, or a polygon, can be represented by a set of pixels that have the same color or intensity. For example, a line can be represented by a sequence of pixels that are connected by straight or diagonal segments.
- A raster display is a type of display that uses pixels to form images. A raster display has a finite resolution, which is the number of pixels per unit length. The resolution affects the quality and smoothness of the images.

### Primitives and Rasterization

- A primitive is a basic graphical object that can be drawn on a raster display, such as a point, a line, a circle, or a polygon. Primitives are the building blocks of more complex graphical objects and scenes.
- Rasterization is the process of converting a primitive from its mathematical or geometric representation to a set of pixels on the raster display. For example, rasterizing a line means finding the pixels that lie on or near the line.
- Rasterization involves two steps: sampling and quantization. Sampling is the process of finding the points on the primitive that correspond to the pixel positions on the raster display. Quantization is the process of assigning a color or intensity value to each pixel based on the sampled point.
- Rasterization is affected by the resolution of the raster display and the aliasing effect. Aliasing is the distortion or jaggedness of the primitive due to the discrete nature of the pixels. Aliasing can be reduced by using anti-aliasing techniques, such as smoothing or filtering.

### Interpolation

- Interpolation is the process of finding intermediate values between two given values. Interpolation is useful for rasterizing primitives that are not aligned with the pixel grid, such as lines, circles, and curves.
- There are different types of interpolation methods, such as linear, polynomial, and trigonometric interpolation. Linear interpolation is the simplest and most common method, where the intermediate value is calculated by a linear function of the two given values.
- For example, linear interpolation can be used to rasterize a line segment with endpoints (x0,y0) and (x1,y1) by using the equation y = y0 + (y1 - y0) * (x - x0) / (x1 - x0), where x and y are the coordinates of the intermediate point on the line.
- Linear interpolation can also be used to rasterize a circle with center (xc,yc) and radius r by using the parametric equation x = xc + r * cos(t) and y = yc + r * sin(t), where t is the angle of the point on the circle. By varying t from 0 to 2π, we can obtain the points on the circle and rasterize them using linear interpolation.