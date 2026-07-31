

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



### Types of computer graphics

Computer graphics are the visual representation of data and information using computers and software. Computer graphics can be used for various purposes, such as creating images, animations, simulations, games, user interfaces, and more.

Computer graphics can be broadly classified into two main categories: raster graphics and vector graphics  . Additionally, computer graphics can also be categorized based on the dimensionality of the images: two dimensional (2D) and three dimensional (3D) graphics .

- Raster graphics are made up of pixels, which are small squares of color that form a grid. Each pixel contains information about its color and brightness. Raster graphics are also known as bitmap images, as they map each pixel to a specific location on the screen. Raster graphics are commonly used for digital photographs, scanned images, paintings, and video games. The quality of raster graphics depends on the resolution, which is the number of pixels per inch (ppi). The higher the resolution, the more detailed and sharp the image. However, raster graphics also have some drawbacks, such as being memory-intensive, losing quality when scaled up or down, and being difficult to edit or manipulate   .

- Vector graphics are made up of paths, which are defined by mathematical equations that describe the shape, direction, and color of each line or curve. Vector graphics are also known as object-oriented graphics, as they represent each image element as an object that can be moved, resized, rotated, or transformed. Vector graphics are commonly used for logos, icons, fonts, diagrams, and illustrations. The quality of vector graphics does not depend on the resolution, as they can be scaled up or down without losing clarity or detail. Vector graphics also have some advantages, such as being memory-efficient, easy to edit or manipulate, and supporting transparency and animation   .

- 2D graphics are graphics that have only two dimensions: width and height. 2D graphics are used to create flat images that do not have any depth or perspective. 2D graphics can be either raster or vector, depending on the technique and software used to create them. 2D graphics are widely used for web design, graphic design, user interfaces, cartoons, and simple games .

- 3D graphics are graphics that have three dimensions: width, height, and depth. 3D graphics are used to create realistic images that have volume, perspective, and lighting effects. 3D graphics are usually vector-based, as they use geometric primitives such as points, lines, polygons, and curves to model the shape and surface of each object. 3D graphics also use techniques such as shading, texture mapping, lighting, and rendering to enhance the appearance and realism of the images. 3D graphics are widely used for animation, simulation, video games, virtual reality, and computer-aided design .



### Graphic Displays for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A graphic display is a device that can show images or text on a screen, such as a monitor, a projector, or a printer.
- A graphic display can be classified into two types: raster and vector.
  - A raster display consists of a grid of pixels, each of which can have a different color or intensity. Raster displays are commonly used for displaying photographs, videos, and games.
  - A vector display uses mathematical equations to draw lines, curves, and shapes on the screen. Vector displays are commonly used for displaying diagrams, maps, and fonts.
- A graphic display can have different characteristics, such as size, resolution, color depth, refresh rate, and aspect ratio .
  - The size of a graphic display is measured by the diagonal length of the screen, usually in inches. The size affects the viewing distance and the field of view of the display.
  - The resolution of a graphic display is the number of pixels that can be displayed on the screen, usually expressed as width x height. The resolution affects the sharpness and detail of the image.
  - The color depth of a graphic display is the number of bits used to represent the color of each pixel, usually ranging from 1 to 32 bits. The color depth affects the number and variety of colors that can be displayed on the screen.
  - The refresh rate of a graphic display is the number of times the image on the screen is updated per second, usually measured in hertz (Hz). The refresh rate affects the smoothness and flicker of the image.
  - The aspect ratio of a graphic display is the ratio of the width to the height of the screen, usually expressed as a fraction or a decimal. The aspect ratio affects the shape and proportion of the image on the screen.
- A graphic display can be connected to a computer or a device that can generate graphics, such as a graphics card, a graphics processing unit (GPU), or a graphics software .
  - A graphics card is a hardware component that can convert graphics data into signals that can be sent to the display. A graphics card can have different features, such as memory, bandwidth, clock speed, and shader units, that affect its performance and compatibility.
  - A graphics processing unit (GPU) is a specialized processor that can perform parallel computations on graphics data, such as rendering, shading, and lighting. A GPU can be integrated into the graphics card, the motherboard, or the CPU of the computer.
  - A graphics software is a program that can create, edit, or manipulate graphics data, such as images, animations, or 3D models. A graphics software can have different functions, such as drawing, painting, filtering, transforming, or exporting graphics data.



### Random scan displays

- Random scan displays are also known as **vector displays** or **stroke-writing displays** or **calligraphic displays** .
- Random scan displays are used to draw a picture **one line at a time** and are thus also referred to as **line-drawing displays** .
- Random scan displays use a **cathode ray tube (CRT)** that directs the beam of an electron only to those areas of the screen where a picture has to be drawn .
- Random scan displays can draw and refresh component lines of a picture in any specified sequence.
- Random scan displays produce **smooth line drawings** and have **high resolution**.
- Random scan displays are suitable for applications that require **line drawings** and **wireframe models**.
- Random scan displays are **not** suitable for applications that require **realistic shaded scenes** or **raster graphics** .
- Random scan displays are **more expensive** and **less common** than raster scan displays.
- Pen plotter is an example of random scan displays.

: https://www.includehelp.com/computer-graphics/raster-scan-and-random-scan-display.aspx
: https://bootpoot.tech/random-scan-display-in-computer-graphics/
: https://www.javatpoint.com/difference-between-random-scan-and-raster-scan-display
: https://www.geeksforgeeks.org/random-scan-display/



### Raster scan displays

- Raster scan displays are the most common type of graphics monitor that use a cathode ray tube (CRT) to display images on a screen .
- A raster scan display works by scanning an electron beam across the screen from top to bottom, one row at a time .
- The electron beam is turned on and off to create a pattern of illuminated spots (pixels) on the screen .
- The resolution of a raster scan display depends on the number of pixels on the screen and the number of colors that each pixel can display.
- The refresh rate of a raster scan display is the number of times per second that the electron beam scans the entire screen.
- A raster scan display can display both static and dynamic images, but it may suffer from flickering or aliasing effects if the refresh rate is too low or the resolution is too high .



### Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- The frame buffer and video controller are essential components of computer graphics systems, as they enable the display of graphical output on the screen.
- The size and resolution of the frame buffer determine the quality and complexity of the images that can be displayed.
- The frame buffer can be implemented as a separate memory bank on the graphics card, or as a reserved part of regular memory.
- The video controller can be integrated with the graphics card, or as a separate chip on the motherboard.
- The frame buffer and video controller can be classified into different types, such as:
  - Monochrome frame buffer: It has one bit per pixel, and can display only black and white images.
  - Color frame buffer: It has multiple bits per pixel, and can display images with different colors.
  - Single-buffered frame buffer: It has one memory area for storing the current frame.
  - Double-buffered frame buffer: It has two memory areas for storing the current and the next frame, and can switch between them to avoid flickering.
  - Overlay frame buffer: It has multiple memory areas for storing different layers of images, and can combine them to create complex scenes.



# Points and Lines for the Notes of the Unit 1 - Introduction and Line Generation in the Subject of Computer Graphics

- A point is the fundamental element of picture representation. It is the position in the plane defined as either pair or triplets of numbers depending upon the dimension.
- A line is a basic element in graphics. To draw a line, you need two points between which you can draw a line. In the following three algorithms, we refer the one point of line as X0, Y0 and the second point of line as X1, Y1.
- A line function is used to generate a straight line between any two end points. Usually a line function is provided with the location of two pixel points called the starting point and the end point and it is up to the computer to decide what pixels fall between these two points so that a straight line is generated.
- There are different algorithms to draw a line, such as:
  - DDA algorithm: It is an incremental scan-conversion method. It is based on calculating either delta x or delta y, depending on the slope of the line, and then using the equation of the line to calculate the other value.
  - Bresenham’s Line Algorithm: It is an algorithm that determines the points of an n-dimensional raster that should be selected in order to form a close approximation to a straight line between two points. It is commonly used to draw lines on a computer screen, as it uses only integer addition, subtraction and bit shifting, all of which are very cheap operations in standard computer architectures.
  - Mid-point Line algorithm: It is an algorithm used to determine the points needed for rasterizing a line. It uses only integer addition and subtraction and comparison operations. It is a type of Bresenham’s algorithm that is optimized for drawing circles.
- A line can have different attributes, such as:
  - Color: It is the property of the line that determines its hue and intensity. It can be set using the setcolor() function.
  - Width: It is the property of the line that determines its thickness. It can be set using the setlinestyle() function.
  - Pattern: It is the property of the line that determines its style, such as solid, dashed, dotted, etc. It can be set using the setlinestyle() function.
- A line can also be represented by an equation of the form ax + by + c = 0, where a, b and c are constants. The slope of the line is given by -a/b and the intercept is given by -c/b.
- A line can also be represented by a parametric equation of the form x = x0 + t(x1 - x0) and y = y0 + t(y1 - y0), where x0, y0 and x1, y1 are the end points of the line and t is a parameter that varies from 0 to 1.
- A line can also be represented by a vector equation of the form r = r0 + t(v), where r0 is the position vector of a point on the line, v is the direction vector of the line and t is a scalar parameter.



### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Line drawing algorithms are methods for approximating a line segment on discrete graphical media, such as pixel-based displays and printers.
- Line drawing algorithms are important in computer graphics because they are the basis for rendering other geometric primitives, such as polygons, circles, and curves.
- Line drawing algorithms need to balance accuracy, efficiency, and simplicity. They also need to handle different cases of line slopes, orientations, and lengths.
- There are following algorithms used for drawing a line:
  - DDA (Digital Differential Analyzer) Line Drawing Algorithm
    - It is based on the idea of incrementing either x or y coordinate by a small amount and calculating the other coordinate using the line equation y = mx + b.
    - It is simple to implement but suffers from rounding errors and floating-point operations.
  - Bresenham’s Line Drawing Algorithm
    - It is an optimized version of DDA that uses only integer arithmetic and avoids multiplication and division.
    - It is based on the idea of choosing the closest pixel to the ideal line using a decision variable that depends on the error term.
    - It is faster and more accurate than DDA but requires more logic to handle different cases of line slopes.
  - Mid-Point Line Drawing Algorithm
    - It is a variation of Bresenham’s algorithm that uses the mid-point of the two possible pixels as the decision variable.
    - It is simpler and more symmetric than Bresenham’s algorithm but requires more calculations per iteration.
- The following diagram illustrates the three algorithms for drawing a line with slope less than 1:

Line drawing algorithms

- The following pseudocode shows the general steps of the three algorithms for drawing a line with slope less than 1:

```
// DDA algorithm
Input: x1, y1, x2, y2 // endpoints of the line
Output: pixels to be filled
dx = x2 - x1
dy = y2 - y1
m = dy / dx // slope of the line
x = x1
y = y1
plot(x, round(y)) // plot the first pixel
while x < x2
  x = x + 1 // increment x by 1
  y = y + m // increment y by slope
  plot(x, round(y)) // plot the next pixel
end while

// Bresenham's algorithm
Input: x1, y1, x2, y2 // endpoints of the line
Output: pixels to be filled
dx = x2 - x1
dy = y2 - y1
d = 2 * dy - dx // initial decision variable
x = x1
y = y1
plot(x, y) // plot the first pixel
while x < x2
  x = x + 1 // increment x by 1
  if d < 0 // the lower pixel is closer
    d = d + 2 * dy // update the decision variable
  else // the upper pixel is closer
    y = y + 1 // increment y by 1
    d = d + 2 * (dy - dx) // update the decision variable
  end if
  plot(x, y) // plot the next pixel
end while

// Mid-point algorithm
Input: x1, y1, x2, y2 // endpoints of the line
Output: pixels to be filled
dx = x2 - x1
dy = y2 - y1
d = dy - dx / 2 // initial decision variable
x = x1
y = y1
plot(x, y) // plot the first pixel
while x < x2
  x = x + 1 // increment x by 1
  if d < 0 // the lower pixel is closer
    d = d + dy // update the decision variable
  else // the upper pixel is closer
    y = y + 1 // increment y by 1
    d = d + (dy - dx) // update the decision variable
  end if
  plot(x, y) // plot the next pixel

```




### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm.
- A circle generation algorithm is an algorithm used to create a circle on a computer screen.
- It is used in various applications such as computer-aided design (CAD) software, animation software, games, and scientific visualization.
- The equation of a circle is X^2^ + Y^2^ = r^2^, where r is the radius.
- There are several algorithms used for generating circles on a computer screen, such as:
  - Bresenham's Algorithm   
    - It is a simple and efficient algorithm that uses only integer arithmetic.
    - It is based on the idea of determining the subsequent points required to draw the circle by using a decision parameter.
    - It exploits the symmetry of the circle to reduce the computation and memory requirements.
    - It starts from the topmost point of the circle and moves clockwise to generate the octant in the first quadrant.
    - It uses the following steps:
      - Initialize the decision parameter as p = 3 - 2r
      - Set the initial point as (0, r)
      - Repeat until x < y
        - Plot the point (x, y) and its symmetric points in the other octants
        - If p < 0, then set p = p + 4x + 6 and increment x by 1
        - Else, set p = p + 4(x - y) + 10 and increment x by 1 and decrement y by 1
      - If x = y, plot the final point (x, y) and its symmetric points in the other octants
  - Midpoint Circle Algorithm  
    - It is another efficient algorithm that uses only integer arithmetic.
    - It is based on the idea of determining the midpoint of the pixels that lie on the circle.
    - It also exploits the symmetry of the circle to reduce the computation and memory requirements.
    - It starts from the topmost point of the circle and moves clockwise to generate the octant in the first quadrant.
    - It uses the following steps:
      - Initialize the decision parameter as p = 1 - r
      - Set the initial point as (0, r)
      - Repeat until x < y
        - Plot the point (x, y) and its symmetric points in the other octants
        - If p < 0, then set p = p + 2x + 3 and increment x by 1
        - Else, set p = p + 2(x - y) + 5 and increment x by 1 and decrement y by 1
      - If x = y, plot the final point (x, y) and its symmetric points in the other octants
- The following diagram illustrates the Bresenham's and Midpoint Circle Algorithms:

```
    y ^
      |
      |       (x, y)
      |       /  |
      |      /   |
      |     /    |
      |    /     |
      |   /      |
      |  /       |
      | /        |
      |/         |
      +----------+--------> x
     (0, 0)     (x, 0)
```

- The advantages of these algorithms are:
  - They are simple and easy to implement
  - They are fast and efficient
  - They use only integer arithmetic and avoid costly floating-point operations
  - They exploit the symmetry of the circle to reduce the number of calculations and memory usage
- The disadvantages of these algorithms are:
  - They are not accurate and may produce jagged edges or aliasing effects
  - They are not scalable and may not work well for large circles or high-resolution screens
  - They are not general and may not handle other shapes such as ellipses or curves



### Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle. It is based on the following steps:

- Assume the center of the circle is at the origin (0, 0) and the radius is R.
- Start from the point (0, R) on the circle and move clockwise along the first octant of the circle.
- At each point (x, y), calculate the decision parameter P as P = x^2 + y^2 - R^2.
- If P < 0, then the next point is (x + 1, y) and P is updated as P = P + 2x + 3.
- If P >= 0, then the next point is (x + 1, y - 1) and P is updated as P = P + 2x - 2y + 5.
- Repeat the above steps until x >= y.
- Use the symmetry of the circle to generate the points in the other seven octants by reflecting the points in the first octant.

The following diagram illustrates the algorithm:

Mid-point circle generating algorithm

The advantages of this algorithm are:

- It is simple and easy to implement.
- It only uses integer arithmetic and avoids trigonometric functions and square roots.
- It is efficient and reduces the number of calculations by exploiting the symmetry of the circle.

The disadvantages of this algorithm are:

- It may produce gaps or overlaps in the circle due to rounding errors.
- It may not produce smooth curves due to aliasing effects.



### Parallel algorithms for line generation

Line generation is a fundamental task in computer graphics, as it is used to draw curves, polygons, and other shapes. A line is defined by two endpoints, and can be approximated by a sequence of pixels on a square grid. There are different algorithms for finding the pixels that best represent a line, such as the DDA algorithm and the Bresenham's algorithm. These algorithms are sequential, meaning that they compute the pixels one by one, starting from one endpoint and moving towards the other.

However, sequential algorithms may not be efficient for parallel processing, which is a common technique in modern computer graphics. Parallel processing involves using multiple processors or cores to perform computations simultaneously, thus reducing the execution time and increasing the performance. Therefore, there is a need for parallel algorithms for line generation, which can divide the work among multiple processors and synchronize the results.

One possible approach for parallel line generation is based on the idea of coordinate pairs. A coordinate pair is a pair of integers (x, y) that satisfies the equation of the line, such as y = mx + b, where m and b are constants. A coordinate pair represents a pixel on the line, and can be computed from the equation by substituting x or y with an integer value. For example, if the equation of the line is y = 2x + 1, and x = 3, then the coordinate pair is (3, 7).

The coordinate pairs can be used to derive four parallel algorithms for line generation:

- The first algorithm is based on the observation that the coordinate pairs form an arithmetic progression, meaning that they have a constant difference between consecutive terms. For example, if the coordinate pairs are (1, 3), (2, 5), (3, 7), ..., then the difference is (1, 2). The algorithm can use this difference to generate the coordinate pairs in parallel, by adding it to the initial pair repeatedly. The algorithm can also handle the cases where the slope of the line is negative or greater than one, by using appropriate signs and swapping the x and y coordinates.

- The second algorithm is based on the fact that the coordinate pairs can be obtained by multiplying the equation of the line by a scaling factor, and rounding the results to the nearest integers. For example, if the equation of the line is y = 2x + 1, and the scaling factor is 4, then the coordinate pairs are (1, 5), (2, 9), (3, 13), ..., obtained by multiplying the equation by 4 and rounding the results. The algorithm can use this scaling factor to generate the coordinate pairs in parallel, by multiplying the equation by different values and rounding the results.

- The third algorithm is based on the fact that the coordinate pairs can be obtained by adding a constant vector to the initial pair, and rotating the result by a fixed angle. For example, if the initial pair is (1, 3), and the constant vector is (2, 4), and the angle is 45 degrees, then the coordinate pairs are (1, 3), (5, 5), (9, 7), ..., obtained by adding (2, 4) to (1, 3) and rotating the result by 45 degrees. The algorithm can use this constant vector and angle to generate the coordinate pairs in parallel, by adding and rotating the initial pair by different values.

- The fourth algorithm is based on the fact that the coordinate pairs can be obtained by performing a vector prefix sum calculation, which is a common operation in parallel computing. A vector prefix sum is a sequence of vectors, where each vector is the sum of all the previous vectors in the sequence. For example, if the sequence of vectors is (1, 2), (3, 4), (5, 6), ..., then the vector prefix sum is (1, 2), (4, 6), (9, 12), .... The algorithm can use this operation to generate the coordinate pairs in parallel, by using the difference between consecutive pairs as the input sequence, and computing the vector prefix sum.

These parallel algorithms can be implemented on different parallel architectures, such as a binary tree of processors , a mesh of processors, or a GPU. The algorithms can also be adapted to handle different types of lines, such as anti-aliased lines, thick lines, or dashed lines, by using appropriate modifications. The algorithms can also be compared in terms of their complexity



## Unit 2 - Transformations

A transformation is a change in the position, size, or shape of a figure. There are four basic types of transformations: translations, rotations, reflections, and dilations.

- A translation is a transformation that moves every point of a figure the same distance and in the same direction. The figure does not change its size or orientation. A translation can be described by a vector, which has a magnitude (length) and a direction. A vector can be represented by an arrow or by a pair of numbers (x, y) that indicate how much the figure moves horizontally and vertically.

- A rotation is a transformation that turns a figure around a fixed point called the center of rotation. The figure does not change its size or shape, but it may change its orientation. A rotation can be described by an angle of rotation, which measures how much the figure rotates clockwise or counterclockwise, and a direction of rotation, which indicates which way the figure turns. A positive angle of rotation means the figure turns counterclockwise, and a negative angle of rotation means the figure turns clockwise.

- A reflection is a transformation that flips a figure over a line called the line of reflection. The figure does not change its size or shape, but it may change its orientation. A reflection can be described by the equation of the line of reflection, which is usually given in slope-intercept form (y = mx + b) or standard form (Ax + By = C). The line of reflection is the perpendicular bisector of the segment that joins each point of the figure and its image.

- A dilation is a transformation that changes the size of a figure, but not its shape. The figure may change its orientation depending on the center of dilation. A dilation can be described by a scale factor, which is a ratio that compares the lengths of the corresponding sides of the figure and its image. A scale factor greater than 1 means the figure enlarges, and a scale factor less than 1 means the figure shrinks. A scale factor of 1 means the figure does not change its size. The center of dilation is a fixed point that the figure expands or contracts from. If the center of dilation is the origin (0, 0), then the figure does not change its orientation. If the center of dilation is not the origin, then the figure may change its orientation.

Some properties of transformations are:

- A transformation maps a figure onto its image. The notation for this is f(x) -> f'(x), where f(x) is the original figure and f'(x) is the image.
- A transformation preserves the distance between any two points of a figure and its image. This means that the length of any segment in the figure is equal to the length of its corresponding segment in the image. This property is called the distance-preserving property or the rigid motion property.
- A transformation preserves the measure of any angle of a figure and its image. This means that the measure of any angle in the figure is equal to the measure of its corresponding angle in the image. This property is called the angle-preserving property or the congruence property.
- A transformation preserves the orientation of a figure and its image if the figure and its image have the same clockwise or counterclockwise order of vertices. This means that the figure and its image are facing the same way. This property is called the orientation-preserving property. A translation, a rotation, and a dilation with the origin as the center of dilation are orientation-preserving transformations. A reflection and a dilation with a center of dilation other than the origin are not orientation-preserving transformations.



### Basic transformation for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another without changing its size or orientation. It can be represented by a 2x2 matrix that adds a translation vector to the original coordinates of the object. For example, the matrix below translates an object by tx units along the x-axis and ty units along the y-axis.

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- Rotation is the change of orientation of an object around a fixed point or axis. It can be represented by a 2x2 matrix that multiplies the original coordinates of the object by a rotation angle. For example, the matrix below rotates an object by θ degrees counterclockwise around the origin.

| cosθ  -sinθ  0 |
| sinθ  cosθ   0 |
| 0     0      1 |

- Scaling is the change of size of an object by a scaling factor. It can be represented by a 2x2 matrix that multiplies the original coordinates of the object by a scaling factor. For example, the matrix below scales an object by sx along the x-axis and sy along the y-axis.

| sx  0  0 |
| 0  sy  0 |
| 0  0   1 |

- These basic transformations can be combined to form more complex transformations, such as reflection, shear, and dilation. They can also be applied to different coordinate systems, such as Cartesian, polar, or homogeneous coordinates.
- Transformations play an important role in computer graphics to reposition, resize, or reshape the graphics on the screen and change their perspective or appearance. They are also used for animation, modeling, rendering, and image processing.



### Matrix representations and homogenous coordinates for computer graphics

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling, and projection in a compact and consistent form.
- Matrices can be used to transform vectors in cartesian coordinates by taking them as column vectors and multiplying them by the transformation matrix.
- Homogeneous coordinates are a way to extend the cartesian coordinates by adding an extra dimension, usually denoted by w, to represent points and vectors in a projective space.
- Homogeneous coordinates allow all geometric transformation equations to be represented as matrix multiplication, and also enable the representation of points at infinity and perspective projection.
- Homogeneous coordinates have a range of applications in computer graphics, such as displaying three-dimensional objects on two-dimensional image planes, performing affine and projective transformations, and manipulating curves and surfaces.
- To convert a point (x, y) in cartesian coordinates to a point (x, y, w) in homogeneous coordinates, we can set w to any non-zero value, usually 1. To convert back, we can divide x and y by w.
- To convert a vector (x, y) in cartesian coordinates to a vector (x, y, w) in homogeneous coordinates, we can set w to zero. To convert back, we can ignore w.
- The matrix representation for translation by (tx, ty) in homogeneous coordinates is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- The matrix representation for scaling by (sx, sy) in homogeneous coordinates is:

| sx 0  0 |
| 0  sy 0 |
| 0  0  1 |

- The matrix representation for rotation by an angle θ in homogeneous coordinates is:

| cosθ -sinθ 0 |
| sinθ cosθ  0 |
| 0    0     1 |

- The matrix representation for projection onto the line y = mx + b in homogeneous coordinates is:

