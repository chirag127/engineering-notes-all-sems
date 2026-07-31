

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



# Types of computer graphics

Computer graphics are the visual representation of data and information using digital devices such as computers, monitors, printers, scanners, etc. Computer graphics can be used for various purposes such as education, entertainment, art, design, engineering, simulation, etc.

There are different types of computer graphics based on how they are created, stored, and displayed. Some of the common types are:

- **Raster graphics**: These are made up of pixels, which are small dots of color arranged in a grid. Each pixel has a specific color and brightness value. Raster graphics are also known as bitmap images. They are commonly used for photographs, digital paintings, icons, etc. Raster graphics have a fixed resolution and size, which means they can lose quality when scaled or zoomed. Some of the popular file formats for raster graphics are JPEG, PNG, GIF, BMP, etc.   

- **Vector graphics**: These are made up of paths, which are defined by mathematical equations. Paths can be lines, curves, shapes, etc. Vector graphics are also known as scalable graphics. They are commonly used for logos, diagrams, fonts, illustrations, etc. Vector graphics have a flexible resolution and size, which means they can retain quality when scaled or zoomed. Some of the popular file formats for vector graphics are SVG, EPS, PDF, AI, etc.    

- **3D graphics**: These are made up of polygons, which are flat surfaces that form a 3D shape. Each polygon has a color, texture, and lighting effect. 3D graphics are also known as computer-generated imagery (CGI). They are commonly used for animation, video games, movies, virtual reality, etc. 3D graphics require special software and hardware to create and render. Some of the popular file formats for 3D graphics are OBJ, STL, FBX, GLTF, etc.  

- **Animated graphics**: These are made up of a sequence of images or frames that create the illusion of motion. Animated graphics can be either raster or vector based. They are commonly used for cartoons, web pages, presentations, etc. Animated graphics require special software and hardware to create and play. Some of the popular file formats for animated graphics are GIF, APNG, WEBP, MP4, etc.



# Graphic Displays for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Graphic displays are devices that can show images or graphics on a screen or other surface.
- Graphic displays are used for various purposes, such as presenting information, visualizing data, creating art, playing games, and so on.
- Graphic displays can be classified into different types based on their technology, such as CRT, LCD, LED, OLED, plasma, etc.
- Graphic displays can also be categorized based on their characteristics, such as resolution, aspect ratio, color depth, refresh rate, contrast ratio, brightness, etc  .
- Graphic displays can be connected to a computer or other device through various interfaces, such as VGA, HDMI, DVI, DisplayPort, USB, etc.
- Graphic displays require a graphics processing unit (GPU) to generate and render the images or graphics on the screen.
- A GPU is a specialized hardware component that can perform complex mathematical operations and parallel processing to create realistic and detailed graphics.
- A GPU can be integrated into the CPU (such as Intel, AMD, or ARM) or discrete (such as NVIDIA or AMD) depending on the performance and power consumption requirements.
- A GPU can also be classified into different types based on its architecture, such as rasterization, ray tracing, or hybrid.
- A GPU can support various graphics APIs, such as OpenGL, DirectX, Vulkan, Metal, etc, that provide a standard way of communicating with the graphics hardware and software.
- A GPU can also support various graphics features, such as anti-aliasing, anisotropic filtering, texture mapping, lighting, shading, etc, that enhance the quality and realism of the graphics.
- Line generation is one of the basic and fundamental tasks in computer graphics, as it is used to draw shapes, curves, and edges.
- Line generation algorithms are methods that can determine the pixels that form a line between two given points on a graphic display.
- Line generation algorithms can be classified into different types based on their accuracy, efficiency, and simplicity, such as DDA, Bresenham, midpoint, etc.
- Line generation algorithms can also be modified or extended to draw other geometric primitives, such as circles, ellipses, polygons, etc.



# Random Scan Displays

- Random scan displays are also known as **vector displays** or **stroke-writing displays** or **calligraphic displays**  .
- Random scan displays are used to draw a picture **one line at a time** and are thus also referred to as **line-drawing displays**  .
- Random scan displays use a **cathode ray tube (CRT)** that directs the beam of an electron only to those areas of the screen where a picture has to be drawn  .
- Random scan displays can draw and refresh component lines of a picture in any specified sequence.
- Random scan displays produce **smooth line drawings** and have **high resolution**.
- Random scan displays are suitable for applications that require **line drawings** such as **engineering drawings** and **computer-aided design (CAD)**  .
- Random scan displays cannot display realistic shades or scenes.
- Random scan displays require a **display processor** or a **display file** to store the line coordinates and refresh the screen .
- Random scan displays have a **refresh rate** that depends on the number and complexity of lines .
- Random scan displays are more expensive and less common than raster scan displays  .



# Raster scan displays

- Raster scan displays are the most common type of graphics monitor that use a cathode ray tube (CRT) to display images on a screen  .
- A raster scan display works by scanning an electron beam across the screen from top to bottom, one row at a time  .
- The electron beam is turned on and off to create a pattern of illuminated spots (pixels) on the screen  .
- The resolution of a raster scan display depends on the number of pixels on the screen and the number of colors that each pixel can display .
- The refresh rate of a raster scan display is the number of times the screen is redrawn per second. A higher refresh rate reduces flickering and improves the quality of animation and video .
- Raster scan displays are suitable for displaying realistic images, complex shapes, and various colors, but they have some limitations, such as:
  - They require a large amount of memory to store the pixel values .
  - They are slow to update the screen when the image changes .
  - They cannot display sharp lines or curves without aliasing or jagged edges .



# Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- A video controller may also perform other functions, such as graphics acceleration, video decoding, or cursor generation.

## Features of frame buffer and video controller

- The frame buffer is the size of the maximum image that can be displayed, and it may be a separate memory bank on the graphics card, GPU or a reserved part of regular memory.
- The frame buffer can store different types of information, such as color, depth, alpha, stencil, or multisample values.
- The frame buffer can be accessed by the CPU or the GPU, depending on the system architecture and the graphics API.
- The video controller can support different modes of operation, such as text, graphics, or video.
- The video controller can also support different resolutions, color depths, refresh rates, and scan formats.
- The video controller can interface with different types of monitors, such as CRT, LCD, or OLED.

## Applications of frame buffer and video controller

- Frame buffer and video controller are essential components of any computer graphics system, as they enable the display of images on the screen.
- Frame buffer and video controller are also used in other domains, such as video games, multimedia, digital signage, or virtual reality.
- Frame buffer and video controller can enhance the performance and quality of the graphics output, by providing features such as double buffering, hardware acceleration, or anti-aliasing.
- Frame buffer and video controller can also enable the interaction and manipulation of the graphics output, by providing features such as overlay, cursor, or touch input .



# Points and lines for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A point is the simplest graphical element that can be displayed on a screen. It is represented by a pair of coordinates (x, y) that specify its position on a two-dimensional plane.
- A line is a sequence of points that are connected by straight or curved segments. It is represented by two endpoints (x1, y1) and (x2, y2) that specify the start and end of the line, or by a slope-intercept equation y = mx + b that specifies the direction and position of the line.
- Lines are used to draw shapes, curves, boundaries, and other graphical elements. They are also the basis for many algorithms in computer graphics, such as clipping, rasterization, and anti-aliasing.
- There are different methods to generate lines on a screen, depending on the type of display device and the desired quality and efficiency of the output. Some of the common methods are:

  - DDA algorithm: This algorithm uses the concept of digital differential analyzer to incrementally calculate the intermediate points along a line. It is simple and fast, but it may produce round-off errors and unevenly spaced points.
  - Bresenham's algorithm: This algorithm uses the concept of decision variables to determine the next point along a line. It is more accurate and efficient than the DDA algorithm, as it avoids floating-point arithmetic and produces evenly spaced points.
  - Midpoint algorithm: This algorithm uses the concept of midpoint to determine the next point along a line. It is similar to Bresenham's algorithm, but it can handle lines with any slope and can be extended to draw circles and ellipses.
  - Wu's algorithm: This algorithm uses the concept of anti-aliasing to smooth the jagged edges of a line. It assigns different intensities to the pixels along a line, based on their distance from the ideal line. It is more complex and slower than the previous algorithms, but it produces higher quality output.



# Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A line drawing algorithm is a method for estimating a line segment on discrete graphical media such as pixel-based screens and printers in computer graphics.
- A line segment is defined by two endpoints, each with an x and y coordinate.
- To draw a line, a computer must work out which pixels need to be filled so that the line looks straight.
- There are different algorithms for drawing a line, each with different advantages and disadvantages in terms of accuracy, efficiency, and simplicity.
- Some of the common line drawing algorithms are:

  - Naive algorithm: This algorithm simply uses the slope-intercept form of the equation of a line (y = mx + b) to calculate the y coordinate for each x coordinate along the line. However, this algorithm is inefficient and inaccurate, as it involves floating-point arithmetic, rounding errors, and gaps or overlaps in the line.
  - Digital Differential Analyzer (DDA) algorithm: This algorithm is similar to the naive algorithm, but it uses integer arithmetic and avoids multiplication and division by incrementing the x and y coordinates by a small amount in each step. This algorithm is faster and more accurate than the naive algorithm, but it still suffers from rounding errors and pixel gaps .
  - Bresenham's line algorithm: This algorithm is an optimized version of the DDA algorithm, which uses only integer arithmetic and avoids multiplication and division by using a decision variable to determine whether to increment the x or y coordinate in each step. This algorithm is faster and more accurate than the DDA algorithm, and it produces a smooth line with no gaps .
  - Mid-point line algorithm: This algorithm is another variation of the DDA algorithm, which uses a mid-point between the current pixel and the next pixel to decide whether to increment the x or y coordinate in each step. This algorithm is also faster and more accurate than the DDA algorithm, and it produces a smooth line with no gaps.



# Circle Generating Algorithms

A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm. A circle generation algorithm is an algorithm used to create a circle on a computer screen. It is used in various applications such as computer-aided design (CAD) software, animation software, games, and scientific visualization.

There are several algorithms used for generating circles on a computer screen, but the most popular ones are:

- **Bresenham's Algorithm**: This algorithm is based on the idea of drawing a circle using eight-way symmetry and using only integer arithmetic. It is efficient and simple to implement. It works by determining the next pixel to be plotted based on the previous pixel and the decision parameter, which is the difference between the actual distance of the pixel from the center and the ideal distance (radius). 

- **Midpoint Circle Algorithm**: This algorithm is similar to Bresenham's algorithm, but it uses the midpoint of the two possible pixels as the decision parameter. It is also based on eight-way symmetry and integer arithmetic. It works by computing the initial value of the decision parameter and then updating it for each pixel based on whether the midpoint is inside or outside the circle. It is more accurate than Bresenham's algorithm, but slightly more complex. 

The following are the steps for both algorithms:

