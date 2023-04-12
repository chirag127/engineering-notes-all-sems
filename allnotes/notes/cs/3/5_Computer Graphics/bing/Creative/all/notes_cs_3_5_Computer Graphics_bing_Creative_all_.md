

## Unit 1 - Introduction and Line Generation

- This unit introduces the basic concepts and techniques of computer graphics, such as pixels, coordinates, primitives, rasterization, and interpolation.
- It also covers the algorithms for generating lines, circles, and other curves on a raster display, such as DDA, Bresenham's, and Midpoint algorithms.
- The objectives of this unit are to:
  - Understand the fundamentals of computer graphics and its applications.
  - Learn how to represent and manipulate graphical objects using pixels and coordinates.
  - Learn how to draw lines, circles, and curves using various algorithms and compare their advantages and disadvantages.
  - Implement the line generation algorithms in a programming language of your choice.

### 1.1 Introduction to Computer Graphics

- Computer graphics is the field of study that deals with the creation, manipulation, and display of images using computers.
- Computer graphics can be divided into two main categories: raster graphics and vector graphics.
  - Raster graphics are composed of pixels, which are discrete units of color that form a grid on the screen. Each pixel has a fixed location and size, and can only display one color at a time. Examples of raster graphics are digital photos, paintings, and video games.
  - Vector graphics are composed of geometric primitives, such as points, lines, curves, and polygons, that are defined by mathematical equations. Each primitive has attributes such as color, thickness, and style, and can be scaled, rotated, and transformed without losing quality. Examples of vector graphics are logos, fonts, and diagrams.
- Computer graphics can also be classified based on the dimensionality of the images: 2D graphics and 3D graphics.
  - 2D graphics are images that have only two dimensions: width and height. They are typically used for illustrations, icons, and user interfaces. 2D graphics can be created using raster or vector techniques, or a combination of both.
  - 3D graphics are images that have three dimensions: width, height, and depth. They are typically used for simulations, animations, and virtual reality. 3D graphics are usually created using vector techniques, and then rendered into raster images using various algorithms and techniques.
- Computer graphics has many applications in various domains, such as entertainment, education, engineering, medicine, and art. Some examples of computer graphics applications are:
  - Video games, which use computer graphics to create immersive and interactive environments and characters for the players.
  - Computer-aided design (CAD), which uses computer graphics to design and model complex objects and structures, such as buildings, cars, and machines.
  - Computer animation, which uses computer graphics to create realistic and expressive movements and expressions for characters and objects, such as cartoons, movies, and advertisements.
  - Data visualization, which uses computer graphics to present and analyze large and complex data sets, such as maps, charts, and graphs.
  - Image processing, which uses computer graphics to enhance, modify, and manipulate images, such as filters, effects, and transformations.

### 1.2 Pixels and Coordinates

- A pixel, short for picture element, is the smallest unit of a raster image that can be displayed on a screen. A pixel has a fixed location, size, and color, and cannot be subdivided further.
- The color of a pixel is determined by its color model, which is a way of representing colors using numerical values. The most common color models are RGB (red, green, blue), CMYK (cyan, magenta, yellow, black), and HSL (hue, saturation, lightness).
  - RGB is based on the additive color mixing of three primary colors: red, green, and blue. Each color component can have a value from 0 to 255, where 0 means no color and 255 means full color. For example, the color white is represented by (255, 255, 255), and the color black is represented by (0, 0, 0).
  - CMYK is based on the subtractive color mixing of four primary colors: cyan, magenta, yellow, and black. Each color component can have a value from 0 to 100, where 0 means full color and 100 means no color. For example, the color white is represented by (0, 0, 0, 0), and the color black is represented by (0, 0, 0, 100).
  - HSL is based on the perceptual attributes of color: hue, saturation, and lightness. Hue is the color itself, ranging from 0 to 360 degrees, where 0 is red, 120 is green, and 240 is blue. Saturation is the intensity of the color,



# Types of computer graphics

Computer graphics are the visual representation of data and information using computers and software. Computer graphics can be used for various purposes, such as creating images, animations, simulations, games, user interfaces, and more.

There are different types of computer graphics, depending on how the images are created and stored. The main types of computer graphics are:

- **Raster graphics**: Raster graphics are made up of pixels, which are small dots of color arranged in a grid. Each pixel has a specific color and brightness value. Raster graphics are also known as bitmap graphics, because they map each pixel to a specific location in memory. Raster graphics are commonly used for digital photos, web graphics, and video games. The quality of raster graphics depends on the resolution, which is the number of pixels per unit of area. Higher resolution means more detail and clarity, but also more memory and processing power required. Raster graphics can be edited by changing the color and brightness of individual pixels or groups of pixels. However, raster graphics are not scalable, meaning that they lose quality when enlarged or reduced. Examples of raster graphics formats are JPEG, PNG, GIF, BMP, and TIFF.

- **Vector graphics**: Vector graphics are made up of paths, which are lines or curves defined by mathematical equations. Each path has attributes such as color, stroke, fill, and style. Vector graphics are also known as object-oriented graphics, because they treat each path as an independent object that can be moved, resized, rotated, and transformed. Vector graphics are commonly used for logos, icons, diagrams, illustrations, and fonts. The quality of vector graphics does not depend on the resolution, because they are resolution-independent. Vector graphics can be scaled up or down without losing quality, because they are redrawn according to the mathematical equations. Vector graphics can be edited by changing the attributes and equations of the paths or objects. Examples of vector graphics formats are SVG, EPS, PDF, and AI.

- **Animated graphics**: Animated graphics are a sequence of images that create the illusion of motion. Animated graphics can be either raster or vector, depending on the type of images used. Animated graphics are commonly used for cartoons, movies, web pages, and games. The quality of animated graphics depends on the frame rate, which is the number of images displayed per second. Higher frame rate means smoother and more realistic motion, but also more memory and processing power required. Animated graphics can be edited by changing the images or the timing of the sequence. Examples of animated graphics formats are GIF, APNG, WebP, and MP4.



# Graphic Displays for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Graphic displays are devices that can show images or graphics on a screen or other surface. They are used for various purposes, such as displaying information, creating visual effects, or rendering realistic scenes.
- Graphic displays can be classified into two types: raster and vector. Raster displays use pixels, which are small dots of color, to form images. Vector displays use lines, curves, and polygons, which are defined by mathematical equations, to form images.
- Raster displays are more common and widely used, as they can display complex and realistic images with high resolution and color depth. However, they also require more memory and processing power, and can suffer from aliasing, which is the appearance of jagged edges or staircases on diagonal or curved lines.
- Vector displays are less common and mostly used for specialized applications, such as computer-aided design (CAD), scientific visualization, or gaming. They can display smooth and crisp lines and curves, and can be easily scaled or rotated without losing quality. However, they cannot display detailed textures or shading, and can be difficult to create or edit.
- Some examples of raster displays are liquid crystal displays (LCDs), light-emitting diode (LED) displays, organic light-emitting diode (OLED) displays, and cathode ray tube (CRT) monitors. Some examples of vector displays are oscilloscopes, pen plotters, and laser projectors.
- Graphic displays can also be characterized by their properties, such as size, resolution, aspect ratio, refresh rate, color gamut, contrast ratio, brightness, and viewing angle. These properties affect the quality and performance of the display, and can vary depending on the type and model of the display.
- Size is the diagonal measurement of the display screen, usually in inches. Resolution is the number of pixels that the display can show, usually in width by height format. Aspect ratio is the ratio of the width to the height of the display, usually expressed as a fraction or a decimal. Refresh rate is the number of times that the display updates the image per second, usually in hertz (Hz). Color gamut is the range of colors that the display can produce, usually measured by a standard such as sRGB or Adobe RGB. Contrast ratio is the ratio of the brightest white to the darkest black that the display can show, usually expressed as a number or a logarithm. Brightness is the amount of light that the display emits, usually measured in candelas per square meter (cd/m2) or nits. Viewing angle is the angle at which the display can be viewed without losing color or contrast, usually measured in degrees from the center of the screen.
- Graphic displays are essential for computer graphics, as they enable the visualization and interaction of graphical data. They can also enhance the user experience and the aesthetic appeal of the graphical output. However, they also pose some challenges and limitations, such as compatibility, cost, power consumption, and environmental impact. Therefore, choosing the right graphic display for a specific purpose or application requires careful consideration and evaluation of the available options and trade-offs.



# Random Scan Displays

- Random scan displays are also known as **vector displays** or **stroke-writing displays** or **calligraphic displays**.
- Random scan displays use a **cathode ray tube (CRT)** to draw a picture on the screen in one line at a time .
- Random scan displays direct the electron beam only to those areas of the screen where a picture has to be drawn .
- Random scan displays can draw and refresh component lines of a picture in any specified sequence.
- Random scan displays produce smooth line drawings and have high resolution.
- Random scan displays are suitable for applications that require line drawings, such as engineering and computer-aided design (CAD).
- Random scan displays cannot display realistic shaded scenes or complex images.
- Random scan displays require more memory than raster scan displays, as they store the coordinates of the endpoints of each line.
- Pen plotter is an example of random scan displays.



# Raster scan displays

- Raster scan displays are the most common type of graphics monitor that use a cathode ray tube (CRT) to display images on a screen  .
- Raster scan displays are based on television technology, where an electron beam sweeps across the screen from top to bottom, covering one row of pixels at a time  .
- The electron beam turns on and off as it moves across each row, creating a pattern of illuminated spots or pixels on the screen .
- The resolution of a raster scan display depends on the number of pixels on the screen and the number of colors that each pixel can display .
- The refresh rate of a raster scan display is the number of times per second that the electron beam redraws the entire screen .
- A higher refresh rate reduces the flickering effect and improves the quality of the display .
- Raster scan displays are suitable for displaying realistic images, animations, and video games, but they have some limitations, such as:
  - They require a large amount of memory to store the pixel values for the entire screen .
  - They are not efficient for drawing geometric shapes, such as lines, circles, and polygons, as they require a lot of calculations to determine which pixels to turn on and off .
  - They are not able to display smooth curves or sharp edges, as the pixels are discrete and rectangular .



# Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display .
- It is a memory buffer containing data representing all the pixels in a complete video frame .
- The frame buffer is the size of the maximum image that can be displayed, and it may be a separate memory bank on the graphics card (display adapter), GPU or a reserved part of regular memory.
- A video controller or display controller is a device that passes the contents of the frame buffer to the monitor .
- It controls the operation of the display device and provides the interface between the frame buffer and the monitor.
- It may also perform additional functions such as generating the timing signals, providing a cursor, or performing basic graphics operations.



# Points and lines for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A point is the simplest graphical element that can be displayed on a screen. It is represented by a pair of coordinates (x, y) that specify its position on a two-dimensional plane.
- A line is a sequence of points that are connected by straight or curved segments. It is represented by two endpoints (x1, y1) and (x2, y2) that specify the start and end of the line, or by a slope-intercept equation y = mx + b that specifies the direction and position of the line.
- There are different algorithms for generating lines on a raster display, such as DDA (Digital Differential Analyzer), Bresenham's, and Xiaolin Wu's algorithms. These algorithms differ in their accuracy, efficiency, and smoothness of the lines they produce.
- DDA algorithm uses the equation of the line to incrementally calculate the x and y coordinates of each point along the line. It is simple but slow and prone to rounding errors.
- Bresenham's algorithm uses integer arithmetic and decision variables to determine the next point along the line. It is faster and more accurate than DDA, but it can only handle lines with slopes between -1 and 1.
- Xiaolin Wu's algorithm uses anti-aliasing techniques to smooth the edges of the lines by varying the intensity of the pixels along the line. It is more complex and slower than Bresenham's, but it can handle lines with any slope and produce high-quality results.



# Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Line drawing algorithms are methods for approximating a line segment on discrete graphical media, such as pixel-based displays and printers.
- Line drawing algorithms are important for computer graphics because they are used to render basic shapes, such as polygons, curves, and fonts.
- Line drawing algorithms need to be efficient, accurate, and smooth, meaning they should minimize the number of pixels used, avoid gaps and jagged edges, and produce a visually pleasing result.
- There are different types of line drawing algorithms, each with its own advantages and disadvantages. Some of the most common ones are:

  - **Naive algorithm**: This algorithm simply rounds the x and y coordinates of each point on the line to the nearest integer and plots the corresponding pixel. This algorithm is simple and easy to implement, but it can produce gaps and uneven spacing between pixels, especially for steep lines.
  - **Digital Differential Analyzer (DDA) algorithm**: This algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each point on the line and rounds them to the nearest integer. This algorithm is more accurate and smooth than the naive algorithm, but it can be slow and inefficient, especially for large slopes, because it involves floating-point arithmetic and rounding operations.
  - **Bresenham's algorithm**: This algorithm uses integer arithmetic and error terms to incrementally determine which pixel to plot for each x or y coordinate, depending on the slope of the line. This algorithm is faster and more efficient than the DDA algorithm, because it avoids floating-point operations and minimizes the number of pixels used. However, it can be more complex to implement and understand, and it can produce jagged edges for some lines.
  - **Mid-point algorithm**: This algorithm uses a decision variable to determine whether to plot the pixel above or below the mid-point of the line segment between two consecutive x or y coordinates, depending on the slope of the line. This algorithm is similar to Bresenham's algorithm, but it can be more accurate and smooth, because it avoids rounding errors and produces fewer jagged edges. However, it can also be more complex to implement and understand, and it can still produce gaps for some lines.