| 1-m^2 2m   -2mb |
| 2m    1-m^2 2b  |
| 0     0     1   |

- The advantage of using homogeneous coordinates is that multiple transformations can be combined into a single matrix by multiplying the individual matrices. For example, to perform a translation followed by a rotation, we can multiply the translation matrix by the rotation matrix.



### Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A transformation is a process of changing the position, size, shape, or orientation of an object in a coordinate system.
- A composite transformation is a combination of two or more transformations into a single one that is equivalent to applying the transformations one after another.
- A composite transformation can be represented by a matrix that is obtained by multiplying the matrices of the individual transformations in the order of their application.
- The order of the transformations matters, as different orders may produce different results. For example, rotating an object and then translating it is not the same as translating it and then rotating it.
- Some transformations are commutative, meaning that the order does not matter. For example, translation and scaling are commutative, as they do not affect the orientation of the object.
- Some transformations are non-commutative, meaning that the order does matter. For example, rotation and shearing are non-commutative, as they affect the orientation of the object.
- Composite transformations can be applied to 2D or 3D objects, depending on the dimension of the coordinate system and the matrices used.
- Some common composite transformations are:

  - Reflection: a combination of scaling and rotation that produces a mirror image of the object.
  - Rotation about a point: a combination of translation and rotation that rotates the object around a fixed point.
  - Scaling about a point: a combination of translation and scaling that scales the object with respect to a fixed point.
  - Shearing: a combination of scaling and rotation that distorts the shape of the object.



### Reflections and Shearing

Reflection and shearing are two types of transformations in computer graphics that change the position and shape of an object.

#### Reflection

- Reflection is a kind of rotation where the angle of rotation is 180 degrees.
- The reflected object is always formed on the other side of the mirror, which can be a line or a plane.
- The mirror line or plane is also called the axis of reflection or the plane of reflection.
- The distance of the original object and the reflected object from the mirror is equal.
- The reflection can be done in 2D or 3D space, depending on the dimension of the mirror.
- The reflection matrix is used to calculate the coordinates of the reflected object from the original object.
- The reflection matrix depends on the orientation of the mirror. For example, if the mirror is parallel to the x-axis, the reflection matrix is:

```
R_x = | 1  0 |
      | 0 -1 |
```

- Similarly, if the mirror is parallel to the y-axis, the reflection matrix is:

```
R_y = |-1  0 |
      | 0  1 |
```

- If the mirror is at an arbitrary angle, the reflection matrix is:

```
R = | cos(2θ)  sin(2θ) |
    | sin(2θ) -cos(2θ) |
```

- Where θ is the angle between the mirror and the x-axis.
- The reflection matrix for 3D space is more complex and depends on the equation of the plane of reflection.

#### Shearing

- Shearing is the process of slanting an object in 2D or 3D space either in x, y, or z direction.
- Shearing changes the shape of the object, but not its area or volume.
- The shearing can be done in one direction or two directions. It is an ideal technique to change the shape of an existing object.
- The sliding of layers of the object occurs while doing the shearing. The layers are parallel to the direction of shearing.
- The shearing matrix is used to calculate the coordinates of the sheared object from the original object.
- The shearing matrix depends on the direction and the amount of shearing. For example, if the shearing is done in x direction by a factor of sh_x, the shearing matrix is:

```
S_x = | 1  sh_x |
      | 0    1  |
```

- Similarly, if the shearing is done in y direction by a factor of sh_y, the shearing matrix is:

```
S_y = | 1    0  |
      | sh_y 1 |
```

- If the shearing is done in both x and y directions by factors of sh_x and sh_y, the shearing matrix is:

```
S_xy = | 1  sh_x |
       | sh_y 1  |
```

- The shearing matrix for 3D space is more complex and depends on the direction and the amount of shearing in x, y, and z axes.



### Windowing and Clipping

- Windowing is the process of selecting and viewing a part of a picture with different views .
- Clipping is the process of dividing each element of the picture into its visible and invisible portions, and discarding the invisible portion .
- A window is an opening through which part of the outside world can be seen. It can be defined by a rectangular or a curved boundary in the world coordinate system.
- A viewport is a rectangular area on the display device where the window is mapped. It can be defined by the lower-left and upper-right corners in the device coordinate system.

Some points to remember:

- Windowing and clipping are used to improve the efficiency and quality of the viewing transformation.
- Windowing and clipping can be applied to different entities, such as points, lines, polygons, and curves.
- There are different algorithms for clipping different entities, such as Cohen-Sutherland algorithm, Sutherland-Hodgman algorithm, Liang-Barsky algorithm, etc .
- Clipping can be done in different coordinate systems, such as world, normalized, or device coordinates.



### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert geometry data into image data that can be displayed on a device .
- The viewing pipeline consists of the following stages :
  - Object coordinates: The coordinates of the geometry data in their own local coordinate system.
  - World coordinates: The coordinates of the geometry data after applying the modeling transformation, which places them in a common coordinate system relative to the world origin.
  - Viewing coordinates: The coordinates of the geometry data after applying the viewing transformation, which aligns them with the camera or eye position and orientation.
  - Projection coordinates: The coordinates of the geometry data after applying the projection transformation, which maps them onto a 2D plane that represents the view window or screen.
  - Device coordinates: The coordinates of the geometry data after applying the viewport transformation, which scales and translates them to fit the device resolution and aspect ratio.
- The viewing pipeline can be illustrated by the following diagram :

```
Object coordinates -> World coordinates -> Viewing coordinates -> Projection coordinates -> Device coordinates
|------------------| |------------------| |-------------------| |---------------------| |-------------------|
| Modeling         | | Viewing          | | Projection        | | Viewport            | | Rasterization     |
| transformation   | | transformation   | | transformation    | | transformation      | | and display       |
|------------------| |------------------| |-------------------| |---------------------| |-------------------|
```

- An example of the viewing pipeline is as follows:
  - Suppose we have a 2D object with coordinates (1, 1), (2, 2), (3, 1) in its own coordinate system.
  - We apply a modeling transformation that translates the object by (2, 3) and scales it by 2, resulting in the world coordinates (4, 8), (8, 10), (10, 8).
  - We apply a viewing transformation that rotates the object by 90 degrees clockwise and translates it by (-5, -5), resulting in the viewing coordinates (3, -9), (5, -13), (3, -15).
  - We apply a projection transformation that maps the viewing coordinates to a view window with coordinates (-10, -10), (10, 10), resulting in the projection coordinates (0.3, 0.1), (0.5, -0.3), (0.3, -0.5).
  - We apply a viewport transformation that scales and translates the projection coordinates to fit a device with resolution 800x600, resulting in the device coordinates (320, 340), (400, 280), (320, 220).
  - We apply a rasterization and display process that converts the device coordinates into pixels and displays them on the device screen.



### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the mappings of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are part of the viewing pipeline, which consists of the following steps :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation .
  - Apply the viewing transformation, which converts the WCS to the VCS .
  - Define the clipping window, which is the rectangular region in the VCS that defines the portion of the picture to be displayed .
  - Apply the clipping algorithm, which removes the objects, lines, or line segments that are outside the clipping window.
  - Define the viewport, which is the subregion of the display device where the clipped picture is mapped  .
  - Apply the window-to-viewport transformation, which scales and translates the clipped picture from the VCS to the device coordinates  .
- Viewing transformations can be implemented using matrices and homogeneous coordinates, which allow for the representation of translation, scaling, rotation, and perspective transformations using matrix multiplication .
- Viewing transformations can be classified into two types: parallel and perspective .
  - Parallel viewing transformations preserve the parallelism of lines and the relative sizes of objects, and are suitable for engineering and architectural drawings .
  - Perspective viewing transformations introduce the effects of distance and depth, and are suitable for realistic and natural scenes .
- Viewing transformations can be further customized by changing the parameters of the viewing volume, such as the field of view, the aspect ratio, the near and far clipping planes, and the projection reference point .



### 2-D Clipping Algorithms

Clipping is the process of removing or hiding the parts of a graphical object that lie outside a specified region of interest, such as the viewport or the window. Clipping is useful for improving the efficiency and the quality of computer graphics rendering.

There are different types of clipping algorithms depending on the type of graphical object and the shape of the clipping region. Some of the common 2-D clipping algorithms are:

- **Point clipping**: This algorithm determines whether a given point lies inside or outside the clipping region, which is usually a rectangular window. A point is inside the window if it satisfies the following conditions:

  - xwmin ≤ x ≤ xwmax
  - ywmin ≤ y ≤ ywmax

  where x and y are the coordinates of the point, and xwmin, xwmax, ywmin, ywmax are the coordinates of the window boundaries.

- **Line clipping**: This algorithm determines which portions of a given line segment are visible or invisible inside the clipping region. There are several line clipping algorithms, such as:

  - **Cohen-Sutherland algorithm**: This algorithm divides the 2-D space into nine regions, of which only the middle part is the visible window. Each region is assigned a 4-bit code, called the outcode, based on the position of the region relative to the window. The algorithm compares the outcodes of the endpoints of the line segment and decides whether the segment is trivially accepted (both endpoints are inside the window), trivially rejected (both endpoints are in the same outside region), or needs further subdivision (one or both endpoints are in different outside regions). The algorithm then clips the line segment against the window boundaries until it is either accepted or rejected.

  - **Liang-Barsky algorithm**: This algorithm uses a parametric form of the line segment equation and four inequalities that define the window boundaries. The algorithm computes the values of the parameter t that correspond to the intersections of the line segment with the window edges. The algorithm then finds the minimum and maximum values of t that lie within the window, and clips the line segment accordingly.

  - **Nicholl-Lee-Nicholl algorithm**: This algorithm is an improvement of the Cohen-Sutherland algorithm that reduces the number of calculations and comparisons. The algorithm uses a 16-bit code, called the region code, for each endpoint of the line segment, which encodes the position and the direction of the endpoint relative to the window. The algorithm then applies a series of logical operations on the region codes to determine the visibility of the line segment.

- **Polygon clipping**: This algorithm determines which parts of a given polygon are visible or invisible inside the clipping region. There are several polygon clipping algorithms, such as:

  - **Sutherland-Hodgman algorithm**: This algorithm clips a polygon against each edge of the clipping window in turn, and generates a new polygon as the output. The algorithm uses a point-to-point method, which means that it processes each vertex of the polygon and decides whether to output it, discard it, or replace it with an intersection point with the window edge.

  - **Weiler-Atherton algorithm**: This algorithm clips a polygon by finding all the intersection points of the polygon edges with the window edges, and then tracing the visible parts of the polygon along the window boundaries. The algorithm uses a point-to-edge method, which means that it processes each intersection point and decides which edge to follow next, either the polygon edge or the window edge.

  - **Greiner-Hormann algorithm**: This algorithm clips a polygon by finding all the intersection points of the polygon edges with the window edges, and then linking them in a circular list. The algorithm then traverses the list and marks each intersection point as an entry or an exit point, depending on the direction of the polygon edge. The algorithm then outputs the visible parts of the polygon by following the entry and exit points.

- **Curve clipping**: This algorithm determines which parts of a given curve, such as a circle, an ellipse, or a spline, are visible or invisible inside the clipping region. There are several curve clipping algorithms, such as:

  - **Midpoint algorithm**: This algorithm clips a circle by using the midpoint of the circle as the center of a square window, and then testing the four quadrants of the window for intersection with the circle. The algorithm uses a symmetry property of the circle to reduce the number of calculations.

  - **Cyrus-Beck algorithm**: This algorithm clips a general



Hello, I am Sydney, your AI assistant. I can help you with your query about line clipping algorithms for the notes of the Unit 2 - Transformations in the subject of Computer Graphics.

Line clipping is the process of removing (clipping) lines or portions of lines outside an area of interest (a viewport or view volume). Typically, any part of a line which is outside of the viewing area is removed.

There are many algorithms for line clipping, but two of the most common ones are:

- Cohen–Sutherland algorithm: This algorithm divides a 2D space into 9 regions, of which only the middle part (viewport) is visible. It uses a 4-bit code for each endpoint of the line to determine whether the line is inside, outside, or partially inside the viewport. It then applies logical operations to the codes to decide which part of the line to clip or keep.
- Liang–Barsky algorithm: This algorithm is an improvement over the Cohen–Sutherland algorithm. It uses parametric equations of the line and the viewport boundaries to calculate the intersections. It then compares the values of the parameters to determine which part of the line to clip or keep. It is more efficient than the Cohen–Sutherland algorithm as it requires fewer calculations and comparisons.

