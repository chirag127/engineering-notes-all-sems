

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



### Types of computer graphics

Computer graphics are the visual representation of data and information using computers and software. Computer graphics can be used for various purposes, such as creating images, animations, simulations, games, user interfaces, and more.

Computer graphics can be broadly classified into two main categories: raster graphics and vector graphics  . Additionally, computer graphics can also be categorized based on the dimensionality of the images: two dimensional (2D) and three dimensional (3D) graphics .

- **Raster graphics** are made up of pixels, which are small squares of color arranged in a grid. Each pixel contains information about its color and brightness. Raster graphics are also known as bitmap images, as they map each pixel to a specific location on the screen. Raster graphics are commonly used for digital photographs, paintings, and scanned images. The quality and resolution of raster graphics depend on the number of pixels per inch (ppi) or dots per inch (dpi). The more pixels or dots, the higher the quality and detail of the image. However, raster graphics also require more storage space and processing power, and they can lose quality when scaled up or down.

- **Vector graphics** are made up of paths, which are defined by mathematical equations that describe the shape, direction, and color of each line or curve. Vector graphics are also known as object-oriented graphics, as they represent each image element as an object that can be manipulated independently. Vector graphics are commonly used for logos, icons, fonts, diagrams, and illustrations. The quality and resolution of vector graphics do not depend on the number of pixels or dots, as they are rendered by the computer based on the equations. Therefore, vector graphics can be scaled up or down without losing quality or detail. However, vector graphics also require more complex software and algorithms, and they can be less realistic or expressive than raster graphics.

- **2D graphics** are graphics that have only two dimensions: width and height. 2D graphics can be either raster or vector, depending on how they are created and stored. 2D graphics are widely used for web design, graphic design, animation, and gaming. 2D graphics can create the illusion of depth, perspective, and motion by using techniques such as shading, lighting, shadows, gradients, and parallax.

- **3D graphics** are graphics that have three dimensions: width, height, and depth. 3D graphics can also be either raster or vector, depending on how they are created and stored. 3D graphics are mainly used for computer-aided design (CAD), simulation, virtual reality, and gaming. 3D graphics can create realistic and immersive images by using techniques such as modeling, rendering, texturing, lighting, shading, and animation.



### Graphic Displays for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A graphic display is a device that can show images, text, or graphics on a screen or other surface.
- Graphic displays are used for various purposes, such as presenting information, visualizing data, creating art, or playing games.
- Graphic displays can be classified into different types based on their technology, such as CRT, LCD, LED, OLED, plasma, or e-ink.
- Graphic displays can also be categorized based on their characteristics, such as resolution, aspect ratio, color depth, refresh rate, contrast ratio, brightness, or viewing angle  .
- Graphic displays can be connected to a computer or other device through various interfaces, such as VGA, DVI, HDMI, DisplayPort, or USB-C.
- Graphic displays can be controlled by a graphics processing unit (GPU), which is a specialized chip that handles the computation and rendering of graphics.
- A GPU can be integrated into the CPU or the motherboard, or it can be a separate card that can be installed or replaced.
- A GPU can have different features and capabilities, such as memory size, memory type, memory bandwidth, clock speed, shader cores, or ray tracing support.
- A GPU can also support different graphics standards and APIs, such as OpenGL, DirectX, Vulkan, or Metal.
- A GPU can affect the performance and quality of graphics applications, such as computer-aided design (CAD), video editing, animation, or gaming .
- A line is a basic element of graphics that can be used to draw shapes, curves, or contours.
- A line can be defined by two endpoints, or by a starting point, a direction, and a length.
- A line can have different attributes, such as color, thickness, style, or texture.
- A line can be generated by various algorithms, such as DDA, Bresenham, or Wu.
- A line generation algorithm can have different criteria, such as accuracy, speed, simplicity, or smoothness.
- A line generation algorithm can also have different challenges, such as dealing with slopes, rounding errors, or aliasing.



### Random scan displays

- Random scan displays are also known as **vector displays** or **stroke-writing displays** or **calligraphic displays**  .
- Random scan displays are used to draw a picture **one line at a time** and are thus also referred to as **line-drawing displays**  .
- Random scan displays use a **cathode ray tube (CRT)** that directs the beam of an electron only to those areas of the screen where a picture has to be drawn  .
- Random scan displays can draw and refresh component lines of a picture in any specified sequence.
- Random scan displays produce **smooth line drawings** and have **high resolution**.
- Random scan displays are suitable for applications that require **line drawings** such as engineering and computer-aided design (CAD) .
- Random scan displays cannot display realistic shaded scenes or complex images .
- Random scan displays require more memory than raster scan displays as they store the coordinates of the endpoints of each line .
- Random scan displays are more expensive and less common than raster scan displays .
- Pen plotter is an example of random scan displays.



### Raster scan displays

- Raster scan displays are the most common type of graphics monitor that use a cathode ray tube (CRT) to display images on a screen  .
- Raster scan displays are based on television technology, where an electron beam sweeps across the screen from top to bottom, covering one row of pixels at a time  .
- The electron beam turns on and off as it moves across each row, creating a pattern of illuminated spots or pixels on the screen .
- The resolution of a raster scan display depends on the number of pixels on the screen and the number of colors that each pixel can display .
- The refresh rate of a raster scan display is the number of times per second that the electron beam redraws the entire screen . A higher refresh rate reduces flickering and improves the quality of animation and video.
- Raster scan displays are suitable for displaying realistic images, complex shapes, and various colors, but they have some limitations, such as:
  - They require a large amount of memory to store the pixel values for each frame .
  - They are slow to update the screen when the image changes frequently or drastically .
  - They cannot display sharp lines or curves, as they are composed of discrete pixels .
  - They suffer from aliasing, which is the distortion of edges and shapes due to the pixelation of the image .



### Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- A video controller may also perform additional functions, such as graphics acceleration, video decoding, or cursor generation.

Some points to note about frame buffer and video controller are:

- The frame buffer is the size of the maximum image that can be displayed, and it may be a separate memory bank on the graphics card, GPU or a reserved part of regular memory.
- The frame buffer can store different types of information, such as color, depth, alpha, or stencil values.
- The frame buffer can be accessed by the CPU or the GPU, depending on the system architecture and the graphics API.
- The video controller can have different modes of operation, such as text mode, graphics mode, or overlay mode.
- The video controller can support different types of monitors, such as CRT, LCD, or OLED.



### Points and lines for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A point is the simplest graphical element that can be displayed on a screen. It is represented by a single pixel or a dot.
- A line is a sequence of points that connects two endpoints. It is one of the most basic and common shapes in computer graphics.
- There are different methods to generate lines on a raster display, such as DDA algorithm, Bresenham's algorithm, midpoint algorithm, etc.
- These algorithms are based on the concept of incremental calculation, which means that the next point on the line is computed from the previous point using some arithmetic operations.
- The main criteria to evaluate the performance of these algorithms are accuracy, speed, and simplicity.
- Accuracy refers to how closely the generated line approximates the ideal line, which is defined by the slope and the endpoints.
- Speed refers to how fast the algorithm can generate the line, which depends on the number of calculations and memory accesses required for each point.
- Simplicity refers to how easy the algorithm is to implement and understand, which affects the code size and complexity.
- Some of the advantages and disadvantages of these algorithms are:

  - DDA algorithm: It is simple and accurate, but slow and requires floating-point operations.
  - Bresenham's algorithm: It is fast and efficient, but less accurate and works only for lines with slope less than 1 in magnitude.
  - Midpoint algorithm: It is accurate and works for any slope, but more complex and requires more calculations than Bresenham's algorithm.



### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Line drawing algorithms are methods for approximating a line segment on discrete graphical media, such as pixel-based displays and printers.
- Line drawing algorithms are important for computer graphics because they are used to render basic shapes, such as polygons, curves, and fonts.
- Line drawing algorithms need to be efficient, accurate, and smooth, meaning that they should minimize the number of pixels used, avoid gaps and jagged edges, and produce a visually pleasing result.
- There are several algorithms for drawing a line, each with different advantages and disadvantages. Some of the most common ones are :
  - Naive algorithm: This algorithm simply rounds the x and y coordinates of each point on the line to the nearest integer and plots the corresponding pixel. It is simple to implement, but it can produce gaps and jagged edges, especially for steep lines.
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each point on the line. It avoids gaps, but it can be slow and inaccurate due to the use of floating-point arithmetic.
  - Bresenham's algorithm: This algorithm uses integer arithmetic and error terms to determine which pixel to plot for each step along the line. It is fast and accurate, but it can produce jagged edges for steep lines.
  - Mid-point algorithm: This algorithm uses a decision variable based on the mid-point between two possible pixels to choose which one to plot for each step along the line. It is similar to Bresenham's algorithm, but it can handle any slope and produce smoother lines.
- The following diagram illustrates the difference between some of the line drawing algorithms for a line with slope 2/3:

Line drawing algorithms comparison

- The following pseudocode shows the basic steps of the naive, DDA, and Bresenham's algorithms for drawing a line from (x1, y1) to (x2, y2) :

```
// Naive algorithm
function naive_line(x1, y1, x2, y2)
  // Calculate the slope of the line
  m = (y2 - y1) / (x2 - x1)
  // Loop over the x coordinates from x1 to x2
  for x from x1 to x2
    // Calculate the corresponding y coordinate using the slope
    y = m * (x - x1) + y1
    // Round the y coordinate to the nearest integer
    y = round(y)
    // Plot the pixel at (x, y)
    plot(x, y)
  end for
end function

// DDA algorithm
function dda_line(x1, y1, x2, y2)
  // Calculate the absolute difference between x1 and x2, and between y1 and y2
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  // Choose the larger of dx and dy as the number of steps
  steps = max(dx, dy)
  // Calculate the increment for x and y for each step
  x_inc = dx / steps
  y_inc = dy / steps
  // Initialize the current x and y coordinates to x1 and y1
  x = x1
  y = y1
  // Loop over the number of steps
  for i from 0 to steps
    // Plot the pixel at the current x and y coordinates
    plot(x, y)
    // Increment x and y by x_inc and y_inc
    x = x + x_inc
    y = y + y_inc
  end for
end function

// Bresenham's algorithm
function bresenham_line(x1, y1, x2, y2)
  // Calculate the absolute difference between x1 and x2, and between y1 and y2
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  // Initialize the error term to zero
  error = 0
  // Choose the initial y coordinate based on the sign of the slope
  if y1 < y2 then
    y = y1
    y_inc = 1

```




### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm.
- A circle generation algorithm is an algorithm used to create a circle on a computer screen by determining the subsequent points required to draw the circle .
- The equation of a circle is X^2^ + Y^2^ = r^2^, where r is the radius of the circle.
- There are several algorithms used for generating circles on a computer screen, such as:
  - Bresenham's Algorithm
  - Midpoint Circle Algorithm
  - Polar Coordinates Method
  - Trigonometric Method