- Step 1: Input the center coordinates (h, k) and the radius r of the circle.
- Step 2: Initialize the starting point (x, y) as (0, r).
- Step 3: Initialize the decision parameter d as 3 - 2r for Bresenham's algorithm and 1 - r for Midpoint Circle Algorithm.
- Step 4: Plot the initial point (h + x, k + y) and its symmetric points using eight-way symmetry.
- Step 5: Repeat the following steps until x >= y:
  - Step 5.1: If d < 0, then the next point is (x + 1, y) and the new value of d is d + 4x + 6 for Bresenham's algorithm and d + 2x + 3 for Midpoint Circle Algorithm.
  - Step 5.2: If d >= 0, then the next point is (x + 1, y - 1) and the new value of d is d + 4(x - y) + 10 for Bresenham's algorithm and d + 2(x - y) + 5 for Midpoint Circle Algorithm.
  - Step 5.3: Plot the new point and its symmetric points using eight-way symmetry.
  - Step 5.4: Increment x by 1 and decrement y by 1 if d >= 0.

The following are the pseudocodes for both algorithms:

```
// Bresenham's Algorithm
Input: center (h, k), radius r
Output: circle pixels

x = 0
y = r
d = 3 - 2r

Plot (h + x, k + y) and its symmetric points

While x < y
  If d < 0
    x = x + 1
    d = d + 4x + 6
  Else
    x = x + 1
    y = y - 1
    d = d + 4(x - y) + 10
  End If
  Plot (h + x, k + y) and its symmetric points
End While
```

```
// Midpoint Circle Algorithm
Input: center (h, k), radius r
Output: circle pixels

x = 0
y = r
d = 1 - r

Plot (h + x, k + y) and its symmetric points

While x < y
  If d < 0
    x = x + 1
    d = d + 2x + 3
  Else
    x = x + 1
    y = y - 1
    d = d + 2(x - y) + 5
  End If
  Plot (h + x, k + y) and its symmetric points
End While
```

The following are the diagrams for both algorithms:

Bresenham's Algorithm