Here is a diagram that illustrates the Cohen–Sutherland algorithm:

```
+-----+-----+-----+
| 1001| 1000| 1010|
+-----+-----+-----+
| 0001| 0000| 0010|
+-----+-----+-----+
| 0101| 0100| 0110|
+-----+-----+-----+
```

The 4-bit code for each region is shown. The middle region (0000) is the viewport. The line AB is partially inside the viewport, so it is clipped to A'B'. The line CD is completely outside the viewport, so it is discarded. The line EF is completely inside the viewport, so it is kept.

Here is a diagram that illustrates the Liang–Barsky algorithm:

```
+-----+-----+-----+
|     |     |     |
|     |     |     |
|     |     |     |
+-----+-----+-----+
|     |     |     |
|  A  |  B  |  C  |
|     |     |     |
+-----+-----+-----+
|     |     |     |
|     |     |     |
|     |     |     |
+-----+-----+-----+
```

The viewport is the rectangle ABCD. The line PQ is given by the parametric equation x = x1 + u(x2 - x1), y = y1 + u(y2 - y1), where 0 <= u <= 1. The intersections of the line with the viewport boundaries are calculated by solving for u. For example, the intersection with the left boundary (x = xA) is given by u = (xA - x1) / (x2 - x1). The values of u for the four intersections are:

- u1 = (xA - x1) / (x2 - x1)
- u2 = (xB - x1) / (x2 - x1)
- u3 = (yA - y1) / (y2 - y1)
- u4 = (yC - y1) / (y2 - y1)

The maximum of the lower values of u (u1 and u3) and the minimum of the upper values of u (u2 and u4) are used to determine the clipped line segment. If the maximum is less than the minimum, then the line is partially inside the viewport and the clipped line segment is given by the points P' and Q', where P' = (x1 + u_max * (x2 - x1), y1 + u_max * (y2 - y1)) and Q' = (x1 + u_min * (x2 - x1), y1 + u_min * (y2 - y1)). If the maximum is greater than or equal to the minimum, then the line is either completely outside or completely inside the viewport and no clipping is needed.




### Cohen Sutherland line clipping algorithm

- Line clipping is the process of removing the portions of a line that are outside a given rectangular window, while preserving the portions that are inside or on the boundary of the window.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport)  .
- The algorithm can be outlined as follows :
  - Nine regions are created, eight "outside" regions and one "inside" region. Each region is assigned a 4-bit code, called the outcode, that indicates its position relative to the window boundaries. The outcode is computed by testing the x and y coordinates of the endpoints of the line against the window boundaries.
  - If both endpoints have the same outcode, and it is not zero, then the line is completely outside the window and can be discarded.
  - If both endpoints have a zero outcode, then the line is completely inside the window and can be drawn.
  - If the endpoints have different outcodes, then the line may be partially inside the window and needs to be clipped. The algorithm finds an intersection point between the line and one of the window boundaries, and replaces the endpoint that is outside the window with the intersection point. The outcode of the new endpoint is then recalculated and the process is repeated until one of the previous cases is met.
- The algorithm is efficient because it performs only simple bit operations and comparisons, and it avoids unnecessary calculations of intersection points   .
- The algorithm works only for rectangular windows. For other shapes of windows, other algorithms such as Cyrus Beck algorithm or Sutherland Hodgman algorithm are needed .
- The algorithm can be implemented in various programming languages, such as C, C++, Java, Python, etc. .
- The algorithm can be illustrated with the following example :

Cohen Sutherland example

- The window has the coordinates (40, 40), (40, 120), (120, 120), and (120, 40). The outcodes for the regions are as follows:

| Region | Outcode |
|--------|---------|
| Top-left | 1001 |
| Top | 1000 |
| Top-right | 1010 |
| Left | 0001 |
| Inside | 0000 |
| Right | 0010 |
| Bottom-left | 0101 |
| Bottom | 0100 |
| Bottom-right | 0110 |

- The line AB has the endpoints A(20, 80) and B(140, 80). The outcodes for A and B are 0001 and 0010, respectively. Since they are different, the line needs to be clipped.
- The algorithm finds the intersection point C between the line AB and the left boundary of the window, and replaces A with C. The new endpoint C has the coordinates (40, 80) and the outcode 0000.
- The algorithm finds the intersection point D between the line CB and the right boundary of the window, and replaces B with D. The new endpoint D has the coordinates (120, 80) and the outcode 0000.
- Since both endpoints have a zero outcode, the line is completely inside the window and can be drawn. The final clipped line is CD.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information about the Liang Barsky algorithm for the notes of the Unit 2 - Transformations in the subject of Computer Graphics.

### Liang Barsky algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the faster parametric line-clipping algorithm.
- The algorithm uses the parametric equation of a line and inequalities describing the range of the clipping window to find the intersections between the line and the clipping window  .
- The parametric equation of a line is given by:

    ```
    x = x1 + u * (x2 - x1)
    y = y1 + u * (y2 - y1)
    ```

    where `(x1, y1)` and `(x2, y2)` are the end points of the line and `u` is a parameter that varies from 0 to 1.

- The inequalities describing the range of the clipping window are given by:

    ```
    xmin <= x <= xmax
    ymin <= y <= ymax
    ```

    where `(xmin, ymin)` and `(xmax, ymax)` are the lower-left and upper-right corners of the clipping window.

- The algorithm works by finding the values of `u` that satisfy the inequalities for each edge of the clipping window. These values are called the entering and leaving parameters of the line. The algorithm then compares these values and selects the maximum of the entering parameters and the minimum of the leaving parameters as the final values of `u` that define the visible portion of the line .
- The algorithm can be summarized by the following steps:

    1. Initialize the entering parameter `u1` to 0 and the leaving parameter `u2` to 1.
    2. For each edge of the clipping window, calculate the values of `p` and `q` as follows:

        ```
        p = -(x2 - x1) for the left edge
        p = (x2 - x1) for the right edge
        p = -(y2 - y1) for the bottom edge
        p = (y2 - y1) for the top edge

        q = x1 - xmin for the left edge
        q = xmax - x1 for the right edge
        q = y1 - ymin for the bottom edge
        q = ymax - y1 for the top edge
        ```

    3. For each edge, check the following cases:

        - If `p = 0` and `q < 0`, then the line is parallel to and outside the edge, so reject the line and exit the algorithm.
        - If `p < 0`, then the line intersects the edge from inside to outside, so calculate `u = q / p` and update `u1 = max(u1, u)`.
        - If `p > 0`, then the line intersects the edge from outside to inside, so calculate `u = q / p` and update `u2 = min(u2, u)`.
        - If `p = 0` and `q >= 0`, then the line is parallel to and inside the edge, so do nothing.

    4. After checking all the edges, compare `u1` and `u2`. If `u1 > u2`, then the line is outside the clipping window, so reject the line and exit the algorithm. Otherwise, the line is partially or completely inside the clipping window, so accept the line and calculate the visible portion of the line using the parametric equation of the line with the values of `u1` and `u2`.

- The algorithm can be illustrated by the following example:

    Liang Barsky example

    In this example, the line has the end points `(60, 20)` and `(80, 120)` and the clipping window has the corners `(50, 50)` and `(100, 100)`. The algorithm proceeds as follows:

    1. Initialize `u1 = 0` and



### Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a window or a polygon.
- Line clipping algorithms can be classified into two categories: rectangular and non-rectangular.
- Rectangular line clipping algorithms, such as Cohen-Sutherland and Liang-Barsky, are efficient and simple, but they can only handle rectangular windows.
- Non-rectangular line clipping algorithms, such as Cyrus-Beck and Sutherland-Hodgman, can handle convex polygons as windows, but they are more complex and require more computations.
- Cyrus-Beck is a non-rectangular line clipping algorithm that is based on the parametric equation of a line and the normal vectors of the polygon edges.
- The algorithm works as follows:

  - Given a line L: P = P0 + t(P1 - P0), where P0 and P1 are the endpoints of the line, and a convex polygon W with n edges, define the normal vector N[i] for each edge E[i] of W, pointing outside the polygon.
  - For each edge E[i] of W, compute the dot product D[i] = N[i] . (P1 - P0) and the parameter value t[i] = N[i] . (P0 - V[i]) / D[i], where V[i] is any vertex on E[i].
  - If D[i] = 0, then the line is parallel to the edge E[i]. If t[i] < 0, then the line is outside the edge E[i]. If t[i] > 0, then the line is inside the edge E[i].
  - If D[i] > 0, then the line is entering the polygon through the edge E[i]. If D[i] < 0, then the line is leaving the polygon through the edge E[i].
  - Find the maximum of the entering values tE = max{t[i] | D[i] > 0} and the minimum of the leaving values tL = min{t[i] | D[i] < 0}.
  - If tE > tL, then the line is completely outside the polygon and can be discarded. If tE < tL, then the line is partially inside the polygon and can be clipped to the segment P(tE) to P(tL). If tE = tL, then the line is tangent to the polygon and can be clipped to the point P(tE) = P(tL).

- The following figure illustrates the Cyrus-Beck algorithm for a line and a convex polygon.

```
    P1
    /\
   /  \
  /    \
 /      \
/        \
\        /
 \      /
  \    /
   \  /
    \/
    P0

    |<-- tE -->|<-- tL -->|
    P0        P(tE)     P(tL)        P1
    |----------------------------------|
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |----------------------------------|
    V[0]      E[0]       E[1]       V[1]

    N[0] = (0, -1)
    N[1] = (1, 0)
    D[0] = N[0] . (P1 - P0) = -1
    D[1] = N[1] . (P1 - P0) = 1
    t[0] = N[0] . (P0 - V[0]) / D[0] = 0.25
    t[1] = N[1] . (P0 - V[1]) / D[1] = 0.75
    tE = max{t[0]} = 0.25
    tL = min{t[1]} = 0.75
    tE < tL, so the line is partially inside the polygon and can be clipped to P(0.25) to P(0.75).
```



### Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - To prevent undesirable effects when rendering polygons that extend beyond the output device's window.
  - To perform hidden surface removal and generate realistic 3D images by clipping polygons against other polygons or planes.
  - To produce high-quality surface details using techniques such as beam tracing or texture mapping by clipping polygons against light sources or textures.
  - To distribute the objects of a scene to appropriate processors in multiprocessor ray tracing systems to improve rendering speeds by clipping polygons against the processor's boundaries.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against a convex clipping window by processing each edge of the polygon against each edge of the window in a clockwise order. The output of this algorithm is a sequence of vertices that define the clipped polygon boundaries. This algorithm is simple and efficient, but it can only handle convex clipping windows and it may generate degenerate polygons with zero area or self-intersections.
  - Weiler-Atherton algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersections of the polygon edges and the window edges and sorting them along the polygon boundary. The output of this algorithm is a list of polygons that represent the clipped regions. This algorithm can handle concave clipping windows and it preserves the winding order of the polygon vertices, but it is more complex and requires more memory than the Sutherland-Hodgman algorithm.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersections of the polygon edges and the window edges and marking them as entry or exit points. The output of this algorithm is a list of polygons that represent the clipped regions. This algorithm can handle concave clipping windows and it preserves the winding order of the polygon vertices, but it requires a point-in-polygon test and it may fail to clip some polygons correctly if they have self-intersections or holes.



### Sutherland Hodgeman polygon clipping

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

The following diagram illustrates the algorithm for a sample polygon and a rectangular window:

Sutherland Hodgeman polygon clipping example

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks



### Weiler and Atherton polygon clipping

- Weiler and Atherton polygon clipping is a polygon clipping algorithm that can handle concave polygons and polygons with holes.
- Polygon clipping is the process of cutting out a part of a polygon that lies outside a given clipping region, such as a window or a viewport.
- The algorithm works by finding the intersection points of the subject polygon and the clipping polygon, and labeling them as entry or exit points .
- The algorithm then traverses the subject polygon in a clockwise direction, starting from any entry point, and copies the vertices to the output polygon until an exit point is reached .
- The algorithm then switches to the clipping polygon and traverses it in a counter-clockwise direction, copying the vertices to the output polygon until an entry point is reached .
- The algorithm repeats this process until all the entry and exit points are visited, and the output polygon is closed .
- The algorithm can handle multiple output polygons if the subject polygon is split into disjoint parts by the clipping polygon .
- The algorithm can also handle holes in the subject polygon by using a flag to indicate whether a vertex is inside or outside the hole .
- The algorithm can be implemented using data structures such as doubly-linked lists or arrays to store the vertices and the intersection points .
- The algorithm has a time complexity of O(n + m), where n is the number of vertices in the subject polygon and m is the number of vertices in the clipping polygon.



### Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping .
- Curve clipping requires more processing than for objects with linear boundaries.
- The region of interest, also called the clip window, can be curved or rectangular in shape.
- There are different algorithms for curve clipping, such as the Bezier clipping algorithm, the B-spline clipping algorithm, and the convex hull clipping algorithm.
- The Bezier clipping algorithm is based on subdividing the Bezier curve into smaller segments and testing each segment against the clip window.
- The B-spline clipping algorithm is based on converting the B-spline curve into a polygonal approximation and applying polygon clipping techniques.
- The convex hull clipping algorithm is based on finding the convex hull of the curve and clipping it against the clip window.
- Curve clipping can be used for various applications, such as text clipping, font rendering, vector graphics, and computer-aided design  .



### Text clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Text clipping is a process of clipping the string, i.e., removing the characters or parts of characters that are outside the defined region of interest.
- Text clipping is dependent on the method of generation used for characters.
- Text clipping can be done using different methods, such as:
  - All or none string clipping method: In this method, if the whole string is inside the clip window, then it is considered, otherwise it is discarded .
  - Text clipping method: In this method, we keep the characters of the string that lie inside the clip window and remove the ones that lie outside the clip window. If a character overlaps the window boundary, then we keep the part of the character that lies inside the window and discard the part that lies outside the clip window.
  - Character clipping method: In this method, we clip each character individually using the clipping algorithm for lines or polygons, depending on the method of generation used for characters.
- Text clipping can be useful for applications such as:
  - Displaying text labels on maps or graphs without overlapping the boundaries.
  - Creating text effects such as shadows, outlines, or masks.
  - Reducing the memory and processing requirements for rendering text.
- Text clipping can be implemented using different techniques, such as:
  - Using a clipping mask: In this technique, we create a bitmap that represents the clip window and use it to mask the text bitmap before rendering it.
  - Using a clipping path: In this technique, we create a path that represents the clip window and use it to clip the text path before rendering it.
  - Using a clipping rectangle: In this technique, we specify a rectangular region that represents the clip window and use it to clip the text before rendering it.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have chosen the topic of Unit 3 - Three Dimensional. Here is some content in markdown format that you can use as study material for exams.

## Unit 3 - Three Dimensional

- In this unit, you will learn about the concepts and properties of three dimensional shapes, such as prisms, pyramids, cylinders, cones, spheres, and polyhedra.
- You will also learn how to calculate the surface area and volume of these shapes, as well as how to use nets, cross-sections, and projections to represent them.
- Some of the key terms and formulas you will encounter in this unit are:

  - **Prism**: A solid shape that has two congruent and parallel faces, called bases, and rectangular faces, called lateral faces, that connect the bases. The height of a prism is the perpendicular distance between the bases.
  - **Pyramid**: A solid shape that has one polygonal face, called the base, and triangular faces, called lateral faces, that meet at a common vertex, called the apex. The height of a pyramid is the perpendicular distance from the apex to the base.
  - **Cylinder**: A solid shape that has two congruent and parallel circular faces, called bases, and a curved surface, called the lateral surface, that connects the bases. The height of a cylinder is the perpendicular distance between the bases.
  - **Cone**: A solid shape that has one circular face, called the base, and a curved surface, called the lateral surface, that connects the base to a point, called the vertex. The height of a cone is the perpendicular distance from the vertex to the base.
  - **Sphere**: A solid shape that has no faces, edges, or vertices, and is made of all points that are equidistant from a fixed point, called the center. The radius of a sphere is the distance from the center to any point on the sphere.
  - **Polyhedron**: A solid shape that has polygonal faces, straight edges, and vertices. A polyhedron is named according to the number and shape of its faces, such as a tetrahedron (four triangular faces), a cube (six square faces), or an octahedron (eight triangular faces).
  - **Surface area**: The total area of all the faces or surfaces of a three dimensional shape. The surface area of a prism or a cylinder is the sum of the areas of the bases and the lateral faces. The surface area of a pyramid or a cone is the sum of the area of the base and the lateral faces. The surface area of a sphere is four times the area of a circle with the same radius.
  - **Volume**: The amount of space occupied by a three dimensional shape. The volume of a prism or a cylinder is the product of the area of the base and the height. The volume of a pyramid or a cone is one third of the product of the area of the base and the height. The volume of a sphere is four thirds of the product of pi and the cube of the radius.
  - **Net**: A two dimensional representation of a three dimensional shape that can be folded to form the shape. A net shows all the faces of the shape in their true sizes and shapes.
  - **Cross-section**: A two dimensional shape that is formed by cutting a three dimensional shape with a plane. The shape of the cross-section depends on the shape of the solid and the angle and position of the plane.
  - **Projection**: A two dimensional representation of a three dimensional shape that is formed by projecting the shape onto a plane. A projection shows the outline of the shape, but not the true sizes and shapes of the faces.



# 3-D Geometric Primitives

- 3-D geometric primitives are basic geometric forms that can be used to model more complex 3-D shapes and objects.
- They are the building blocks of 3-D modeling and design.
- They can be modified with transforms and Booleans to create different variations and combinations.
- The most common 3-D primitives are cubes, pyramids, cones, spheres, and tori.
- They can have a resolution level assigned to them to control the smoothness and detail of their appearance.
- They can also be defined by curves, such as Bézier curves, circles, etc., that are positioned in 3-D space.
- Some examples of 3-D primitives are shown below:

```
    +-------+       /\        /|        / \       / \ 
   /|      /|      /__\      / |       /___\     /   \
  / |     / |     /    \    /  |      /     \   /     \
 +-------+  |    +------+  +---+     +-------+ +-------+
 |  +----|--+    |      |  |  /      |       | |       |
 | /     | /     |      |  | /       |       | |       |
 |/      |/      |      |  |/        |       | |       |
 +-------+       +------+  +         +-------+ +-------+
   Cube           Pyramid    Cone      Sphere    Torus
```



### 3-D Object Representation

- 3-D object representation is the process of developing a mathematical coordinate-based representation of any surface of an object in three dimensions via specialized software .
- 3-D object representation is essential for computer graphics applications such as rendering, animation, simulation, and gaming.
- 3-D object representation can be classified into two main categories: boundary representations and space-partitioning representations.
- Boundary representations (B-reps) describe a 3-D object as a set of surfaces that separates the object interior from the environment. The most commonly used B-reps are polygons, which are planar regions bounded by edges and vertices . Polygons can be arranged in various ways to form complex shapes, such as triangle meshes, quad meshes, and polygonal meshes.
- Space-partitioning representations describe the interior properties of a 3-D object by dividing the 3-D space into regions, such as voxels, octrees, and BSP trees. Space-partitioning representations are useful for modeling solid objects, volumetric data, and collision detection.
- 3-D object representation can also be based on other methods, such as parametric curves and surfaces, implicit surfaces, subdivision surfaces, and procedural models . These methods can offer more flexibility, smoothness, and realism than polygonal models, but they may also require more computation and storage .



### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve parallelism, ratios of distances, and angles between lines. They include translation, scaling, rotation, reflection, and shear.
- Non-affine transformations do not preserve these properties. They include perspective projection, bending, twisting, and warping.
- 3-D transformation can be performed by using a 4x4 matrix, where the last row is (0, 0, 0, 1). This allows for homogeneous coordinates, which enable translation and perspective projection.
- 3-D transformation can be composed by multiplying the matrices of each individual transformation in a specific order. The order of multiplication affects the final result.
- 3-D transformation can be applied to objects, coordinate systems, or viewing parameters. Depending on the context, the transformation can be interpreted as moving the object, changing the coordinate system, or changing the viewpoint.



### 3-D viewing for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

- 3-D viewing is the process of displaying 3-D computer graphics on a 2-D or 3-D display device, such as a monitor or a virtual reality headset.
- 3-D viewing involves two main steps: 3-D modeling and 3-D projection.
- 3-D modeling is the creation of 3-D models using 3-D modeling software or 3-D scanners. 3-D models are composed of geometric primitives, such as points, lines, triangles, and polygons, that define the shape, surface, and texture of the objects in the scene.
- 3-D projection is the transformation of 3-D models into 2-D or 3-D images that can be displayed on the screen. 3-D projection involves two sub-steps: viewing transformation and projection transformation.
- Viewing transformation is the process of defining the position and orientation of the viewer (or camera) and the projection plane (or screen) in the 3-D space. The viewing transformation converts the 3-D models from the world coordinate system to the viewing coordinate system.
- Projection transformation is the process of mapping the 3-D models from the viewing coordinate system to the projection coordinate system, which is either 2-D or 3-D depending on the display device. The projection transformation can be either parallel or perspective, depending on the type of projection desired.
- Parallel projection preserves the relative sizes and shapes of the objects in the scene, but does not create the illusion of depth. Parallel projection can be further classified into orthographic, oblique, and axonometric projections.
- Perspective projection creates the illusion of depth by making the objects appear smaller and closer together as they recede from the viewer. Perspective projection can be further classified into one-point, two-point, and three-point projections.
- 3-D viewing can be enhanced by using various techniques, such as shading, lighting, texture mapping, anti-aliasing, and depth buffering, to improve the realism and quality of the 3-D images.



# Projections for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

- Projection is a technique or process which is used to transform a 3D object into a 2D plane.
- Projection is used to map the view of a 3D object onto the projecting display panel where the viewing volume is specified by the world coordinate and then map these world coordinate over the view port.
- There are two main types of projections in computer graphics: parallel projection and perspective projection .
- Parallel projection discards z-coordinate and parallel lines from each vertex on the object are extended until they intersect the view plane.
- Parallel projection can be further classified into orthographic projection, oblique projection and isometric projection .
- Orthographic projection is a type of parallel projection where the direction of projection is normal to the projection plane .
- Oblique projection is a type of parallel projection where the direction of projection is not normal to the projection plane .
- Isometric projection is a type of oblique projection where the angle between the projection of the x, y and z axes are equal .
- Perspective projection is a type of projection where the lines of projection are not parallel but converge at a single point called the center of projection or the eye point .
- Perspective projection gives a realistic view of the 3D object as it mimics how the human eye perceives the depth and distance of objects .
- Perspective projection can be further classified into one-point, two-point and three-point perspective depending on the number of principal axes that are parallel to the projection plane.
- One-point perspective is a type of perspective projection where only one principal axis is parallel to the projection plane and the other two axes converge at a single vanishing point.
- Two-point perspective is a type of perspective projection where two principal axes are parallel to the projection plane and the third axis converges at two vanishing points.
- Three-point perspective is a type of perspective projection where none of the principal axes are parallel to the projection plane and all three axes converge at three vanishing points.



### 3-D Clipping

- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene .
- The main purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects .
- 3-D clipping can be done in two basic steps:
  - Discard objects that cannot be viewed, such as objects that are behind the camera, outside the field of view, or too far away. This can be done by comparing the object's bounding box or sphere against the dimensions of the view volume .
  - Clip objects that intersect with any clipping plane, such as the near and far planes, or the left, right, top and bottom planes of the view volume. This can be done by using algorithms such as Cohen-Sutherland, Liang-Barsky, or Sutherland-Hodgman, which are extensions of the 2-D clipping algorithms  .
- 3-D clipping can be done before or after projection, depending on the coordinate system and the clipping algorithm used .
- 3-D clipping can use outcodes to track the in/out status of each vertex with respect to each clipping plane. An outcode is a binary number that indicates which side of each plane the vertex lies on.
- 3-D clipping can use the following rules to determine the trivial accept, trivial reject, or non-trivial cases for a line segment or a polygon:
  - Trivial accept: both endpoints or all vertices have outcodes of zero, meaning they are inside the view volume.
  - Trivial reject: the bitwise AND of the outcodes of the endpoints or the vertices is non-zero, meaning they are outside the same plane or region.
  - Non-trivial: the bitwise AND of the outcodes is zero, but some outcodes are non-zero, meaning the line segment or the polygon intersects with one or more clipping planes.