- Bresenham's Algorithm :
  - It is an efficient and incremental algorithm that uses only integer arithmetic and avoids floating-point operations.
  - It is based on the idea of using the midpoint of the circle to decide the next point to be plotted.
  - It starts from the point (0, r) and moves in an anti-clockwise direction along the octant of the circle in the first quadrant.
  - It uses a decision variable d to determine whether to choose the pixel at (x+1, y) or (x+1, y-1) as the next point.
  - The initial value of d is 3 - 2r and it is updated at each step as follows:
    - If d < 0, then d = d + 4x + 6 and the next point is (x+1, y)
    - If d >= 0, then d = d + 4(x-y) + 10 and the next point is (x+1, y-1)
  - The algorithm stops when x >= y, as the remaining points can be obtained by symmetry.
- Midpoint Circle Algorithm :
  - It is similar to Bresenham's Algorithm, but it uses a different decision variable and update rules.
  - It is based on the idea of using the midpoint of the line joining the two candidate pixels to decide the next point to be plotted.
  - It starts from the point (0, r) and moves in an anti-clockwise direction along the octant of the circle in the first quadrant.
  - It uses a decision variable p to determine whether to choose the pixel at (x+1, y) or (x+1, y-1) as the next point.
  - The initial value of p is 1 - r and it is updated at each step as follows:
    - If p < 0, then p = p + 2x + 3 and the next point is (x+1, y)
    - If p >= 0, then p = p + 2(x-y) + 5 and the next point is (x+1, y-1)
  - The algorithm stops when x >= y, as the remaining points can be obtained by symmetry.
- Polar Coordinates Method:
  - It is an algorithm that uses the polar coordinates of the circle to generate the points on the circle.
  - It is based on the idea of using the angle theta and the radius r to calculate the Cartesian coordinates of the points on the circle.
  - It starts from the point (r, 0) and increments the angle theta by a small value delta until it reaches 2*pi radians.
  - It uses the following formulas to calculate the Cartesian coordinates of the points on the circle:
    - x = r * cos(theta)
    - y = r * sin(theta)
  - The algorithm requires floating-point operations and trigonometric functions, which may be costly and inaccurate.
- Trigonometric Method:
  - It is an algorithm that uses the trigonometric identities of the circle to generate the points on the circle.
  - It is based on the idea of using the angle theta and the radius r to calculate the Cartesian coordinates of the points on the circle.
  - It starts from the point (r, 0) and increments the angle theta by a small value delta until it reaches 2*pi radians.
  - It uses the following formulas to calculate the Cartesian coordinates of the points on the circle:
    - x = r * cos(theta)
    - y = r * sin(theta)
  - It also uses the following trigonometric identities to avoid calculating the same values repeatedly



### Mid-point circle generating algorithm

- The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle  .
- It is based on the mid-point theorem which states that if the points along the circumference of a circle are equidistant from the center of the circle, then the points will lie on the circle.
- The algorithm uses the symmetry of the circle to reduce the computation to the first octant only, and then prints the points along with their mirror points in the other octants .
- The algorithm works as follows:

  - Step 1: Assign the starting point coordinates (X0, Y0) as:

    - X0 = 0
    - Y0 = R

  - Step 2: Calculate the value of initial decision parameter P0 as:

    - P0 = 1 - R

  - Step 3: Suppose the current point is (Xk, Yk) and the next point is (Xk+1, Yk+1).

    - If Pk < 0, then the next point is (Xk+1, Yk) and the new decision parameter is:

      - Pk+1 = Pk + 2Xk+1 + 1

    - If Pk >= 0, then the next point is (Xk+1, Yk-1) and the new decision parameter is:

      - Pk+1 = Pk + 2Xk+1 + 1 - 2Yk+1

  - Step 4: Repeat step 3 until Xk >= Yk.

  - Step 5: Print the points (Xk, Yk) along with their mirror points in the other octants using the following relations:

    - (Xk, Yk) -> (Xk, Yk), (-Xk, Yk), (Xk, -Yk), (-Xk, -Yk)
    - (Yk, Xk) -> (Yk, Xk), (-Yk, Xk), (Yk, -Xk), (-Yk, -Xk)

- The algorithm can be generalized to conic sections.
- The algorithm is efficient and simple to implement .
- The algorithm is derived from Bresenham's circle algorithm.



### Parallel algorithms for line generation

- Line generation is a fundamental task in computer graphics, where a straight line segment is approximated by a sequence of pixels on a discrete grid.
- There are several algorithms for line generation, such as DDA (Digital Differential Analyzer), Bresenham's algorithm, and Midpoint algorithm, which are based on incremental calculations of the coordinates of the next pixel along the line.
- However, these algorithms are sequential and require a loop to iterate over the pixels, which can be inefficient for parallel processing or hardware implementation.
- A parallel approach for line generation is to derive the coordinate pairs of the pixels from the line equation, and then use a parallel algorithm to compute and display them.
- One such parallel algorithm is based on the concept of edge functions, which are linear functions that have a value greater than zero on one side of an edge and less than zero on the opposite side. The edge function of a pixel can be interpolated from the edge function of its neighbors, and the sign of the edge function can be used to determine if the pixel is inside or outside the line segment.
- Another parallel algorithm is based on the fact that line generation is equivalent to a vector prefix sums calculation, which is a common operation in parallel computing. The vector prefix sums of a line segment can be computed by a binary tree of processors, where each node performs a simple calculation involving only additions and shifts.
- These parallel algorithms can achieve a speedup of O(log n) over the sequential algorithms, where n is the number of pixels in the line segment. They can also be easily implemented in hardware, such as FPGA (Field Programmable Gate Array) or GPU (Graphics Processing Unit), to achieve high performance and low power consumption.



## Unit 2 - Transformations

- A transformation is a change in the position, size, or shape of a figure.
- There are four main types of transformations: translations, rotations, reflections, and dilations.
- A translation is a transformation that moves every point of a figure by the same distance and in the same direction.
- A rotation is a transformation that turns every point of a figure around a fixed point called the center of rotation by a given angle and in a given direction.
- A reflection is a transformation that flips every point of a figure over a line called the line of reflection.
- A dilation is a transformation that enlarges or reduces every point of a figure by a scale factor with respect to a fixed point called the center of dilation.
- A transformation is called rigid or isometric if it preserves the size and shape of the figure. Translations, rotations, and reflections are rigid transformations.
- A transformation is called non-rigid or similar if it changes the size but not the shape of the figure. Dilations are non-rigid transformations.
- A transformation is called congruent if it maps one figure onto another figure that is exactly the same size and shape. Rigid transformations are congruent transformations.
- A transformation is called similar if it maps one figure onto another figure that has the same shape but not necessarily the same size. Non-rigid transformations are similar transformations.
- A transformation can be described by a rule that gives the coordinates of the image point for each pre-image point. For example, the rule (x, y) -> (x + 3, y - 2) describes a translation that moves every point 3 units to the right and 2 units down.
- A transformation can also be represented by a matrix that gives the coordinates of the image point for each pre-image point. For example, the matrix [[1, 0, 3], [0, 1, -2], [0, 0, 1]] represents the same translation as the rule above.
- A transformation can be composed of two or more transformations applied in sequence. For example, a reflection followed by a rotation is a composition of transformations. The order of the transformations matters in a composition.
- A transformation can be inverted by applying the opposite transformation. For example, the inverse of a translation is a translation in the opposite direction. The inverse of a rotation is a rotation in the opposite direction. The inverse of a reflection is the same reflection. The inverse of a dilation is a dilation with the reciprocal scale factor.



### Basic transformation for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another without changing its size or orientation. It can be represented by a 2x2 matrix that adds a translation vector to the original coordinates of the object. For example, if the translation vector is (tx, ty), then the translation matrix is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- Rotation is the change of orientation of an object around a fixed point or axis. It can be represented by a 2x2 matrix that multiplies the original coordinates of the object by a rotation angle. For example, if the rotation angle is θ, then the rotation matrix is:

| cosθ  -sinθ  0 |
| sinθ  cosθ   0 |
| 0     0      1 |

- Scaling is the change of size of an object by a scaling factor. It can be represented by a 2x2 matrix that multiplies the original coordinates of the object by a scaling factor. For example, if the scaling factor is (sx, sy), then the scaling matrix is:

| sx  0  0 |
| 0  sy  0 |
| 0  0   1 |

- These basic transformations can be combined to form more complex transformations, such as reflection, shear, and dilation. They can also be applied to 3D objects by using 3x3 or 4x4 matrices.



### Matrix representations and homogenous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling and perspective projection in computer graphics.
- Matrix representations allow us to perform multiple transformations in a single operation by multiplying the matrices of each transformation.
- Homogeneous coordinates are a way to extend the normal Cartesian coordinates by adding an extra dimension, usually denoted by w.
- Homogeneous coordinates allow us to represent affine transformations (such as translation) and projective transformations (such as perspective projection) as matrix multiplications, which are not possible in Cartesian coordinates.
- Homogeneous coordinates also allow us to represent points at infinity, which are useful for perspective projection and parallel lines.
- To convert a Cartesian coordinate (x, y) to a homogeneous coordinate, we use the formula (x, y, 1).
- To convert a homogeneous coordinate (x, y, w) to a Cartesian coordinate, we use the formula (x/w, y/w), if w is not zero.
- The matrix representation for translation by (tx, ty) in homogeneous coordinates is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- The matrix representation for rotation by an angle θ in homogeneous coordinates is:

| cosθ  -sinθ  0 |
| sinθ  cosθ   0 |
| 0     0      1 |

- The matrix representation for scaling by (sx, sy) in homogeneous coordinates is:

| sx  0   0 |
| 0   sy  0 |
| 0   0   1 |

- The matrix representation for perspective projection with a focal length f in homogeneous coordinates is:

| 1  0  0  0 |
| 0  1  0  0 |
| 0  0  1  0 |
| 0  0  1/f 0 |

- To apply a matrix transformation M to a point P in homogeneous coordinates, we multiply them as column vectors: P' = M * P
- To apply a sequence of matrix transformations M1, M2, ..., Mn to a point P in homogeneous coordinates, we multiply them from right to left: P' = Mn * ... * M2 * M1 * P



### Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A transformation is a process of changing the position, size, shape, or orientation of an object in a coordinate system.
- A composite transformation is a combination of two or more transformations into a single one that is equivalent to applying the transformations one after another.
- A composite transformation can be represented by a matrix that is obtained by multiplying the matrices of the individual transformations in the order of their application.
- The order of the transformations matters, as some transformations are not commutative, meaning that changing the order will change the result.
- The most common types of transformations in computer graphics are translation, scaling, rotation, and shear.
- Translation is the process of moving an object by a given displacement vector without changing its size, shape, or orientation.
- Scaling is the process of changing the size of an object by a given scale factor along each axis without changing its shape or orientation.
- Rotation is the process of rotating an object by a given angle around a given axis or point without changing its size or shape.
- Shear is the process of distorting an object by a given shear factor along one axis without changing its size or orientation.
- Composite transformations can be used to perform complex transformations that are not possible with a single transformation, such as rotating an object around an arbitrary point, reflecting an object across a line, or projecting an object onto a plane.



### Reflections and Shearing