- The choice of the best line drawing algorithm depends on the application, the hardware, and the desired trade-off between speed, accuracy, and smoothness. Some applications may require more than one algorithm to achieve the best results. For example, anti-aliasing techniques can be used to reduce the jaggedness and improve the appearance of lines drawn by any algorithm.



# Circle generating algorithms

A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm. A circle generation algorithm is an algorithm used to create a circle on a computer screen. It is used in various applications such as computer-aided design (CAD) software, animation software, games, and scientific visualization.

There are several algorithms used for generating circles on a computer screen, such as:

- Bresenham's algorithm
- Midpoint circle algorithm
- Trigonometric method
- Polar coordinates method

## Bresenham's algorithm

Bresenham's algorithm is an efficient and simple algorithm for drawing a circle. It is based on the idea of using only integer arithmetic and exploiting the symmetry of the circle. The algorithm works as follows:

- Given the center (xc, yc) and radius r of the circle, initialize an error variable e = 3 - 2r and a point (x, y) = (0, r).
- Plot the initial point (xc + x, yc + y) and its symmetric points in the other seven octants of the circle.
- Repeat the following steps until x <= y:
  - If e < 0, then increment x by 1 and update e as e = e + 4x + 6.
  - If e >= 0, then increment x by 1, decrement y by 1 and update e as e = e + 4(x - y) + 10.
  - Plot the new point (xc + x, yc + y) and its symmetric points in the other seven octants of the circle.

The algorithm can be illustrated by the following pseudocode:

```
Input: center (xc, yc) and radius r of the circle
Output: a set of points on the circle

Initialize e = 3 - 2r and (x, y) = (0, r)
Plot (xc + x, yc + y) and its symmetric points
While x <= y
  If e < 0
    x = x + 1
    e = e + 4x + 6
  Else
    x = x + 1
    y = y - 1
    e = e + 4(x - y) + 10
  Plot (xc + x, yc + y) and its symmetric points
End while
```

The algorithm has a time complexity of O(r) and a space complexity of O(1).

## Midpoint circle algorithm

Midpoint circle algorithm is another efficient and simple algorithm for drawing a circle. It is based on the idea of using the midpoint of the line segment joining the current point and the next point on the circle as a decision parameter. The algorithm works as follows:

- Given the center (xc, yc) and radius r of the circle, initialize a point (x, y) = (0, r) and a decision parameter p = 1 - r.
- Plot the initial point (xc + x, yc + y) and its symmetric points in the other seven octants of the circle.
- Repeat the following steps until x <= y:
  - If p < 0, then increment x by 1 and update p as p = p + 2x + 3.
  - If p >= 0, then increment x by 1, decrement y by 1 and update p as p = p + 2(x - y) + 5.
  - Plot the new point (xc + x, yc + y) and its symmetric points in the other seven octants of the circle.

The algorithm can be illustrated by the following pseudocode:

```
Input: center (xc, yc) and radius r of the circle
Output: a set of points on the circle

Initialize (x, y) = (0, r) and p = 1 - r
Plot (xc + x, yc + y) and its symmetric points
While x <= y
  If p < 0
    x = x + 1
    p = p + 2x + 3
  Else
    x = x + 1
    y = y - 1
    p = p + 2(x - y) + 5
  Plot (xc + x, yc + y) and its symmetric points
End while
```

The algorithm has a time complexity of O(r) and a space complexity of O(1).

## Trigonometric method

Trigonometric method is a simple but less efficient algorithm for



# Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle. It is based on the following idea:

- A circle is symmetric about its center, so we only need to calculate the points in one octant (e.g., the first octant where x >= 0 and y >= 0) and then reflect them to the other octants.
- A circle with radius r and center (0, 0) has the equation x^2 + y^2 = r^2. We can use this equation to check whether a point (x, y) is on the circle, inside the circle, or outside the circle.
- We start from the point (0, r) and move along the circle in a counter-clockwise direction. At each step, we have two possible choices for the next point: (x + 1, y) or (x + 1, y - 1). We choose the one that is closer to the circle.
- We can use a decision parameter p to determine which point to choose. Initially, p = 1 - r. If p < 0, then the point (x + 1, y) is closer to the circle, so we choose it and update p as p = p + 2x + 3. If p >= 0, then the point (x + 1, y - 1) is closer to the circle, so we choose it and update p as p = p + 2x - 2y + 5.
- We repeat this process until x >= y, which means we have reached the end of the first octant.

The algorithm can be summarized as follows:

- Input: radius r of the circle
- Output: the points on the circle in the first octant
- Algorithm:
  - Set x = 0 and y = r
  - Set p = 1 - r
  - While x < y
    - Plot the point (x, y) and its reflections in the other octants
    - If p < 0
      - Set x = x + 1
      - Set p = p + 2x + 3
    - Else
      - Set x = x + 1 and y = y - 1
      - Set p = p + 2x - 2y + 5
  - If x == y
    - Plot the point (x, y) and its reflections in the other octants

The following figure shows an example of the algorithm for r = 5:

midpoint circle algorithm example

Source:



# Parallel Algorithms for Line Generation in Computer Graphics

- Line generation is a fundamental task in computer graphics, as it is used to draw curves, polygons, and other shapes.
- A line can be represented by a linear equation of the form `y = mx + b`, where `m` is the slope and `b` is the intercept.
- A line can also be represented by a parametric equation of the form `x = x0 + t * dx` and `y = y0 + t * dy`, where `(x0, y0)` is a point on the line, `dx` and `dy` are the increments along the `x` and `y` axes, and `t` is a parameter that varies from 0 to 1.
- A line can be approximated by a sequence of discrete points on a square grid, such that the distance between the points and the line is minimized. This is called rasterization or scan conversion.
- There are several algorithms for rasterizing lines, such as DDA (Digital Differential Analyzer), Bresenham's algorithm, and Midpoint algorithm. These algorithms are sequential, meaning they generate one point at a time, starting from one endpoint and moving towards the other endpoint.
- Parallel algorithms for line generation aim to generate multiple points at the same time, using multiple processors or cores. This can improve the performance and efficiency of line drawing, especially for large or complex scenes.
- There are different ways to parallelize line generation algorithms, such as:

  - Divide the line into segments and assign each segment to a processor. Each processor can use a sequential algorithm to rasterize its segment. This is called data parallelism or domain decomposition.  
  - Divide the grid into tiles and assign each tile to a processor. Each processor can use a sequential algorithm to rasterize the line within its tile. This is called spatial parallelism or image decomposition. 
  - Use a parallel prefix sum algorithm to compute the coordinates of the points on the line. This is based on the observation that the coordinates of the points on the line are the cumulative sums of the increments `dx` and `dy`. This is called algorithmic parallelism or functional decomposition. 
  - Use a parallel edge function algorithm to determine whether a pixel is inside or outside the line. This is based on the observation that the line can be defined by a linear function that has a positive value on one side of the line and a negative value on the other side. The value of the function can be interpolated and computed in parallel for adjacent pixels. This is also called algorithmic parallelism or functional decomposition. 

- The advantages of parallel algorithms for line generation are:

  - They can reduce the execution time and increase the throughput of line drawing.
  - They can exploit the parallelism and concurrency of modern hardware architectures, such as GPUs, multicore CPUs, and distributed systems.
  - They can handle large or complex scenes that may require high resolution or accuracy.

- The challenges of parallel algorithms for line generation are:

  - They may introduce synchronization and communication overheads among the processors, which can affect the performance and scalability of the algorithms.
  - They may require more memory or storage space to store the intermediate or final results of the algorithms.
  - They may introduce artifacts or errors in the rasterization, such as gaps, overlaps, or aliasing, due to the discretization or approximation of the line.



## Unit 2 - Transformations

A transformation is a change in the position, size, or shape of a figure. There are four basic types of transformations: translations, rotations, reflections, and dilations.

- A translation is a transformation that moves every point of a figure the same distance and in the same direction. The figure does not change its size or orientation. A translation can be described by a vector, which has a magnitude (length) and a direction. A vector can be represented by an arrow or by a pair of numbers (x, y) that indicate how much the figure moves horizontally and vertically.

- A rotation is a transformation that turns a figure around a fixed point called the center of rotation. The figure does not change its size or shape, but it may change its orientation. A rotation can be described by an angle of rotation, which measures how much the figure rotates clockwise or counterclockwise. A positive angle means a clockwise rotation, and a negative angle means a counterclockwise rotation. A rotation can also be described by a point and a direction, such as "90 degrees about the origin" or "180 degrees around point P".

- A reflection is a transformation that flips a figure over a line called the line of reflection. The figure does not change its size or shape, but it may change its orientation. A reflection can be described by the equation of the line of reflection, such as "y = x" or "x = -2". A reflection can also be described by a direction, such as "across the x-axis" or "over the y-axis".

- A dilation is a transformation that enlarges or reduces a figure by a scale factor. The figure changes its size, but not its shape or orientation. A dilation can be described by a scale factor, which is a positive number that indicates how much the figure grows or shrinks. A scale factor greater than 1 means an enlargement, and a scale factor less than 1 means a reduction. A dilation can also be described by a center of dilation, which is a point that does not move during the transformation. The center of dilation can be any point, but it is often the origin or a vertex of the figure.

Some properties of transformations are:

- A transformation maps a figure to its image. The original figure is called the pre-image, and the resulting figure is called the image. The notation for a transformation is T(pre-image) = image, where T is the name of the transformation.

- A transformation is rigid if it preserves the distance and angle measures of the figure. Translations, rotations, and reflections are rigid transformations. A rigid transformation is also called an isometry.

- A transformation is non-rigid if it changes the distance or angle measures of the figure. Dilations are non-rigid transformations. A non-rigid transformation is also called a similarity.

- A transformation is congruent if it preserves the shape and size of the figure. Translations, rotations, and reflections are congruent transformations. Two figures are congruent if there is a congruent transformation that maps one figure to the other.

- A transformation is similar if it preserves the shape but not the size of the figure. Dilations are similar transformations. Two figures are similar if there is a similar transformation that maps one figure to the other.

- A transformation is equivalent if it produces the same image as another transformation. For example, a translation followed by a rotation is equivalent to a single rotation. Two transformations are equivalent if they have the same effect on any figure.

- A transformation is inverse if it undoes another transformation. For example, a translation by (x, y) is inverse to a translation by (-x, -y). Two transformations are inverse if they cancel each other out.

- A transformation is composed if it is the result of applying two or more transformations in sequence. For example, a reflection followed by a dilation is a composition of transformations. The notation for a composition is T1(T2(pre-image)), where T1 and T2 are the names of the transformations. The order of the transformations matters, as different orders may produce different images.

Some examples of transformations are:

- A translation by (3, -2) moves a figure 3 units to the right and 2 units down.

- A rotation of 90 degrees about the origin turns a figure 90 degrees clockwise around the origin.

- A reflection over the line y = x flips a figure over the line y = x.

- A dilation by a scale factor of 2 with the origin as the center of dilation doubles the size of a figure.

- A composition of a reflection over the x-axis and a translation by (1, 4) flips a figure over the x-axis and then moves it 1 unit to the right and



# Basic Transformation for the Notes of the Unit 2 - Transformations in the Subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- Transformations are useful for repositioning and resizing graphics on the screen, as well as for creating animations and effects.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another by adding a constant vector to its coordinates.
- Rotation is the change of orientation of an object around a fixed point or axis by a certain angle.
- Scaling is the change of size of an object by multiplying its coordinates by a constant factor.
- Transformations can be represented by matrices that can be multiplied with the coordinates of the object to obtain the transformed coordinates.
- The matrix for translation is:

| 1 0 tx |
| 0 1 ty |
| 0 0 1  |

where tx and ty are the translation factors along the x and y axes.

- The matrix for rotation is:

| cosθ -sinθ 0 |
| sinθ cosθ 0 |
| 0 0 1 |

where θ is the angle of rotation in the counterclockwise direction.

- The matrix for scaling is:

| sx 0 0 |
| 0 sy 0 |
| 0 0 1 |

where sx and sy are the scaling factors along the x and y axes.