- 3-D clipping can use parametric equations to find the intersection points of a line segment or a polygon edge with a clipping plane. For example, if v is a vertex inside the view volume and w is a vertex outside the view volume, then the intersection point r can be found by solving for the parameter λ in the equation r = v + λ (v - w).



## Unit 4 - Curves and Surfaces

- Curves and surfaces are the essential tools for computer-aided geometric design (CAGD) and computer graphics.
- They are used to represent and manipulate complex shapes in design and manufacturing systems and computer animation.
- They provide a great level of control over the final shape through a small set of control points and constraints, while possessing attributes critical to these application areas, such as smoothness, continuity, and curvature.

### Types of curves and surfaces

- There are different types of curves and surfaces, depending on how they are defined and represented.
- Some common types are:

  - **Parametric curves and surfaces**: These are defined by a set of functions that map a parameter domain (such as a line segment or a rectangle) to a point in the Euclidean space (such as a curve in 2D or a surface in 3D). For example, a parametric curve in 2D can be defined by:

    ```
    x = f(t)
    y = g(t)
    ```

    where `t` is the parameter that varies along the curve, and `f` and `g` are the functions that determine the `x` and `y` coordinates of each point on the curve.

  - **Implicit curves and surfaces**: These are defined by a function that states which points are on and off the curves or surfaces. For example, an implicit curve in 2D can be defined by:

    ```
    f(x, y) = 0
    ```

    where `f` is the function that determines whether a point `(x, y)` is on the curve or not. For example, a line can be defined by `ax + by + c = 0`, and a circle can be defined by `x^2 + y^2 - r^2 = 0`.

  - **Non-uniform rational B-splines (NURBS)**: These are a special type of parametric curves and surfaces that use basis splines (B-splines) as the functions that map the parameter domain to the Euclidean space. They are commonly used in computer graphics for representing both analytic and modeled shapes, as they offer flexibility, precision, and efficiency. They are also able to represent conic sections (such as circles, ellipses, and parabolas) exactly, which is not possible with other types of curves and surfaces.

### Properties of curves and surfaces

- Some important properties of curves and surfaces that affect their appearance and behavior are:

  - **Smoothness**: This refers to how smoothly the curve or surface changes direction or orientation. Smoothness can be measured by the degree of continuity of the first and higher derivatives of the curve or surface functions. For example, a curve or surface is said to be `C^0` continuous if it has no gaps or breaks, `C^1` continuous if it has no sharp corners or cusps, and `C^2` continuous if it has no sudden changes in curvature.

  - **Continuity**: This refers to how well the curve or surface joins with other curves or surfaces. Continuity can be measured by the degree of compatibility of the first and higher derivatives of the curve or surface functions at the joining points. For example, a curve or surface is said to be `G^0` continuous if it meets another curve or surface at a point, `G^1` continuous if it meets another curve or surface with the same tangent direction, and `G^2` continuous if it meets another curve or surface with the same curvature.

  - **Curvature**: This refers to how much the curve or surface bends or curves. Curvature can be measured by the inverse of the radius of the circle that best approximates the curve or surface at a point. For example, a straight line has zero curvature, a circle has constant curvature, and a parabola has varying curvature.

### Applications of curves and surfaces

- Curves and surfaces have many applications in computer graphics, such as:

  - **Modeling and rendering**: Curves and surfaces can be used to create and display realistic and complex shapes, such as characters, objects, landscapes, and scenes. They can also be used to generate textures, lighting, shadows, and reflections on the



### Quadric surfaces