- Reflections and shearing are two types of transformations in computer graphics that change the position, orientation, or shape of an object.
- A reflection is a transformation that flips an object over a line or a plane, creating a mirror image of the original object. The line or plane is called the axis of reflection or the mirror.
- A shearing is a transformation that slants an object in one or more directions, changing its shape but not its area or volume. The amount of slanting is called the shear factor or the shear angle.
- Some properties and examples of reflections and shearing are:

#### Reflections

- A reflection preserves the size, shape, and orientation of the object, but reverses its handedness (left-right or clockwise-counterclockwise).
- A reflection can be performed in 2D or 3D space, depending on the dimension of the axis of reflection. For example, a 2D reflection can be done over a line, while a 3D reflection can be done over a plane.
- A reflection can be represented by a matrix multiplication, where the matrix depends on the axis of reflection. For example, a reflection over the x-axis can be represented by the matrix:

```
[1  0]
[0 -1]
```

- A reflection can be composed with other transformations, such as rotations, translations, or scaling. For example, a reflection over the line y = x can be obtained by rotating the object by 90 degrees clockwise, then reflecting it over the x-axis, then rotating it by 90 degrees counterclockwise.
- A reflection can be used to create symmetrical patterns, such as kaleidoscopes, snowflakes, or logos.

#### Shearing

- A shearing preserves the area or volume of the object, but changes its shape and orientation.
- A shearing can be performed in 2D or 3D space, depending on the direction of the slanting. For example, a 2D shearing can be done along the x-axis or the y-axis, while a 3D shearing can be done along the x-axis, the y-axis, or the z-axis.
- A shearing can be represented by a matrix multiplication, where the matrix depends on the direction and the shear factor of the slanting. For example, a shearing along the x-axis by a factor of k can be represented by the matrix:

```
[1 k]
[0 1]
```

- A shearing can be composed with other transformations, such as rotations, translations, or scaling. For example, a shearing along the x-axis by a factor of k can be obtained by rotating the object by an angle of arctan(k), then scaling it by a factor of 1/sqrt(1 + k^2), then rotating it by an angle of -arctan(k).
- A shearing can be used to create perspective effects, such as foreshortening, distortion, or skewing.



### Windowing and Clipping

- Windowing is the process of selecting and viewing a part of a picture with different views .
- Clipping is the process of dividing each element of the picture into its visible and invisible portions, and discarding the invisible portion .
- A window is a rectangular region of the picture that defines the area of interest or the view that is to be displayed .
- A viewport is a rectangular region of the display device where the window is mapped to be shown .
- The purpose of windowing and clipping is to improve the efficiency and quality of the graphics output by eliminating the parts of the picture that are outside the viewing area or behind other objects .
- There are different types of clipping algorithms for different types of objects, such as point clipping, line clipping, polygon clipping, text clipping, and curve clipping .
- Some of the common line clipping algorithms are Cohen-Sutherland algorithm, Liang-Barsky algorithm, and Cyrus-Beck algorithm .
- Some of the common polygon clipping algorithms are Sutherland-Hodgman algorithm, Weiler-Atherton algorithm, and Greiner-Hormann algorithm .
- Some of the common curve clipping algorithms are Cohen-Sutherland algorithm, Midpoint subdivision algorithm, and Nicholl-Lee-Nicholl algorithm .



### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that map geometric data from the world coordinate system to the device coordinate system, where they can be displayed on a screen or other output device .
- The viewing pipeline consists of the following stages  :
  - **Modeling transformation**: This stage transforms the geometric data from the object coordinate system (the local coordinate system of each object) to the world coordinate system (the global coordinate system of the scene).
  - **Viewing transformation**: This stage transforms the geometric data from the world coordinate system to the viewing coordinate system (the coordinate system of the camera or the eye).
  - **Projection transformation**: This stage transforms the geometric data from the viewing coordinate system to the normalized device coordinate system (a unit cube that represents the view volume).
  - **Viewport transformation**: This stage transforms the geometric data from the normalized device coordinate system to the device coordinate system (the coordinate system of the output device, such as pixels on a screen).
- The viewing pipeline can be applied to both 2D and 3D data, with some differences in the projection and viewport transformations  :
  - For 2D data, the projection transformation is usually a parallel projection that preserves the shape and size of the objects, and the viewport transformation is a scaling and translation that maps the view window (a rectangular region in the viewing coordinate system) to the view port (a rectangular region in the device coordinate system).
  - For 3D data, the projection transformation can be either a parallel projection or a perspective projection that creates a realistic sense of depth and perspective, and the viewport transformation is a scaling, translation and clipping that maps the view volume (a pyramidal or prismatic region in the viewing coordinate system) to the view port.
- The viewing pipeline can be implemented using matrices and matrix multiplication, which allow for easy concatenation and manipulation of the transformations .
- The viewing pipeline is an essential concept in computer graphics, as it enables the creation and display of realistic and interactive scenes and animations .



### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the mappings of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are part of the viewing pipeline, which consists of the following stages :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation.
  - Define the projection type, which can be parallel or perspective, and the projection plane, which is the plane where the picture is projected onto.
  - Define the window, which is the rectangular region of the projection plane that contains the picture of interest.
  - Define the viewport, which is the rectangular region of the display device where the window is mapped to.
  - Apply the viewing transformation, which is the transformation from the WCS to the VCS.
  - Apply the projection transformation, which is the transformation from the VCS to the projection plane.
  - Apply the window-to-viewport transformation, which is the transformation from the window to the viewport.
  - Apply the clipping, which is the process of removing objects, lines, or line segments that are outside the window or the viewport.
- Viewing transformations can be represented by matrices, and can be composed by matrix multiplication.
- Viewing transformations can affect the appearance, size, shape, and perspective of the objects in the picture.



### 2-D Clipping algorithms

- Clipping is the process of removing or hiding the parts of graphics primitives that lie outside a specified region of interest, such as the viewport or the window .
- Clipping is useful for improving the efficiency and quality of rendering, as well as for implementing effects such as fog, shadows, or depth of field.
- In 2D, the clipping process can be applied to a variety of graphics primitives such as points, lines, polygons and curves. Clipping is performed with respect to a clipping boundary, which may be a convex or concave polygonal boundary.
- There are different algorithms for clipping different types of primitives. Some of the common 2D clipping algorithms are:
  - Point clipping: This algorithm determines whether a given point lies inside or outside the clipping boundary . A simple way to do this is to test the point against each edge of the boundary and check if it satisfies the edge equation . If the point satisfies all the edge equations, it is inside the boundary; otherwise, it is outside .
  - Line clipping: This algorithm determines which part of a given line segment lies inside or outside the clipping boundary . There are several line clipping algorithms, such as Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, and Nicholl-Lee-Nicholl  . These algorithms use different techniques to find the intersection points of the line segment with the boundary edges, and then discard or retain the appropriate subsegments  .
  - Polygon clipping: This algorithm determines which part of a given polygon lies inside or outside the clipping boundary. There are several polygon clipping algorithms, such as Sutherland-Hodgman, Weiler-Atherton, Greiner-Hormann, and Vatti. These algorithms use different techniques to find the intersection points of the polygon edges with the boundary edges, and then generate new vertices and edges to form the clipped polygon.
  - Curve clipping: This algorithm determines which part of a given curve lies inside or outside the clipping boundary. There are several curve clipping algorithms, such as Cohen-Sutherland for conic sections, Bezier clipping for Bezier curves, and de Casteljau subdivision for B-splines. These algorithms use different techniques to find the intersection points of the curve with the boundary edges, and then split or approximate the curve to form the clipped curve.



### Line clipping algorithms

- Line clipping is the process of removing (clipping) lines or portions of lines outside an area of interest (a viewport or view volume) in computer graphics.
- Line clipping is useful for rendering only the visible parts of a scene, reducing the computational cost and improving the performance of graphics applications.
- There are many algorithms for line clipping, but two of the most common ones are Cohen–Sutherland and Liang–Barsky.
- Cohen–Sutherland algorithm:
  - It divides a 2D space into 9 regions, of which only the middle part (viewport) is visible.
  - It assigns a 4-bit code to each endpoint of a line, based on its position relative to the viewport boundaries (top, bottom, left, right).
  - It uses bitwise operations to determine if a line is trivially accepted (both endpoints inside the viewport), trivially rejected (both endpoints outside the viewport and on the same side), or partially clipped (one or both endpoints outside the viewport and on different sides).
  - It uses the parametric equation of a line to find the intersection points of the line with the viewport edges, and replaces the outside endpoints with the intersection points.
  - It repeats the process until all lines are either accepted or rejected.
- Liang–Barsky algorithm:
  - It uses the parametric equation of a line and the inequalities of the viewport boundaries to find four parameters that define the visible portion of the line.
  - It compares the four parameters to determine if a line is trivially accepted, trivially rejected, or partially clipped.
  - It uses the four parameters to calculate the intersection points of the line with the viewport edges, and replaces the outside endpoints with the intersection points.
  - It is more efficient than Cohen–Sutherland algorithm, as it requires fewer calculations and comparisons.



### Cohen Sutherland line clipping algorithm

- Line clipping is a process of removing the portions of a line that are outside a given rectangular window, while preserving the portions that are inside or on the boundary of the window.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport).
- The algorithm can be outlined as follows:
  - Nine regions are created, eight "outside" regions and one "inside" region. Each region is assigned a 4-bit code, called the outcode, that indicates its position relative to the window boundaries. The outcode is computed by testing the x and y coordinates of the endpoints of the line against the window boundaries.
  - If both endpoints have the same outcode, and it is not zero, then the line is completely outside the window and can be discarded.
  - If both endpoints have a zero outcode, then the line is completely inside the window and can be drawn.
  - If the endpoints have different outcodes, then the line may be partially inside the window and needs to be clipped. The algorithm finds an intersection point between the line and one of the window boundaries, and replaces the endpoint that is outside the window with the intersection point. The outcode of the new endpoint is then recomputed and the process is repeated until one of the previous cases is encountered.
- The algorithm is efficient because it performs only simple bit operations and comparisons, and avoids unnecessary calculations of intersection points.
- The algorithm works only for rectangular windows. For other shapes of windows, other algorithms such as Cyrus Beck algorithm or Sutherland Hodgman algorithm are needed.
- The algorithm can be implemented using the following pseudocode:

```
function clipLine(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
  // compute the outcodes for the endpoints
  outcode1 = computeOutcode(x1, y1, xmin, ymin, xmax, ymax)
  outcode2 = computeOutcode(x2, y2, xmin, ymin, xmax, ymax)
  // loop until the line is either accepted or rejected
  while true
    // if both outcodes are zero, the line is inside the window
    if outcode1 == 0 and outcode2 == 0
      return (x1, y1, x2, y2) // accept the line
    // if the logical AND of the outcodes is not zero, the line is outside the window
    else if outcode1 & outcode2 != 0
      return null // reject the line
    // otherwise, the line is partially inside the window and needs to be clipped
    else
      // choose an endpoint that is outside the window
      if outcode1 != 0
        outcode = outcode1
      else
        outcode = outcode2
      // find the intersection point with the window boundary
      // using the slope of the line (m = (y2 - y1) / (x2 - x1))
      // and the bitwise operations to test the outcode bits
      if outcode & TOP // point is above the window
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
        y = ymax
      else if outcode & BOTTOM // point is below the window
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
        y = ymin
      else if outcode & RIGHT // point is to the right of the window
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
      else if outcode & LEFT // point is to the left of the window
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
      // replace the endpoint that is outside the window with the intersection point
      if outcode == outcode1
        x1 = x
        y1 = y
        outcode1 = computeOutcode(x1, y1, xmin, ymin, xmax, ymax)
      else
        x2 = x
        y2 = y
        outcode2 = computeOutcode(x2, y2, xmin, ymin,

```