- Transformations can be combined by multiplying the matrices in the order of the desired operations.
- For example, to translate an object by (tx, ty) and then rotate it by θ, the matrix is:

| cosθ -sinθ tx |
| sinθ cosθ ty |
| 0 0 1 |

- Transformations can also be applied to vectors, such as the direction and magnitude of a force or a velocity.
- Transformations can be implemented in computer graphics using various libraries and frameworks, such as OpenGL, which provides functions for translation, rotation, and scaling.



# Matrix representations and homogenous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling and perspective projection in computer graphics .
- Homogenous coordinates are a way to represent points and vectors in a higher-dimensional space using an extra coordinate, usually denoted by w.
- Homogenous coordinates allow all geometric transformation equations to be represented as matrix multiplication, which simplifies the computation and the combination of multiple transformations .
- Homogenous coordinates also enable the representation of points at infinity, which are useful for perspective projection and parallel lines.
- To convert a point (x, y) in Cartesian coordinates to a point (x, y, w) in homogenous coordinates, we can use any value of w except zero, and divide the coordinates by w to get the original point. For example, (2, 3) can be represented as (4, 6, 2) or (6, 9, 3) in homogenous coordinates .
- To convert a point (x, y, w) in homogenous coordinates to a point (x, y) in Cartesian coordinates, we divide the coordinates by w, as long as w is not zero. For example, (4, 6, 2) can be converted to (2, 3) by dividing by 2 .
- To represent a vector (x, y) in homogenous coordinates, we use w = 0, which indicates that the vector does not have a position. For example, (2, 3) can be represented as (2, 3, 0) in homogenous coordinates .
- To represent a matrix transformation in homogenous coordinates, we use a square matrix of size one greater than the dimension of the space. For example, a 2D transformation can be represented by a 3x3 matrix, and a 3D transformation can be represented by a 4x4 matrix .
- The matrix representation for translation in homogenous coordinates is:

translation matrix

where tx and ty are the translation distances along the x and y axes, respectively .

- The matrix representation for rotation in homogenous coordinates is:

rotation matrix

where θ is the angle of rotation in the counterclockwise direction .

- The matrix representation for scaling in homogenous coordinates is:

scaling matrix

where sx and sy are the scaling factors along the x and y axes, respectively .

- The matrix representation for perspective projection in homogenous coordinates is:

perspective projection matrix

where f is the focal length of the camera, and n and f are the near and far clipping planes, respectively .

- To apply a matrix transformation to a point or a vector in homogenous coordinates, we multiply the matrix by the column vector of the coordinates. For example, to translate the point (2, 3) by (4, 5), we multiply the translation matrix by the column vector of the point:

matrix multiplication example

which gives the result (6, 8, 1), which can be converted to (6, 8) in Cartesian coordinates .

- To combine multiple matrix transformations, we multiply the matrices in the reverse order of the transformations. For example, to first translate the point (2, 3) by (4, 5) and then rotate it by 90 degrees, we multiply the rotation matrix by the translation matrix and then by the column vector of the point:

matrix combination example

which gives the result (-8, 6, 1), which can be converted to (-8, 6) in Cartesian coordinates [^3



# Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A composite transformation is a combination of two or more transformations into a single one that is equivalent to the transformations that are performed one after another over a 2D or 3D object  .
- The process of combining the transformations is called concatenation, and the resulting matrix is called the composite matrix.
- The order of the transformations matters, as different orders may produce different results. Some transformations are commutative, meaning that the order does not affect the outcome, while others are non-commutative, meaning that the order does affect the outcome.
- For example, translation and scaling are commutative, as translating and then scaling an object is the same as scaling and then translating it. However, rotation and scaling are non-commutative, as rotating and then scaling an object is not the same as scaling and then rotating it.
- To perform a composite transformation, we need to multiply the matrices of the individual transformations in the reverse order of the desired sequence. For example, if we want to translate an object by (tx, ty) and then rotate it by an angle θ, we need to multiply the rotation matrix by the translation matrix, and then multiply the result by the object's coordinates.
- The general formula for a composite transformation matrix is:

  M = Mn * Mn-1 * ... * M2 * M1

  where M is the composite matrix, Mn is the last transformation matrix, and M1 is the first transformation matrix.
- Some common composite transformations are:

  - Rotation about an arbitrary point: This can be achieved by translating the object to the origin, rotating it by the desired angle, and then translating it back to the original position  .
  - Scaling about an arbitrary point: This can be achieved by translating the object to the origin, scaling it by the desired factors, and then translating it back to the original position  .
  - Reflection about an arbitrary line: This can be achieved by translating the object to the origin, rotating it to align the line with the x-axis, reflecting it about the x-axis, and then reversing the previous steps  .
  - Shearing about an arbitrary line: This can be achieved by translating the object to the origin, rotating it to align the line with the x-axis, shearing it along the x-axis, and then reversing the previous steps  .

- Composite transformations are useful for creating complex effects and animations in computer graphics, such as scaling and rotating a scene, or transforming a character's pose.



# Reflections and Shearing

## Reflection

- Reflection is a type of transformation in computer graphics that produces a mirror image of an object.
- Reflection can be performed in any direction, such as horizontal, vertical, diagonal, or along an arbitrary axis.
- Reflection is equivalent to a rotation of 180 degrees about the line of reflection, which acts as a mirror.
- To perform reflection, we need to find the coordinates of the reflected point with respect to the line of reflection.
- The general formula for reflection is:

  - If the line of reflection is y = mx + c, then the reflected point (x', y') of a point (x, y) is given by:

    - x' = (x + 2my - 2c) / (1 + m^2)
    - y' = (y + 2mx + 2c) / (1 + m^2)

  - If the line of reflection is x = k, then the reflected point (x', y') of a point (x, y) is given by:

    - x' = 2k - x
    - y' = y

  - If the line of reflection is y = k, then the reflected point (x', y') of a point (x, y) is given by:

    - x' = x
    - y' = 2k - y

- An example of reflection is shown below:

  - The original object is a triangle with vertices A(1, 1), B(3, 4), and C(5, 2).
  - The line of reflection is y = x.
  - The reflected object is a triangle with vertices A'(1, 1), B'(4, 3), and C'(2, 5).

```
  y
  ^
  |   B'  C'
  |  / \ /
  | /   X
  |/   / \
  +---------> x
 /|   /   \
/ |  /     \
   A'      A B
           \ |
            \|
             C
```

## Shearing

- Shearing is a type of transformation in computer graphics that changes the shape of an object by sliding its layers in one or more directions.
- Shearing can be performed in any direction, such as horizontal, vertical, or along an arbitrary axis.
- Shearing does not change the area or volume of the object, but it may change its orientation and aspect ratio.
- To perform shearing, we need to find the coordinates of the sheared point with respect to the shearing factor and the direction of shearing.
- The general formula for shearing is:

  - If the shearing is in the x-direction, then the sheared point (x', y') of a point (x, y) is given by:

    - x' = x + shx * y
    - y' = y

    - where shx is the shearing factor in the x-direction.

  - If the shearing is in the y-direction, then the sheared point (x', y') of a point (x, y) is given by:

    - x' = x
    - y' = y + shy * x

    - where shy is the shearing factor in the y-direction.

- An example of shearing is shown below:

  - The original object is a rectangle with vertices A(1, 1), B(5, 1), C(5, 3), and D(1, 3).
  - The shearing is in the x-direction with a shearing factor of 0.5.
  - The sheared object is a parallelogram with vertices A'(1, 1), B'(7.5, 1), C'(7.5, 3), and D'(3, 3).

```
  y
  ^
  |   C'  B'
  |   |\ /|
  |   | X |
  |   |/ \|
  +---------> x
  |   /   \
  |  /     \
  | /       \
  D'        A' B
  |         | |
  |         | |
  D         A C
```



# Windowing and Clipping

Windowing and clipping are two techniques used in computer graphics to display a part of a scene or an object on the screen.

## Windowing

- Windowing is the process of selecting and viewing the picture with different views .
- A window is an area on the screen that defines the region of interest or the portion of the scene that is visible .
- A window can be rectangular or arbitrary in shape.
- A window can be moved, resized, or rotated to change the view of the scene.
- Windowing is useful for zooming in or out, panning, or focusing on a specific part of the scene.

## Clipping

- Clipping is the process of dividing each element of the picture into its visible and invisible portions, allowing the invisible portion to be discarded .
- Clipping is necessary to remove objects, lines, or line segments that are outside the window or the viewing volume .
- Clipping can be done in two dimensions or three dimensions .
- Clipping can be done using various algorithms, such as Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman, etc .
- Clipping is useful for saving memory, improving performance, and avoiding rendering artifacts .

## Window and Viewport

- A window and a viewport are two related concepts in computer graphics .
- A window is a region of interest in the world coordinate system, which defines what part of the scene is visible .
- A viewport is a region on the device coordinate system, which defines where and how the window is displayed on the screen .
- A window and a viewport can have different shapes and sizes, but they are usually rectangular.
- A window and a viewport can be related by a transformation that maps the coordinates of the window to the coordinates of the viewport.
- A window and a viewport can be used to achieve various effects, such as scaling, translation, rotation, or perspective.



# Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert the geometry data of a scene into the image data that can be displayed on a device .
- The viewing pipeline consists of the following stages:
  - Object coordinates: The coordinates of the vertices and primitives that define the objects in the scene.
  - World coordinates: The coordinates of the objects after applying the modeling transformation, which positions and orientates them in the 3D space.
  - Viewing coordinates: The coordinates of the objects after applying the viewing transformation, which defines the position and orientation of the camera or the eye.
  - Projection coordinates: The coordinates of the objects after applying the projection transformation, which maps the 3D scene onto a 2D plane.
  - Normalized device coordinates: The coordinates of the objects after applying the normalization transformation, which scales and translates the projected scene to fit into a unit cube.
  - Device coordinates: The coordinates of the objects after applying the viewport transformation, which maps the normalized device coordinates to the actual device coordinates, such as pixels on a screen.
- The following diagram illustrates the viewing pipeline for 3D graphics:

Viewing pipeline diagram

- The following diagram illustrates the viewing pipeline for 2D graphics :

Viewing pipeline diagram

- The viewing pipeline allows the computer graphics system to display complex scenes with different objects, perspectives, and projections on various devices.
- The viewing pipeline also enables the manipulation of the scene by changing the parameters of the transformations, such as the position and orientation of the camera, the type and parameters of the projection, and the size and location of the viewport.



# Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the processes of mapping coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are necessary to remove objects, lines, or line segments that are outside the viewing pane or behind the viewer, and to adjust the size and position of the picture on the screen.
- Viewing transformations consist of two steps: projection and window-to-viewport mapping .
- Projection is the process of transforming 3D world coordinates into 2D eye coordinates, which are relative to the viewer's position and orientation.
- Projection can be either parallel or perspective, depending on whether the lines of projection are parallel or converge at a single point.
- Window-to-viewport mapping is the process of transforming 2D eye coordinates into 2D device coordinates, which are relative to the display device's resolution and origin.
- Window-to-viewport mapping involves defining a window, which is a rectangular region of interest in the eye coordinate system, and a viewport, which is a rectangular region of the display device where the window is mapped to.
- Window-to-viewport mapping can be done by applying scaling, translation, and clipping operations to the eye coordinates to fit them into the viewport.



# 2-D Clipping Algorithms

- Clipping is the process of removing or hiding the parts of graphics primitives that lie outside a specified region of interest, such as the viewport or the window.
- Clipping is necessary to avoid rendering unnecessary or invisible pixels, to improve the performance and the quality of the graphics output.
- Clipping can be applied to various graphics primitives, such as points, lines, polygons and curves.
- Clipping algorithms are methods to determine which parts of the primitives are inside or outside the clipping region, and how to modify them accordingly.
- There are different types of clipping regions, such as rectangular, circular, polygonal, convex or concave. Each type may require a different clipping algorithm.
- Some of the common 2-D clipping algorithms are:

  - Point clipping: This algorithm checks whether a given point lies inside or outside the clipping region, and discards it if it is outside. This is the simplest form of clipping, and can be done by comparing the coordinates of the point with the boundaries of the clipping region.
  - Line clipping: This algorithm clips a given line segment by finding the intersections of the line with the boundaries of the clipping region, and discarding the parts that are outside. There are several line clipping algorithms, such as Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, Nicholl-Lee-Nicholl, etc. Each algorithm has its own advantages and disadvantages in terms of efficiency, accuracy and complexity   .
  - Polygon clipping: This algorithm clips a given polygon by finding the intersections of the polygon edges with the boundaries of the clipping region, and creating new vertices and edges to form a clipped polygon. There are several polygon clipping algorithms, such as Sutherland-Hodgman, Weiler-Atherton, Greiner-Hormann, etc. Each algorithm has its own advantages and disadvantages in terms of efficiency, accuracy and complexity.
  - Curve clipping: This algorithm clips a given curve by finding the intersections of the curve with the boundaries of the clipping region, and discarding the parts that are outside. There are several curve clipping algorithms, such as Bezier clipping, B-spline clipping, etc. Each algorithm has its own advantages and disadvantages in terms of efficiency, accuracy and complexity.



# Line clipping algorithms

Line clipping algorithms are used to remove parts of lines that lie outside a specified region of interest, such as a viewport or a view volume. This is done to improve the efficiency and quality of rendering by avoiding unnecessary calculations and pixels. Line clipping algorithms typically work by testing the endpoints of each line segment against the boundaries of the clipping region, and then either discarding, accepting, or clipping the segment accordingly.

There are many line clipping algorithms, but two of the most common ones are:

- **Cohen–Sutherland algorithm**: This algorithm divides the 2D space into 9 regions, of which only the middle one is the visible viewport. Each region is assigned a 4-bit code, based on whether the point is above, below, left, or right of the viewport. The algorithm then compares the codes of the endpoints of each line segment, and applies one of the following rules:

  - If both codes are 0000, the segment is completely inside the viewport and is accepted.
  - If the bitwise AND of the codes is not 0000, the segment is completely outside the viewport and is rejected.
  - If neither of the above cases apply, the segment is partially inside the viewport and is clipped. The algorithm finds the intersection point of the segment with one of the viewport boundaries, and replaces the endpoint with the outside code with the intersection point. The new segment is then tested again with the same rules.

- **Liang–Barsky algorithm**: This algorithm is based on the parametric equation of a line segment, and uses four inequalities to test whether the segment is inside or outside the viewport. The algorithm then finds the minimum and maximum values of the parameter t that satisfy the inequalities, and uses them to clip the segment. The algorithm is more efficient than the Cohen–Sutherland algorithm, as it requires fewer calculations and comparisons.

Here is a pseudocode for the Liang–Barsky algorithm:

```
Input: x1, y1, x2, y2 // the endpoints of the line segment
       xmin, ymin, xmax, ymax // the boundaries of the viewport
Output: x1c, y1c, x2c, y2c // the clipped endpoints of the line segment, or null if rejected

// calculate the differences and the direction parameters
dx = x2 - x1
dy = y2 - y1
p = [-dx, dx, -dy, dy]
q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

// initialize the minimum and maximum values of t
tmin = 0
tmax = 1

// loop through the four boundaries
for i = 0 to 3
  // if the line is parallel to the boundary
  if p[i] == 0
    // if the line is outside the boundary, reject it
    if q[i] < 0
      return null
  // if the line is not parallel to the boundary
  else
    // calculate the intersection parameter
    t = q[i] / p[i]
    // if the line is entering the boundary
    if p[i] < 0
      // update the minimum value of t
      tmin = max(tmin, t)
    // if the line is leaving the boundary
    else
      // update the maximum value of t
      tmax = min(tmax, t)
    // if the line is outside the boundary, reject it
    if tmin > tmax
      return null

// calculate the clipped endpoints using the minimum and maximum values of t
x1c = x1 + tmin * dx
y1c = y1 + tmin * dy
x2c = x1 + tmax * dx
y2c = y1 + tmax * dy

// return the clipped endpoints
return x1c, y1c, x2c, y2c
```



# Cohen Sutherland line clipping algorithm

- Cohen Sutherland algorithm is a line clipping algorithm that cuts lines to portions which are within a rectangular area.
- Line clipping is the process of removing lines or portions of lines outside an area of interest.
- The area of interest is also called the clipping window or the viewport .
- The algorithm divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport)  .
- The algorithm can be outlined as follows:
  - Nine regions are created, eight "outside" regions and one "inside" region.
  - Each region is assigned a 4-bit code, called the outcode, based on its position relative to the clipping window.
  - The outcode is computed by testing the endpoints of the line against the four boundaries of the clipping window.
  - The outcode is 0000 for the inside region, and has a 1-bit for each boundary that the region is outside of. For example, the outcode for the top-left region is 1001, meaning it is outside the top and left boundaries.
  - If both endpoints of the line have the same outcode, the line is trivially rejected, meaning it is entirely outside the clipping window.
  - If both endpoints of the line have the outcode 0000, the line is trivially accepted, meaning it is entirely inside the clipping window.
  - If the endpoints of the line have different outcodes, the line may be partially inside the clipping window, and needs to be clipped.
  - To clip the line, the algorithm finds an intersection point between the line and one of the boundaries of the clipping window, using the parametric equation of the line.
  - The intersection point replaces the endpoint that is outside the clipping window, and the outcode is recalculated for the new endpoint.
  - The algorithm repeats until the line is either trivially accepted or trivially rejected.