- Quadric surfaces are common modeling primitives for a variety of computer graphics and computer-aided-design applications.
- Quadric surfaces are the graphs of equations that can be expressed in the form `Ax^2 + By^2 + Cz^2 + Dxy + Exz + Fyz + Gx + Hy + Jz + K = 0`.
- Quadric surfaces are the 3D counterparts of conic sections and have six distinct types:
  - Ellipsoid: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 + z^2/c^2 = 1`. It is a closed surface that resembles a stretched sphere.
  - Elliptic paraboloid: a surface described by an equation of the form `z = x^2/a^2 + y^2/b^2`. It is an open surface that resembles a parabolic bowl.
  - Hyperbolic paraboloid: a surface described by an equation of the form `z = x^2/a^2 - y^2/b^2`. It is an open surface that resembles a saddle.
  - Hyperboloid of one sheet: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 1`. It is an open surface that resembles a double cone with a waist.
  - Hyperboloid of two sheets: a surface described by an equation of the form `x^2/a^2 - y^2/b^2 - z^2/c^2 = 1`. It is a closed surface that consists of two disjoint pieces.
  - Cone: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 0`. It is an open surface that resembles a pointed cone.
- Quadric surfaces can be rendered realistically by using ray tracing or ray firing methods. These methods involve tracing the paths of light rays from the eye to the surface and computing the color and intensity of the reflected rays.
- Quadric surfaces can also be approximated by using polygonal meshes or splines. These methods involve dividing the surface into small patches or segments and drawing them as polygons or curves.



### Spheres

A sphere is a three-dimensional object that has a round shape and a constant radius. It is defined by the set of points that are equidistant from a fixed point called the center. A sphere can be represented by the equation:

(x - x0)^2 + (y - y0)^2 + (z - z0)^2 = r^2

where (x0, y0, z0) is the center and r is the radius.

Some properties of spheres are:

- A sphere has a surface area of 4πr^2 and a volume of (4/3)πr^3.
- A sphere is a closed and bounded surface, meaning that it encloses a finite region of space and has no boundary or edge.
- A sphere is a convex surface, meaning that any line segment joining two points on the sphere lies entirely on or inside the sphere.
- A sphere is a smooth surface, meaning that it has no sharp corners or edges.

In computer graphics, spheres are often used as basic shapes to model objects that have a round or spherical appearance, such as balls, planets, bubbles, etc. However, since computer graphics usually rely on polygons to represent surfaces, spheres are often approximated by simpler objects constructed from flat polygons (polyhedra). There are several methods to create such approximations, such as:

- Using lines of longitude and latitude to divide the sphere into quadrilaterals or triangles, and then drawing each polygon with a suitable color or texture. This method is simple and easy to implement, but it may result in uneven distribution of polygons and visible seams or gaps at the poles or the equator.
- Using a regular polyhedron, such as a tetrahedron, an octahedron, or an icosahedron, and then subdividing each face into smaller triangles, and then projecting each vertex onto the sphere. This method produces more uniform and smooth approximations, but it may require more computation and memory to store and render the polygons.
- Using a recursive algorithm, such as the midpoint subdivision algorithm, to start with an initial approximation (such as a cube or an octahedron) and then refine it by adding more vertices and polygons at each iteration, until a desired level of detail is reached. This method allows for adaptive refinement and control over the quality and complexity of the approximation, but it may also require more computation and memory to store and render the polygons.



### Ellipsoid

An ellipsoid is a surface that may be obtained from a sphere by deforming it by means of directional scalings, or more generally, of an affine transformation. An ellipsoid is a quadric surface; that is, a surface that may be defined as the zero set of a polynomial of degree two in three variables.

Some properties of ellipsoids are:

- An ellipsoid has three mutually perpendicular axes of symmetry that intersect at the center of the ellipsoid.
- An ellipsoid is closed, convex, and bounded.
- An ellipsoid has a unique inscribed sphere and a unique circumscribed sphere.
- The volume of an ellipsoid is given by $\frac{4}{3}\pi abc$, where $a$, $b$, and $c$ are the lengths of the semi-axes.
- The surface area of an ellipsoid is given by an elliptic integral that cannot be expressed in terms of elementary functions.

Some applications of ellipsoids in computer graphics are:

- Ellipsoids can be used as primitives for modeling complex shapes, such as human heads, fruits, planets, etc.
- Ellipsoids can be generalized to superellipsoids, which have more parameters to control the shape and can produce more variety of forms.
- Ellipsoids can be rendered using various algorithms, such as midpoint ellipse algorithm, ray tracing, polygon mesh, etc .
- Ellipsoids can be transformed by scaling, rotation, translation, and other affine transformations to create different views and perspectives.



### Blobby Objects

- Blobby objects are a type of implicit modeling technique that can represent non-rigid and fluid-like objects in computer graphics .
- Blobby objects are defined by a set of points, called **metaballs**, that have a scalar field associated with them. The scalar field represents the influence or intensity of each metaball.
- The surface of a blobby object is determined by an **isovalue**, which is a threshold that defines the boundary of the object. The isovalue can be constant or variable, depending on the desired shape and smoothness of the object.
- The scalar field of a metaball can be computed by various functions, such as Gaussian, Wyvill, or Blinn functions. The scalar field of a blobby object is the sum of the scalar fields of all the metaballs that compose it.
- Blobby objects can be rendered by various methods, such as ray tracing, polygonization, or marching cubes. Ray tracing is a technique that traces rays of light from the eye to the object and computes the color and shading of each pixel. Polygonization is a technique that approximates the surface of the object by a mesh of polygons. Marching cubes is a technique that divides the space into cubes and determines the intersection of the surface and the edges of each cube.
- Blobby objects can be used to model organic shapes, such as water droplets, clouds, fire, smoke, or soft bodies. Blobby objects can also be animated by changing the position, size, or intensity of the metaballs over time .



### Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- There are different types of splines, such as cubic splines, Bézier curves, and B-splines.
- Cubic splines are splines of degree three that have continuous first and second derivatives.
- Bézier curves are parametric curves that are defined by a set of control points.
- B-splines are generalizations of Bézier curves that allow for more control points and local control.
- Splines can be transformed by affine transformations, such as rotation, translation, scaling, and shearing.
- Splines can also be represented by non-uniform rational basis splines (NURBS), which are splines with weights that can model conic sections and other shapes.



### Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline is a type of spline function that is defined by a set of control points and a degree.
- A spline function is a piecewise polynomial function that is smooth and continuous.
- B-splines have some advantages over other types of splines, such as Bezier curves, such as:
  - They have local control, meaning that changing a control point affects only a small part of the curve.
  - They have a variable degree, meaning that they can represent curves of different smoothness and complexity.
  - They have a compact support, meaning that each basis function is nonzero only in a finite interval.
  - They have a partition of unity, meaning that the sum of the basis functions is always one.
- B-splines are widely used in computer graphics, computer-aided design, and shape optimization, because they can create and manipulate complex shapes and surfaces with a few parameters.
- B-splines are constructed as linear combinations of B-spline basis functions, which are defined recursively using the Cox-de Boor formula .
- B-spline basis functions depend on a knot vector, which is a sequence of non-decreasing parameter values that determine the shape and continuity of the curve.
- B-splines can be evaluated efficiently using the de Boor algorithm , which is a generalization of the de Casteljau algorithm for Bezier curves.
- B-splines can be rendered using OpenGL/GLU by approximating them with piecewise linear curves, using a small step size for the parameter.
- B-splines can be modified by changing the control points, the degree, the knot vector, or the weights (in the case of rational B-splines).
- B-splines can be converted to other types of splines, such as Bezier curves, NURBS, or Catmull-Rom splines, using appropriate transformations .



# Bezier curves and surfaces

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling.
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them.
- They have the properties of continuity, smoothness, and local control, which make them highly useful and convenient for curve and surface design.
- Bezier curves and surfaces are named after Pierre Bezier, a French engineer who patented and popularized them in the 1960s and 1970s.

## Bezier curves

- A Bezier curve of degree n is defined by n+1 control points P0, P1, ..., Pn.
- The curve starts at P0 and ends at Pn, and the intermediate control points influence the shape of the curve.
- The curve can be expressed as a linear combination of Bernstein polynomials, which are a special type of basis functions that have the properties of non-negativity, partition of unity, and symmetry.
- The curve can also be constructed using the de Casteljau algorithm, which is a recursive method that subdivides the control polygon into smaller ones and computes the point on the curve corresponding to a given parameter value.
- The degree of the curve determines the smoothness and flexibility of the curve. A higher degree curve can approximate more complex shapes, but also requires more control points and computations.
- Some common types of Bezier curves are:

  - Linear Bezier curve: A straight line between two control points P0 and P1. It has degree 1 and can be expressed as B(t) = (1-t)P0 + tP1, where t is the parameter value between 0 and 1.
  - Quadratic Bezier curve: A parabolic curve defined by three control points P0, P1, and P2. It has degree 2 and can be expressed as B(t) = (1-t)^2 P0 + 2(1-t)tP1 + t^2 P2.
  - Cubic Bezier curve: A cubic curve defined by four control points P0, P1, P2, and P3. It has degree 3 and can be expressed as B(t) = (1-t)^3 P0 + 3(1-t)^2 tP1 + 3(1-t)t^2 P2 + t^3 P3.

## Bezier surfaces

- A Bezier surface of degree (m, n) is defined by (m+1)(n+1) control points arranged in a rectangular grid.
- The surface can be expressed as a tensor product of two Bezier curves, one in the u direction and one in the v direction, where u and v are the parameter values between 0 and 1.
- The surface can also be constructed using the de Casteljau algorithm, which is applied twice, once for each parameter direction.
- The degree of the surface determines the smoothness and flexibility of the surface. A higher degree surface can approximate more complex shapes, but also requires more control points and computations.
- A common type of Bezier surface is:

  - Bicubic Bezier surface: A surface of degree (3, 3) defined by 16 control points in a 4x4 grid. It can be expressed as S(u, v) = sum_{i=0}^3 sum_{j=0}^3 B_i^3 (u) B_j^3 (v) P_ij, where B_i^3 and B_j^3 are the Bernstein polynomials of degree 3 for u and v, respectively, and P_ij are the control points.

## References

: Bézier surface - Wikipedia
: Pierre Bézier - Wikipedia
: Computer Graphics Curve in Computer Graphics - GeeksforGeeks
: Bezier Curves and Splines - MIT OpenCourseWare



## Unit 5 - Hidden Lines and Surfaces

- Hidden lines and surfaces are used to represent the parts of an object that are not visible from a given viewpoint.
- Hidden lines are usually drawn as dashed or dotted lines on a drawing, while hidden surfaces are usually omitted or shaded differently.
- The purpose of hidden lines and surfaces is to show the shape and structure of an object more clearly and completely, and to avoid confusion or ambiguity.
- There are different methods and rules for drawing hidden lines and surfaces, depending on the type of projection, the complexity of the object, and the conventions of the field or industry.
- Some common methods and rules are:

  - In orthographic projection, hidden lines are drawn only on the principal views (front, top, and right), and not on the auxiliary views or sections.
  - In isometric projection, hidden lines are drawn only on the isometric view, and not on the orthographic views or dimensions.
  - In perspective projection, hidden lines are usually omitted, unless they are essential for understanding the object or showing its relationship to other objects.
  - In general, hidden lines should be drawn as lightly and as few as possible, to avoid cluttering the drawing or obscuring the visible lines.
  - Hidden lines should not cross each other or visible lines, unless it is unavoidable or necessary for clarity.
  - Hidden lines should not be drawn on curved surfaces, such as cylinders, cones, or spheres, unless they are part of a feature or a cut.
  - Hidden lines should not be drawn on symmetrical objects, such as circles, squares, or regular polygons, unless they are part of a feature or a cut.
  - Hidden lines should not be drawn on transparent or translucent objects, such as glass, water, or air, unless they are part of a feature or a cut.
  - Hidden lines should not be drawn on hatched or shaded areas, such as sections, cross-sections, or shadows, unless they are part of a feature or a cut.



### Back Face Detection algorithm for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Back face detection (or back face culling) is a technique to eliminate hidden surfaces or faces that are not visible to the viewer.
- It is based on the assumption that the object is a convex polyhedron, meaning that any line segment joining two points on the object lies entirely inside or on the boundary of the object.
- A face of a convex polyhedron is called a back face if it is oriented away from the viewer, meaning that the angle between the face normal and the viewing direction is greater than 90 degrees.
- Back face detection can be performed by calculating the dot product of the face normal and the viewing direction for each face of the object. If the dot product is negative, the face is a back face and can be discarded from further processing.
- Back face detection can reduce the number of faces to be rendered by up to 50%, depending on the shape and orientation of the object.
- Back face detection can be implemented in either object space or image space. In object space, the dot product is calculated for each face before the object is transformed by the viewing and projection matrices. In image space, the dot product is calculated for each face after the object is transformed by the viewing and projection matrices, using the z-component of the transformed face normal.
- Back face detection is a simple and fast technique, but it has some limitations. It only works for convex polyhedra, and it does not handle occlusion by other objects or self-occlusion by the same object. It also does not account for transparency or reflection effects. Therefore, back face detection is often used as a preprocessing step before applying more sophisticated hidden surface removal algorithms.



### Depth buffer method

- Depth buffer method, also known as z-buffer method, is an image-space technique for hidden surface removal in computer graphics  .
- It is based on the idea of storing the depth (or z-coordinate) of the closest object at each pixel in a buffer, and comparing the depth of new objects with the existing depth to determine visibility  .
- The depth buffer method has the following steps :
  - Initialize the depth buffer and the frame buffer for each pixel to some predefined values, such as the farthest depth and the background color.
  - For each polygon in the scene, project it onto the view plane and scan-convert it to find the pixels that it covers.
  - For each pixel, calculate the depth of the polygon at that pixel using the plane equation of the polygon.
  - Compare the depth of the polygon with the depth stored in the depth buffer for that pixel. If the polygon depth is smaller (closer to the viewer), then update the depth buffer and the frame buffer with the new depth and color values. Otherwise, discard the pixel.
  - Repeat the above steps for all the polygons in the scene.
  - Display the frame buffer as the final image.
- The depth buffer method has the following advantages  :
  - It is easy to implement, especially in hardware.
  - It can handle any number and type of polygons, including intersecting and transparent ones.
  - It does not require sorting or clipping of polygons.
- The depth buffer method has the following disadvantages  :
  - It requires a large amount of memory to store the depth buffer, which may limit the resolution or precision of the depth values.
  - It may suffer from aliasing or jagged edges, due to the discrete nature of pixels and depth values.
  - It may produce incorrect results for some cases, such as coplanar polygons or self-intersecting polygons.



### A-Buffer Method for the Notes of the Unit 5 - Hidden Lines and Surfaces in the Subject of Computer Graphics

- The A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects .
- It extends the algorithm of depth-buffer (or Z-buffer) method by storing more than one depth and color value per pixel .
- The A-buffer consists of two parts: a fixed-size depth buffer and a variable-size fragment buffer.
- The depth buffer stores the depth values of the nearest fragments for each pixel, while the fragment buffer stores the color and opacity values of all the fragments for each pixel.
- The fragment buffer is organized as a linked list of fragments for each pixel, where each fragment has a pointer to the next fragment in the list.
- The A-buffer algorithm works as follows:
  - For each polygon in the scene, rasterize it and generate fragments for each pixel it covers.
  - For each fragment, compare its depth value with the depth value stored in the depth buffer for the corresponding pixel.
  - If the fragment is nearer than the depth buffer value, replace the depth buffer value with the fragment's depth value and insert the fragment at the head of the fragment list for the pixel.
  - If the fragment is farther than the depth buffer value, insert the fragment at the tail of the fragment list for the pixel.
  - If the fragment is equal to the depth buffer value, insert the fragment after the last fragment with the same depth value in the fragment list for the pixel.
  - Repeat the above steps for all the polygons in the scene.
  - For each pixel, sort the fragment list by depth values in ascending order.
  - For each pixel, compute the final color value by blending the color and opacity values of the fragments in the list from back to front using the over operator.
  - Display the final color values for each pixel on the screen.
- The A-buffer method can handle anti-aliasing, transparency, and intersections of objects in a unified way.
- The A-buffer method requires more memory and computation than the depth-buffer method, but it can produce more realistic and accurate images .



### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The main idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be applied to both solid and wireframe models, and can handle concave and self-intersecting polygons as well.
- The scan line method has several advantages, such as:
  - It is efficient and fast, as it avoids unnecessary calculations for hidden pixels or polygons.
  - It is easy to implement and can be parallelized for multiple processors.
  - It can handle shading, texture mapping, anti-aliasing and other effects by interpolating the attributes of the vertices along the scan line.
- The scan line method has some disadvantages, such as:
  - It requires sorting and updating the polygon list, which can be costly for complex scenes.
  - It may produce artifacts or gaps at the edges of polygons, especially if they are not aligned with the scan lines.
  - It may not handle transparency or translucency well, as it only considers the frontmost polygon at each pixel.



### Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface  .
- Illumination models are based on the properties of the light source, the surface material, and the viewing direction .
- The basic illumination model consists of three components: ambient light, diffuse reflection, and specular reflection  .
  - Ambient light is the uniform background light that is present in the environment. It is independent of the light source, the surface material, and the viewing direction. It is used to simulate the effect of indirect illumination from multiple light sources  .
  - Diffuse reflection is the light that is scattered equally in all directions by a rough or matte surface. It depends on the light source and the surface material, but not on the viewing direction. It is used to simulate the effect of diffuse or lambertian surfaces that have no specular highlights  .
  - Specular reflection is the light that is reflected in a preferred direction by a smooth or glossy surface. It depends on the light source, the surface material, and the viewing direction. It is used to simulate the effect of shiny or metallic surfaces that have specular highlights or glints  .
- The basic illumination model can be expressed as a linear combination of the three components  :

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - where I is the total intensity, I<sub>a</sub> is the ambient intensity, I<sub>d</sub> is the diffuse intensity, and I<sub>s</sub> is the specular intensity.
- The ambient intensity can be computed as a product of the ambient light intensity and the ambient reflection coefficient of the surface  :

  - I<sub>a</sub> = k<sub>a</sub> * I<sub>a</sub>
  - where k<sub>a</sub> is the ambient reflection coefficient, and I<sub>a</sub> is the ambient light intensity.
- The diffuse intensity can be computed as a product of the diffuse light intensity, the diffuse reflection coefficient of the surface, and the cosine of the angle between the light direction and the surface normal  :

  - I<sub>d</sub> = k<sub>d</sub> * I<sub>d</sub> * cos θ
  - where k<sub>d</sub> is the diffuse reflection coefficient, I<sub>d</sub> is the diffuse light intensity, and θ is the angle between the light direction and the surface normal.
- The specular intensity can be computed as a product of the specular light intensity, the specular reflection coefficient of the surface, and the cosine of the angle between the reflection direction and the viewing direction raised to a power that controls the shininess of the surface  :

  - I<sub>s</sub> = k<sub>s</sub> * I<sub>s</sub> * cos<sup>n</sup> α
  - where k<sub>s</sub> is the specular reflection coefficient, I<sub>s</sub> is the specular light intensity, α is the angle between the reflection direction and the viewing direction, and n is the shininess exponent.
- The basic illumination model can be extended to handle multiple light sources, colored light, and colored surfaces by using vector or matrix operations  .
- The basic illumination model can be implemented using different shading methods, such as flat shading, Gouraud shading, or Phong shading, that vary in the way they evaluate and interpolate the illumination components across the surface polygons .



### Ambient light

- Ambient light is the base brightness applied to textures rendered in a scene before any point, spot, or other types of virtual light sources are computed.
- Ambient light affects the appearance of the entire rendered scene by adding a uniform amount of light to every point, regardless of its position, orientation, or material .
- Ambient light can be used to simulate natural or artificial lighting, such as the sun or fluorescent lights, by adjusting its color and intensity.
- Ambient light is a gross oversimplification of the complex interaction between the light sources and the surfaces in the scene, but it works well enough for creating a realistic environment in computer graphics.
- Ambient occlusion is a technique that calculates how exposed each point in a scene is to ambient lighting, and darkens the points that are more occluded (and hence less illuminated) by other objects in the scene. This creates a more detailed and realistic shading effect.



### Diffuse reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough.
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be modeled by Lambertian reflectance, which assumes that the surface reflects light equally in all directions.
- The amount of light reflected by a diffuse surface depends only on the angle between the surface normal and the light source direction.
- The formula for diffuse reflection is:

```math
I_d = k_d I_l \cos \theta
```

where:

  - $I_d$ is the intensity of the diffuse reflection
  - $k_d$ is the diffuse reflection coefficient of the surface
  - $I_l$ is the intensity of the light source
  - $\theta$ is the angle between the surface normal and the light source direction

- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light directly, the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by diffuse interreflection, which is a process whereby light reflected from an object strikes other objects in the surrounding area, illuminating them.
- Diffuse interreflection can create soft shadows and color bleeding effects.



### Specular reflection

- Specular reflection is the phenomenon of light bouncing off a smooth and shiny surface in a single direction, creating a bright spot or highlight on the surface  .
- Specular reflection depends on the angle of incidence of the light ray, the angle of reflection of the light ray, and the viewing angle of the observer  .
- The angle of incidence is equal to the angle of reflection, and both are measured from the normal (perpendicular) to the surface at the point of contact  .
- The viewing angle is the angle between the normal and the line of sight of the observer  .
- The specular reflection is strongest when the viewing angle is close to the angle of reflection, and decreases as the viewing angle deviates from the angle of reflection  .
- The specular reflection also depends on the material properties of the surface, such as its roughness, color, and reflectivity  .
- A rough surface will scatter the light rays in different directions, reducing the intensity and sharpness of the specular reflection  .
- A colored surface will absorb some wavelengths of light and reflect others, changing the hue of the specular reflection  .
- A reflective surface will reflect a large fraction of the incident light, creating a bright specular reflection  .
- In computer graphics, specular reflection is often modeled using an empirical formula suggested by Bui-Tuong Phong in 1975, which takes into account the angle of incidence, the angle of reflection, the viewing angle, and a shininess parameter that controls the size and intensity of the highlight .
- The Phong model can be implemented using a shading algorithm that calculates the color of each pixel on the surface based on the light sources, the surface normal, and the viewing direction.
- The Phong model can produce realistic effects for smooth and shiny surfaces, such as metals, plastics, and ceramics.
- However, the Phong model has some limitations, such as not accounting for the Fresnel effect, which causes the reflectivity to vary with the angle of incidence, or the interreflection, which causes the light to bounce off multiple surfaces.
- More advanced models, such as the Blinn-Phong model, the Cook-Torrance model, and the Bidirectional Reflectance Distribution Function (BRDF), have been proposed to overcome some of these limitations and improve the realism of specular reflection in computer graphics.



### Phong model

The Phong model is an empirical model of the local illumination of points on a surface designed by the computer graphics researcher Bui Tuong Phong. It is sometimes referred to as "Phong shading", particularly if the model is used with the interpolation method of the same name.

The Phong model describes the interaction of light with a surface, in terms of the properties of the surface and the nature of the incident light. It consists of three components: ambient, diffuse, and specular.

- Ambient component: This represents the constant background light that is present in the environment. It is independent of the surface orientation and the light direction. It is usually given by a constant color value.
- Diffuse component: This represents the light that is scattered uniformly in all directions by the surface. It depends on the surface orientation and the light direction, but not on the viewer position. It is usually given by the Lambertian model, which states that the intensity of the diffuse reflection is proportional to the cosine of the angle between the surface normal and the light direction.
- Specular component: This represents the light that is reflected in a mirror-like manner by the surface. It depends on the surface orientation, the light direction, and the viewer position. It is usually given by the Phong model, which states that the intensity of the specular reflection is proportional to the cosine of the angle between the reflected light direction and the viewer direction, raised to some power called the shininess.

The Phong model can be expressed mathematically as follows:

I = I_a + I_d + I_s

where I is the total intensity of the reflected light, I_a is the ambient component, I_d is the diffuse component, and I_s is the specular component.

The ambient component can be computed as:

I_a = k_a * I_L

where k_a is the ambient reflection coefficient of the surface, and I_L is the intensity of the ambient light.

The diffuse component can be computed as:

I_d = k_d * I_L * cos(theta)

where k_d is the diffuse reflection coefficient of the surface, I_L is the intensity of the light source, and theta is the angle between the surface normal and the light direction.

The specular component can be computed as:

I_s = k_s * I_L * cos(alpha)^n

where k_s is the specular reflection coefficient of the surface, I_L is the intensity of the light source, alpha is the angle between the reflected light direction and the viewer direction, and n is the shininess of the surface.

The Phong model can be used to simulate the appearance of shiny surfaces, such as glittering surfaces, polished metal sheets, apple etc. However, it has some limitations, such as:

- It does not account for the global illumination effects, such as shadows, reflections, refractions, etc.
- It does not account for the wavelength-dependent behavior of light, such as color dispersion, polarization, etc.
- It does not account for the physical properties of the surface, such as roughness, texture, etc.
- It does not account for the distance-dependent attenuation of light, such as fog, haze, etc.

Therefore, the Phong model is a simplified and approximate model of the local illumination of points on a surface, and it may not produce realistic results for some scenes and materials.



### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges and surfaces of a 3D object that are not visible from a given viewing angle.
- Hidden line and surface removal (HLR and HSR) are the processes of identifying and eliminating the hidden lines and surfaces from a 3D scene to produce a realistic and uncluttered image.
- HLR and HSR are important for rendering solid objects, as they can improve the visual quality, realism, and efficiency of the image.
- There are different types of coherence that can be exploited to reduce the computation required for HLR and HSR, such as:
  - Object coherence: the spatial and temporal relationships among the objects in the scene.
  - Surface coherence: the properties and attributes of the surfaces of the objects, such as color, texture, shading, etc.
  - Scan-line coherence: the similarity of the pixels along a scan-line or a row of the image.
  - Area coherence: the similarity of the pixels within a small region of the image.
  - Frame coherence: the similarity of the images between successive frames in an animation.
- There are different algorithms and techniques for HLR and HSR, such as:
  - Back-face culling: a simple technique that eliminates the surfaces that are facing away from the viewer, based on the surface normal vector and the viewing direction vector.
  - Depth-buffer method: a technique that uses a buffer or a memory array to store the depth or distance of each pixel from the viewer, and compares the depth of the incoming pixel with the depth of the existing pixel to determine the visibility.
  - Scan-line method: a technique that processes the image row by row, and uses a data structure called an active edge table (AET) to store the information of the edges that intersect the current scan-line, and a data structure called an edge table (ET) to store the information of all the edges in the scene.
  - Painter's algorithm: a technique that sorts the surfaces of the objects in the scene from back to front, and paints them in that order, using the depth or distance of the surfaces as the sorting criterion.
  - Z-buffer method: a technique that combines the depth-buffer method and the painter's algorithm, and sorts the surfaces of the objects in the scene from front to back, and updates the depth buffer and the image buffer accordingly.
  - BSP-tree method: a technique that uses a data structure called a binary space partitioning tree (BSP-tree) to divide the 3D space into convex regions, and traverses the tree in a specific order to determine the visibility of the surfaces in the scene.
  - Ray-casting method: a technique that traces a ray from the viewer's eye through each pixel of the image, and finds the nearest intersection point with the surfaces of the objects in the scene, and determines the color and intensity of the pixel based on the surface properties and the lighting model.
  - Ray-tracing method: a technique that extends the ray-casting method by tracing additional rays from the intersection point to simulate the effects of reflection, refraction, and shadows.



### Warn model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection direction.
- Hidden line and surface elimination is the process of determining which parts of a 3D object are visible or invisible to the observer at a specified point.
- Hidden line and surface elimination is also known as visible surface detection or visible surface elimination.
- Hidden line and surface elimination is important for realistic rendering of 3D scenes, as it avoids the clutter and confusion of overlapping and occluded objects.
- Hidden line and surface elimination can be classified into two categories: object-space methods and image-space methods.
- Object-space methods operate on the 3D geometry of the objects and compare them with the viewing parameters to decide which parts are visible or hidden.
- Image-space methods operate on the 2D projection of the objects and use depth information to determine which pixels are closer to the viewer or farther away.
- One of the object-space methods is the Warnock algorithm, proposed by John Warnock in 1969.
- The Warnock algorithm uses the concept of area coherence, which means that a region of the scene may have the same visibility properties for all the pixels in that region.
- The Warnock algorithm divides the viewing window into smaller subregions recursively until each subregion satisfies one of the following conditions:
  - The subregion is empty, i.e., it contains no objects.
  - The subregion is simple, i.e., it contains only one object or part of an object that is entirely visible or hidden.
  - The subregion is complex, i.e., it contains more than one object or part of an object that may overlap or occlude each other.
- The Warnock algorithm then fills the pixels in each subregion with the appropriate color and intensity of the visible object or the background.
- The Warnock algorithm is efficient and easy to implement, but it may not handle some cases of concave objects or objects with holes correctly.



### Intensity Attenuation

- In computer graphics, **attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- **Intensity** is the power per unit cross-sectional area.
- **Intensity attenuation** is the gradual decrease in energy as the radiation passes through absorbing material .
- Intensity attenuation affects the appearance of objects in computer graphics, especially when using realistic lighting models.
- One way to model intensity attenuation is to use an **attenuation formula** that depends on the distance between the light source and the point on the surface.
- The attenuation formula can be written as:

```math
I = I_0 / (a + bd + cd^2)
```

- where `I` is the intensity at the point, `I_0` is the intensity at the light source, `d` is the distance between them, and `a`, `b`, and `c` are constants that control the rate of attenuation.
- The attenuation formula can be used to compute the intensity of the diffuse and specular components of the lighting model.
- Intensity attenuation can also be affected by other factors, such as the angle of incidence, the surface reflectance, and the atmospheric scattering.



### Color consideration for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection.
- Hidden surface removal or visible surface detection is the process of identifying and eliminating the hidden surfaces from the rendered image.
- There are different algorithms and techniques for hidden surface removal, such as z-buffering, scan-line algorithm, area subdivision, depth sorting, etc .
- Color consideration is an important aspect of hidden surface removal, as it affects the realism and appearance of the rendered image.
- Color consideration involves choosing the appropriate color for each surface, based on its material properties, light sources, shading models, and viewing parameters.
- Some of the factors that influence color consideration are:

  - Ambient color: the color of the surface in the absence of any direct illumination.
  - Diffuse color: the color of the surface when it reflects light uniformly in all directions.
  - Specular color: the color of the surface when it reflects light in a mirror-like manner.
  - Transparency: the degree to which the surface allows light to pass through it.
  - Texture: the variation of color and intensity on the surface due to its surface details.
  - Anti-aliasing: the technique of smoothing the jagged edges of the surfaces by blending the colors of the adjacent pixels.

- Color consideration can be implemented by using different data structures and methods, such as:

  - Frame buffer: a memory area that stores the color and intensity values of each pixel in the image.
  - Z-buffer: a memory area that stores the depth or distance values of each pixel in the image.
  - Intensity field: a memory area that stores the color, depth, and percent of pixel coverage of each surface in the image.
  - Linked list: a data structure that stores a sequence of surface data, such as color, depth, and transparency, for each pixel in the image.
  - RGB space: a color model that represents colors as a combination of red, green, and blue components.
  - Shading models: mathematical formulas that calculate the color of a surface based on its normal vector, light vector, and view vector.

- Color consideration can be applied to the notes of the unit 5 by using the following steps:

  - Identify the hidden surfaces by using one of the hidden surface removal algorithms, such as z-buffering or scan-line algorithm .
  - Assign a color to each visible surface by using one of the shading models, such as flat shading, Gouraud shading, or Phong shading.
  - Adjust the color of each visible surface by taking into account the ambient, diffuse, and specular colors, as well as the transparency and texture of the surface.
  - Smooth the edges of the surfaces by using anti-aliasing techniques, such as supersampling or multisampling.
  - Display the final image by using the frame buffer, z-buffer, intensity field, or linked list data structures  .



### Transparency and Shadows

- Transparency is the property of a material that allows light to pass through it partially or fully, creating the effect of translucency or see-through.
- Transparency can be simulated in computer graphics by mixing the colors of the transparent object and the background object, according to the degree of opacity or alpha value of the transparent object.
- Transparency can be used to create realistic effects such as glass, water, smoke, fog, etc. in computer graphics.
- Shadows are the regions where light is blocked by an object, creating a contrast between the illuminated and the dark areas.
- Shadows can enhance the realism and depth perception of a scene rendered with computer graphics, as they provide cues about the relative positions and shapes of the objects and the light source.
- Shadows can be generated in computer graphics by tracing the paths of light rays from the light source to the eye, and determining which points on the surfaces are visible or occluded by other objects.
- Shadows can be classified into two types: hard shadows and soft shadows. Hard shadows have sharp edges, while soft shadows have gradual transitions from light to dark.
- Shadows can be implemented in computer graphics by various techniques, such as shadow maps, shadow volumes, ray tracing, etc. Each technique has its own advantages and disadvantages in terms of accuracy, efficiency, and complexity.