### Liang Barsky algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is based on the parametric equation of a line, which is given by:

    `x = x1 + u * (x2 - x1)`

    `y = y1 + u * (y2 - y1)`

    where `(x1, y1)` and `(x2, y2)` are the end points of the line, and `u` is a parameter that varies from 0 to 1.

- The algorithm also uses four inequalities that describe the range of the clipping window, which are:

    `xwmin <= x <= xwmax`

    `ywmin <= y <= ywmax`

    where `(xwmin, ywmin)` and `(xwmax, ywmax)` are the lower-left and upper-right corners of the window, respectively.

- The algorithm works by finding the values of `u` that satisfy the four inequalities, and then using the minimum and maximum values of `u` to compute the intersection points of the line and the window.

- The algorithm can be summarized by the following steps :

    1. Initialize `u1 = 0` and `u2 = 1`, which represent the lower and upper bounds of the visible portion of the line.
    2. For each of the four boundaries of the window, calculate the value of `u` that corresponds to the intersection of the line and the boundary, using the parametric equation and the inequality. Let `p` and `q` be the coefficients of `u` in the inequality, such that `p * u + q <= 0` or `p * u + q >= 0`, depending on the boundary.
    3. If `p < 0`, then the line is entering the window. Update `u1 = max(u1, q / p)`.
    4. If `p > 0`, then the line is leaving the window. Update `u2 = min(u2, q / p)`.
    5. If `p = 0` and `q < 0`, then the line is parallel to and outside the window. Reject the line and exit the algorithm.
    6. If `u1 > u2`, then the line is outside the window. Reject the line and exit the algorithm.
    7. Otherwise, the line is partially or completely inside the window. Accept the line and calculate the intersection points using the parametric equation and the values of `u1` and `u2`.

- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the fastest parametric line-clipping algorithm.