![Midpoint Circle Algorithm](https://www.ge



# Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle. It is based on the midpoint theorem which states that if the points along the circumference of a circle are equidistant from the center of the circle, then the points will lie on the circle  .

The algorithm works as follows:

- Start with the point (0, r) on the x-axis, where r is the radius of the circle.
- Calculate the initial decision parameter p0 as 1 - r.
- For each point (xk, yk) in the first octant of the circle, do the following:
  - Plot the point (xk, yk) and its symmetric points in the other seven octants.
  - If pk < 0, then the next point is (xk+1, yk) and pk+1 = pk + 2xk+1 + 1.
  - If pk >= 0, then the next point is (xk+1, yk-1) and pk+1 = pk + 2xk+1 + 1 - 2yk+1.
  - Repeat until xk >= yk.

The algorithm can be generalized to conic sections.

The following diagram illustrates the algorithm for a circle with radius 5:

Mid-point circle generating algorithm

: https://www.geeksforgeeks.org/computer-graphics-circle-generation-algorithm/
: https://www.geeksforgeeks.org/mid-point-circle-drawing-algorithm/
: https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
: https://www.gatevidyalay.com/mid-point-circle-drawing-algorithm/



# Parallel Algorithms for Line Generation in Computer Graphics

- Line generation is a fundamental task in computer graphics, as it is used to draw curves, polygons, and other shapes.
- A line can be represented by a linear equation of the form `y = mx + b`, where `m` is the slope and `b` is the intercept.
- A line can also be represented by a parametric equation of the form `x = x0 + t*dx` and `y = y0 + t*dy`, where `(x0, y0)` is a point on the line, `dx` and `dy` are the increments along the `x` and `y` axes, and `t` is a parameter that varies from 0 to 1.
- A line can be approximated by a sequence of discrete points on a square grid, such that the distance between the points and the line is minimized.
- There are several algorithms for generating such points, such as the DDA algorithm, the Bresenham algorithm, and the midpoint algorithm.
- These algorithms are sequential, meaning that they generate one point at a time, starting from one endpoint and moving towards the other endpoint.
- Parallel algorithms are algorithms that can generate multiple points at the same time, using multiple processors or cores.
- Parallel algorithms can improve the performance and efficiency of line generation, especially for large or complex lines.
- Parallel algorithms can also exploit the parallelism inherent in the line equation, as each point on the line can be computed independently from the others.
- There are different ways to design parallel algorithms for line generation, depending on the data structure, the communication pattern, and the computation model used.
- Some examples of parallel algorithms for line generation are:

  - The vector prefix sums algorithm, which uses a binary tree of processors to compute the prefix sums of the increments `dx` and `dy`, and then uses them to generate the points on the line.
  - The edge function algorithm, which uses a linear function to represent each edge of a polygon, and then interpolates the function values to determine the pixels inside the polygon.
  - The parallel DDA algorithm, which divides the line into equal segments, and then assigns each segment to a processor that uses the DDA algorithm to generate the points within the segment.
  - The parallel Bresenham algorithm, which divides the line into equal segments, and then assigns each segment to a processor that uses the Bresenham algorithm to generate the points within the segment.
  - The parallel midpoint algorithm, which divides the line into equal segments, and then assigns each segment to a processor that uses the midpoint algorithm to generate the points within the segment.



## Unit 2 - Transformations

A transformation is a change in the position, size, or shape of a figure. There are four types of transformations: translations, reflections, rotations, and dilations.

- A translation is a transformation that moves every point of a figure the same distance and in the same direction. The figure does not change its size or orientation. A translation can be described by a vector, which has a magnitude (length) and a direction.
- A reflection is a transformation that flips a figure over a line of symmetry, called the axis of reflection. The figure and its image are congruent and opposite. A reflection can be described by the equation of the axis of reflection, or by the angle of incidence and the angle of reflection.
- A rotation is a transformation that turns a figure around a fixed point, called the center of rotation. The figure and its image are congruent and have the same orientation. A rotation can be described by the angle of rotation, the direction of rotation (clockwise or counterclockwise), and the center of rotation.
- A dilation is a transformation that changes the size of a figure, but not its shape or orientation. The figure and its image are similar, meaning they have the same angles and proportional sides. A dilation can be described by the scale factor, which is the ratio of the lengths of corresponding sides, and the center of dilation, which is the fixed point that the figure is enlarged or reduced from.



# Basic Transformation for the Notes of the Unit 2 - Transformations in the Subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- Transformations are useful for repositioning and resizing graphics on the screen, as well as for creating animations and effects.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another on the plane. It can be described by a vector that specifies the displacement in the x and y directions. Translation can be performed by adding the displacement vector to the original coordinates of the object.
- Rotation is the turning of an object around a fixed point on the plane. It can be described by an angle that specifies the amount of rotation in the clockwise or counterclockwise direction. Rotation can be performed by multiplying the original coordinates of the object by a rotation matrix that depends on the angle and the point of rotation.
- Scaling is the change of size of an object on the plane. It can be described by a factor that specifies the ratio of the new size to the original size. Scaling can be performed by multiplying the original coordinates of the object by a scaling matrix that depends on the factor and the point of scaling.
- Transformations can be combined to create more complex effects. For example, a rotation followed by a translation is equivalent to a rotation around a different point. A scaling followed by a rotation is equivalent to a rotation followed by a scaling with a different factor. The order of transformations matters, as different orders may produce different results.
- Transformations can be represented by matrices and vectors, which are convenient for performing calculations and storing information. A 2D object can be represented by a vector of its coordinates, such as (x, y). A 2D transformation can be represented by a 2x2 matrix that operates on the vector, such as [[a, b], [c, d]]. The result of the transformation is another vector, such as (x', y').
- The following are some examples of matrices that represent common transformations:

  - Translation by (tx, ty): [[1, 0], [0, 1]] + (tx, ty)
  - Rotation by θ around the origin: [[cos θ, -sin θ], [sin θ, cos θ]]
  - Scaling by sx and sy around the origin: [[sx, 0], [0, sy]]
  - Reflection across the x-axis: [[1, 0], [0, -1]]
  - Reflection across the y-axis: [[-1, 0], [0, 1]]
  - Shearing along the x-axis by shx: [[1, shx], [0, 1]]
  - Shearing along the y-axis by shy: [[1, 0], [shy, 1]]

- To apply a transformation to an object, we need to multiply the matrix of the transformation by the vector of the object. For example, to rotate an object by 90 degrees around the origin, we need to multiply the matrix [[0, -1], [1, 0]] by the vector (x, y) to get the vector (-y, x).
- To apply multiple transformations to an object, we need to multiply the matrices of the transformations in the reverse order of the transformations. For example, to translate an object by (tx, ty) and then rotate it by θ around the origin, we need to multiply the matrix [[cos θ, -sin θ], [sin θ, cos θ]] by the matrix [[1, 0], [0, 1]] + (tx, ty) and then by the vector (x, y) to get the vector (x'cos θ - y'sin θ, x'sin θ + y'cos θ), where x' = x + tx and y' = y + ty.



# Matrix representations and homogeneous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling, and projection in computer graphics.
- A matrix can be multiplied by a vector to obtain a transformed vector, or by another matrix to obtain a composed transformation.
- Homogeneous coordinates are a way to extend the normal Cartesian coordinates with an extra dimension, usually denoted by w, to allow affine and projective transformations to be represented by matrices.
- Homogeneous coordinates have the property that any multiple of a coordinate vector represents the same point, as long as w is not zero. For example, (x, y, 1) and (2x, 2y, 2) are equivalent in homogeneous coordinates.
- To convert from homogeneous coordinates to Cartesian coordinates, we divide by w. For example, (2x, 2y, 2) becomes (x, y) in Cartesian coordinates.
- To convert from Cartesian coordinates to homogeneous coordinates, we append a 1 as the w component. For example, (x, y) becomes (x, y, 1) in homogeneous coordinates.
- Homogeneous coordinates are useful in computer graphics because they allow us to represent translation, rotation, scaling, and projection as matrix operations, and to compose them easily by matrix multiplication.
- For example, the matrix representation for translation by (tx, ty) in homogeneous coordinates is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- To translate a point (x, y, 1) by (tx, ty), we multiply it by the translation matrix:

| 1  0  tx |   | x |   | x + tx |
| 0  1  ty | * | y | = | y + ty |
| 0  0  1  |   | 1 |   |   1    |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by w (which is 1 in this case).
- Similarly, the matrix representation for rotation by an angle theta in homogeneous coordinates is:

| cos(theta)  -sin(theta)  0 |
| sin(theta)   cos(theta)  0 |
|     0            0       1 |

- To rotate a point (x, y, 1) by an angle theta, we multiply it by the rotation matrix:

| cos(theta)  -sin(theta)  0 |   | x |   | x cos(theta) - y sin(theta) |
| sin(theta)   cos(theta)  0 | * | y | = | x sin(theta) + y cos(theta) |
|     0            0       1 |   | 1 |   |             1               |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by w (which is 1 in this case).
- Similarly, the matrix representation for scaling by (sx, sy) in homogeneous coordinates is:

| sx  0  0 |
| 0  sy  0 |
| 0  0   1 |

- To scale a point (x, y, 1) by (sx, sy), we multiply it by the scaling matrix:

| sx  0  0 |   | x |   | sx x |
| 0  sy  0 | * | y | = | sy y |
| 0  0   1 |   | 1 |   |  1   |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by w (which is 1 in this case).
- Finally, the matrix representation for projection onto a plane with normal vector (a, b, c) and distance d from the origin in homogeneous coordinates is:

| a^2 + b^2  -a c  -a d |
| -a c  c^2 + b^2  -c d |
| -a d  -c d  a^2 + c^2 |

- To project a point (x, y, z, 1) onto the plane, we multiply it by the projection matrix:

| a^2 + b^2  -a c  -a d |   | x |   | (a^2 + b^2) x - a c z - a d |
| -a c  c^2 + b^2



# Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A transformation is a process of changing the position, size, shape, or orientation of an object in a coordinate system.
- A composite transformation is a combination of two or more transformations into a single one that is equivalent to applying the transformations one after another.
- A composite transformation can be represented by a matrix that is obtained by multiplying the matrices of the individual transformations in the order of their application.
- The order of the transformations matters, as some transformations are not commutative, meaning that changing the order of the transformations changes the final result.
- The most common types of transformations in computer graphics are translation, scaling, rotation, and shear.
- Translation is a transformation that moves an object by a given displacement vector without changing its size, shape, or orientation.
- Scaling is a transformation that changes the size of an object by a given scale factor along each axis, without changing its shape or orientation.
- Rotation is a transformation that rotates an object by a given angle around a given axis, without changing its size or shape.
- Shear is a transformation that distorts an object by a given shear factor along a given direction, without changing its size or orientation.
- Composite transformations can be used to perform complex transformations that are not possible with a single transformation, such as rotating an object around an arbitrary point, reflecting an object across an arbitrary line, or projecting an object onto a different plane.



# Reflections and Shearing

Reflections and shearing are two types of transformations in computer graphics that change the position and shape of an object.

## Reflection

Reflection is a transformation that flips an object over a line or a plane, creating a mirror image of the original object. The line or plane is called the mirror line or the mirror plane. The angle of reflection is equal to the angle of incidence, and the distance of the reflected point from the mirror is equal to the distance of the original point from the mirror.

Reflection can be performed in two dimensions or three dimensions. In two dimensions, the mirror line can be horizontal, vertical, or diagonal. In three dimensions, the mirror plane can be xy-plane, yz-plane, xz-plane, or any arbitrary plane.

Reflection can be represented by a matrix multiplication, where the matrix depends on the mirror line or plane. For example, the matrix for reflection over the x-axis in two dimensions is:

```
| 1  0 |
| 0 -1 |
```

The matrix for reflection over the yz-plane in three dimensions is:

```
|-1  0  0 |
| 0  1  0 |
| 0  0  1 |
```

## Shearing

Shearing is a transformation that slants an object in one or two directions, changing the shape of the object. The object is distorted by sliding the layers of the object parallel to a fixed direction. The fixed direction is called the shear direction, and the amount of sliding is called the shear factor.

Shearing can be performed in two dimensions or three dimensions. In two dimensions, the shear direction can be horizontal or vertical, and the shear factor can be positive or negative. In three dimensions, the shear direction can be x, y, or z, and the shear factor can be a pair of values corresponding to the other two axes.

Shearing can also be represented by a matrix multiplication, where the matrix depends on the shear direction and factor. For example, the matrix for shearing in the x-direction with a factor of k in two dimensions is:

```
| 1  k |
| 0  1 |
```

The matrix for shearing in the z-direction with factors of kx and ky in three dimensions is:

```
| 1  0  kx |
| 0  1  ky |
| 0  0  1  |
```



# Windowing and Clipping

Windowing and clipping are two techniques used in computer graphics to display a part of a scene or an object on the screen. They are useful for reducing the computational cost and improving the performance of graphics applications.

## Windowing

- Windowing is the process of selecting and viewing a picture with different views .
- A window is an opening through which part of the outside world can be seen.
- A window can be defined by specifying its coordinates in the world coordinate system or the user coordinate system.
- A window can be moved, resized, rotated, or zoomed to change the view of the picture.
- A window can also be clipped by another window to create a subwindow.

## Clipping

- Clipping is the process of dividing each element of the picture into its visible and invisible portions, allowing the invisible portion to be discarded .
- Clipping is necessary to remove objects, lines, or line segments that are outside the viewing pane or behind the viewer.
- Clipping can also be used to extract a desired part of an object, to create objects using solid modeling, or to perform drawing operations.
- Clipping can be done in different coordinate systems, such as world, user, normalized device, or screen coordinates.
- Clipping can be applied to different types of objects, such as points, lines, polygons, curves, or surfaces.
- Clipping can be done using different algorithms, such as Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman, or Cyrus-Beck.
- Clipping algorithms usually assign a region code for each endpoint of a line or a vertex of a polygon, and then perform logical operations to determine whether the object is inside, outside, or partially inside the clipping window.



# Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert the geometry data of a scene into the image data that can be displayed on a device .
- The viewing pipeline consists of the following stages:
  - Object coordinates: The coordinates of the vertices and primitives that define the objects in the scene.
  - World coordinates: The coordinates of the objects after applying the modeling transformations, such as translation, rotation, scaling, etc. These transformations position and orient the objects in the global coordinate system of the scene.
  - Viewing coordinates: The coordinates of the objects after applying the viewing transformation, which defines the position and orientation of the camera or the eye. This transformation maps the scene to a view volume, which is a region of space that is visible to the camera.
  - Projection coordinates: The coordinates of the objects after applying the projection transformation, which defines the type of projection to be used, such as parallel or perspective. This transformation maps the view volume to a canonical view volume, which is a standard region of space that is independent of the projection type.
  - Normalized device coordinates: The coordinates of the objects after applying the normalization transformation, which scales and translates the canonical view volume to a unit cube with the origin at the center and the range of [-1, 1] for each axis.
  - Device coordinates: The coordinates of the objects after applying the viewport transformation, which maps the unit cube to the physical device coordinate system, such as the screen or the printer. This transformation defines the size and position of the viewport, which is the region of the device where the image is displayed.
- The following diagram illustrates the viewing pipeline for 2D graphics :

2D viewing pipeline

- The following diagram illustrates the viewing pipeline for 3D graphics:

3D viewing pipeline

- The viewing pipeline can be implemented using matrices and vectors, which allow for efficient and compact representation and manipulation of the transformations. The final image data can be obtained by multiplying the object coordinates by the composite transformation matrix, which is the product of the individual transformation matrices in the pipeline.



# Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the processes of mapping the coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are necessary to adjust the position, orientation, and size of the picture to fit the display device and the viewer's preferences .
- Viewing transformations can be divided into two types: projection and windowing .
- Projection is the process of transforming the three-dimensional world coordinates of the picture into two-dimensional eye coordinates that are relative to the viewer's position and direction.
- Projection can be either parallel or perspective, depending on whether the lines of projection are parallel or convergent.
- Parallel projection preserves the relative sizes and shapes of the objects, but does not create the illusion of depth.
- Perspective projection creates the illusion of depth by making the objects appear smaller and closer together as they are farther from the viewer, but distorts the relative sizes and shapes of the objects.
- Windowing is the process of selecting a rectangular region of the eye coordinates, called the window, that contains the part of the picture that the viewer wants to see .
- Windowing is also called clipping, as it removes the objects, lines, or line segments that are outside the window.
- Windowing is followed by mapping the window onto a subregion of the display device, called the viewport, that specifies the area on the screen where the picture will be displayed .
- Windowing can be either uniform or non-uniform, depending on whether the window and the viewport have the same or different aspect ratios.
- Uniform windowing preserves the relative proportions of the objects, but may leave some empty space on the screen or crop some parts of the picture.
- Non-uniform windowing fills the entire screen with the picture, but may stretch or compress the objects horizontally or vertically.
- Windowing can be done by using a simple scaling and translation formula that relates the window and the viewport coordinates.



# 2-D Clipping Algorithms

- Clipping is the process of removing parts of graphics primitives that lie outside a specified region, called the clipping boundary or the clipping window .
- Clipping is useful for optimizing the rendering performance, avoiding unnecessary calculations for invisible objects, and improving the visual quality by removing unwanted artifacts.
- In 2-D, the clipping process can be applied to a variety of graphics primitives such as points, lines, polygons and curves.
- The clipping boundary can be a convex or a concave polygon, or a simple rectangle.
- There are different algorithms for clipping different types of primitives, such as:
  - Point clipping: This algorithm checks whether a given point lies inside or outside the clipping boundary, and discards the point if it is outside .
  - Line clipping: This algorithm finds the intersection points of a given line segment with the clipping boundary, and retains only the part of the line that lies inside the boundary. Some examples of line clipping algorithms are Cohen-Sutherland algorithm, Liang-Barsky algorithm, and Cyrus-Beck algorithm.
  - Polygon clipping: This algorithm clips a given polygon against the clipping boundary, and produces a new polygon or a set of polygons that lie inside the boundary. Some examples of polygon clipping algorithms are Sutherland-Hodgman algorithm, Weiler-Atherton algorithm, and Greiner-Hormann algorithm.
  - Curve clipping: This algorithm clips a given curve, such as a Bézier curve or a B-spline curve, against the clipping boundary, and produces a new curve or a set of curves that lie inside the boundary. Some examples of curve clipping algorithms are Cohen-Sutherland algorithm for parametric curves, and de Casteljau algorithm for Bézier curves.



# Line clipping algorithms

- Line clipping is the process of removing (clipping) lines or portions of lines outside an area of interest (a viewport or view volume) in computer graphics.
- Line clipping is useful for rendering only the visible parts of a scene, reducing the computational cost and improving the performance of graphics applications.
- There are many algorithms for line clipping, but two of the most common ones are Cohen–Sutherland and Liang–Barsky.

## Cohen–Sutherland algorithm

- The Cohen–Sutherland algorithm (named after Danny Cohen and Ivan Sutherland) is a line-clipping algorithm that divides a 2D space into 9 regions, of which only the middle part (viewport) is visible.
- The algorithm assigns a 4-bit code to each endpoint of a line, based on its position relative to the viewport. The code indicates which of the four boundaries (top, bottom, left, right) the point is outside of, or zero if the point is inside the viewport.
- The algorithm then performs a series of tests on the codes to determine if the line is trivially accepted (both endpoints are inside the viewport), trivially rejected (both endpoints are outside the same boundary), or needs to be clipped (one or both endpoints are outside different boundaries).
- If the line needs to be clipped, the algorithm finds the intersection point of the line with the boundary that corresponds to the first non-zero bit in the code, and replaces the endpoint with the intersection point. The algorithm then repeats the process until the line is either accepted or rejected.

## Liang–Barsky algorithm

- The Liang–Barsky algorithm is a line-clipping algorithm that uses a parametric form of the line equation to find the intersection points of the line with the viewport boundaries.
- The algorithm assumes that the line can be represented as P(t) = P0 + t(P1 - P0), where P0 and P1 are the endpoints of the line, and t is a parameter that ranges from 0 to 1.
- The algorithm then computes four values, p, q, r, and s, that represent the coefficients and constants of the inequalities that define the viewport. For example, p = P1x - P0x, q = P0x - xmin, r = p/q, and s = q/p, where xmin is the left boundary of the viewport.
- The algorithm then finds the values of t that satisfy the inequalities, and uses them to determine the intersection points of the line with the viewport. The algorithm then clips the line segment between the minimum and maximum values of t that are within the range of 0 to 1.



# Cohen Sutherland line clipping algorithm

- It is an algorithm used for line clipping in computer graphics.
- Line clipping is the process of removing the portions of a line that are outside a given rectangular region of interest (the viewport).
- The algorithm divides a two-dimensional space into 9 regions: one inside region and eight outside regions.
- Each region is assigned a 4-bit code, called the outcode, based on the position of the region relative to the viewport boundaries.
- The outcode is computed as follows:

  - The first bit is 1 if the region is above the viewport, 0 otherwise.
  - The second bit is 1 if the region is below the viewport, 0 otherwise.
  - The third bit is 1 if the region is to the right of the viewport, 0 otherwise.
  - The fourth bit is 1 if the region is to the left of the viewport, 0 otherwise.

- For example, the outcode for the region above and to the right of the viewport is 1001, and the outcode for the inside region is 0000.
- The algorithm proceeds in three steps:

  - If both endpoints of the line have the same outcode, and it is not 0000, then the line is entirely outside the viewport and can be discarded.
  - If both endpoints of the line have the outcode 0000, then the line is entirely inside the viewport and can be drawn.
  - If the endpoints of the line have different outcodes, then the line may be partially inside the viewport and needs to be clipped. To do this, the algorithm finds an intersection point between the line and one of the viewport boundaries, and replaces the endpoint that is outside the viewport with the intersection point. Then, the algorithm repeats the process with the new line segment until one of the first two cases applies.

- The algorithm is efficient because it avoids unnecessary calculations and comparisons by using the outcode information.
- The algorithm works only for rectangular viewports. For other shapes, other algorithms such as Cyrus-Beck or Sutherland-Hodgman are needed.



# Liang Barsky Algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window.
- The algorithm is based on the parametric equation of a line, which is given by:

  ```
  x = x1 + u * (x2 - x1)
  y = y1 + u * (y2 - y1)
  ```

  where `(x1, y1)` and `(x2, y2)` are the end points of the line, and `u` is a parameter that varies from 0 to 1.
- The algorithm also uses four inequalities that describe the range of the clipping window, which are given by:

  ```
  xwmin <= x <= xwmax
  ywmin <= y <= ywmax
  ```

  where `(xwmin, ywmin)` and `(xwmax, ywmax)` are the lower-left and upper-right corners of the window, respectively.
- The algorithm works by finding the values of `u` that satisfy the four inequalities, and then using the minimum and maximum values of `u` to compute the intersection points of the line and the window.
- The algorithm can be summarized by the following steps:

  1. Initialize `u1 = 0` and `u2 = 1`, which represent the lower and upper bounds of the visible portion of the line.
  2. For each of the four boundaries of the window, calculate the value of `u` that corresponds to the intersection of the line and the boundary, using the following formula:

     ```
     u = (p * q) / (p * r)
     ```

     where `p` and `q` are constants that depend on the boundary and the direction of the line, and `r` is the difference between the end points of the line along the boundary's axis. For example, for the left boundary, `p = x1 - x2`, `q = x1 - xwmin`, and `r = x2 - x1`.
  3. If `p * r < 0`, then the line is entering the window through the boundary. In this case, update `u1 = max(u1, u)`, which means taking the larger value of `u1` and `u`.
  4. If `p * r > 0`, then the line is leaving the window through the boundary. In this case, update `u2 = min(u2, u)`, which means taking the smaller value of `u2` and `u`.
  5. If `p * r = 0`, then the line is parallel to the boundary. In this case, if `q < 0`, then the line is completely outside the window and can be rejected. Otherwise, the line is completely inside the window and can be accepted.
  6. After checking all four boundaries, if `u1 > u2`, then the line is outside the window and can be rejected. Otherwise, the line is inside the window or partially inside the window, and can be accepted.
  7. If the line is accepted, then the visible portion of the line can be drawn by using the values of `u1` and `u2` to calculate the intersection points of the line and the window, using the parametric equation of the line.

- The algorithm is more efficient than the Cohen-Sutherland algorithm, and can be extended to 3-Dimensional clipping. The algorithm is considered to be the faster parametric line-clipping algorithm   .



# Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a window or a viewport.
- Line clipping algorithms can be classified into two categories: rectangular and non-rectangular.
- Rectangular line clipping algorithms, such as Cohen-Sutherland and Liang-Barsky, are efficient and simple, but they can only handle rectangular windows.
- Non-rectangular line clipping algorithms, such as Cyrus-Beck and Sutherland-Hodgman, can handle arbitrary convex or concave polygons as windows, but they are more complex and require more computations.

## Cyrus-Beck Algorithm

- Cyrus-Beck is a line clipping algorithm that is made for convex polygons. It allows line clipping for non-rectangular windows, unlike Cohen-Sutherland or Nicholl Le Nicholl. It also removes the repeated clipping needed in Cohen-Sutherland.
- The algorithm works as follows:

  1. Define the convex area of interest by a set of coordinates given in a clockwise fashion.
  2. Assign a normal vector to each edge of the polygon, pointing outward from the polygon.
  3. For each line to be clipped, calculate the parameter t for each intersection point with the polygon edges, using the formula:

     `t = (P - Pe) . n / D . n`

     where P is any point on the line, Pe is any point on the edge, n is the normal vector of the edge, D is the direction vector of the line, and . is the dot product operator.
  4. Discard the intersection points with t < 0 or t > 1, as they lie outside the line segment.
  5. Discard the intersection points with D . n > 0, as they lie on the wrong side of the edge (inside the polygon).
  6. Sort the remaining intersection points by increasing values of t.
  7. The visible portion of the line is between the first and the last intersection points in the sorted list.

- The algorithm can be extended to handle concave polygons by using the parity rule: a point is inside the polygon if it crosses an odd number of edges to reach infinity.

## Sutherland-Hodgman Algorithm

- Sutherland-Hodgman is a polygon clipping algorithm that can handle any polygon as a window, convex or concave. It clips a polygon against each edge of the window polygon, one at a time, and outputs a new polygon that is inside the window.
- The algorithm works as follows:

  1. Define the window polygon by a set of coordinates given in a clockwise fashion.
  2. Assign a normal vector to each edge of the window polygon, pointing inward from the window.
  3. For each edge of the window polygon, do the following:
     - Initialize an empty list of output vertices.
     - For each edge of the polygon to be clipped, do the following:
       - Let S and P be the start and end points of the edge, respectively.
       - If S is inside the window edge, add S to the output list.
       - If S and P are on opposite sides of the window edge, add the intersection point of the edge and the window edge to the output list.
     - Replace the polygon to be clipped with the output list of vertices.
  4. The final output list of vertices is the clipped polygon.

- The algorithm can be modified to handle non-simple polygons (with self-intersections) by using the even-odd rule: a point is inside the polygon if it crosses an even number of edges to reach infinity.



# Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - To prevent undesirable effects when rendering polygons that extend beyond the output device's window.
  - To perform hidden surface removal and generate realistic 3D images by clipping polygons against other polygons or planes.
  - To produce high-quality surface details using techniques such as beam tracing or texture mapping by clipping polygons against light sources or textures.
  - To distribute the objects of a scene to appropriate processors in multiprocessor ray tracing systems to improve rendering speeds by clipping polygons against the processor's boundaries.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against a convex clipping window by processing each edge of the polygon against each edge of the window in a clockwise order. The output of this algorithm is a sequence of vertices that define the clipped polygon boundaries. This algorithm is simple and efficient, but it can only handle convex clipping windows and it may introduce degenerate cases such as self-intersecting polygons or zero-area polygons.
  - Weiler-Atherton algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersection points between the polygon edges and the window edges, and then tracing the boundary of the clipped polygon by following the intersection points and the original vertices in a clockwise order. The output of this algorithm is a list of polygons that represent the clipped regions. This algorithm can handle concave clipping windows and it preserves the original topology of the polygon, but it is more complex and requires more memory and computation than the Sutherland-Hodgman algorithm.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersection points between the polygon edges and the window edges, and then marking the entry and exit points of the polygon with respect to the window. The output of this algorithm is a list of polygons that represent the clipped regions. This algorithm can handle concave clipping windows and it is faster and simpler than the Weiler-Atherton algorithm, but it may produce incorrect results for self-intersecting polygons or polygons with holes.
- Polygon clipping can be illustrated by the following diagrams:

  - Sutherland-Hodgman algorithm:

  ```
  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  +---------------------+

  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |   +-----------+     |
  |   |           |     |
  |   |           |     |
  |   |           |     |
  +---+-----------+-----+

  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |   +-----------+     |
  |   |           |     |
  |   |           |     |
  |   |           |     |
  |   +-----------+     |
  +---------------------+
  ```

  - Weiler-Atherton algorithm:

  ```
  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  +---------------------+

  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |   +-----+   +---+   |
  |   |     |   |   |   |
  |   |     +---+   |   |
  |   |             |   |
  |   +-------------+   |
  +---------------------+

  +---------------------+
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |                     |
  |   +-----+   +---

```




# Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon, and processes the boundary of the polygon against each window edge.
- For each window edge, the algorithm generates a new list of vertices by iterating over the input list and applying the following rules:
  - If the current vertex is inside the window edge, and the previous vertex is outside, then output the intersection point of the polygon edge and the window edge, followed by the current vertex.
  - If the current vertex is inside the window edge, and the previous vertex is also inside, then output the current vertex.
  - If the current vertex is outside the window edge, and the previous vertex is inside, then output the intersection point of the polygon edge and the window edge.
  - If the current vertex is outside the window edge, and the previous vertex is also outside, then output nothing.
- The output list of vertices becomes the input list for the next window edge, until all four edges are processed.
- The final output list contains the vertices of the clipped polygon, in the same order as the original polygon.

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks



# Weiler and Atherton polygon clipping

- Weiler and Atherton polygon clipping is a polygon clipping algorithm that can handle concave polygons and polygons with holes.
- Polygon clipping is the process of finding the intersection of a polygon and a clipping region, such as a window or a viewport.
- The algorithm works by finding the intersection points of the subject polygon and the clipping polygon, and labeling them as entry or exit points .
- The algorithm then traverses the subject polygon in a clockwise direction, starting from any entry point, and adds the vertices to the output polygon until an exit point is reached .
- The algorithm then switches to the clipping polygon and traverses it in a counter-clockwise direction, adding the vertices to the output polygon until an entry point is reached .
- The algorithm repeats this process until all the entry and exit points are visited, and the output polygon is closed .
- The algorithm can handle multiple output polygons if the subject polygon is split into disjoint parts by the clipping polygon .
- The algorithm can also handle holes in the subject polygon by using a flag to indicate whether a vertex is inside or outside the hole.
- The algorithm is more efficient than the Sutherland-Hodgman algorithm for concave polygons, but it requires more preprocessing and sorting of the intersection points .



# Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping .
- Curve clipping requires more processing than for objects with linear boundaries.
- The region of interest, also called the clip window, can be curved or rectangular in shape.
- There are different algorithms for curve clipping, such as the Bezier clipping algorithm, the B-spline clipping algorithm, and the rational Bezier clipping algorithm.
- The Bezier clipping algorithm is based on the convex hull property of Bezier curves, which states that the curve lies entirely within the convex hull of its control points.
- The B-spline clipping algorithm is based on the convex hull property of B-spline curves, which states that the curve lies entirely within the convex hull of its control polygon.
- The rational Bezier clipping algorithm is based on the perspective projection of rational Bezier curves, which preserves the convex hull property.
- The general steps of curve clipping algorithms are:
  - Divide the curve into segments using the control points or the control polygon.
  - Test each segment against the clip window boundaries.
  - If the segment is entirely inside the clip window, accept it.
  - If the segment is entirely outside the clip window, reject it.
  - If the segment intersects the clip window boundaries, subdivide it and repeat the process.



# Text clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

Text clipping is a process of clipping the string. In this process, we clip the whole character or only some part of it depending on the requirement of the application. Text clipping is useful for removing text that is outside the viewing window or overlapping the window boundary.

There are three methods for text clipping which are listed below:

- All or none string clipping method: In this method, if the whole string is inside the clip window then we consider it. Otherwise, we discard the whole string. This method is simple but may result in loss of information.
- Text clipping method: In this method, we keep the characters of the string that lie inside the clip window and remove all the characters that lie outside the clip window. If a character overlaps the window boundary then we keep that part of the character that lies inside the window and discard that part that lies outside the clip window. This method is more flexible but may result in distorted characters.
- Character clipping method: In this method, we treat each character as a polygon and apply polygon clipping algorithms to clip the character. This method preserves the shape of the characters but may be computationally expensive.

The following diagram illustrates the three methods of text clipping:

text clipping methods

The text clipping methods can be implemented using various techniques such as scan-line algorithms, Cohen-Sutherland algorithm, Sutherland-Hodgman algorithm, etc. The choice of the technique depends on the methods used to generate characters and the requirements of a particular application.



## Unit 3 - Three Dimensional

- This unit covers the concepts and applications of three dimensional geometry, such as vectors, dot product, cross product, lines, planes, and distances.
- A vector is a quantity that has both magnitude and direction. It can be represented by an arrow or a directed line segment.
- The dot product of two vectors is a scalar that measures the angle between them. It is defined as the product of their magnitudes and the cosine of the angle. It can also be computed by multiplying the corresponding components of the vectors and adding them up.
- The cross product of two vectors is a vector that is perpendicular to both of them. It has a magnitude equal to the product of their magnitudes and the sine of the angle between them. It can also be computed by using a determinant with the unit vectors i, j, and k as the first row, and the components of the vectors as the second and third rows.
- A line in three dimensional space can be defined by a point and a direction vector, or by two points. The parametric equations of a line are x = x0 + at, y = y0 + bt, and z = z0 + ct, where (x0, y0, z0) is a point on the line, (a, b, c) is the direction vector, and t is the parameter.
- A plane in three dimensional space can be defined by a point and a normal vector, or by three non-collinear points. The equation of a plane is ax + by + cz = d, where (a, b, c) is the normal vector, and d is the distance from the origin to the plane.
- The distance between a point and a line is the length of the perpendicular segment from the point to the line. It can be found by using the cross product of the direction vector of the line and the vector from a point on the line to the given point, and dividing by the magnitude of the direction vector.
- The distance between a point and a plane is the length of the perpendicular segment from the point to the plane. It can be found by using the dot product of the normal vector of the plane and the vector from a point on the plane to the given point, and dividing by the magnitude of the normal vector.
- The distance between two parallel lines is the distance between any two points on the lines. It can be found by using the cross product of the direction vectors of the lines and the vector from a point on one line to a point on the other line, and dividing by the magnitude of the cross product.
- The distance between two skew lines is the length of the common perpendicular segment between them. It can be found by using the dot product and the cross product of the direction vectors of the lines, and the vector from a point on one line to a point on the other line.



# 3-D Geometric Primitives

- 3-D geometric primitives are basic geometric forms that can be used to model more complex 3-D shapes and objects.
- 3-D geometric primitives can be classified into two categories: standard primitives and extended primitives.
- Standard primitives are simple shapes that can be created by specifying a few parameters, such as length, width, height, radius, etc. Examples of standard primitives are cubes, spheres, cones, cylinders, tori, etc.
- Extended primitives are more complex shapes that can be created by combining or modifying standard primitives, such as lathing, extruding, lofting, etc. Examples of extended primitives are teapots, pyramids, wedges, chamfer boxes, etc.
- 3-D geometric primitives can have different levels of resolution, which determine how smooth or faceted they appear. Resolution can be controlled by adjusting the number of sides, segments, steps, or slices used to define the primitive.
- 3-D geometric primitives can be transformed, modified, or combined using various operations, such as translation, rotation, scaling, Boolean, etc. These operations can change the shape, size, position, orientation, or appearance of the primitive.
- 3-D geometric primitives are the building blocks of 3-D modeling and design, and can be used to create realistic or abstract scenes and objects.



# 3-D Object Representation

- 3-D object representation is the process of describing the shape, appearance, and properties of an object in three-dimensional space using mathematical models and data structures.
- 3-D object representation is essential for computer graphics applications such as animation, rendering, simulation, gaming, virtual reality, etc.
- 3-D object representation can be classified into two main categories: boundary representation and space-partitioning representation.

## Boundary Representation (B-rep)

- Boundary representation describes a 3-D object as a set of surfaces that separate the object interior from the environment.
- Boundary representation is also known as surface representation or surface modeling.
- Boundary representation is the most commonly used method for 3-D object representation in computer graphics systems.
- Boundary representation can use different types of surfaces to model an object, such as polygons, curves, patches, meshes, etc.
- Boundary representation has the following advantages and disadvantages:

  - Advantages:
    - It is easy to display and render on graphics hardware.
    - It can handle complex and irregular shapes.
    - It can support various surface properties such as color, texture, shading, etc.
  - Disadvantages:
    - It may not capture the interior properties of an object, such as density, material, etc.
    - It may not be able to represent objects with holes, gaps, or self-intersections.
    - It may require a large amount of data to store and process.

## Space-Partitioning Representation

- Space-partitioning representation describes a 3-D object by dividing the space into smaller regions and assigning attributes to each region.
- Space-partitioning representation is also known as volumetric representation or solid modeling.
- Space-partitioning representation is mainly used for applications that require interior information of an object, such as medical imaging, physics simulation, etc.
- Space-partitioning representation can use different methods to partition the space, such as octrees, voxels, constructive solid geometry, etc.
- Space-partitioning representation has the following advantages and disadvantages:

  - Advantages:
    - It can capture the interior properties of an object, such as density, material, etc.
    - It can represent objects with holes, gaps, or self-intersections.
    - It can support various operations on objects, such as boolean operations, transformations, etc.
  - Disadvantages:
    - It may be difficult to display and render on graphics hardware.
    - It may not handle complex and irregular shapes well.
    - It may require a large amount of data to store and process.



# 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve the parallelism and ratios of distances between points, but not the angles or lengths. Examples of affine transformations are translation, scaling, rotation, and shear.
- Non-affine transformations do not preserve any of the properties of the original shape. Examples of non-affine transformations are perspective and distortion.

## Translation
- Translation is the simplest affine transformation that moves every point of a shape by a fixed distance in a given direction.
- Translation can be represented by a 3x3 matrix, where the last row is (0, 0, 1).
- The translation matrix for moving a point (x, y, z) by (tx, ty, tz) is:

| 1 | 0 | 0 | tx |
| 0 | 1 | 0 | ty |
| 0 | 0 | 1 | tz |
| 0 | 0 | 0 | 1  |

- The result of applying the translation matrix to a point (x, y, z, 1) is:

| x + tx |
| y + ty |
| z + tz |
| 1      |

## Scaling
- Scaling is an affine transformation that changes the size of a shape by multiplying the coordinates of each point by a scaling factor.
- Scaling can be represented by a 3x3 matrix, where the last row is (0, 0, 1).
- The scaling matrix for scaling a point (x, y, z) by (sx, sy, sz) is:

| sx | 0  | 0  | 0 |
| 0  | sy | 0  | 0 |
| 0  | 0  | sz | 0 |
| 0  | 0  | 0  | 1 |

- The result of applying the scaling matrix to a point (x, y, z, 1) is:

| sx * x |
| sy * y |
| sz * z |
| 1      |

## Rotation
- Rotation is an affine transformation that rotates a shape around an axis by a given angle.
- Rotation can be represented by a 3x3 matrix, where the last row is (0, 0, 1).
- The rotation matrix for rotating a point (x, y, z) around the x-axis by an angle θ is:

| 1 | 0      | 0       | 0 |
| 0 | cos θ  | -sin θ  | 0 |
| 0 | sin θ  | cos θ   | 0 |
| 0 | 0      | 0       | 1 |

- The rotation matrix for rotating a point (x, y, z) around the y-axis by an angle θ is:

| cos θ  | 0 | sin θ  | 0 |
| 0      | 1 | 0      | 0 |
| -sin θ | 0 | cos θ  | 0 |
| 0      | 0 | 0      | 1 |

- The rotation matrix for rotating a point (x, y, z) around the z-axis by an angle θ is:

| cos θ  | -sin θ | 0 | 0 |
| sin θ  | cos θ  | 0 | 0 |
| 0      | 0      | 1 | 0 |
| 0      | 0      | 0 | 1 |

- The result of applying the rotation matrix to a point (x, y, z, 1) is:

| x * cos θ - y * sin θ |
| x * sin θ + y * cos θ |
| z                     |
| 1                     |

- For rotation around an arbitrary axis, the axis vector needs to be normalized and the rotation matrix can be derived using the Rodrigues' rotation formula.

## Shear
- Shear is an affine transformation that distorts a shape by sliding one plane parallel to another.
- Shear can be represented by a 3x3 matrix, where the last row is (0, 0, 1



# 3-D Viewing

- 3-D viewing is the process of displaying 3-D computer graphics on a 2-D or 3-D display device, such as a monitor or a virtual reality headset.
- 3-D viewing involves two main steps: modelling transformation and viewing transformation.
- Modelling transformation is the process of defining and manipulating the 3-D objects in a scene, such as their shape, size, position, orientation, and color.
- Viewing transformation is the process of defining and manipulating the observer's viewpoint and the projection plane, such as their location, direction, and field of view.
- Projection is the process of mapping the 3-D scene onto the 2-D or 3-D projection plane, such as using parallel, perspective, or stereoscopic methods.
- 3-D viewing requires special software and hardware to create, manipulate, and display 3-D graphics, such as 3D Viewer, 3ds Max, or VR headsets.
- 3-D viewing has many applications in various fields, such as entertainment, education, engineering, medicine, and art.



# Projections in Computer Graphics

- Projection is a technique or process which is used to transform a 3D object into a 2D plane.
- Projection is necessary to display a 3D object on a 2D screen or paper.
- Projection can be classified into two types: parallel projection and perspective projection.

## Parallel Projection

- Parallel projection discards z-coordinate and parallel lines from each vertex on the object are extended until they intersect the view plane.
- Parallel projection preserves the relative proportions and angles of the object, but not the true distances or sizes.
- Parallel projection can be further divided into orthographic projection, oblique projection and isometric projection.

### Orthographic Projection

- Orthographic projection is a type of parallel projection where the direction of projection is normal to the projection plane .
- Orthographic projection shows only one face of the object, and the hidden lines are removed or dashed.
- Orthographic projection can be defined by a 6-tuple, (left, right, bottom, top, near, far), which defines the clipping planes.
- Orthographic projection is commonly used in engineering and technical drawings.

### Oblique Projection

- Oblique projection is a type of parallel projection where the direction of projection is not normal to the projection plane .
- Oblique projection shows more than one face of the object, and the hidden lines are usually visible.
- Oblique projection can be classified into cavalier projection and cabinet projection, depending on the angle between the projection direction and the projection plane.
- Oblique projection is often used to create a 3D effect in 2D drawings.

### Isometric Projection

- Isometric projection is a special case of oblique projection where the direction of projection makes equal angles with the three principal axes of the object .
- Isometric projection shows three faces of the object, and the angles between them are 120 degrees.
- Isometric projection preserves the lengths of the edges of the object, but not the angles or areas.
- Isometric projection is widely used in video games, technical illustrations and architectural drawings.

## Perspective Projection

- Perspective projection simulates the way a human eye perceives a 3D scene.
- Perspective projection preserves the relative sizes and distances of the object, but not the parallelism or angles.
- Perspective projection can be defined by a center of projection (or eye point), a view plane (or image plane), and a view reference point (or look-at point).
- Perspective projection can be classified into one-point, two-point and three-point perspective, depending on the number of vanishing points on the view plane.
- Perspective projection is commonly used in art, photography and computer graphics.



# 3-D Clipping

- Clipping is the process of removing parts of objects that are outside the viewing volume or the region of interest.
- Clipping is important for efficiency and accuracy in computer graphics.
- Clipping can be done in different stages of the graphics pipeline, such as object space, eye space, clip space or screen space.
- Clipping can be applied to different types of primitives, such as points, lines, polygons, curves or surfaces.
- Clipping can be done using different methods, such as parametric, geometric, Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman or Weiler-Atherton.
- Clipping can be done using different shapes of clipping regions, such as rectangles, circles, polygons or polyhedra.
- Clipping can be done using different types of clipping planes, such as near, far, left, right, top or bottom.

## Object Space Clipping

- Object space clipping is done before the transformation of objects from their local coordinate systems to the world coordinate system.
- Object space clipping is useful for culling objects that are completely outside the viewing volume or the region of interest.
- Object space clipping can be done using bounding boxes or bounding spheres that enclose the objects and test their intersection with the clipping region.
- Object space clipping can be done using hierarchical data structures, such as octrees or BSP trees, that partition the objects and the space into smaller regions and test their inclusion or exclusion with the clipping region.

## Eye Space Clipping

- Eye space clipping is done after the transformation of objects from the world coordinate system to the eye coordinate system, where the eye is at the origin and the viewing direction is along the negative z-axis.
- Eye space clipping is useful for culling objects that are behind the eye or outside the field of view.
- Eye space clipping can be done using outcodes, which are binary codes that indicate the position of a point relative to the six clipping planes of the view frustum.
- Eye space clipping can be done using the Cohen-Sutherland algorithm for line clipping, which uses the outcodes to determine the trivial accept, trivial reject or subdivision cases.
- Eye space clipping can be done using the Liang-Barsky algorithm for line clipping, which uses the parametric equation of the line and the inequalities of the clipping planes to compute the intersection points.
- Eye space clipping can be done using the Sutherland-Hodgman algorithm for polygon clipping, which uses the clipping planes as boundaries and clips the polygon against each boundary in turn, generating a new polygon at each step.
- Eye space clipping can be done using the Weiler-Atherton algorithm for polygon clipping, which uses the intersection points of the polygon edges and the clipping planes as vertices and constructs a list of entry and exit points for each polygon and each clipping region.

## Clip Space Clipping

- Clip space clipping is done after the transformation of objects from the eye coordinate system to the clip coordinate system, where the coordinates are normalized by the homogeneous component w.
- Clip space clipping is useful for perspective projection, where the view frustum is a truncated pyramid and the clipping region is a unit cube.
- Clip space clipping can be done using the homogeneous clipping algorithm, which uses the sign and magnitude of the homogeneous coordinates to determine the trivial accept, trivial reject or subdivision cases.
- Clip space clipping can be done using the perspective divide, which divides the homogeneous coordinates by w and maps the clip space coordinates to the normalized device coordinates, which range from -1 to 1 in each axis.
- Clip space clipping can be done using the guard-band clipping algorithm, which extends the clipping region slightly beyond the unit cube and allows some tolerance for numerical errors.

## Screen Space Clipping

- Screen space clipping is done after the transformation of objects from the clip coordinate system to the screen coordinate system, where the coordinates are mapped to the pixel coordinates of the display device.
- Screen space clipping is useful for rasterization, where the primitives are converted to pixels and drawn on the screen.
- Screen space clipping can be done using the 2D clipping algorithm, which clips the primitives against the screen boundaries and prevents drawing outside the screen.
- Screen space clipping can be done using the scan-line algorithm, which clips the primitives against the horizontal scan-lines and fills the pixels inside the primitives.



## Unit 4 - Curves and Surfaces

- A curve is a one-dimensional object that can be represented by a function of one or more parameters, such as x(t), y(t), z(t).
- A surface is a two-dimensional object that can be represented by a function of two or more parameters, such as x(u,v), y(u,v), z(u,v).
- Curves and surfaces are important in computer graphics, computer-aided design, and geometric modeling, as they can be used to create and manipulate complex shapes and objects.
- Some common types of curves and surfaces are:

  - **Polynomial curves and surfaces**: These are defined by algebraic expressions of a fixed degree, such as lines, circles, ellipses, parabolas, hyperbolas, Bezier curves and surfaces, B-spline curves and surfaces, and NURBS curves and surfaces.
  - **Rational curves and surfaces**: These are defined by ratios of polynomial expressions, such as conic sections, rational Bezier curves and surfaces, rational B-spline curves and surfaces, and NURBS curves and surfaces.
  - **Trigonometric curves and surfaces**: These are defined by trigonometric functions, such as sine, cosine, and tangent, or their combinations, such as Fourier series, cycloids, and trochoids.
  - **Transcendental curves and surfaces**: These are defined by non-algebraic functions, such as exponential, logarithmic, and power functions, or their combinations, such as spirals, helices, and catenaries.

- Some properties and operations on curves and surfaces are:

  - **Degree**: The degree of a polynomial curve or surface is the highest power of the parameter(s) in its expression. The degree of a rational curve or surface is the highest degree of the numerator and denominator polynomials. The degree affects the shape and smoothness of the curve or surface.
  - **Continuity**: The continuity of a curve or surface is the degree of smoothness at the points where it is joined or split. There are different types of continuity, such as positional continuity (C0), tangential continuity (C1), curvature continuity (C2), and higher-order continuity (Cn).
  - **Control points**: The control points of a curve or surface are a set of points that influence its shape and position. The control points can be interpolated (pass through the curve or surface) or approximated (lie near the curve or surface). The control points can be manipulated to modify the curve or surface.
  - **Control polygon and control net**: The control polygon of a curve is a polygon that connects the control points of the curve. The control net of a surface is a mesh that connects the control points of the surface. The control polygon and control net can be used to visualize and edit the curve or surface.
  - **Knots and knot vectors**: The knots of a curve or surface are a set of values that determine the domain and subdivision of the parameter(s). The knot vector of a curve or surface is a sequence of knots arranged in ascending order. The knots and knot vectors affect the shape and continuity of the curve or surface.
  - **Basis functions**: The basis functions of a curve or surface are a set of functions that define the contribution of each control point to the curve or surface. The basis functions depend on the type and degree of the curve or surface, and the knots and knot vectors. The basis functions can be used to evaluate and manipulate the curve or surface.



# Quadric Surfaces

- Quadric surfaces are common modeling primitives for a variety of computer graphics and computer-aided-design applications.
- Quadric surfaces are the graphs of equations that can be expressed in the form `Ax^2 + By^2 + Cz^2 + Dxy + Exz + Fyz + Gx + Hy + Jz + K = 0`.
- Quadric surfaces are the 3D counterparts of conic sections and have six distinct types.
- The six types of quadric surfaces are:
  - Ellipsoid: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 + z^2/c^2 = 1`. It is a closed surface that resembles a stretched sphere.
  - Elliptic paraboloid: a surface described by an equation of the form `z = x^2/a^2 + y^2/b^2`. It is an open surface that resembles a parabolic bowl.
  - Hyperbolic paraboloid: a surface described by an equation of the form `z = x^2/a^2 - y^2/b^2`. It is an open surface that resembles a saddle.
  - Hyperboloid of one sheet: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 1`. It is an open surface that resembles a double cone with a waist.
  - Hyperboloid of two sheets: a surface described by an equation of the form `x^2/a^2 - y^2/b^2 - z^2/c^2 = 1`. It is a closed surface that consists of two disjoint pieces.
  - Cone: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 0`. It is an open surface that resembles a pointed cone.
- When a quadric surface intersects a coordinate plane, the trace is a conic section.
- Ray tracing or ray firing is a popular method used for realistic renderings of quadric surfaces.



# Spheres

A sphere is a three-dimensional object that has a round shape and a constant radius. It is defined by the set of points that are equidistant from a fixed point called the center. A sphere can be represented by the equation:

(x - x0)^2 + (y - y0)^2 + (z - z0)^2 = r^2

where (x0, y0, z0) is the center and r is the radius of the sphere.

Some properties of spheres are:

- A sphere has a surface area of 4πr^2 and a volume of (4/3)πr^3.
- A sphere is a closed and bounded surface, meaning that it encloses a finite region of space and has no boundary or edge.
- A sphere is a convex surface, meaning that any line segment joining two points on the sphere lies entirely on or inside the sphere.
- A sphere is a smooth surface, meaning that it has no corners or sharp edges.

In computer graphics, spheres are often used to model objects that have a round shape, such as balls, planets, or bubbles. However, spheres are not easy to draw or manipulate on a computer screen, because they are not composed of flat polygons, which are the basic building blocks of computer graphics. Therefore, spheres are usually approximated by simpler objects constructed from flat polygons, such as polyhedra.

There are several methods to approximate a sphere by a polyhedron, such as:

- Using lines of longitude and latitude to divide the sphere into quadrilaterals or triangles. This method is simple and intuitive, but it produces uneven polygons that are more dense near the poles and less dense near the equator.
- Using a regular polyhedron, such as a tetrahedron, an octahedron, or an icosahedron, and subdividing each face into smaller triangles. This method produces more uniform polygons, but it requires more computation and memory to store the vertices and faces of the polyhedron.
- Using a bounding sphere, which is the smallest sphere that contains a given object . This method is useful for collision detection and culling, because it simplifies the shape of the object and reduces the number of calculations needed to determine if the object intersects with another object or the view frustum. However, a bounding sphere may not be a good approximation of the object's shape, especially if the object is not round or symmetrical.



# Ellipsoid

An ellipsoid is a surface that may be obtained from a sphere by deforming it by means of directional scalings, or more generally, of an affine transformation. An ellipsoid is a quadric surface; that is, a surface that may be defined as the zero set of a polynomial of degree two in three variables.

Some properties of ellipsoids are:

- An ellipsoid has three mutually perpendicular axes of symmetry that intersect at the center of the ellipsoid.
- An ellipsoid is closed, convex, and bounded.
- An ellipsoid has a unique inscribed sphere (tangent to each of the ellipsoid's three axes) and a unique circumscribed sphere (tangent to the ellipsoid at four points).
- An ellipsoid has four umbilical points, where the principal curvatures are equal.

Some applications of ellipsoids in computer graphics are:

- Ellipsoids can be used as geometric primitives for modeling and rendering complex shapes, such as human heads, fruits, planets, etc.
- Ellipsoids can be generalized to superellipsoids, which have more parameters to control the shape and can produce more variety of forms, such as cubes, octahedra, cylinders, etc.
- Ellipsoids can be drawn using algorithms that find the points of the ellipse in each quadrant, such as the midpoint ellipse algorithm, which is based on the midpoint circle algorithm.
- Ellipsoids can be triangulated to form a polygon mesh, which can be used for rendering, collision detection, and other operations. One method of triangulation is to use parametric equations of the ellipsoid and sample the angles to obtain the vertices.



# Blobby Objects

- Blobby objects are a type of implicit modeling technique in computer graphics that can represent non-rigid and fluid-like objects, such as cloth, rubber, liquids, water droplets, etc.  
- Blobby objects are defined by a set of points, called **metaballs**, that have a scalar field associated with them. The scalar field represents the influence or intensity of each metaball at a given point in space.
- The surface of a blobby object is determined by an **isovalue**, which is a threshold that defines the boundary of the object. The isovalue can be constant or variable, depending on the desired shape and smoothness of the object.
- The scalar field of a metaball can be computed by various functions, such as Gaussian, Wyvill, or Blinn functions. The scalar field of a blobby object is the sum of the scalar fields of all the metaballs that compose it.
- Blobby objects can be rendered by various methods, such as ray tracing, polygonization, or marching cubes. Ray tracing is a technique that traces rays of light from the eye to the object and computes the color and shading of each pixel. Polygonization is a technique that converts the implicit surface of a blobby object into a mesh of polygons that can be rendered by standard graphics hardware. Marching cubes is a technique that subdivides the space into cubes and computes the intersection of the surface and the edges of each cube, forming vertices and polygons.
- Blobby objects can be animated by changing the position, size, or intensity of the metaballs over time. This can create realistic effects of deformation, merging, splitting, or dripping of the object.



# Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that runs through a series of given points.
- Splines are very useful for modeling arbitrary functions, and are used extensively in computer graphics.
- There are different types of splines, such as cubic splines, Bézier curves, and B-splines, that have different properties and applications .
- A spline can be defined by a set of control points, a degree, and a basis function.
- A spline can be evaluated at any parameter value by using a recursive algorithm called de Boor's algorithm.
- A spline can be transformed by an affine transform (rotation, translation, etc.) without changing its shape.



# Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline or basis spline is a piecewise polynomial function with specific properties that determine the polynomial degree/order .
- The idea behind using a B-spline curve is to determine a unique polynomial representation of a set of data, whether that data be structural points in 3D space or a set of data on a graph.
- A B-spline function is a combination of flexible bands that is controlled by a number of points that are called control points, creating smooth curves .
- These functions are used to create and manage complex shapes and surfaces using a number of points.
- A B-spline curve is defined by the following parameters:
  - A set of control points P0, P1, ..., Pn that define the shape of the curve.
  - A degree p that determines the order of the polynomial segments.
  - A knot vector U = {u0, u1, ..., um} that determines the domain and continuity of the curve.
- A B-spline curve can be expressed as a linear combination of B-spline basis functions of degree p as follows:

  B-spline curve equation

  where N<sub>i,p</sub>(u) are the B-spline basis functions of degree p defined recursively by the Cox-de Boor formula:

  B-spline basis functions

- Some properties of B-spline curves are :
  - They are invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - They have local control, meaning that changing one control point only affects the curve in a local region.
  - They have variation diminishing property, meaning that the curve does not oscillate more than the control polygon.
  - They have convex hull property, meaning that the curve lies within the convex hull of the control points.
  - They have C<sup>p-k</sup> continuity at the k-th multiple knot, where k is the multiplicity of the knot and p is the degree of the curve.
  - They can approximate any smooth curve arbitrarily well by increasing the number of control points and adjusting their positions.



# Bezier curves and surfaces

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling .
- They are named after Pierre Bezier, a French engineer who patented and popularized them in the 1960s.
- They are defined by a set of control points, which are discrete points that influence the shape of the curve or surface.
- The curve or surface passes through the first and last control points, but not necessarily through the intermediate ones.
- The degree of the curve or surface is equal to the number of control points minus one.
- The curve or surface is parametric, meaning that it can be expressed as a function of one or two parameters, usually denoted by u and v.
- The curve or surface is smooth and continuous, and has desirable properties such as convex hull, affine invariance, and variation diminishing.
- The curve or surface can be evaluated using a recursive algorithm called de Casteljau's algorithm, which subdivides the control points into smaller segments and computes the point on the curve or surface corresponding to a given parameter value.
- The curve or surface can be modified by changing the position or number of the control points, which affects the shape and smoothness of the curve or surface.
- The curve or surface can be approximated by a polygonal mesh, which is a collection of triangles or quadrilaterals that cover the curve or surface.
- The curve or surface can be used to model complex shapes that are otherwise difficult to represent mathematically or geometrically, such as fonts, logos, car bodies, terrain, etc  .



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



# Back Face Detection Algorithm

- Back face detection (or back face culling) is a technique to eliminate hidden surfaces or lines in computer graphics.
- It is based on the assumption that a polygonal model of a solid object is represented by a set of faces that are oriented outward from the object's interior.
- A face is said to be back facing if it is oriented away from the viewer, i.e., its normal vector points in the opposite direction of the viewing vector.
- Back facing faces are not visible to the viewer and can be discarded from the rendering process, saving computation time and memory.
- The algorithm to determine whether a face is back facing or not is as follows:

  - For each face F in the polygonal model, compute its normal vector N by taking the cross product of two non-parallel edges of F.
  - For each face F, compute its centroid C by taking the average of its vertices.
  - For each face F, compute the viewing vector V by subtracting the viewer's position P from the centroid C, i.e., V = C - P.
  - For each face F, compute the dot product of N and V, i.e., D = N.V.
  - If D is positive, then F is back facing and can be discarded. If D is negative or zero, then F is front facing and should be rendered.



# Depth buffer method

The depth buffer method, also known as the z-buffer method, is a technique for hidden surface removal in computer graphics. It is an image-space approach that compares the depth of each pixel on the screen with the depth of the object that is projected onto that pixel. The depth buffer method works as follows:

- For each pixel on the screen, initialize a depth buffer value to a very large number, representing the farthest possible distance from the viewer.
- For each polygon in the scene, project it onto the screen and calculate the depth of each pixel that it covers, using the equation of the plane that contains the polygon.
- For each pixel that the polygon covers, compare its depth with the depth buffer value. If the depth of the pixel is smaller than the depth buffer value, it means that the pixel is closer to the viewer than the previous object that covered it. In that case, update the depth buffer value to the depth of the pixel, and also update the color buffer value to the color of the polygon. Otherwise, if the depth of the pixel is larger than the depth buffer value, it means that the pixel is farther from the viewer than the previous object that covered it. In that case, ignore the pixel and do not change the depth buffer or the color buffer values.
- Repeat the above steps for all the polygons in the scene, in any order.
- Display the color buffer values on the screen, which represent the visible surfaces of the scene.

The depth buffer method has some advantages and disadvantages. Some of the advantages are:

- It is easy to implement and can be done in hardware or software.
- It can handle any number of polygons and any type of polygon, including concave, intersecting, or transparent polygons.
- It does not require sorting the polygons by depth or splitting them into smaller pieces.

Some of the disadvantages are:

- It requires a lot of memory to store the depth buffer and the color buffer values for each pixel on the screen.
- It can cause aliasing artifacts, such as jagged edges or popping effects, due to the discrete nature of the pixels and the depth values.
- It can waste computation time by processing pixels that are eventually occluded by closer objects.



# A-Buffer Method for Hidden Lines and Surfaces

- A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects .
- It extends the algorithm of depth-buffer (or Z-buffer) method by storing more than one depth and color value per pixel.
- It uses a linked list data structure to store the fragments of objects that contribute to a pixel.
- Each fragment has four attributes: depth, color, opacity, and coverage.
- The depth attribute is the distance of the fragment from the view plane.
- The color attribute is the color of the fragment.
- The opacity attribute is the degree of transparency of the fragment.
- The coverage attribute is the fraction of the pixel area covered by the fragment.
- The fragments are sorted in decreasing order of depth in the linked list.
- The final color of the pixel is computed by blending the colors of the fragments according to their opacity and coverage.
- The advantages of A-buffer method are:
  - It can handle transparent and intersecting objects.
  - It can produce anti-aliased images by using sub-pixel sampling.
  - It can support various shading and lighting effects.
- The disadvantages of A-buffer method are:
  - It requires more memory and processing time than depth-buffer method.
  - It may suffer from aliasing artifacts due to finite resolution of the depth buffer.
  - It may not handle some complex cases such as cyclic overlaps or self-intersections.



# Scan Line Method for Hidden Surface Removal

- A scan line method of hidden surface removal is an image space method that processes one line at a time rather than one pixel at a time.
- It is an extension of the scan line algorithm for filling polygon interiors, but it deals with more than one surface.
- As each scan line is processed, it examines all polygon surfaces intersecting that line to determine which are visible.
- The scan line method of hidden surface removal also stores a flag for each surface that is set on or off to indicate whether a position along a scan line is inside or outside of the surface.
- Scan lines are processed from left to right, and the depth values of the visible surfaces are compared to find the closest one at each pixel position.
- The scan line method of hidden surface removal can be summarized as follows:

  - For each scan line, find the intersections of the scan line with all polygon edges.
  - Sort the intersections by increasing x value.
  - Initialize the depth buffer and the surface flag buffer.
  - For each pair of intersections, determine which surface is visible by comparing the depth values and the surface flags.
  - Fill the pixel positions between the pair of intersections with the color of the visible surface.
  - Update the depth buffer and the surface flag buffer accordingly.



# Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the properties of the surface and the properties of the light sources.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, ignoring the effects of other objects in the scene.
  - Global illumination models consider all the interactions and exchange of light among objects in the scene, including reflection, refraction, and shadows.
- The most common local illumination model is the Phong model, which consists of three components: ambient, diffuse, and specular .
  - Ambient component represents the uniform background light that is present in the environment, independent of the light sources and the surface orientation .
  - Diffuse component represents the light that is scattered equally in all directions by a matte or rough surface, depending on the angle between the surface normal and the light direction .
  - Specular component represents the light that is reflected in a mirror-like manner by a shiny or smooth surface, depending on the angle between the surface normal, the light direction, and the view direction .
- The Phong model can be expressed mathematically as follows :

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - I<sub>a</sub> = k<sub>a</sub> * I<sub>al</sub>
  - I<sub>d</sub> = k<sub>d</sub> * I<sub>l</sub> * cos θ
  - I<sub>s</sub> = k<sub>s</sub> * I<sub>l</sub> * cos<sup>n</sup> α
  - where I is the total intensity, I<sub>a</sub> is the ambient intensity, I<sub>d</sub> is the diffuse intensity, I<sub>s</sub> is the specular intensity, k<sub>a</sub> is the ambient reflection coefficient, k<sub>d</sub> is the diffuse reflection coefficient, k<sub>s</sub> is the specular reflection coefficient, I<sub>al</sub> is the ambient light intensity, I<sub>l</sub> is the light source intensity, θ is the angle between the surface normal and the light direction, α is the angle between the reflection direction and the view direction, and n is the shininess exponent.

- The following diagram illustrates the Phong model:

  Phong model diagram

- The Phong model can be extended to include multiple light sources, color, and attenuation factors .
- The Phong model is a simple and efficient local illumination model, but it has some limitations, such as ignoring the effects of shadows, interreflections, and transparency .
- Global illumination models are more realistic and complex, but they are also more computationally expensive and difficult to implement.
- Some examples of global illumination models are ray tracing, radiosity, and photon mapping.



# Ambient light

- Ambient light is the base brightness applied to textures rendered in a scene before any point, spot, or other types of virtual light sources are computed.
- Ambient light affects the appearance of the entire rendered scene by adding a uniform amount of light to every point, regardless of its position, orientation, or material .
- Ambient light can be used to simulate natural or artificial lighting, such as the sun or fluorescent lights, by adjusting its color and intensity.
- Ambient light is a gross oversimplification of the complex interaction between the light sources and the surfaces in the scene, but it works well enough for some applications.
- Ambient light does not create any shadows or highlights, as it does not depend on the direction of the light rays.
- Ambient light can be combined with other types of lighting, such as diffuse, specular, or ambient occlusion, to create more realistic and detailed effects .
- Ambient light can be implemented in computer graphics using various techniques, such as constant shading, Gouraud shading, Phong shading, or ray tracing .



# Diffuse Reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough .
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by the surrounding objects, which can reflect light onto the surface.
- This phenomenon is called diffuse interreflection and it adds more realism to the scene.
- Diffuse reflection can be modeled by the Lambertian reflectance model, which assumes that the surface reflects light equally in all directions.
- The Lambertian model can be expressed by the formula:

![Lambertian model formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/9f0c9f9f9b9c1f0f0c6f8c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c



# Specular reflection

- Specular reflection is the phenomenon of light bouncing off a smooth and shiny surface in a single direction, creating a bright spot or highlight on the surface .
- Specular reflection depends on the angle of incidence of the light ray, the angle of reflection of the light ray, and the viewing angle of the observer .
- The angle of incidence is equal to the angle of reflection, and both are measured with respect to the normal vector of the surface .
- The viewing angle is the angle between the normal vector and the line of sight of the observer .
- The intensity of the specular reflection is highest when the viewing angle is equal to the angle of reflection, and decreases as the viewing angle deviates from the angle of reflection .
- Specular reflection is influenced by the color and intensity of the light source, the material and roughness of the surface, and the distance between the light source, the surface, and the observer   .
- In computer graphics, specular reflection is often modeled using empirical formulas that approximate the physical behavior of light and materials .
- One of the most common models is the Phong model, proposed by Bui-Tuong Phong in 1975, which uses a power function to calculate the intensity of the specular reflection based on the angle of reflection and the viewing angle .
- The Phong model has three parameters: the ambient component, the diffuse component, and the specular component, which represent the contribution of each type of reflection to the final color of the surface.
- The ambient component is a constant value that accounts for the background illumination of the scene.
- The diffuse component is proportional to the cosine of the angle of incidence, and represents the reflection of light in all directions by a rough surface.
- The specular component is proportional to the cosine of the angle between the angle of reflection and the viewing angle, raised to a power called the shininess, and represents the reflection of light in a single direction by a smooth surface.
- The shininess parameter controls the size and sharpness of the highlight, with higher values resulting in smaller and sharper highlights.
- The Phong model can produce realistic effects for many types of materials, but it has some limitations, such as not accounting for the Fresnel effect, the polarization of light, or the interreflection of light between surfaces.
- Other models that extend or improve the Phong model include the Blinn-Phong model, the Cook-Torrance model, the Ward model, and the Bidirectional reflectance distribution function (BRDF) model.



# Phong model

The Phong model is a widely used model for the local illumination of points on a surface in computer graphics. It was designed by Bui Tuong Phong in 1973 and is based on the observation that different materials reflect light differently, depending on the angle of incidence and the angle of reflection.

The Phong model consists of three components: ambient, diffuse, and specular. Each component represents a different aspect of how light interacts with a surface.

- Ambient component: This component accounts for the general illumination of the scene, regardless of the direction of the light source or the viewer. It is usually a constant value that is added to the final color of the point.
- Diffuse component: This component represents the scattering of light in all directions by a rough or matte surface. It depends on the angle between the light source and the surface normal, and is proportional to the cosine of that angle. The diffuse component is also affected by the color and intensity of the light source and the surface.
- Specular component: This component represents the reflection of light by a shiny or glossy surface. It depends on the angle between the reflection vector and the viewer vector, and is proportional to the cosine of that angle raised to a power called the shininess. The specular component is also affected by the color and intensity of the light source and the surface.

The Phong model can be expressed mathematically as follows:

`I = I_a + I_d + I_s`

where `I` is the final color of the point, `I_a` is the ambient component, `I_d` is the diffuse component, and `I_s` is the specular component.

The ambient component can be calculated as:

`I_a = k_a * I_a_l`

where `k_a` is the ambient reflection coefficient of the surface, and `I_a_l` is the ambient light intensity.

The diffuse component can be calculated as:

`I_d = k_d * I_l * (N * L)`

where `k_d` is the diffuse reflection coefficient of the surface, `I_l` is the light intensity, `N` is the surface normal, and `L` is the light vector.

The specular component can be calculated as:

`I_s = k_s * I_l * (R * V)^n`

where `k_s` is the specular reflection coefficient of the surface, `R` is the reflection vector, `V` is the viewer vector, and `n` is the shininess.

The Phong model can produce realistic results for a variety of materials, but it also has some limitations. For example, it does not account for the global illumination effects, such as shadows, reflections, or refractions. It also assumes that the light source and the viewer are infinitely far away, which is not always true in real scenes. Furthermore, it does not consider the wavelength of the light, which can affect the color and intensity of the reflection. Therefore, the Phong model is often used as a basis for more advanced models that can handle these issues.



# Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal algorithms are used to improve the realism and clarity of the rendered images by eliminating the hidden parts.
- Hidden line and surface removal algorithms can be classified into two categories: object space methods and image space methods .
- Object space methods compare the objects and parts of objects to each other within the scene definition to determine which surfaces, as a whole or in part, are hidden .
- Image space methods compare each projected pixel position on the view plane against a depth value stored in the refresh buffer to determine visibility .
- Some of the common object space methods are back-face removal, depth sorting, binary space partitioning, and area subdivision .
- Some of the common image space methods are z-buffer, scan-line, and ray tracing .
- A combined approach can use both object space and image space methods to achieve a balance between efficiency and accuracy.
- A possible combined approach is to use back-face removal and depth sorting as object space methods, and then use z-buffer as an image space method.
- Back-face removal eliminates the polygons that are facing away from the viewer, reducing the number of polygons to be processed.
- Depth sorting orders the polygons from back to front, so that the closer polygons can overwrite the farther ones in the image buffer.
- Z-buffer assigns a depth value to each pixel in the image buffer, and compares it with the depth value of the incoming polygon at that pixel. If the incoming polygon is closer, it replaces the pixel value and depth value; otherwise, it is discarded.
- This combined approach can handle concave and intersecting polygons, as well as transparency effects.



# Warn Model for the Notes of the Unit 5 - Hidden Lines and Surfaces in the Subject of Computer Graphics

- The Warn model is a lighting model that approximates large non-point sources close to objects in a scene by using several point sources arranged in a grid.
- The Warn model also allows one to specify "flaps" on the sides of the lighting region to give the light more directionality.
- The Warn model can be used to simulate studio lighting effects, such as spotlights.
- The Warn model takes into account the reflectance properties of the surface as well as the physics of light reflection.
- The Warn model can be implemented by using the following steps :
  - Define the position, size, and shape of the light source grid.
  - Define the position, orientation, and flaps of the light source region.
  - Define the intensity and color of each point source in the grid.
  - For each point source, calculate the distance and angle to the surface point to be illuminated.
  - Apply the intensity attenuation and color consideration formulas to determine the contribution of each point source to the surface point.
  - Sum up the contributions of all the point sources to get the final illumination value for the surface point.



# Intensity Attenuation

- In computer graphics, **attenuation** is reduction or loss of intensity of any kind of flux through a medium .
- For instance, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water.
- Attenuation is the gradual decrease in energy as the X-radiation passes through absorbing material .
- Intensity = power per unit cross sectional area.
- Attenuation can be expressed by the formula:

$$
I = I_0 e^{-\alpha x}
$$

where $I$ is the intensity after passing through a distance $x$ of the medium, $I_0$ is the initial intensity, $e$ is the base of the natural logarithm, and $\alpha$ is the attenuation coefficient.
- The attenuation coefficient depends on the properties of the medium and the wavelength of the radiation.
- Attenuation can affect the appearance of objects in computer graphics, especially when using realistic lighting models.
- For example, attenuation can cause specular highlights to fade as the distance from the light source increases.



# Color consideration for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces of an object that are not visible from a particular viewpoint or projection.
- Hidden surface removal is the process of identifying and eliminating the hidden surfaces from the rendered image.
- Color consideration for the notes of hidden lines and surfaces is important for enhancing the readability and clarity of the notes, as well as for highlighting the key concepts and algorithms.
- Some of the color considerations for the notes are:

  - Use different colors for visible and hidden lines and surfaces, such as black for visible and gray for hidden, or solid and dashed lines.
  - Use consistent and contrasting colors for different objects or surfaces, such as red, green, blue, yellow, etc.
  - Use colors that match the surface properties, such as diffuse, specular, ambient, etc.
  - Use colors that indicate the depth or distance of the surfaces, such as darker for closer and lighter for farther, or use a depth buffer to store the depth values of each pixel .
  - Use colors that reflect the light source and the shading model, such as Phong, Gouraud, flat, etc.
  - Use colors that are suitable for the display device and the viewing environment, such as RGB, CMYK, HSV, etc.
  - Use colors that are easy to distinguish and remember, such as primary, secondary, tertiary, etc.



# Transparency and Shadows

## Transparency
- Transparency is the property of a material that allows light to pass through it partially or fully.
- Transparency can be used to create realistic effects such as glass, water, ice, etc. in computer graphics.
- Transparency can be classified into two types: **binary transparency** and **partial transparency** .
- Binary transparency is when a pixel is either fully transparent or fully opaque. This can be achieved by using an alpha channel that stores a binary value for each pixel.
- Partial transparency is when a pixel can have varying degrees of transparency, from fully transparent to fully opaque. This can be achieved by using an alpha channel that stores a fractional value for each pixel, or by blending the colors of the pixel and the background according to a transparency function .
- Partial transparency can also be called **translucency** .
- Transparency can be implemented in different ways, such as alpha blending, alpha testing, alpha compositing, etc.

## Shadows
- Shadows are the regions where light is blocked by an object or a surface.
- Shadows can enhance the realism and depth of a scene rendered with computer graphics.
- Shadows can be classified into two types: **hard shadows** and **soft shadows**.
- Hard shadows are when the boundary between the shadow and the illuminated region is sharp and well-defined. This can be achieved by using a single point light source or a directional light source.
- Soft shadows are when the boundary between the shadow and the illuminated region is fuzzy and gradual. This can be achieved by using an area light source or multiple light sources.
- Shadows can be implemented in different ways, such as shadow mapping, shadow volumes, ray tracing, etc.