- Cohen Sutherland algorithm works only for rectangular clip window which means if the area of interest has any other shape than a rectangle, it will not work.
- For area of interest with other shapes, we need to use other algorithms like Cyrus Beck algorithm and Sutherland Hodgman algorithm.
- Cohen Sutherland algorithm is efficient because it quickly eliminates the lines that are outside the clipping window, and reduces the number of intersection calculations .
- Cohen Sutherland algorithm is also easy to implement and understand.



# Liang Barsky Algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the faster parametric line-clipping algorithm.
- The algorithm uses the parametric equation of a line and inequalities describing the range of the clipping window to find the intersections between the line and the window  .
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

    where `(xmin, ymin)` and `(xmax, ymax)` are the coordinates of the lower-left and upper-right corners of the window respectively.
- The algorithm works by finding the values of `u` that satisfy the inequalities for each edge of the window and then taking the maximum of the lower values and the minimum of the upper values as the final values of `u` that define the visible portion of the line .
- The algorithm can be summarized as follows:

    1. Initialize the lower and upper values of `u` as `u1 = 0` and `u2 = 1`.
    2. For each edge of the window, calculate the values of `p` and `q` as:

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
        - If `p < 0`, then the line is entering the window through the edge, so calculate `r = q / p` and update `u1 = max(u1, r)`.
        - If `p > 0`, then the line is leaving the window through the edge, so calculate `r = q / p` and update `u2 = min(u2, r)`.
        - If `p = 0` and `q >= 0`, then the line is parallel to and inside the edge, so do nothing.

    4. After checking all the edges, check the final values of `u1` and `u2`:

        - If `u1 > u2`, then the line is outside the window, so reject the line and exit the algorithm.
        - If `u1 <= u2`, then the line is partially or completely inside the window, so accept the line and calculate the visible end points as:

            ```
            x'1 = x1 + u1 * (x2 - x1)
            y'1 = y1 + u1 * (y2 - y1)
            x'2 = x1 + u2 * (x2 - x1)
            y'2 = y1 + u2 * (y2 - y1)
            ```

- The following diagram illustrates an example of the Liang Barsky algorithm:

    ```
    +-----------------+ ymax
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    +-----------------+ ymin
    xmin             xmax
    ``

```




# Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a rectangular window or a convex polygon.
- Line clipping algorithms are useful for computer graphics applications, such as rendering, clipping, and visibility testing.
- There are different line clipping algorithms for different types of regions. For rectangular regions, the Cohen-Sutherland algorithm is a popular and efficient method that uses a region code to classify the endpoints of a line and determine whether it is trivially accepted, trivially rejected, or needs further clipping.
- For non-rectangular regions, such as convex polygons, the Cyrus-Beck algorithm is a generalization of the Cohen-Sutherland algorithm that uses a parametric equation of a line and the normal vectors of the polygon edges to find the intersection points and clip the line .
- The Cyrus-Beck algorithm works as follows:
  - Input: A convex polygon defined by a set of coordinates given in a clockwise fashion, and a line segment defined by two endpoints.
  - Output: The clipped line segment, or none if the line is completely outside the polygon.
  - Algorithm:
    - Initialize the parameter t of the line segment as t0 = 0 and t1 = 1.
    - For each edge of the polygon, do the following:
      - Compute the dot product of the normal vector of the edge and the direction vector of the line segment.
      - If the dot product is zero, the line is parallel to the edge and does not intersect it.
      - If the dot product is negative, the line enters the polygon through the edge.
      - If the dot product is positive, the line exits the polygon through the edge.
      - Compute the intersection point of the line and the edge using the parametric equation of the line.
      - Compute the parameter value of the intersection point using the parametric equation of the line.
      - If the dot product is negative, update t0 as the maximum of t0 and the parameter value.
      - If the dot product is positive, update t1 as the minimum of t1 and the parameter value.
    - If t0 > t1, the line is completely outside the polygon and no clipping is done.
    - If t0 <= t1, the line is partially or completely inside the polygon and the clipped line segment is given by the points corresponding to t0 and t1 using the parametric equation of the line.
- The Cyrus-Beck algorithm allows line clipping for non-rectangular windows, unlike Cohen-Sutherland or Nicholl Lee Nicholl. It also removes the repeated clipping needed in Cohen-Sutherland.
- The Cyrus-Beck algorithm is illustrated in the following figure:

Cyrus-Beck algorithm example

- The Cyrus-Beck algorithm can be extended to clip lines against non-convex polygons by using a convex decomposition of the polygon and applying the algorithm to each convex sub-polygon.



# Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - To prevent undesirable effects when displaying polygons on the output device.
  - To render 3D images through hidden surface removal.
  - To produce high-quality surface details using techniques such as beam tracing.
  - To distribute the objects of a scene to appropriate processors in multiprocessor raytracing systems to improve rendering speeds.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against a convex clipping window by processing each edge of the polygon against each edge of the window in a clockwise order .
  - Weiler-Atherton algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersection points of the polygon and the window edges and then tracing the clipped polygon boundaries.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against a convex or concave clipping window by using a doubly-connected edge list data structure and a boolean operation to determine the clipped polygon boundaries.
- Polygon clipping can be illustrated by the following example:

Polygon clipping example

In this example, the blue polygon is clipped against the red clipping window using the Sutherland-Hodgman algorithm. The resulting clipped polygon is shown in green.



# Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon, and processes them against each edge of the clip polygon in a clockwise order .
- For each edge of the clip polygon, the algorithm generates a new list of vertices by examining each pair of consecutive vertices in the input list and applying one of the following rules :
  - If both vertices are inside the clip edge, output the second vertex.
  - If the first vertex is outside and the second vertex is inside, output the intersection point of the edge and the clip boundary, followed by the second vertex.
  - If the first vertex is inside and the second vertex is outside, output the intersection point of the edge and the clip boundary.
  - If both vertices are outside, output nothing.
- The output list of vertices becomes the input list for the next clip edge, until all edges are processed .
- The final output list contains the vertices of the clipped polygon .

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks



# Weiler and Atherton polygon clipping

- Weiler and Atherton polygon clipping is a polygon clipping algorithm that can handle concave polygons and polygons with holes.
- Polygon clipping is the process of cutting out a part of a polygon that lies outside a given clipping region, such as a window or a viewport.
- The algorithm works by finding the intersection points of the subject polygon and the clipping polygon, and labeling them as entry or exit points  .
- The algorithm then traverses the subject polygon in a clockwise direction, starting from any entry point, and adds the vertices to the output polygon until an exit point is reached  .
- The algorithm then switches to the clipping polygon and traverses it in a counter-clockwise direction, adding the vertices to the output polygon until an entry point is reached  .
- The algorithm repeats this process until all the entry and exit points are visited, and the output polygon is closed  .
- The algorithm can handle multiple output polygons if the subject polygon is split into disjoint parts by the clipping polygon  .
- The algorithm can also handle holes in the subject polygon by reversing the entry and exit labels for the vertices inside the hole  .
- The algorithm is more efficient than the Sutherland-Hodgman algorithm for concave polygons, but it requires more preprocessing to find and label the intersection points  .



# Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping .
- Curve clipping requires more processing than for objects with linear boundaries.
- The region of interest, also called the clip window, can be curved or rectangular in shape.
- There are different algorithms for curve clipping, such as the Bezier clipping algorithm, the B-spline clipping algorithm, and the convex hull clipping algorithm.
- The Bezier clipping algorithm uses the convex hull property of Bezier curves to clip them against a rectangular window.
- The B-spline clipping algorithm uses the convex hull property of B-splines to clip them against a rectangular window.
- The convex hull clipping algorithm uses the convex hull of a set of points to clip them against a convex polygonal window .
- Curve clipping can be used for various applications, such as text clipping, font rendering, vector graphics, and computer-aided design  .



# Text clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

Text clipping is a process of clipping the string. In this process, we clip the whole character or only some part of it depending on the requirement of the application. Text clipping is useful for removing the text that is outside the viewing window or overlapping the window boundary.

There are three methods for text clipping which are listed below  :

- **All or none string clipping method**: In this method, if the whole string is inside the clip window then we consider it. Otherwise, we discard the whole string even if some part of it is inside the window. This method is simple but may result in loss of information.