- An example of the algorithm is shown below, where the line `(x1, y1) = (10, 10)` and `(x2, y2) = (80, 80)` is clipped by the window `(xwmin, ywmin) = (20, 20)` and `(xwmax, ywmax) = (60, 60)`.

    Liang Barsky example

    - The values of `p` and `q` for each boundary are:

        | Boundary | Inequality | p | q |
        |----------|------------|---|---|
        | Left | x >= xwmin | x2 - x1 | xwmin - x1 |
        | Right | x <= xwmax | x1 - x2 | x2 - xwmax |
        | Bottom | y >= ywmin | y2 - y1 | ywmin - y1 |
        | Top | y <= ywmax | y1 - y2 | y2 - ywmax |

    - The values of `u` for each boundary are:

        | Boundary | u |
        |----------|---|
        | Left | 0.125 |
        | Right | 0.625 |
        | Bottom | 0.125 |
        | Top | 0.625 |

    - The values of `u1` and `



### Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a rectangular window or a convex polygon.
- Line clipping algorithms are useful for computer graphics applications, such as rendering, clipping, and visibility testing.
- There are different algorithms for line clipping, depending on the shape and properties of the clipping region. Some of the common algorithms are:

  - Cohen-Sutherland algorithm: This algorithm is suitable for clipping a line against a rectangular window. It uses a region code for each endpoint of the line to determine whether the line is inside, outside, or partially inside the window. It also uses a logical AND operation to test whether the line intersects any of the window edges. This algorithm is simple and efficient, but it may require repeated clipping for lines that cross multiple window edges.
  - Cyrus-Beck algorithm: This algorithm is suitable for clipping a line against a convex polygon. It uses a parametric equation for the line and a normal vector for each edge of the polygon to calculate the intersection points. It also uses a dot product to test whether the intersection points lie on the polygon edges. This algorithm is more general and robust than the Cohen-Sutherland algorithm, but it may require more computations for complex polygons .
  - Liang-Barsky algorithm: This algorithm is a modification of the Cohen-Sutherland algorithm that avoids unnecessary intersection calculations. It uses a parametric equation for the line and four inequalities for the window edges to find the minimum and maximum values of the parameter that define the visible portion of the line. This algorithm is more efficient and accurate than the Cohen-Sutherland algorithm, but it is still limited to rectangular windows .
  - Sutherland-Hodgman algorithm: This algorithm is suitable for clipping a polygon against another polygon. It uses a divide-and-conquer approach that clips the subject polygon against each edge of the clipping polygon in turn. It also uses a point-in-polygon test to determine whether a vertex of the subject polygon is inside or outside the clipping polygon. This algorithm is more versatile and flexible than the previous algorithms, but it may generate degenerate polygons or self-intersecting polygons in some cases .



### Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - Preventing undesirable effects on the output device when rendering polygons that extend beyond the window boundaries.
  - Performing hidden surface removal and generating high-quality surface details using techniques such as beam tracing.
  - Distributing the objects of a scene to appropriate processors in multiprocessor raytracing systems to improve rendering speeds.
  - Applying two-dimensional transformations such as scaling, rotation, translation, and shearing to polygons.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against each edge of the clipping window in turn, generating a new polygon as the output. The algorithm uses the concept of inside and outside vertices, and generates new vertices at the intersection points of the polygon edges and the clipping window edges .
  - Weiler-Atherton algorithm: This algorithm clips a polygon against another polygon, generating one or more closed areas as the output. The algorithm uses the concept of entry and exit vertices, and generates new vertices at the intersection points of the polygon edges and the clipping polygon edges.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against another polygon, generating one or more closed areas as the output. The algorithm uses the concept of winding numbers, and marks the vertices of the polygons as inside or outside based on their winding numbers.
- Polygon clipping can be implemented using various data structures, such as:
  - Linked lists: This data structure can store the vertices of the polygons and the clipping window, and allow easy insertion and deletion of new vertices during the clipping process.
  - Doubly connected edge lists: This data structure can store the vertices, edges, and faces of the polygons and the clipping window, and allow easy traversal and manipulation of the polygon boundaries during the clipping process.



### Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon in clockwise order.
- The algorithm then clips the input polygon against each edge of the clip polygon, one at a time, and produces a new list of vertices for the output polygon.
- The algorithm repeats this process for all four edges of the clip polygon, and the final output polygon is the result of the clipping.
- The algorithm can handle concave subject polygons, but the clip polygon must be convex.
- The algorithm can also handle holes in the subject polygon, by reversing the order of the vertices for the hole and treating it as a separate polygon.
- The algorithm is efficient and simple to implement, but it can produce degenerate cases, such as when a vertex lies on an edge of the clip polygon, or when an edge of the subject polygon is parallel to an edge of the clip polygon.
- The algorithm can be modified to handle these cases, by using a different vertex selection rule, or by introducing a small perturbation to the vertices or the edges.

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks



### Weiler and Atherton polygon clipping

- Weiler and Atherton polygon clipping is a polygon clipping algorithm that can handle concave polygons and polygons with holes.
- Polygon clipping is the process of cutting out a part of a polygon that lies outside a given clipping region, such as a window or a viewport.
- The algorithm works by finding the intersection points of the subject polygon and the clipping polygon, and labeling them as entry or exit points  .
- The algorithm then traverses the subject polygon in a clockwise direction, starting from any entry point, and copies the vertices to the output polygon until an exit point is reached  .
- The algorithm then switches to the clipping polygon and traverses it in a counter-clockwise direction, copying the vertices to the output polygon until an entry point is reached  .
- The algorithm repeats this process until all the entry and exit points are visited, and the output polygon is closed  .
- The algorithm can handle multiple output polygons if the subject polygon is split into disjoint parts by the clipping polygon  .
- The algorithm can also handle holes in the subject polygon by using a special flag to indicate whether a vertex is inside or outside a hole.
- The algorithm can be implemented using data structures such as doubly linked lists or circular lists to store the vertices and the intersection points  .
- The algorithm has a time complexity of O(n + m), where n and m are the number of vertices in the subject and clipping polygons, respectively .



### Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest, such as a rectangular window.
- Curve clipping involves complex procedures as compared to line clipping, because curves are not linear and may have multiple intersections with the window boundaries.
- Curve clipping requires more processing than for objects with linear boundaries, because it may involve finding the parametric values of the curve at the intersection points, splitting the curve into segments, and discarding the segments that are outside the window.
- There are different algorithms for curve clipping, depending on the type of curve and the shape of the window. Some examples are:
  - Cohen-Sutherland algorithm for line clipping, which can be extended to quadratic curves by using the convex hull property.
  - Liang-Barsky algorithm for line clipping, which can be extended to cubic curves by using the convex hull property.
  - Sutherland-Hodgman algorithm for polygon clipping, which can be applied to any curve by approximating it with a polygon.
  - Cyrus-Beck algorithm for line clipping, which can be generalized to any convex window and any curve by using the normal vectors of the window edges.
- Curve clipping can be used for various purposes, such as:
  - Improving the performance and efficiency of rendering by avoiding unnecessary calculations for the parts of the curve that are not visible.
  - Creating artistic effects, such as masking, cropping, or framing, by using different shapes of windows.
  - Implementing user interactions, such as zooming, panning, or selecting, by changing the size and position of the window.



### Text clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Text clipping is a process of clipping the string, which means removing the characters or parts of characters that are outside the clipping window.
- Text clipping is useful for displaying text in a limited area, such as a menu, a label, or a title.
- Text clipping depends on the methods used to generate characters and the requirements of a particular application.
- There are three main methods for text clipping:
  - All or none string clipping: This method clips the whole string if any part of it is outside the clipping window. It is simple but may result in loss of information.
  - Text clipping: This method clips only the characters or parts of characters that are outside the clipping window. It preserves more information but may produce distorted or incomplete characters.
  - Text clipping with character precision: This method clips the characters or parts of characters that are outside the clipping window, but also adjusts the spacing and alignment of the remaining characters to avoid gaps or overlaps. It produces the best visual quality but is more complex and time-consuming.



## Unit 3 - Three Dimensional

- In this unit, you will learn about the concepts and properties of three dimensional (3D) shapes and objects.
- A 3D shape or object is one that has length, width and height. It occupies some space and has volume.
- Some examples of 3D shapes are cubes, spheres, cylinders, cones, pyramids, prisms, etc.
- You can describe a 3D shape or object by its faces, edges and vertices.
  - A face is a flat or curved surface of a 3D shape or object. For example, a cube has six square faces.
  - An edge is a line segment where two faces meet. For example, a cube has 12 edges.
  - A vertex is a point where three or more edges meet. For example, a cube has 8 vertices.
- You can also classify 3D shapes or objects by their symmetry, nets and cross-sections.
  - A 3D shape or object has symmetry if it can be divided into two identical parts by a plane or a line. For example, a cube has six planes of symmetry and four lines of symmetry.
  - A net is a two dimensional (2D) shape that can be folded to form a 3D shape or object. For example, a net of a cube is a square with four attached squares on each side.
  - A cross-section is a 2D shape that is formed by cutting a 3D shape or object by a plane. For example, a cross-section of a cylinder can be a circle, an ellipse, a rectangle or a parallelogram, depending on the angle and position of the plane.
- You can also measure and calculate the surface area and volume of 3D shapes or objects using formulas and methods.
  - The surface area of a 3D shape or object is the total area of all its faces. For example, the surface area of a cube is 6s^2, where s is the length of a side.
  - The volume of a 3D shape or object is the amount of space it occupies. For example, the volume of a cube is s^3, where s is the length of a side.
  - Some common formulas for surface area and volume of 3D shapes or objects are:

| Shape | Surface Area | Volume |
| ----- | ------------ | ------ |
| Cube | 6s^2 | s^3 |
| Rectangular Prism | 2(lw + lh + wh) | lwh |
| Cylinder | 2πr^2 + 2πrh | πr^2h |
| Cone | πr^2 + πrl | (1/3)πr^2h |
| Sphere | 4πr^2 | (4/3)πr^3 |
| Pyramid | (1/2)pl + B | (1/3)Bh |

where l, w, h are the length, width and height of the shape, r is the radius of the base, s is the slant height, p is the perimeter of the base, and B is the area of the base.



### 3-D Geometric Primitives

- 3-D geometric primitives are basic geometric forms that can be used to model more complex 3-D shapes and objects  .
- They are also called 3-D primitives or simply primitives.
- Some common 3-D primitives are cubes, pyramids, cones, spheres, cylinders, and tori  .
- 3-D primitives can be modified with transforms (such as translation, rotation, scaling, and shearing) and Booleans (such as union, intersection, and difference) to create new shapes .
- 3-D primitives can also have a resolution level assigned to them, which determines the number of sides and steps used to define them. A higher resolution makes the primitive look smoother, but also increases the complexity and memory usage .
- Some 3-D primitives can be defined by a single point (such as a sphere or a cone), while others require two or more points (such as a cube or a cylinder). The points can be specified by their coordinates or by using a mouse or a stylus .
- Some 3-D primitives can also be defined by curves, such as Bézier curves, circles, ellipses, and splines. Curves can be used to create smooth and organic shapes, such as flowers, leaves, and faces .
- 3-D primitives are useful for creating simple and abstract models, such as logos, icons, and diagrams. They can also be used as the starting point for more detailed and realistic models, such as characters, vehicles, and buildings .



### 3-D Object Representation

- 3-D object representation is the process of developing a mathematical coordinate-based representation of any surface of an object in three dimensions via specialized software .
- 3-D object representation is essential for computer graphics applications such as animation, rendering, simulation, and gaming.
- 3-D object representation can be divided into two main categories: boundary representations and space-partitioning representations.
- Boundary representations (B-reps) describe a 3-D object as a set of surfaces that separates the object interior from the environment. B-reps are useful for modeling solid objects with well-defined boundaries and complex shapes. B-reps can be further classified into polygonal meshes, parametric surfaces, implicit surfaces, and subdivision surfaces.
- Polygonal meshes are the most common type of B-reps, which consist of a collection of vertices, edges, and faces (usually triangles or quadrilaterals) that define the shape of the object. Polygonal meshes are easy to manipulate, store, and render, but they may suffer from aliasing, cracks, and holes.
- Parametric surfaces are B-reps that define the shape of the object using mathematical functions of one or more parameters. Parametric surfaces can represent smooth and curved surfaces with high accuracy, but they may be difficult to edit, intersect, and tessellate.
- Implicit surfaces are B-reps that define the shape of the object using a scalar function that assigns a value to every point in space. The object is then defined as the set of points where the function is zero (or some other threshold). Implicit surfaces can represent complex and organic shapes with ease, but they may be challenging to render, deform, and convert to other representations.
- Subdivision surfaces are B-reps that define the shape of the object using a coarse polygonal mesh and a set of rules to refine it recursively. Subdivision surfaces can represent smooth and detailed surfaces with low memory requirements, but they may be computationally expensive and hard to control.
- Space-partitioning representations describe the interior properties of a 3-D object by dividing the space into smaller regions and assigning attributes to each region. Space-partitioning representations are useful for modeling volumetric objects with heterogeneous materials and internal structures. Space-partitioning representations can be further classified into voxel grids, octrees, and constructive solid geometry (CSG) trees.
- Voxel grids are space-partitioning representations that divide the space into a regular grid of cubic cells (voxels) and store the properties of each voxel in a 3-D array. Voxel grids can represent objects with high resolution and fidelity, but they may consume a lot of memory and processing power.
- Octrees are space-partitioning representations that divide the space into a hierarchical tree of cubic cells, where each cell can be further subdivided into eight smaller cells if needed. Octrees can represent objects with variable resolution and adaptivity, but they may introduce artifacts and discontinuities at different levels of detail.
- CSG trees are space-partitioning representations that define the shape of the object using a set of primitive solids (such as spheres, cubes, cylinders, etc.) and boolean operations (such as union, intersection, and difference) to combine them. CSG trees can represent objects with simple and regular shapes, but they may be inefficient and ambiguous for complex and irregular shapes.



### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a coordinate triplet (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve the parallelism and ratios of distances between points, but not the angles or lengths. Examples of affine transformations are translation, scaling, rotation, and shear.
- Non-affine transformations do not preserve any of the properties of the original shape. Examples of non-affine transformations are perspective projection, bending, and twisting.
- 3-D transformation can be performed using matrices, which are convenient for combining multiple transformations into one.
- A 3-D transformation matrix is a 4x4 matrix that operates on a 4D homogeneous coordinate vector, where the fourth coordinate is 1 for a point and 0 for a vector.
- The general form of a 3-D transformation matrix is:

| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| m | n | o | p |

- The matrix can be decomposed into three parts: a 3x3 linear transformation matrix, a 3x1 translation vector, and a 1x4 perspective vector.
- The linear transformation matrix affects the rotation, scaling, and shear of the shape, while the translation vector affects the position of the shape, and the perspective vector affects the projection of the shape.
- Some common 3-D transformation matrices are:

- Translation by (tx, ty, tz):

| 1 | 0 | 0 | tx |
|---|---|---|----|
| 0 | 1 | 0 | ty |
| 0 | 0 | 1 | tz |
| 0 | 0 | 0 | 1  |

- Scaling by (sx, sy, sz):

| sx | 0  | 0  | 0 |
|----|----|----|---|
| 0  | sy | 0  | 0 |
| 0  | 0  | sz | 0 |
| 0  | 0  | 0  | 1 |

- Rotation about x-axis by angle θ:

| 1 | 0      | 0       | 0 |
|---|--------|---------|---|
| 0 | cos θ  | -sin θ  | 0 |
| 0 | sin θ  | cos θ   | 0 |
| 0 | 0      | 0       | 1 |

- Rotation about y-axis by angle θ:

| cos θ  | 0 | sin θ  | 0 |
|--------|---|--------|---|
| 0      | 1 | 0      | 0 |
| -sin θ | 0 | cos θ  | 0 |
| 0      | 0 | 0      | 1 |

- Rotation about z-axis by angle θ:

| cos θ  | -sin θ | 0 | 0 |
|--------|--------|---|---|
| sin θ  | cos θ  | 0 | 0 |
| 0      | 0      | 1 | 0 |
| 0      | 0      | 0 | 1 |

- Shear along x-axis by factors shx and shy:

| 1  | shx | 0  | 0 |
|----|-----|----|---|
| shy| 1   | 0  | 0 |
| 0  | 0   | 1  | 0 |
| 0  | 0   | 0  | 1 |

- Shear along y-axis by factors shy and shz:

| 1  | 0  | 0  | 0 |
|----|----|----|---|
| 0  | 1  | shy| 0 |
| 0  | shz| 1  | 0 |
| 0  | 0  | 0  | 1 |

- Shear along z-axis by factors shz and shx:

| 1  | 0  | shx| 0 |
|----|----|----|---|
| 0  | 1  | 0  | 0 |
|



### 3-D viewing for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

- 3-D viewing is the process of generating and displaying 3-D computer graphics on a 2-D or 3-D display device .
- 3-D viewing involves two main steps: 3-D modeling and 3-D projection .
- 3-D modeling is the creation of 3-D models using 3-D modeling software or modelers. 3-D models are composed of basic geometric primitives such as points, lines, triangles and other polygonal patches.
- 3-D projection is the transformation of 3-D models into 2-D or 3-D images that can be displayed on a screen or a projection plane. 3-D projection involves two sub-steps: modeling transformation and viewing transformation.
- Modeling transformation is the manipulation of 3-D models using 3-D transformations such as translation, rotation, scaling, shearing, reflection and projection. Modeling transformation changes the position, orientation, size and shape of 3-D models in the 3-D world coordinate system.
- Viewing transformation is the specification of the observer viewing position and the position of the projection plane in the 3-D world coordinate system. Viewing transformation defines the viewing-coordinate system, which is used as a reference for projecting 3-D models onto the projection plane.
- There are different types of 3-D projection methods, such as parallel projection and perspective projection. Parallel projection preserves the relative sizes and shapes of 3-D models, but does not create the illusion of depth. Perspective projection creates the illusion of depth by reducing the size of objects as they recede from the viewer, but distorts the shapes of objects.
- 3-D viewing can be used for various applications, such as movies, video games, graphics and virtual reality  . 3-D viewing can create realistic, immersive and interactive 3-D scenes that can enhance the user experience and engagement.



### Projections for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

- Projection is a technique or process which is used to transform a 3D object into a 2D plane.
- Projection is necessary to display a 3D object on a 2D screen or paper.
- There are two main types of projection: parallel projection and perspective projection  .
- Parallel projection is a type of projection where the direction of projection is parallel to the projection plane. Parallel projection preserves the relative proportions and angles of the 3D object, but does not show the depth or distance  .
- Parallel projection can be further classified into orthographic projection, oblique projection, and isometric projection  .
- Orthographic projection is a type of parallel projection where the direction of projection is normal to the projection plane. Orthographic projection shows the true shape and size of the 3D object, but does not show the perspective or foreshortening   .
- Oblique projection is a type of parallel projection where the direction of projection is not normal to the projection plane. Oblique projection shows the front face of the 3D object in true shape and size, but the other faces are distorted and appear slanted  .
- Isometric projection is a special case of oblique projection where the direction of projection makes equal angles with the three principal axes of the 3D object. Isometric projection shows the three visible faces of the 3D object in equal proportions, but does not show the true shape and size of the object  .
- Perspective projection is a type of projection where the direction of projection is not parallel to the projection plane, but converges to a single point called the center of projection or the eye point. Perspective projection shows the 3D object as it appears to the human eye, with the depth and distance effects. Objects that are closer to the eye point appear larger and objects that are farther away appear smaller  .
- Perspective projection can be further classified into one-point, two-point, and three-point perspective, depending on the number of vanishing points on the projection plane. A vanishing point is a point where parallel lines appear to converge in perspective projection  .
- One-point perspective is a type of perspective projection where there is only one vanishing point on the projection plane. One-point perspective is used when the 3D object is parallel to two of the principal axes and perpendicular to the third axis  .
- Two-point perspective is a type of perspective projection where there are two vanishing points on the projection plane. Two-point perspective is used when the 3D object is parallel to one of the principal axes and oblique to the other two axes  .
- Three-point perspective is a type of perspective projection where there are three vanishing points on the projection plane. Three-point perspective is used when the 3D object is oblique to all three principal axes  .
- The following diagrams illustrate the different types of projection:

Parallel projection

Parallel projection

Orthographic projection

Orthographic projection

Oblique projection

Oblique projection

Isometric projection

Isometric projection

Perspective projection

Perspective projection

One-point perspective

One-point perspective

Two-point perspective

Two-point perspective



### 3-D Clipping

- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene.
- The purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects.
- 3-D clipping can be done in two basic steps:
  - Discard objects that cannot be viewed, such as objects that are behind the camera, outside the field of view, or too far away.
  - Clip objects that intersect with any clipping plane, such as the near and far planes, or the left, right, top and bottom planes of the viewing volume.
- 3-D clipping can be done before or after projection, depending on the coordinate system and the clipping algorithm used .
- 3-D clipping algorithms can use various techniques, such as outcodes, parametric equations, homogeneous coordinates, or Sutherland-Hodgman algorithm, to determine the intersection points of the objects with the clipping planes and generate the clipped polygons  .



## Unit 4 - Curves and Surfaces

- In this unit, we will learn about the mathematical representation and manipulation of curves and surfaces, which are essential for computer graphics and animation.
- A curve is a one-dimensional object that can be defined by a function, a parametric equation, or a set of control points.
- A surface is a two-dimensional object that can be defined by a function, a parametric equation, or a set of control points.
- Some common types of curves and surfaces are:
  - Line: a straight curve defined by two points or a slope and an intercept.
  - Circle: a curve defined by a center point and a radius.
  - Ellipse: a curve defined by a center point, two axes, and two radii.
  - Parabola: a curve defined by a focus point and a directrix line.
  - Hyperbola: a curve defined by two focus points and two asymptotes.
  - Bezier curve: a curve defined by a set of control points and a degree.
  - B-spline curve: a curve defined by a set of control points and a knot vector.
  - NURBS curve: a curve defined by a set of control points, a knot vector, and a weight vector.
  - Plane: a flat surface defined by a normal vector and a distance from the origin.
  - Sphere: a surface defined by a center point and a radius.
  - Ellipsoid: a surface defined by a center point, three axes, and three radii.
  - Cylinder: a surface defined by a center line, a radius, and two end points.
  - Cone: a surface defined by a vertex point, a base circle, and a height.
  - Torus: a surface defined by a center point, a major radius, and a minor radius.
  - Bezier surface: a surface defined by a grid of control points and two degrees.
  - B-spline surface: a surface defined by a grid of control points and two knot vectors.
  - NURBS surface: a surface defined by a grid of control points, two knot vectors, and a weight matrix.
- To manipulate curves and surfaces, we can use various operations such as:
  - Translation: moving a curve or surface by a vector.
  - Rotation: rotating a curve or surface by an angle around an axis.
  - Scaling: resizing a curve or surface by a factor along each axis.
  - Shearing: skewing a curve or surface by an angle along each axis.
  - Affine transformation: a combination of translation, rotation, scaling, and shearing.
  - Homogeneous transformation: an affine transformation that preserves the perspective of a curve or surface.
  - Inverse transformation: the opposite of a transformation that restores the original curve or surface.
  - Composition: applying multiple transformations in sequence to a curve or surface.
  - Interpolation: finding a curve or surface that passes through a given set of points.
  - Approximation: finding a curve or surface that is close to a given set of points.
  - Subdivision: dividing a curve or surface into smaller segments or patches.
  - Blending: combining two or more curves or surfaces into a smooth transition.
  - Extrusion: creating a surface by sweeping a curve along a path.
  - Revolution: creating a surface by rotating a curve around an axis.
  - Lofting: creating a surface by interpolating between two or more curves.
  - Deformation: changing the shape of a curve or surface by moving its control points.
  - Evaluation: finding the point, tangent, normal, or curvature of a curve or surface at a given parameter value.
  - Intersection: finding the point or curve where two curves or surfaces meet.
  - Clipping: removing the parts of a curve or surface that are outside a given region.
  - Tessellation: converting a curve or surface into a mesh of triangles or polygons.



### Quadric surfaces

- Quadric surfaces are common modeling primitives for a variety of computer graphics and computer-aided-design applications .
- Quadric surfaces are the graphs of equations that can be expressed in the form `Ax^2 + By^2 + Cz^2 + Dxy + Exz + Fyz + Gx + Hy + Jz + K = 0`.
- Quadric surfaces are the 3D counterparts of conic sections and have six distinct types:
  - Ellipsoid: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 + z^2/c^2 = 1`. It is a closed surface that resembles a stretched sphere.
  - Elliptic paraboloid: a surface described by an equation of the form `z = x^2/a^2 + y^2/b^2`. It is an open surface that resembles a parabolic bowl.
  - Hyperbolic paraboloid: a surface described by an equation of the form `z = x^2/a^2 - y^2/b^2`. It is an open surface that resembles a saddle.
  - Hyperboloid of one sheet: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 1`. It is an open surface that resembles a double cone with a waist.
  - Hyperboloid of two sheets: a surface described by an equation of the form `x^2/a^2 - y^2/b^2 - z^2/c^2 = 1`. It is a closed surface that consists of two disjoint pieces.
  - Cone: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 0`. It is an open surface that resembles a pointed hat.
- Quadric surfaces can be rendered using ray tracing or ray firing, which is a method of simulating the interaction of light rays with the surface .
- Quadric surfaces can also be transformed using matrix operations, such as translation, rotation, scaling, and shearing.
- Quadric surfaces can be classified using the eigenvalues of the matrix formed by the coefficients of the quadratic terms. The number and sign of the nonzero eigenvalues determine the type of the quadric surface.



### Spheres

- A sphere is a three-dimensional object that has a round shape and a constant radius from its center.
- In computer graphics, spheres are often used to model objects such as balls, planets, bubbles, etc.
- Spheres can be represented mathematically by the equation: x^2 + y^2 + z^2 = r^2, where r is the radius and (x, y, z) are the coordinates of any point on the sphere.
- Spheres can also be defined parametrically by the equations: x = r cos(u) cos(v), y = r cos(u) sin(v), z = r sin(u), where u and v are the angles of longitude and latitude, respectively, and r is the radius.
- Spheres can be approximated by simpler objects constructed from flat polygons (polyhedra) by dividing the surface into small patches and drawing triangles or quadrilaterals that connect the vertices of the patches.
- A bounding sphere is a special type of bounding volume that encloses a set of points or objects in a sphere. It is used in computer graphics and computational geometry to perform collision detection, visibility testing, and other operations .
- A bounding sphere can be constructed by finding the smallest sphere that contains all the points or objects, or by finding the sphere that minimizes some criterion such as the volume or the surface area. There are several fast and simple bounding sphere construction algorithms with a high practical value in real-time computer graphics applications .



### Ellipsoid

- An ellipsoid is a surface that may be obtained from a sphere by deforming it by means of directional scalings, or more generally, of an affine transformation.
- An ellipsoid is a quadric surface; that is, a surface that may be defined as the zero set of a polynomial of degree two in three variables.
- The general equation of an ellipsoid centered at the origin is:

$$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$$

where $a$, $b$, and $c$ are the semi-axes of the ellipsoid along the $x$, $y$, and $z$ axes, respectively.
- An ellipsoid can be parameterized by two angles, $\theta$ and $\phi$, as follows:

$$x = a \cos \theta \cos \phi$$
$$y = b \cos \theta \sin \phi$$
$$z = c \sin \theta$$

where $0 \leq \theta \leq \pi$ and $0 \leq \phi \leq 2\pi$.
- An ellipsoid can be used in computer graphics as a primitive shape for modeling and rendering .
- An ellipsoid can be drawn in computer graphics using algorithms such as the midpoint ellipse algorithm, which plots points of an ellipse on the first quadrant by dividing the quadrant into two regions.
- An ellipsoid can be triangulated into a polygon mesh by sampling the parametric model of the ellipsoid and connecting the vertices with triangles.



### Blobby objects

- Blobby objects are a type of implicit modeling technique in computer graphics that can represent non-rigid and fluid-like objects .
- Blobby objects are defined by a set of primitive shapes, such as spheres, cylinders, or ellipsoids, that have a scalar field associated with them.
- The scalar field represents the influence or intensity of each primitive shape at any point in space.
- The surface of a blobby object is defined by an iso-surface, which is a set of points that have the same scalar field value.
- The iso-surface can be computed by summing up the scalar fields of all the primitive shapes and comparing it with a threshold value.
- The iso-surface can be rendered using various techniques, such as polygonization, ray tracing, or marching cubes.
- Blobby objects can be used to model organic shapes, such as water droplets, clouds, or soft bodies .
- Blobby objects can also be animated by changing the parameters of the primitive shapes, such as their position, orientation, size, or scalar field function.
- Blobby objects can be blended, deformed, or merged with other blobby objects to create complex shapes.
- Blobby objects are also known as metaballs, soft objects, or implicit surfaces .



### Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- Splines can be classified into different types based on their degree, basis functions, and continuity conditions.
- Some common types of splines are:
  - Linear splines: Splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: Splines of degree two that consist of parabolic segments joined at the given points.
  - Cubic splines: Splines of degree three that have smooth transitions between the given points.
  - Bezier curves: Splines that are defined by a set of control points that influence the shape of the curve. They can have any degree, but are usually cubic.
  - B-splines: Splines that are defined by a set of control points and a knot vector that determines the domain and continuity of the curve. They can have any degree, but are usually cubic.
  - NURBS: Non-uniform rational B-splines that are a generalization of B-splines that allow for rational weights on the control points. They can represent conic sections and other curves that are not possible with B-splines.
- Splines can be transformed by affine transformations, such as rotation, translation, scaling, and shearing, without changing their shape.
- Splines can be used to create complex curves and surfaces by combining multiple splines or by using higher-dimensional splines.



### Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline or basis spline is a piecewise polynomial function with specific properties that determine the polynomial degree/order .
- The idea behind using a B-spline curve is to determine a unique polynomial representation of a set of data, whether that data be structural points in 3D space or a set of data on a graph.
- A B-spline function is a combination of flexible bands that is controlled by a number of points that are called control points, creating smooth curves .
- These functions are used to create and manage complex shapes and surfaces using a number of points.
- A B-spline curve can be defined as follows:

  - Let P0, P1, ..., Pn be a set of control points in a d-dimensional space, where d is usually 2 or 3.
  - Let t0, t1, ..., tm be a non-decreasing sequence of real numbers, called the knot vector, where m = n + k + 1 and k is the degree of the B-spline curve.
  - The B-spline curve of degree k with control points P0, P1, ..., Pn and knot vector t0, t1, ..., tm is given by:

    - C(t) = sum_{i=0}^n N_{i,k}(t) P_i, for t_k <= t <= t_{m-k}

  - where N_{i,k}(t) are the B-spline basis functions of degree k, defined recursively as follows:

    - N_{i,0}(t) = 1, if t_i <= t < t_{i+1}, and 0 otherwise
    - N_{i,k}(t) = (t - t_i) / (t_{i+k} - t_i) N_{i,k-1}(t) + (t_{i+k+1} - t) / (t_{i+k+1} - t_{i+1}) N_{i+1,k-1}(t), for k > 0