- **Text clipping method**: In this method, we keep the characters of the string that lie inside the clip window and remove all the characters that lie outside the clip window. If a character overlaps the window boundary then we keep that part of the character that lies inside the window and discard that part that lies outside the clip window. This method is more accurate but may result in distorted characters.

- **All or none character clipping method**: In this method, we keep the characters of the string that are completely inside the clip window and discard the characters that are partially or completely outside the clip window. This method is a compromise between the previous two methods. It preserves the shape of the characters but may result in incomplete strings.

Text clipping can be implemented using various techniques such as scan-line algorithm, polygon clipping algorithm, or character generation algorithm . The choice of the technique depends on the methods used to generate characters and the requirements of a particular application.



## Unit 3 - Three Dimensional

- In this unit, you will learn about the concepts and applications of three dimensional geometry.
- You will learn how to represent points, lines, planes, and solids in three dimensional space using Cartesian coordinates, vectors, and matrices.
- You will learn how to calculate distances, angles, areas, and volumes of various geometric shapes and figures in three dimensional space.
- You will learn how to perform transformations such as translation, rotation, reflection, and scaling on three dimensional objects using matrices and homogeneous coordinates.
- You will learn how to use cross product and dot product to find the direction and angle between two vectors, and the area of a parallelogram or a triangle formed by two vectors.
- You will learn how to use scalar triple product and vector triple product to find the volume of a parallelepiped or a tetrahedron formed by three vectors.
- You will learn how to find the equation of a line, a plane, a sphere, and a cylinder in three dimensional space, and how to determine the intersection, parallelism, and perpendicularity of these objects.
- You will learn how to use cylindrical and spherical coordinates to describe points and regions in three dimensional space, and how to convert between different coordinate systems.
- You will learn how to use parametric equations and vector functions to model curves and surfaces in three dimensional space, and how to find their derivatives and integrals.
- You will learn how to use partial derivatives and directional derivatives to find the rate of change of a function of two or more variables in a given direction, and how to use the gradient vector to find the direction and magnitude of the maximum rate of change.
- You will learn how to use the divergence and curl operators to measure the divergence and curl of a vector field, and how to use the divergence theorem and Stokes' theorem to relate the integrals of a vector field over a surface or a curve to the integrals over the boundary or the interior of the region.



# 3-D Geometric Primitives

- 3-D geometric primitives are basic geometric forms that can be used to model more complex 3-D shapes and objects  .
- They are also called 3-D primitives or simply primitives.
- They are usually defined by a set of parameters such as vertices, edges, faces, center, radius, height, etc.
- Some common 3-D primitives are:
  - Cube: A six-faced polyhedron with square faces and right angles .
  - Pyramid: A polyhedron with a polygonal base and triangular faces that meet at a common vertex .
  - Cone: A solid with a circular base and a curved surface that tapers to a point called the vertex .
  - Sphere: A solid with all points on its surface equidistant from a fixed point called the center .
  - Torus: A solid with a ring-shaped surface formed by rotating a circle around an axis that does not intersect the circle .
- 3-D primitives can have different levels of resolution, which affect the smoothness and detail of their appearance .
- 3-D primitives can be modified with transforms (such as translation, rotation, scaling, etc.) and Booleans (such as union, intersection, difference, etc.) to create more complex shapes  .
- 3-D primitives can also be used as the basis for sculpting, which is a technique of adding or removing details from a 3-D model using brushes and tools.
- In some cases, curves (such as Bézier curves, circles, etc.) may be considered 3-D primitives, while in other cases, they are complex forms created from many straight, primitive shapes.
- 3-D primitives are commonly used in applications such as computer graphics, computer-aided design, animation, gaming, etc.



# 3-D Object Representation

- 3-D object representation is the process of developing a mathematical coordinate-based representation of any surface of an object in three dimensions via specialized software .
- 3-D object representation is essential for computer graphics applications such as animation, rendering, simulation, and gaming.
- 3-D object representation can be divided into two main categories: boundary representations and space-partitioning representations.

## Boundary Representations (B-reps)

- Boundary representations describe a 3-D object as a set of surfaces that separates the object interior from the environment.
- Boundary representations are also known as surface models or polygonal models.
- Boundary representations can be further classified into three types: wireframe models, surface models, and solid models.

### Wireframe Models

- Wireframe models represent a 3-D object as a collection of vertices, edges, and curves.
- Wireframe models are the simplest and most abstract form of boundary representations.
- Wireframe models do not provide any information about the object's surface properties, such as color, texture, or shading.
- Wireframe models are useful for conceptual design and visualization, but not for realistic rendering or collision detection.

### Surface Models

- Surface models represent a 3-D object as a collection of polygons, patches, or splines.
- Surface models are more detailed and realistic than wireframe models, as they provide information about the object's surface properties, such as color, texture, and shading.
- Surface models can be rendered using various techniques, such as flat shading, Gouraud shading, or Phong shading.
- Surface models are useful for rendering and animation, but not for solid modeling or simulation.

### Solid Models

- Solid models represent a 3-D object as a collection of volumetric primitives, such as cubes, spheres, cylinders, or cones.
- Solid models are the most complex and realistic form of boundary representations, as they provide information about the object's interior properties, such as mass, density, or material.
- Solid models can be rendered using techniques such as ray tracing or radiosity.
- Solid models are useful for solid modeling, simulation, and collision detection, but not for fast rendering or animation.

## Space-Partitioning Representations

- Space-partitioning representations describe a 3-D object by dividing the space into regions and assigning properties to each region.
- Space-partitioning representations are also known as volumetric models or voxel models.
- Space-partitioning representations can be further classified into three types: regular grids, octrees, and constructive solid geometry (CSG) trees.

### Regular Grids

- Regular grids represent a 3-D object by dividing the space into a uniform grid of voxels (volume elements) and storing the properties of each voxel in an array.
- Regular grids are simple and efficient to store and access, but they may waste space and memory for sparse or complex objects.
- Regular grids are useful for medical imaging, terrain modeling, and voxel rendering.

### Octrees

- Octrees represent a 3-D object by dividing the space into a hierarchical tree of octants (cubic regions) and storing the properties of each octant in a node.
- Octrees are adaptive and compact, as they can vary the resolution and detail of the object according to the level of the tree.
- Octrees are useful for visibility culling, collision detection, and level-of-detail rendering.

### Constructive Solid Geometry (CSG) Trees

- CSG trees represent a 3-D object by combining a set of primitive solids using Boolean operations, such as union, intersection, or difference, and storing the result in a binary tree.
- CSG trees are expressive and powerful, as they can create complex and irregular shapes from simple and regular primitives.
- CSG trees are useful for solid modeling, simulation, and ray tracing, but not for fast rendering or animation.



# 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be used to change the position, size, orientation, shape, etc. of the object.
- 3-D transformation can be classified into two types: affine and non-affine.
  - Affine transformations preserve parallelism, distances, and angles between lines, but not necessarily lengths and areas.
  - Non-affine transformations do not preserve any of these properties.
- Some common 3-D transformations are:
  - Translation: moving the object along a given direction by a given distance.
  - Scaling: changing the size of the object by a given factor along each axis.
  - Rotation: rotating the object around a given axis by a given angle.
  - Shear: slanting the object along a given plane by a given factor.
  - Reflection: mirroring the object across a given plane.
  - Projection: mapping the object from a higher dimensional space to a lower dimensional space.
- 3-D transformation can be represented by a 4x4 matrix, where the last row is always (0, 0, 0, 1).
- 3-D transformation can be performed by multiplying the matrix with the homogeneous coordinates of the point (x, y, z, 1).
- 3-D transformation can be composed by multiplying the matrices of the individual transformations in the desired order.



# 3-D Viewing

3-D viewing is the process of displaying and interacting with 3-D computer graphics on a 2-D or 3-D display device. 3-D viewing involves the following steps:

- 3-D modeling: creating 3-D models of objects or scenes using 3-D modeling software or scanners. 3-D models are composed of geometric primitives such as points, lines, triangles, and polygons, and can have attributes such as color, texture, and material properties .
- 3-D transformation: applying mathematical operations such as translation, rotation, scaling, and shearing to 3-D models to change their position, orientation, size, and shape. 3-D transformation can be done in different coordinate systems, such as world, local, or viewing coordinates.
- 3-D viewing: defining the position and orientation of the observer (or camera) and the projection plane (or screen) in the viewing coordinate system. The viewing coordinate system is used to specify the perspective or orthographic projection of 3-D models onto the projection plane.
- 3-D rendering: generating 2-D images of 3-D models by applying algorithms such as rasterization, ray tracing, or radiosity to simulate the effects of light, shadow, reflection, refraction, and transparency. 3-D rendering can also involve techniques such as anti-aliasing, texture mapping, bump mapping, and shading to enhance the realism and quality of the images .
- 3-D display: presenting the 2-D images of 3-D models on a 2-D or 3-D display device, such as a monitor, a projector, a head-mounted display, or a hologram. 3-D display can also involve methods such as stereoscopy, autostereoscopy, or volumetric display to create the illusion of depth and 3-D perception .
- 3-D interaction: manipulating and exploring 3-D models using input devices such as a mouse, a keyboard, a joystick, a touch screen, a gesture sensor, or a voice command. 3-D interaction can also involve techniques such as virtual reality, augmented reality, or mixed reality to create immersive and interactive 3-D environments .

3-D viewing is widely used in various fields and applications, such as computer-aided design, computer animation, video games, simulation, education, entertainment, art, and medicine . 3-D viewing is also a challenging and active research area, as it involves many complex and interrelated problems and techniques in computer graphics, computer vision, and human-computer interaction.



# Projections in Computer Graphics

- Projection is a technique or process which is used to transform a 3D object into a 2D plane.
- Projection is necessary to display a 3D object on a 2D screen or paper.
- Projection can be classified into two types: parallel projection and perspective projection   .
- Parallel projection is a type of projection in which the direction of projection is parallel to the view plane   .
- Parallel projection can be further divided into orthographic projection, oblique projection and isometric projection   .
- Orthographic projection is a type of parallel projection in which the direction of projection is normal to the view plane    .
- Orthographic projection can be used to show the front, top and side views of an object    .
- Oblique projection is a type of parallel projection in which the direction of projection is not normal to the view plane   .
- Oblique projection can be used to show a 3D view of an object with some distortion   .
- Isometric projection is a type of oblique projection in which the direction of projection makes equal angles with the three principal axes of the object   .
- Isometric projection can be used to show a 3D view of an object without any distortion   .
- Perspective projection is a type of projection in which the direction of projection is not parallel to the view plane, but converges to a single point called the center of projection or the eye point   .
- Perspective projection can be used to show a realistic 3D view of an object with depth and perspective   .
- Perspective projection can be classified into one-point, two-point and three-point perspective, depending on the number of vanishing points on the view plane   .
- One-point perspective is a type of perspective projection in which there is only one vanishing point on the view plane, and the object is parallel to one of the principal axes   .
- Two-point perspective is a type of perspective projection in which there are two vanishing points on the view plane, and the object is parallel to two of the principal axes   .
- Three-point perspective is a type of perspective projection in which there are three vanishing points on the view plane, and the object is not parallel to any of the principal axes   .



# 3-D Clipping

- Clipping is the process of removing or hiding the parts of an object that are outside the viewing volume or the region of interest.
- Clipping is important for efficiency, accuracy and aesthetics in computer graphics.
- In three-dimensional graphics, clipping can be done in two stages: object-space clipping and image-space clipping.
- Object-space clipping discards or clips the objects that are completely or partially outside the viewing volume before projection. This reduces the number of objects that need to be transformed and projected.
- Image-space clipping discards or clips the projected objects that are outside the viewport or the screen boundaries. This prevents the drawing routine from accessing invalid memory locations or drawing outside the screen.
- Clipping can be done against different types of clipping regions, such as planes, cubes, spheres, cylinders, cones, etc. The most common clipping region is the view frustum, which is a truncated pyramid that defines the boundaries of the viewing volume.
- Clipping can be done for different types of primitives, such as points, lines, polygons, curves, surfaces, etc. The clipping algorithm depends on the type of primitive and the type of clipping region.
- Clipping algorithms typically use some form of classification or rejection tests to determine the visibility of a primitive or a part of a primitive. For example, outcodes are binary codes that indicate the position of a point relative to the clipping region. Outcodes can be used to quickly accept or reject a line or a polygon based on bitwise operations.
- Clipping algorithms may also use intersection tests to find the points where a primitive crosses the boundary of the clipping region. These points can be used to split or clip the primitive into visible and invisible parts.
- Clipping algorithms may also use homogenous coordinates or clipping coordinates to simplify the clipping process. Clipping coordinates are obtained by applying the projection matrix to the object coordinates. In clipping coordinates, the clipping region is a unit cube with boundaries at -1 and 1 in each axis. Clipping in clipping coordinates can be done by comparing the coordinates of a point with the boundaries of the unit cube.