- Some properties of B-spline curves are:

  - They are invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - They have local control, meaning that changing one control point only affects the curve in a local neighborhood.
  - They have variation diminishing, meaning that the curve does not oscillate more than the control polygon.
  - They have convex hull property, meaning that the curve lies within the convex hull of the control points.
  - They have smoothness, meaning that the curve is continuous and has continuous derivatives up to degree k - 1.



### Bezier curves and surfaces

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling .
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them .
- They have the properties of continuity, smoothness, and local control, which make them highly useful and convenient for curve and surface design.
- Bezier curves and surfaces are named after Pierre Bezier, a French engineer who patented and popularized them in the 1960s and 1970s.

#### Bezier curves

- A Bezier curve is a parametric curve that can be of any degree n, where n is the number of control points minus one.
- The curve is defined by the following formula, where B(t) is the point on the curve at parameter t, P_i are the control points, and b_i,n(t) are the Bernstein polynomials:

  B(t) = sum_{i=0}^n b_i,n(t) P_i, 0 <= t <= 1

- The Bernstein polynomials are given by the following formula, where C(n,i) is the binomial coefficient:

  b_i,n(t) = C(n,i) t^i (1-t)^(n-i), 0 <= i <= n

- The degree of the curve determines its shape and flexibility. The most common types of Bezier curves are:

  - Linear: A straight line between two control points (n=1).
  - Quadratic: A parabolic curve with three control points (n=2).
  - Cubic: A smooth curve with four control points (n=3).

- The curve always starts at the first control point and ends at the last control point. The curve is tangent to the line joining the first two and the last two control points.
- The curve is contained within the convex hull of the control points, which is the smallest polygon that encloses all the control points.
- The curve can be subdivided into smaller Bezier curves at any parameter value t, using a technique called de Casteljau's algorithm.

#### Bezier surfaces

- A Bezier surface is a parametric surface that can be of any degree m and n in the u and v directions, where m and n are the number of control points in each direction minus one.
- The surface is defined by the following formula, where S(u,v) is the point on the surface at parameters u and v, P_i,j are the control points, and b_i,m(u) and b_j,n(v) are the Bernstein polynomials:

  S(u,v) = sum_{i=0}^m sum_{j=0}^n b_i,m(u) b_j,n(v) P_i,j, 0 <= u,v <= 1

- The degree of the surface determines its shape and flexibility. The most common type of Bezier surface is:

  - Bicubic: A smooth surface with 16 control points (m=n=3).

- The surface always passes through the four corner control points. The surface is tangent to the lines joining the adjacent control points along the edges.
- The surface is contained within the convex hull of the control points, which is the smallest polyhedron that encloses all the control points.
- The surface can be subdivided into smaller Bezier surfaces at any parameter values u and v, using a technique similar to de Casteljau's algorithm.

#### Examples

- The following image shows a cubic Bezier curve with four control points. The curve is drawn in blue, the control points are marked with red dots, and the control polygon is drawn in dashed black. The curve is tangent to the control polygon at the endpoints, and is contained within the convex hull of the control points.

  Cubic Bezier curve

- The following image shows a bicubic Bezier surface with 16 control points. The surface is drawn in gray, the control points are marked with red dots, and the control net is drawn in dashed black. The surface passes through the corner control points



## Unit 5 - Hidden Lines and Surfaces

- Hidden lines and surfaces are used to represent the parts of an object that are not visible from a given viewpoint.
- Hidden lines are usually drawn as dashed or dotted lines on a drawing, while hidden surfaces are usually omitted or shaded differently.
- The purpose of hidden lines and surfaces is to show the shape and structure of an object more clearly and completely, and to avoid confusion or ambiguity.
- There are different methods and rules for drawing hidden lines and surfaces, depending on the type of projection, the complexity of the object, and the conventions of the field or industry.
- Some common methods and rules are:

  - In orthographic projection, hidden lines are drawn only on the principal views (front, top, and right), and not on the auxiliary views or sections.
  - In isometric projection, hidden lines are drawn only on the isometric view, and not on the orthographic views or dimensions.
  - In perspective projection, hidden lines are usually omitted, as they would interfere with the realistic appearance of the object.
  - In general, hidden lines should be drawn only when they are necessary to show the shape or structure of the object, and should be avoided when they would clutter the drawing or create confusion.
  - Hidden lines should not cross visible lines, unless they are clearly separated by a gap or a break.
  - Hidden lines should not coincide with center lines, dimension lines, extension lines, or leader lines, unless they are clearly distinguished by a different line type or color.
  - Hidden lines should not be used to show hidden dimensions, hidden holes, hidden threads, or hidden fillets, unless they are explicitly labeled or specified.
  - Hidden surfaces should be omitted or shaded differently when they would obscure the visible surfaces or create confusion about the shape or structure of the object.
  - Hidden surfaces should be shown or shaded differently when they are important for the function or assembly of the object, or when they are required by the standards or specifications of the field or industry.



### Back Face Detection Algorithm

- Back face detection, also known as plane equation method, is an object space method for visible surface detection .
- It is based on the idea that a polygon is a back face if it is oriented away from the viewer, and hence can be eliminated from the rendering process.
- It can be applied to convex polyhedra, such as cubes, pyramids, and prisms, but not to concave polyhedra, such as tori, or objects with holes.
- The algorithm works as follows :
  - For each polygon in the object, compute its normal vector using the cross product of two adjacent edges.
  - For a right-handed coordinate system, if the z-component of the normal vector is positive, then the polygon is a back face. If the z-component is negative, then the polygon is a front face.
  - For a left-handed coordinate system, the opposite is true: if the z-component of the normal vector is negative, then the polygon is a back face. If the z-component is positive, then the polygon is a front face.
  - Alternatively, the dot product of the normal vector and the view vector can be used to determine the orientation of the polygon. If the dot product is positive, then the polygon is a back face. If the dot product is negative, then the polygon is a front face.
  - Discard all the back faces from the rendering process, and only draw the front faces.
- The advantages of back face detection are:
  - It is simple and fast to implement, as it only requires a few arithmetic operations per polygon.
  - It can eliminate up to 50% of the polygons in a typical scene, reducing the computational load for the subsequent stages of the rendering pipeline.
- The disadvantages of back face detection are:
  - It cannot handle concave polyhedra or objects with holes, as some of their back faces may be visible to the viewer.
  - It cannot handle transparent or translucent objects, as their back faces may contribute to the final image.
  - It cannot handle self-intersecting objects, as some of their back faces may be in front of their front faces.



### Depth buffer method

- Depth buffer method, also known as z-buffer method, is an image-space technique for hidden surface removal in computer graphics  .
- It is based on the idea of storing the depth (or z-coordinate) of the closest object at each pixel in a buffer, and comparing the depth of new objects with the existing depth to determine visibility  .
- The depth buffer method has the following steps :
  - Initialize the depth buffer and the frame buffer for each pixel to some predefined values, such as the maximum depth and the background color.
  - For each polygon in the scene, project it onto the view plane and scan-convert it to find the pixels that it covers.
  - For each pixel, calculate the depth of the polygon at that pixel using the plane equation.
  - Compare the depth of the polygon with the depth stored in the depth buffer for that pixel. If the polygon depth is smaller, it means the polygon is closer to the viewer and should be visible. In that case, update the depth buffer and the frame buffer with the new depth and color values. Otherwise, ignore the polygon and move on to the next pixel.
  - Repeat the above steps for all the polygons in the scene.
  - Display the frame buffer as the final image.
- The depth buffer method has some advantages and disadvantages :
  - Advantages:
    - It is easy to implement and can be done in hardware or software.
    - It can handle any number of polygons and any polygon shape, including concave and intersecting polygons.
    - It does not require sorting or clipping of polygons, which can be costly and complex.
  - Disadvantages:
    - It requires a large amount of memory to store the depth buffer, which can be a bottleneck for high-resolution images.
    - It can cause aliasing artifacts, such as jagged edges and popping, due to the discrete nature of pixels and depth values.
    - It does not handle transparency or anti-aliasing well, which may require additional techniques such as alpha blending or A-buffer method.



### A-buffer method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects .
- It extends the algorithm of depth-buffer (or Z-buffer) method by storing more than one depth and color value per pixel .
- It uses a linked list data structure to store the fragments of different objects that overlap a pixel .
- Each fragment has four attributes: depth, color, opacity, and pointer to the next fragment .
- The fragments are sorted in decreasing order of depth, so that the nearest fragment is at the head of the list .
- The final color of a pixel is computed by blending the colors of the fragments according to their opacities .
- A-buffer method can handle anti-aliasing, transparency, and shadows .
- A-buffer method requires more memory and processing time than depth-buffer method .
- A-buffer method can be implemented using hardware or software .



### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The basic idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be applied to both solid and wireframe models, and can handle concave and self-intersecting polygons as well.
- The scan line method can be divided into two phases: initialization and scan conversion.
  - Initialization: In this phase, the polygons are sorted by their minimum y coordinates, and an active edge list (AEL) is created to store the edges that intersect the current scan line. The AEL is sorted by the x coordinates of the intersection points. Each edge in the AEL also has a flag to indicate whether it belongs to a visible surface or not, and a color intensity value to be used for shading.
  - Scan conversion: In this phase, each scan line is processed from top to bottom, and the pixels on the scan line are filled with the appropriate color intensity values according to the AEL. The AEL is updated as the scan line moves down, by adding new edges that start at the current scan line, deleting edges that end at the current scan line, and updating the x coordinates and flags of the existing edges. The color intensity values are also updated according to the shading model used.
- The scan line method has some advantages and disadvantages over other visible surface determination algorithms:
  - Advantages:
    - It is efficient and easy to implement, as it only requires sorting and scanning operations.
    - It can handle complex polygons and hidden surfaces without clipping or subdividing them.
    - It can be combined with various shading models, such as flat, Gouraud, or Phong shading, to produce realistic effects.
  - Disadvantages:
    - It requires a large amount of memory to store the sorted polygon list and the AEL, which may limit the number of polygons that can be rendered.
    - It may produce aliasing artifacts, such as jagged edges or moire patterns, due to the discrete nature of the scan lines and pixels. These can be reduced by using anti-aliasing techniques, such as supersampling or filtering.
    - It may not handle transparent or translucent surfaces well, as it only considers the frontmost surface at each pixel. This can be improved by using depth buffering or ray tracing techniques, which can account for multiple surfaces and their optical properties.



### Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the physical properties of light sources, surface materials, and viewing conditions.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, such as ambient, diffuse, and specular reflection.
  - Global illumination models consider all the interactions and exchange of light among objects, such as reflection, refraction, shadows, and interreflections.
- In this unit, we will focus on the basic local illumination model, which gives reasonably good results and is used in most graphics systems.
- The basic local illumination model consists of three components: ambient light, diffuse reflection, and specular reflection .
  - Ambient light is the uniform and constant light that is present in the environment, regardless of the position and orientation of the objects and the light sources . Ambient light is used to simulate the effect of indirect illumination and to avoid completely dark areas .
  - Diffuse reflection is the light that is reflected equally in all directions by a matte or rough surface . Diffuse reflection depends on the angle between the surface normal and the light direction, and the color and reflectivity of the surface .
  - Specular reflection is the light that is reflected in a mirror-like manner by a shiny or smooth surface . Specular reflection depends on the angle between the surface normal, the light direction, and the viewing direction, and the color and shininess of the surface .
- The basic local illumination model can be expressed as a linear combination of the three components :

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - where I is the total intensity, I<sub>a</sub> is the ambient intensity, I<sub>d</sub> is the diffuse intensity, and I<sub>s</sub> is the specular intensity.
- The basic local illumination model can be applied to each pixel or polygon of a graphics object to compute the intensities and colors to display the surface.
- The basic local illumination model can be extended to include other effects, such as attenuation, spotlights, multiple light sources, and transparency .



### Ambient light

- Ambient light is a type of lighting that is used to create a realistic environment in computer graphics.
- It is usually a soft, warm light that is used to fill in the shadows and create a more natural look.
- Ambient light can be used to simulate natural lightings, such as the sun, or artificial lighting, such as fluorescent lights.
- Ambient light is the base brightness applied to textures rendered in a scene before any point, spot, or other types of virtual light sources are computed.
- The brightness and color of ambient light affect the appearance of the entire rendered scene.
- Ambient light is a very crude approximation of indirect lighting, which is the light that is not absorbed by the surfaces and bounces all over the place.
- Ambient light is often constant and uniform, meaning that it does not depend on the position or orientation of the surfaces.
- Ambient light can be calculated by using a global ambient term, which is a constant value multiplied by the ambient reflectance of the surface.
- Ambient light can also be calculated by using ambient occlusion, which is a technique that measures how exposed each point in a scene is to ambient lighting.
- Ambient occlusion can create more realistic shadows and depth effects by darkening the areas that are more occluded (and hence less exposed) by the ambient light.



### Diffuse reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough .
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by the color and texture of the surface, as well as the position and intensity of the light source.
- Diffuse interreflection is a process whereby light reflected from an object strikes other objects in the surrounding area, illuminating them.
- Diffuse interreflection specifically describes light reflected from objects which are not shiny or specular.
- Diffuse interreflection can create complex lighting effects, such as color bleeding and soft shadows.
- Diffuse interreflection can be simulated by using radiosity or global illumination techniques.



### Specular reflection

- Specular reflection is the phenomenon of light bouncing off a smooth and shiny surface in a single direction, creating a bright spot or highlight on the surface .
- Specular reflection depends on the angle of incidence of the light ray, the angle of reflection of the light ray, and the viewing angle of the observer .
- The angle of incidence is equal to the angle of reflection, and both are measured with respect to the normal vector of the surface .
- The viewing angle is the angle between the normal vector and the line of sight of the observer .
- The intensity of the specular reflection is highest when the viewing angle is equal to the angle of reflection, and decreases as the viewing angle deviates from the angle of reflection .
- Specular reflection is influenced by the material properties of the surface, such as its reflectivity, roughness, and color  .
- Reflectivity is the fraction of incident light that is reflected by the surface  .
- Roughness is the degree of microfacets or small irregularities on the surface that scatter the reflected light in different directions   .
- Color is the wavelength of the light that is reflected by the surface  .
- Specular reflection is often modeled by empirical formulas in computer graphics, such as the Phong model, the Blinn-Phong model, or the Cook-Torrance model  .
- These models use parameters such as the specular exponent, the specular color, and the Fresnel factor to control the shape, size, and intensity of the specular highlight  .
- Specular reflection is important in computer graphics, as it provides a strong visual cue for the shape of an object and its location with respect to light sources in the scene  .



### Phong model

The Phong model is an empirical model of the local illumination of points on a surface designed by the computer graphics researcher Bui Tuong Phong . It is widely used in computer graphics to simulate the appearance of shiny surfaces, such as metal, plastic, or glass. The Phong model consists of three components: ambient, diffuse, and specular reflection .

- Ambient reflection: This component accounts for the constant background light that is present in the environment. It is independent of the surface orientation and the light direction. It is usually modeled as a constant color multiplied by a material coefficient .
- Diffuse reflection: This component accounts for the light that is scattered uniformly in all directions by the surface. It depends on the surface orientation and the light direction, but not on the viewer position. It is usually modeled as the dot product of the surface normal and the light direction, multiplied by a material coefficient and a light color .
- Specular reflection: This component accounts for the light that is reflected in a mirror-like manner by the surface. It depends on the surface orientation, the light direction, and the viewer position. It is usually modeled as the dot product of the reflection vector and the view vector, raised to a power that controls the shininess of the surface, multiplied by a material coefficient and a light color .

The Phong model can be expressed as a formula:

![Phong model formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/1f0b7f0b0f1f7a3f3f0c0a0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c



### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible to the viewer in a 3D scene, because they are occluded by other objects or by the object itself.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image, to improve the realism and efficiency of the rendering process .
- There are different types of coherence that can be exploited to reduce the computation required for HLR and HSR, such as object coherence, image coherence, area coherence, and span coherence.
- Object coherence means that the relative positions and orientations of the objects in the scene do not change significantly from one frame to the next, so the visibility information can be reused.
- Image coherence means that the pixels in the image have similar properties, such as color, depth, and visibility, so they can be processed in groups.
- Area coherence means that the regions of the image that are covered by a single surface have the same visibility, so they can be filled with a uniform color.
- Span coherence means that the pixels along a scan line that are covered by a single surface have the same visibility, so they can be drawn with a single line.
- There are different algorithms for HLR and HSR, such as back-face culling, depth-buffer method, scan-line method, painter's algorithm, z-buffer algorithm, BSP-tree method, ray tracing, and area subdivision method  .
- Back-face culling is a simple technique that eliminates the polygons that are facing away from the viewer, based on the sign of the dot product of the polygon normal and the view vector.
- Depth-buffer method is a technique that assigns a depth value to each pixel in the image, and compares it with the depth value of the incoming polygon, to determine which one is closer to the viewer.
- Scan-line method is a technique that processes the image one scan line at a time, and maintains a list of active edges and surfaces, to determine the visibility of each pixel.
- Painter's algorithm is a technique that sorts the polygons in the scene from back to front, and draws them in that order, so that the closer polygons overwrite the farther ones.
- Z-buffer algorithm is a technique that uses a z-buffer (or depth buffer) to store the depth value of the closest polygon at each pixel, and updates it whenever a closer polygon is encountered.
- BSP-tree method is a technique that uses a binary space partitioning tree to divide the scene into convex regions, and traverses the tree in a back-to-front or front-to-back order, depending on the view position, to draw the polygons.
- Ray tracing is a technique that traces a ray from the eye to each pixel in the image, and finds the closest intersection with the scene objects, to determine the visibility and color of the pixel.
- Area subdivision method is a technique that divides the image into smaller regions, and tests the visibility of each region against the scene objects, to determine which regions are fully visible, fully hidden, or partially visible.



### Warn model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- The Warn model is a lighting model that approximates large non-point sources close to objects in a scene by using several point sources arranged in a grid .
- The Warn model also allows one to specify "flaps" on the sides of the lighting region to give the light more directionality.
- The Warn model can be used to simulate studio lighting effects, such as spotlights.
- The Warn model takes into account the reflectance properties of the surface as well as the physics of light reflection.
- The Warn model can be implemented by using the following steps :
  - Define the position, size, and shape of the light source grid.
  - Define the position, orientation, and color of each point source in the grid.
  - Define the flaps on the sides of the grid and their angles.
  - For each point source, calculate the intensity attenuation based on the distance and angle between the source and the surface point.
  - For each surface point, sum up the contributions of all the point sources and apply the surface reflectance model.
  - For each pixel, determine the color and intensity based on the surface point and the viewing parameters.



### Intensity Attenuation

- In computer graphics, **intensity attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- Intensity attenuation is important for realistic rendering of scenes, as it affects the shading and lighting of objects.
- The intensity of a light source can be modeled as a function of the distance from the source and the angle of incidence.
- The intensity attenuation formula is given by:

$$
I = \frac{I_0}{a + bd + cd^2}
$$

where:

  - $I$ is the intensity at distance $d$ from the source
  - $I_0$ is the intensity at the source
  - $a$, $b$, and $c$ are attenuation coefficients that depend on the medium and the light source
  - $d$ is the distance from the source



### Color consideration for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection.
- Hidden surface removal or visible surface detection is the process of identifying and eliminating the hidden surfaces from the rendered image.
- Color consideration for the notes of this unit is important because it can help to distinguish the visible and hidden parts of the objects, as well as to convey the depth, shading, and lighting effects of the scene  .
- Some of the color considerations for the notes of this unit are:

  - Use different colors for the visible and hidden lines and surfaces, such as black for visible and gray for hidden, or solid for visible and dashed for hidden.
  - Use colors that are consistent with the light source and the material properties of the objects, such as ambient, diffuse, and specular colors.
  - Use colors that are proportional to the depth or distance of the objects from the viewpoint, such as darker for closer and lighter for farther, or use a depth buffer or a z-buffer to store the depth information for each pixel .
  - Use colors that are compatible with the display device and the human perception, such as RGB, CMYK, HSV, or HSL color models, or use a color lookup table or a palette to map the colors to the available ones .



### Transparency and Shadows

- Transparency is the property of a material that allows light to pass through it partially or fully, creating the effect of translucency or see-throughness .
- Transparency can be simulated in computer graphics by mixing the colors of the transparent object and the background object, using a parameter called alpha that represents the degree of opacity or transparency .
- Transparency can be used to create realistic effects such as glass, water, smoke, fog, etc. in computer graphics .
- Shadows are the regions where light is blocked by an opaque object, creating a contrast between the illuminated and the dark areas.
- Shadows can enhance the realism, depth, and mood of a scene rendered with computer graphics.
- Shadows can be generated in computer graphics by tracing the paths of light rays from the light source to the eye, and determining whether they are occluded by any object in the scene .
- Shadows can be classified into two types: hard shadows and soft shadows, depending on the sharpness of the shadow boundary.
- Hard shadows are produced by point light sources, where the shadow boundary is well-defined and crisp.
- Soft shadows are produced by area light sources, where the shadow boundary is blurred and fuzzy, due to the penumbra effect.
- There are various techniques to create shadows in computer graphics, such as shadow mapping, shadow volumes, ray tracing, etc. Each technique has its own advantages and disadvantages in terms of accuracy, efficiency, and complexity .