# Unit 4 - Curves and Surfaces

- Curves and surfaces are the essential tools for computer-aided geometric design (CAGD) and are used extensively in design and manufacturing systems and computer graphics.
- Curves and surfaces can be represented in different ways, such as parametric, implicit, or explicit forms.
- Parametric curves and surfaces are defined by a set of control points and a function that maps a parameter domain to the curve or surface. For example, a parametric curve in 2D can be written as:

    $$\mathbf{p}(t) = (x(t), y(t))$$

    where $t$ is the parameter and $\mathbf{p}(t)$ is the point on the curve.

- Implicit curves and surfaces are defined by a function that states which points are on and off the curve or surface. For example, an implicit curve in 2D can be written as:

    $$f(x, y) = 0$$

    where $(x, y)$ is the point on the curve and $f(x, y)$ is the function.

- Explicit curves and surfaces are defined by a function that maps one or more variables to another variable. For example, an explicit curve in 2D can be written as:

    $$y = f(x)$$

    where $x$ is the independent variable and $y$ is the dependent variable.

- Curves and surfaces can be classified into different types based on their properties, such as degree, continuity, smoothness, rationality, and uniformity.
- Degree is the highest power of the parameter in the parametric form of the curve or surface. For example, a line has degree 1, a parabola has degree 2, and a cubic curve has degree 3.
- Continuity is the measure of how smoothly the curve or surface joins with itself or with another curve or surface. There are different levels of continuity, such as positional continuity ($C^0$), tangential continuity ($C^1$), curvature continuity ($C^2$), and so on.
- Smoothness is the measure of how free the curve or surface is from sharp corners or cusps. A curve or surface is smooth if it has at least $C^1$ continuity.
- Rationality is the property of the curve or surface that allows it to represent conic sections (such as circles, ellipses, parabolas, and hyperbolas) exactly. A curve or surface is rational if it can be written as a ratio of two polynomials in the parameter.
- Uniformity is the property of the curve or surface that determines how evenly the parameter values are distributed along the curve or surface. A curve or surface is uniform if the parameter values are equally spaced, and non-uniform otherwise.

- Curves and surfaces can be constructed using different methods, such as interpolation, approximation, subdivision, blending, and transformation .
- Interpolation is the method of finding a curve or surface that passes through a given set of data points. For example, a polynomial interpolation curve can be found using Lagrange or Newton methods.
- Approximation is the method of finding a curve or surface that is close to a given set of data points, but not necessarily passes through them. For example, a least-squares approximation curve can be found using linear algebra methods.
- Subdivision is the method of refining a coarse curve or surface into a finer one by adding more control points and subdividing the parameter domain. For example, a B-spline curve can be subdivided using the de Boor algorithm.
- Blending is the method of combining two or more curves or surfaces into a single one by using a weighting function. For example, a Bezier curve can be blended from two control points and two tangent vectors using the Bernstein polynomials.
- Transformation is the method of modifying a curve or surface by applying a geometric operation, such as translation, rotation, scaling, or shearing. For example, a circle can be transformed into an ellipse by scaling it along one axis.

- Curves and surfaces can be evaluated, rendered, and manipulated using different algorithms, such as de Casteljau, de Boor, Bresenham, Cohen-Sutherland, and Bezier clipping .
- de Casteljau is



# Quadric Surfaces

- Quadric surfaces are common modeling primitives for a variety of computer graphics and computer-aided-design applications.
- Quadric surfaces are the graphs of equations that can be expressed in the form `Ax^2 + By^2 + Cz^2 + Dxy + Exz + Fyz + Gx + Hy + Jz + K = 0`.
- Quadric surfaces are the 3D counterparts of conic sections and have six distinct types:
  - Ellipsoid: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 + z^2/c^2 = 1`. It is a closed surface that is symmetric about the three coordinate axes and the origin. It looks like a stretched sphere.
  - Elliptic paraboloid: a surface described by an equation of the form `z = x^2/a^2 + y^2/b^2`. It is an open surface that is symmetric about the z-axis and the origin. It looks like a parabolic bowl.
  - Hyperbolic paraboloid: a surface described by an equation of the form `z = x^2/a^2 - y^2/b^2`. It is an open surface that has two opposite corners pointing up and two opposite corners pointing down. It looks like a saddle or a Pringles chip.
  - Hyperboloid of one sheet: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 1`. It is an open surface that is symmetric about the three coordinate axes and the origin. It looks like an hourglass or a cooling tower.
  - Hyperboloid of two sheets: a surface described by an equation of the form `x^2/a^2 - y^2/b^2 - z^2/c^2 = 1`. It is a closed surface that consists of two disjoint parts that are symmetric about the x-axis and the origin. It looks like two hyperboloids of one sheet facing away from each other.
  - Cone: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 0`. It is an open surface that is symmetric about the z-axis and the origin. It looks like a cone or an ice cream cone.
- When a quadric surface intersects a coordinate plane, the trace is a conic section. For example, a sphere intersects a plane in a circle, an ellipsoid intersects a plane in an ellipse, a cone intersects a plane in a parabola or a hyperbola, etc.
- Ray tracing or ray firing is a popular method used for realistic renderings of quadric surfaces. It involves finding the intersection points of rays of light with the surface and calculating the color and intensity of the reflected or refracted light.



# Spheres

A sphere is a three-dimensional object that has a round shape and a constant radius. It is defined by the set of points that are equidistant from a fixed point called the center. A sphere can be represented by the equation:

(x - x0)^2 + (y - y0)^2 + (z - z0)^2 = r^2

where (x0, y0, z0) is the center and r is the radius of the sphere.

Some properties of spheres are:

- A sphere has a surface area of 4πr^2 and a volume of (4/3)πr^3.
- A sphere is a closed and bounded surface, meaning that it encloses a finite region of space and has no boundary or edge.
- A sphere is a convex surface, meaning that any line segment joining two points on the sphere lies entirely on or inside the sphere.
- A sphere is a smooth surface, meaning that it has no corners or sharp edges.

## Spheres in Computer Graphics

In computer graphics, spheres are often used to model objects that have a round shape, such as planets, balls, bubbles, etc. However, spheres are not easy to render or manipulate directly, because they are not composed of flat polygons, which are the basic elements of most graphics systems. Therefore, spheres are usually approximated by simpler objects constructed from flat polygons, such as polyhedra.

There are several methods to approximate a sphere by a polyhedron, such as:

- Using lines of longitude and latitude to divide the sphere into quadrilaterals or triangles. This method is simple and intuitive, but it produces uneven polygons that are more dense near the poles and less dense near the equator.
- Using a regular polyhedron, such as an icosahedron or a dodecahedron, and subdividing each face into smaller triangles. This method produces more uniform polygons, but it requires more computation and storage.
- Using a recursive subdivision algorithm, such as the midpoint subdivision or the butterfly subdivision, to refine an initial polyhedron into a smoother approximation of a sphere. This method allows for adaptive refinement, meaning that the polygons can be more or less dense depending on the level of detail required.

Another challenge in computer graphics is to determine the appearance of a sphere, such as its color, texture, shading, reflection, etc. This depends on the properties of the sphere, such as its material, surface normal, light source, etc. There are various techniques to compute these properties, such as:

- Using a parametric representation of the sphere, such as spherical coordinates, to map a texture image onto the sphere. This method is simple and fast, but it may cause distortion or seams in the texture.
- Using a projection method, such as the cube map or the sphere map, to map a texture image onto the sphere. This method is more accurate and seamless, but it requires more memory and computation.
- Using a shading model, such as the Phong model or the Blinn-Phong model, to compute the color and intensity of each pixel on the sphere. This method is more realistic and dynamic, but it requires more computation and parameters.

## Spheres in Computational Geometry

In computational geometry, spheres are often used as bounding volumes, meaning that they are used to enclose or contain other objects or data. Bounding volumes are useful for various applications, such as collision detection, ray tracing, visibility culling, etc. There are several advantages of using spheres as bounding volumes, such as:

- Spheres are simple and easy to construct and test. They only require the center and the radius as parameters, and they can be computed from a set of points using various algorithms, such as the Ritter's algorithm or the Welzl's algorithm.
- Spheres are invariant under rotation and scaling, meaning that they do not change shape or size when the object or the coordinate system is rotated or scaled. This makes them more robust and efficient than other bounding volumes, such as boxes or cylinders.
- Spheres are tight and optimal, meaning that they have the smallest surface area and volume among all bounding volumes that enclose a given object or data. This makes them more accurate and effective than other bounding volumes, such as spheres of oriented bounding boxes (SOBs) or discrete oriented polytopes (DOPs).

However, spheres also have some disadvantages as bounding volumes, such as:

- Spheres are not axis-aligned, meaning that they do not align with the axes of the coordinate system. This makes them more difficult and costly to test for intersection or containment with other



# Ellipsoid

- An ellipsoid is a surface that may be obtained from a sphere by deforming it by means of directional scalings, or more generally, of an affine transformation.
- An ellipsoid is a quadric surface; that is, a surface that may be defined as the zero set of a polynomial of degree two in three variables .
- An ellipsoid is symmetrical about three mutually perpendicular axes that intersect at the centre.
- If a, b, and c are the principal semiaxes, the general equation of such an ellipsoid is x^2^ / a^2^ + y^2^ / b^2^ + z^2^ / c^2^ = 1 .
- An ellipsoid can also be parametrized using spherical coordinates as follows:

  x = a sin θ cos φ

  y = b sin θ sin φ

  z = c cos θ

  where 0 ≤ θ ≤ π and 0 ≤ φ ≤ 2π.

- An ellipsoid can be rendered in computer graphics using various techniques, such as ray tracing, polygonal approximation, or implicit surface modeling.
- Superquadric ellipsoids and toroids are recent geometric shapes, which are useful for computer graphics modeling. They are defined by raising the coordinates of an ellipsoid or a torus to a power, which controls the roundness or sharpness of the shape.



# Blobby Objects

- Blobby objects are a type of **implicit modeling technique** that can represent non-rigid and fluid-like objects in computer graphics.
- Blobby objects are defined by a set of **metaballs**, which are spherical regions of influence that have a scalar field value that decreases with distance from the center.
- The surface of a blobby object is the **isosurface** of the scalar field, which is the set of points where the field value is equal to a given threshold.
- The scalar field value at any point is computed by summing the contributions of all the metaballs, which can be weighted by different factors.
- Blobby objects can be used to model objects such as cloth, rubber, liquids, water droplets, clouds, etc .
- Blobby objects can exhibit **metamorphosis**, which is the smooth transformation of one shape into another, by changing the positions, sizes, and weights of the metaballs.
- Blobby objects can also exhibit **blending**, which is the merging or splitting of two or more shapes, by adjusting the threshold value of the isosurface.
- Blobby objects can be rendered using **ray tracing** or **polygonization** techniques.
- Ray tracing involves finding the intersection of a ray with the isosurface, which can be done by solving a nonlinear equation or using a root-finding method.
- Polygonization involves approximating the isosurface by a mesh of polygons, which can be done by using a **marching cubes** algorithm or a **marching tetrahedra** algorithm.



# Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- Splines can be classified into different types based on their degree, basis functions, and continuity conditions.
- Some common types of splines are:
  - Linear splines: Splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: Splines of degree two that consist of parabolic segments joined at the given points.
  - Cubic splines: Splines of degree three that consist of cubic polynomial segments joined at the given points.
  - Bezier curves: Splines that are defined by a set of control points that influence the shape of the curve, but do not necessarily lie on the curve.
  - B-splines: Splines that are defined by a set of control points and a knot vector that determines the degree and continuity of the curve.
  - NURBS: Non-uniform rational B-splines that are a generalization of B-splines that allow for rational (non-polynomial) curves and surfaces.
- Splines have several properties that make them suitable for computer graphics, such as:
  - Affine invariance: Splines are invariant under affine transformations, such as rotation, translation, scaling, and shearing.
  - Local control: Splines are controlled by local parameters, such as control points and knots, that affect only a small portion of the curve or surface.
  - Smoothness: Splines can have different levels of smoothness, such as continuity of position, tangent, curvature, etc., depending on the choice of basis functions and knots.
  - Interpolation or approximation: Splines can either interpolate (pass through) or approximate (fit) the given points, depending on the design criteria.



# Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline is a type of spline function that is defined by a set of control points and a knot vector.
- A spline function is a piecewise polynomial function that can be used to model smooth curves and surfaces.
- B-splines have some advantages over other spline functions, such as:
  - They have local control, which means that changing a control point only affects a local part of the curve or surface.
  - They have a variable degree, which means that the degree of the polynomial segments can be chosen independently of the number of control points.
  - They have a compact support, which means that each basis function is nonzero only in a finite interval.
  - They have a convex hull property, which means that the curve or surface lies within the convex hull of the control points.
  - They have a variation diminishing property, which means that the curve or surface does not oscillate more than the control polygon.
- B-splines can be used for various applications in computer graphics, such as:
  - Curve-fitting and numerical differentiation of experimental data.
  - Computer-aided design and computer-aided manufacturing of complex shapes.
  - Interactive manipulation and editing of curves and surfaces.
  - Rendering and animation of smooth objects.



# Bezier curves and surfaces

- Bezier curves and surfaces are a way of representing smooth curves and surfaces using polynomial functions and a set of control points .
- Bezier curves and surfaces are widely used in computer graphics, computer-aided design, animation, and font design.
- Bezier curves and surfaces have some desirable properties, such as:
  - They are invariant under affine transformations, such as translation, rotation, scaling, and shearing .
  - They can be easily subdivided into smaller curves or surfaces that are also Bezier .
  - They can be evaluated efficiently using recursive algorithms, such as de Casteljau's algorithm and Bernstein polynomials .
  - They can be intuitively manipulated by adjusting the positions of the control points .

## Bezier curves

- A Bezier curve of degree n is defined by n+1 control points P0, P1, ..., Pn.
- The curve passes through the first and last control points, P0 and Pn, but not necessarily through the others.
- The curve is a weighted sum of the control points, where the weights are given by the Bernstein polynomials of degree n.
- The curve can be written as:

  B(t) = sum_{i=0}^n B_i^n(t) P_i, 0 <= t <= 1

  where B_i^n(t) = C(n,i) t^i (1-t)^(n-i) are the Bernstein polynomials, and C(n,i) = n! / (i! (n-i)!) are the binomial coefficients.

- The curve can also be computed recursively using de Casteljau's algorithm, which splits the curve into two subcurves at any parameter value t.
- The algorithm can be described as:

  B(t) = P0, if n = 0
  B(t) = (1-t) B0(t) + t B1(t), if n = 1
  B(t) = (1-t) B(t)_{0..n-1} + t B(t)_{1..n}, if n > 1

  where B(t)_{i..j} is the Bezier curve defined by the control points P_i, P_i+1, ..., P_j.

- The curve can be subdivided into two smaller curves at any parameter value t by applying de Casteljau's algorithm and taking the first and last points of each iteration as the new control points.
- The curve can be approximated by a polygonal chain by sampling the curve at regular intervals of t and connecting the points with straight lines.

## Bezier surfaces

- A Bezier surface of degree (m,n) is defined by (m+1)(n+1) control points P_{i,j}, where 0 <= i <= m and 0 <= j <= n.
- The surface is a weighted sum of the control points, where the weights are given by the tensor product of the Bernstein polynomials of degree m and n.
- The surface can be written as:

  S(u,v) = sum_{i=0}^m sum_{j=0}^n B_i^m(u) B_j^n(v) P_{i,j}, 0 <= u,v <= 1

  where B_i^m(u) and B_j^n(v) are the Bernstein polynomials of degree m and n, respectively.

- The surface can also be computed recursively using a generalization of de Casteljau's algorithm, which splits the surface into four subsurfaces at any parameter values (u,v).
- The algorithm can be described as:

  S(u,v) = P_{0,0}, if m = n = 0
  S(u,v) = (1-u) S0(u,v) + u S1(u,v), if m = 1 and n = 0
  S(u,v) = (1-v) S0(u,v) + v S1(u,v), if m = 0 and n = 1
  S(u,v) = (1-u) (1-v) S(u,v)_{0..m-1,0..n-1}



## Unit 5 - Hidden Lines and Surfaces

- Hidden lines and surfaces are used to represent the parts of an object that are not visible from a given viewpoint.
- Hidden lines are usually drawn as dashed or dotted lines on a 2D drawing or a 3D model.
- Hidden surfaces are usually shaded or colored differently from the visible surfaces on a 3D model or a rendering.
- The purpose of hidden lines and surfaces is to show the shape and structure of the object more clearly and completely, and to avoid ambiguity or confusion.
- Hidden lines and surfaces are also used to indicate the internal features of the object, such as holes, slots, ribs, etc.
- Hidden lines and surfaces follow some conventions and rules, such as:
  - Hidden lines should not cross visible lines or other hidden lines.
  - Hidden lines should not be used to show the outline of the object or the edges of the surfaces.
  - Hidden lines should be omitted when they are too close to each other or to the visible lines, or when they clutter the drawing or the model.
  - Hidden surfaces should be distinguished from the visible surfaces by using different colors, shades, textures, or patterns.
  - Hidden surfaces should not obscure the visible surfaces or the important details of the object.
  - Hidden surfaces should be omitted when they are not relevant or necessary for the understanding of the object.



# Back Face Detection Algorithm

- Back face detection, also known as plane equation method, is an object space method for identifying the visible surfaces of a polyhedron .
- A polyhedron is a solid object bounded by flat polygonal faces. Each face has a normal vector that points outward from the object.
- A face is called a back face if its normal vector points away from the viewer, or equivalently, if the angle between the normal vector and the viewing direction is greater than 90 degrees .
- Back face detection algorithm works as follows :
  - For each face of the polyhedron, compute its normal vector by taking the cross product of two adjacent edges.
  - For each face of the polyhedron, compute its plane equation by substituting any vertex into the equation Ax + By + Cz + D = 0, where A, B, C are the components of the normal vector.
  - For each face of the polyhedron, test whether it is a back face by substituting the viewing point into the plane equation and checking the sign of the result. If the result is positive, the face is a back face and can be eliminated. If the result is negative or zero, the face is a front face and should be retained.
- Back face detection algorithm can reduce the number of faces to be processed by the hidden surface removal algorithms, such as Z-buffer, scan-line, or painter's algorithm .
- Back face detection algorithm is also known as back-face culling in computer graphics, and it is a common optimization technique for rendering 3D scenes.



# Depth buffer method

The depth buffer method, also known as the z-buffer method, is a technique for hidden surface removal in computer graphics. It is an image-space approach that works by storing the depth (or z-coordinate) of the closest object at each pixel in a buffer, and comparing the depth of new objects with the existing depth in the buffer. If the new object is closer, its depth and color are stored in the buffer, otherwise it is discarded. This process is repeated for every object in the scene, and the final buffer contains the visible surfaces from the viewpoint.

The depth buffer method has the following advantages:

- It is easy to implement in hardware or software.
- It can handle any type of object, such as polygons, curves, or volumes.
- It can handle transparency and anti-aliasing by using additional buffers or techniques.

The depth buffer method has the following disadvantages:

- It requires a large amount of memory to store the depth buffer, which may limit the resolution or color depth of the image.
- It may suffer from precision errors or artifacts due to finite depth resolution or rounding errors.
- It does not handle overlapping objects or cyclic dependencies well, as it only stores the closest object at each pixel.

The depth buffer method can be summarized by the following steps:

1. Initialize the depth buffer to a large value (such as infinity) and the color buffer to a background color.
2. For each object in the scene, project it onto the image plane and rasterize it into pixels.
3. For each pixel, calculate its depth using the equation of the plane or an increment method.
4. Compare the depth of the pixel with the existing depth in the buffer. If the pixel is closer, update the depth and color in the buffer, otherwise ignore the pixel.
5. Repeat steps 2 to 4 for every object in the scene.
6. Display the color buffer as the final image.



# A-Buffer Method for Hidden Lines and Surfaces

- A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects .
- It extends the algorithm of depth-buffer (or Z-buffer) method by storing more than one depth and color value per pixel.
- It uses a linked list data structure to store the fragments of objects that overlap a pixel.
- Each fragment has four attributes: depth, color, opacity, and pointer to the next fragment.
- The fragments are sorted in decreasing order of depth and stored in the A-buffer.
- The final color of a pixel is computed by blending the colors of the fragments from front to back, using the opacity values as weights.
- A-buffer method can handle anti-aliasing, transparency, and complex intersections.
- A-buffer method requires more memory and processing time than depth-buffer method.
- A-buffer method can be implemented using hardware or software.



# Scan line method

The scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis . The main steps of the scan line method are:

- Sort all the polygons to be rendered by the top y coordinate at which they first appear.
- For each row or scan line of the image, compute the intersection of the scan line with the polygons on the front of the sorted list, while discarding the no-longer-visible polygons.
- Fill the pixels between the intersection points with the color and intensity of the visible polygon, using a refresh buffer to store the pixel values.
- Repeat the process for the next scan line until the entire image is rendered.

The scan line method is based on the image-space method and the concept of coherence. Coherence means that the pixels that are close to each other in the image space are likely to have similar properties, such as color, depth, and visibility. The scan line method exploits the coherence by processing one line at a time, rather than one pixel at a time, which reduces the computational cost and complexity.

The scan line method can handle concave and intersecting polygons, as well as polygons with holes, by using an active edge list (AEL) to store the edges that cross the current scan line, and a parity flag to indicate whether the scan line is inside or outside a polygon. The AEL is updated as the scan line moves down the image, and the parity flag is toggled whenever the scan line crosses an edge. The pixels between the edges in the AEL are filled with the color of the polygon that has the parity flag on, or the background color if the parity flag is off.

The scan line method is one of the simplest and most efficient algorithms for hidden surface removal, as it avoids the need to compare the depth of every pixel in the image. However, it also has some limitations, such as:

- It requires the polygons to be planar and non-overlapping in the image space, which may not be the case for curved or distorted surfaces.
- It does not handle transparency or shading effects, which require more information than just the color and intensity of the visible polygon.
- It may produce aliasing artifacts, which are jagged edges or gaps in the rendered image, due to the discrete nature of the scan line and the pixels. These artifacts can be reduced by using anti-aliasing techniques, such as supersampling or filtering.



# Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the physical properties of light and the interaction of light with different materials.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, such as ambient, diffuse, and specular reflection.
  - Global illumination models consider all the interactions and exchange of light among objects, such as reflection, refraction, shadows, and interreflections.
- In this unit, we will focus on the local illumination models, which are simpler and faster to compute than the global ones.
- The local illumination models have three main components: light sources, surface properties, and viewing parameters.
  - Light sources are the entities that emit light in the scene. They can have different types, such as point, directional, or spot. They can also have different colors and intensities.
  - Surface properties are the characteristics of the material that affect how it reflects light, such as color, reflectivity, roughness, or transparency.
  - Viewing parameters are the factors that depend on the position and orientation of the viewer and the surface, such as the angle of incidence, the angle of reflection, or the distance.
- The local illumination models can be further divided into three types: ambient, diffuse, and specular.
  - Ambient reflection is the uniform and constant light that is present in the scene regardless of the light sources or the viewing parameters. It is used to simulate the effect of indirect illumination from the environment.
  - Diffuse reflection is the light that is reflected equally in all directions from a matte or rough surface. It depends on the angle between the light source and the surface normal, and the color and intensity of the light source and the surface.
  - Specular reflection is the light that is reflected in a mirror-like manner from a shiny or smooth surface. It depends on the angle between the light source, the surface normal, and the viewer, and the color and intensity of the light source and the surface. It also depends on the shininess or glossiness of the surface, which determines how concentrated or spread the reflected light is.
- The basic illumination model combines the ambient, diffuse, and specular components to obtain the final intensity and color of the reflected light at a point on the surface. The formula is:

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - where I is the total intensity, I<sub>a</sub> is the ambient intensity, I<sub>d</sub> is the diffuse intensity, and I<sub>s</sub> is the specular intensity.
  - The ambient intensity is calculated as:

    - I<sub>a</sub> = k<sub>a</sub> * I<sub>al</sub>
    - where k<sub>a</sub> is the ambient reflectance coefficient of the surface, and I<sub>al</sub> is the ambient light intensity.
  - The diffuse intensity is calculated as:

    - I<sub>d</sub> = k<sub>d</sub> * I<sub>l</sub> * cos θ
    - where k<sub>d</sub> is the diffuse reflectance coefficient of the surface, I<sub>l</sub> is the light source intensity, and θ is the angle between the light source and the surface normal.
  - The specular intensity is calculated as:

    - I<sub>s</sub> = k<sub>s</sub> * I<sub>l</sub> * cos<sup>n</sup> α
    - where k<sub>s</sub> is the specular reflectance coefficient of the surface, I<sub>l</sub> is the light source intensity, α is the angle between the reflected light and the viewer, and n is the shininess exponent of the surface.
- The basic illumination model can be extended to include multiple light sources, multiple surfaces, and multiple colors. The formula is:

  - I = I<sub>a</sub> + Σ



# Ambient light

- Ambient light is the base brightness applied to textures rendered in a scene before any point, spot, or other types of virtual light sources are computed.
- Ambient light affects the appearance of the entire rendered scene by adding a uniform amount of light to every point, regardless of its position, orientation, or material .
- Ambient light can be used to simulate natural or artificial lighting, such as the sun or fluorescent lights, by adjusting its color and intensity.
- Ambient light is a gross oversimplification of the complex interaction between the light sources and the surfaces in the scene, but it works well enough for some applications.
- Ambient light does not take into account the occlusion of light by other objects in the scene, which can result in unrealistic or flat-looking images.
- Ambient occlusion is a technique that calculates how exposed each point in a scene is to ambient lighting, and darkens the points that are more occluded by other objects, creating more depth and contrast in the scene.



# Diffuse Reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough.
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by the color and texture of the surface, as well as the position and intensity of the light source.
- Diffuse reflection can be modeled by the Lambertian reflectance model, which assumes that the reflected light is proportional to the cosine of the angle between the surface normal and the light direction.
- Diffuse interreflection is a process whereby light reflected from an object strikes other objects in the surrounding area, illuminating them.
- Diffuse interreflection specifically describes light reflected from objects which are not shiny or specular.
- Diffuse interreflection can be simulated by using radiosity methods, which solve a system of linear equations that represent the energy exchange between surfaces.
- Diffuse interreflection can create soft shadows and color bleeding effects, which add realism to the scene.



# Specular Reflection

- Specular reflection is the phenomenon of light reflecting from a smooth or shiny surface in a mirror-like manner.
- Specular reflection occurs when the angle of incidence is equal to the angle of reflection, and the reflected rays are parallel to each other.
- Specular reflection produces a bright spot of light on the surface, called a specular highlight, that has the color of the light source rather than of the object.
- Specular reflection depends on the surface normal, the direction of the light source, and the direction of the viewer.
- Specular reflection can be modeled by an empirical formula suggested by Bui-Tuong Phong in 1975, which is often used in computer graphics.
- The Phong model defines the specular reflection as:

  - I<sub>s</sub> = k<sub>s</sub> I<sub>l</sub> (R ⋅ V)<sup>n</sup>
  - where I<sub>s</sub> is the intensity of the specular reflection, k<sub>s</sub> is the specular reflection coefficient, I<sub>l</sub> is the intensity of the light source, R is the direction of the reflected ray, V is the direction of the viewer, and n is the shininess exponent.
  - The shininess exponent controls the size and sharpness of the specular highlight. A higher value of n produces a smaller and sharper highlight, while a lower value of n produces a larger and softer highlight.
  - The Phong model assumes that the surface is perfectly smooth and the light source is a point source. It does not account for the effects of roughness, texture, or multiple light sources.



# Phong model

The Phong model is an empirical model of the local illumination of points on a surface designed by the computer graphics researcher Bui Tuong Phong. It is sometimes referred to as "Phong shading", particularly if the model is used with the interpolation method of the same name and in the context of pixel shaders or other places where a lighting calculation can be referred to as “shading”.

The Phong model describes the interaction of light with a surface, in terms of the properties of the surface and the nature of the incident light. It consists of three components: ambient, diffuse, and specular.

- Ambient component: This represents the constant background light that is present in the scene. It is independent of the surface orientation and the light direction. It is usually a constant color or a low-intensity color map.
- Diffuse component: This represents the light that is scattered uniformly in all directions by the surface. It depends on the surface orientation and the light direction, but not on the viewer position. It is proportional to the cosine of the angle between the surface normal and the light direction. It is usually a color map or a texture map multiplied by the light color.
- Specular component: This represents the light that is reflected in a mirror-like manner by the surface. It depends on the surface orientation, the light direction, and the viewer position. It is proportional to the cosine of the angle between the reflection direction and the viewer direction, raised to some power. It is usually a constant color or a specular map multiplied by the light color.

The Phong model can be expressed mathematically as:

I = I_a + I_d + I_s

where I is the total intensity, I_a is the ambient component, I_d is the diffuse component, and I_s is the specular component.

The ambient component can be calculated as:

I_a = k_a * I_L

where k_a is the ambient reflection coefficient, and I_L is the ambient light intensity.

The diffuse component can be calculated as:

I_d = k_d * I_L * (N . L)

where k_d is the diffuse reflection coefficient, I_L is the light intensity, N is the surface normal, and L is the light direction. The dot product (N . L) represents the cosine of the angle between N and L.

The specular component can be calculated as:

I_s = k_s * I_L * (R . V)^n

where k_s is the specular reflection coefficient, I_L is the light intensity, R is the reflection direction, V is the viewer direction, and n is the shininess exponent. The dot product (R . V) represents the cosine of the angle between R and V.

The reflection direction R can be computed as:

R = 2 * (N . L) * N - L

The viewer direction V can be computed as:

V = -E

where E is the eye position.

The Phong model can produce realistic-looking images of shiny surfaces, such as metals, plastics, and ceramics. However, it has some limitations, such as:

- It does not account for the global illumination effects, such as shadows, reflections, and refractions.
- It does not account for the wavelength-dependent behavior of light, such as dispersion and polarization.
- It does not account for the roughness or microstructure of the surface, which can affect the scattering and reflection of light.
- It does not account for the Fresnel effect, which is the variation of reflectance with the angle of incidence.
- It does not account for the subsurface scattering, which is the penetration and diffusion of light inside the surface.

To overcome some of these limitations, more advanced models have been developed, such as the Blinn-Phong model, the Cook-Torrance model, the Oren-Nayar model, and the Bidirectional Reflectance Distribution Function (BRDF) model.



# Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image .
- HLR and HSR are important for creating realistic and accurate images of solid objects and avoiding visual clutter and confusion .
- There are different types of coherence that can be exploited to reduce the computation required for HLR and HSR, such as object coherence, image coherence, and temporal coherence.
- Object coherence refers to the spatial relationship among the objects in the scene, such as occlusion, containment, and adjacency.
- Image coherence refers to the spatial relationship among the pixels in the image, such as scan-line continuity, area coherence, and span coherence.
- Temporal coherence refers to the temporal relationship among the successive frames in an animation, such as object motion, camera motion, and illumination change.
- There are different algorithms for HLR and HSR, such as back-face culling, depth-buffer method, scan-line method, painter's algorithm, z-buffer algorithm, and BSP-tree algorithm  .
- Back-face culling is a simple technique that eliminates the faces that are oriented away from the viewer, based on the sign of the surface normal vector .
- Depth-buffer method is a technique that assigns a depth value to each pixel in the image, and compares the depth values of the overlapping pixels to determine the visible pixel .
- Scan-line method is a technique that processes the image one scan-line at a time, and maintains an active edge list and an active polygon list to determine the visible pixels .
- Painter's algorithm is a technique that sorts the polygons in the scene from back to front, and paints them on the image in that order, overwriting the previously painted pixels .
- Z-buffer algorithm is a technique that assigns a z-value to each pixel in the image, and compares the z-values of the overlapping pixels to determine the visible pixel .
- BSP-tree algorithm is a technique that partitions the scene into convex regions using binary space partitioning, and traverses the BSP-tree in a back-to-front or front-to-back order to determine the visible polygons .
- Each algorithm has its own advantages and disadvantages, such as complexity, memory requirement, accuracy, and speed .
- A combined approach for HLR and HSR can use a combination of different algorithms to achieve a balance between performance and quality .
- For example, a combined approach can use back-face culling to eliminate the invisible faces, depth-buffer method to handle the overlapping polygons, and scan-line method to fill the visible pixels .



# Warn Model for Hidden Lines and Surfaces in Computer Graphics

- Hidden lines and surfaces are the parts of an object that are not visible from a given viewpoint or projection.
- Hidden line and surface removal is an important step in computer graphics to produce realistic and uncluttered images of 3D scenes.
- There are various algorithms for hidden line and surface removal, such as back-face culling, z-buffer, scan-line, painter's, BSP tree, ray tracing, etc.
- The Warn model is an area subdivision algorithm proposed by John Warnock in 1969. It is based on the concept of area coherence, which means that adjacent pixels in an image tend to have similar properties, such as depth, color, and visibility.
- The Warn model divides the viewing window into smaller rectangular areas, called subwindows, and determines the visibility of objects in each subwindow recursively.
- The algorithm works as follows:

  - Start with the entire viewing window as the initial subwindow.
  - For each subwindow, check if it satisfies one of the following conditions:
    - The subwindow is empty, i.e., it contains no objects. In this case, fill the subwindow with the background color and stop the recursion.
    - The subwindow is simple, i.e., it contains only one object or a part of an object that is entirely visible. In this case, fill the subwindow with the color of the object and stop the recursion.
    - The subwindow is complex, i.e., it contains more than one object or a part of an object that is partially visible. In this case, divide the subwindow into four equal subwindows and repeat the algorithm for each subwindow.
  - The recursion stops when the subwindows are small enough to be considered as pixels, or when a predefined depth limit is reached.
- The Warn model is efficient and easy to implement, but it has some drawbacks, such as:
  - It requires a lot of memory to store the subwindows and their properties.
  - It may produce aliasing artifacts, i.e., jagged edges, due to the discrete subdivision of the viewing window.
  - It may not handle curved surfaces or transparent objects well, as it assumes that objects are polygonal and opaque.



# Intensity Attenuation

- In computer graphics, **intensity attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- Intensity attenuation is important for realistic rendering of scenes, as it affects the shading and visibility of objects.
- Intensity attenuation can be modeled by a formula that depends on the distance from the light source, the properties of the medium, and the angle of incidence.
- The formula for intensity attenuation is:

  $$I = I_0 \frac{1}{a + bd + cd^2}$$

  where $I$ is the intensity at distance $d$ from the light source, $I_0$ is the intensity at the light source, $a$, $b$, and $c$ are constants that depend on the medium, and $d$ is the distance from the light source.
- Intensity attenuation can be applied to different types of light sources, such as point lights, spot lights, and directional lights.
- Intensity attenuation can also be combined with other effects, such as ambient, diffuse, and specular lighting, to create more realistic shading models.



# Color consideration for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection.
- Hidden surface removal or visible surface determination is the process of identifying and eliminating the hidden surfaces from the rendered image  .
- Color consideration for the notes of hidden lines and surfaces is important to enhance the readability and clarity of the notes, as well as to highlight the key concepts and techniques.
- Some of the color considerations for the notes are:

  - Use different colors to distinguish between visible and hidden lines and surfaces, such as black for visible and gray for hidden.
  - Use different colors to indicate the depth or distance of the surfaces from the viewpoint, such as darker for closer and lighter for farther.
  - Use different colors to represent the surface color or material properties, such as RGB components or intensity values .
  - Use different colors to illustrate the different algorithms or methods for hidden surface removal, such as z-buffering, scan-line, ray tracing, etc  .
  - Use consistent and contrasting colors to avoid confusion and ambiguity, such as avoiding similar shades or hues of the same color.
  - Use appropriate and appealing colors to attract and retain the attention of the reader, such as avoiding too bright or too dull colors.



# Transparency and Shadows

## Transparency
- Transparency is the property of a material that allows light to pass through it partially or fully.
- Transparency can be used to create realistic effects such as glass, water, ice, etc. in computer graphics.
- Transparency can be classified into two types: **binary transparency** and **partial transparency** .
- Binary transparency is when a pixel is either fully transparent or fully opaque, such as in GIF images or masks.
- Partial transparency is when a pixel can have varying degrees of transparency, such as in PNG images or alpha blending.
- Partial transparency can be simulated by mixing the colors of the transparent object and the background object, using a factor called the **alpha value** .
- The alpha value ranges from 0 to 1, where 0 means fully transparent and 1 means fully opaque.
- The formula for alpha blending is:

  C = alpha * C1 + (1 - alpha) * C2

  where C is the resulting color, C1 is the color of the transparent object, C2 is the color of the background object, and alpha is the alpha value.

- Transparency can also be affected by the viewing angle, the thickness of the material, the refraction of light, and the presence of multiple transparent layers .
- Transparency can be implemented in computer graphics using various techniques, such as ray tracing, depth peeling, alpha testing, etc.

## Shadows
- Shadows are the regions where light is blocked by an object, creating a contrast between the illuminated and the dark areas.
- Shadows can enhance the realism, depth, and mood of a scene in computer graphics.
- Shadows can be classified into two types: **hard shadows** and **soft shadows**.
- Hard shadows are when the boundary between the shadow and the light is sharp and well-defined, such as in a sunny day or a point light source.
- Soft shadows are when the boundary between the shadow and the light is fuzzy and blurred, such as in a cloudy day or an area light source.
- Soft shadows are more realistic than hard shadows, but also more computationally expensive to generate.
- Shadows can be implemented in computer graphics using various techniques, such as shadow mapping, shadow volumes, ray tracing, etc.

