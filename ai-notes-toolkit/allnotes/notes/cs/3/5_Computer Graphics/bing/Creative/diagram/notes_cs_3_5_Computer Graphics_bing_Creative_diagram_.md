

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



### Types of computer graphics

Computer graphics are the visual representation of data and information using computers and software. Computer graphics can be used for various purposes, such as creating images, animations, simulations, games, user interfaces, and more.

Computer graphics can be broadly classified into two main categories: raster graphics and vector graphics  . Additionally, computer graphics can also be categorized based on the dimensionality of the images: two dimensional (2D), three dimensional (3D), and animated graphics .

- **Raster graphics** are made up of pixels, which are small dots of color arranged in a grid. Each pixel contains information about its color and brightness. Raster graphics are also known as bitmap images, as they map each pixel to a specific location on the screen. Raster graphics are commonly used for digital photographs, paintings, and scanned images. The quality of raster graphics depends on the resolution, which is the number of pixels per unit area. Higher resolution means more detail and clarity, but also larger file size and memory usage. Raster graphics can be edited by changing the color or brightness of individual pixels or groups of pixels. However, raster graphics can lose quality when they are scaled up or down, as the pixels become distorted or blurred. Some examples of raster graphics formats are JPEG, PNG, GIF, BMP, and TIFF.
- **Vector graphics** are made up of paths, which are defined by mathematical equations that describe the shape, position, and color of each element. Paths can be composed of lines, curves, polygons, and other geometric primitives. Vector graphics are also known as scalable graphics, as they can be scaled up or down without losing quality or detail. Vector graphics are commonly used for logos, icons, diagrams, fonts, and illustrations. The quality of vector graphics depends on the smoothness and accuracy of the paths. Vector graphics can be edited by changing the attributes or parameters of the paths or elements. Some examples of vector graphics formats are SVG, EPS, PDF, and AI.
- **2D graphics** are images that have only two dimensions: width and height. 2D graphics can be either raster or vector, depending on how they are created and stored. 2D graphics are used for creating flat or simple images, such as icons, logos, charts, maps, and cartoons. 2D graphics can be manipulated by applying transformations, such as rotation, scaling, translation, and skewing. Some examples of 2D graphics software are Photoshop, Illustrator, GIMP, and Inkscape.
- **3D graphics** are images that have three dimensions: width, height, and depth. 3D graphics are usually created using vector-based methods, such as polygons, meshes, surfaces, and curves. 3D graphics are used for creating realistic or complex images, such as models, scenes, characters, and animations. 3D graphics can be manipulated by applying transformations, such as rotation, scaling, translation, and skewing, as well as lighting, shading, texturing, and rendering. Some examples of 3D graphics software are Blender, Maya, 3ds Max, and Unity.
- **Animated graphics** are images that change over time, creating the illusion of motion. Animated graphics can be either 2D or 3D, depending on how they are created and stored. Animated graphics are used for creating dynamic or interactive images, such as movies, games, simulations, and presentations. Animated graphics can be manipulated by applying transformations, as well as timing, sequencing, and transitions. Some examples of animated graphics formats are GIF, MP4, AVI, and SWF. Some examples of animated graphics software are Flash, After Effects, Premiere, and Animate.



### Graphic Displays

- A graphic display is a device that can show images generated by a computer or other electronic system.
- Graphic displays can be classified into two main types: raster and vector.
- Raster displays use a grid of pixels (picture elements) that can be individually turned on or off to create an image. Each pixel has a color and a brightness value. Examples of raster displays are LCD, LED, OLED, and plasma monitors.
- Vector displays use a beam of electrons that traces lines on a phosphor-coated screen to create an image. Each line has a color, a brightness, and a start and end point. Examples of vector displays are oscilloscopes and some arcade games.
- Raster displays are more common and versatile than vector displays, as they can show more complex and realistic images. However, vector displays have some advantages, such as higher resolution, faster response, and lower power consumption.
- Graphic displays can also be characterized by other features, such as:
  - Size: the diagonal measurement of the screen in inches or centimeters.
  - Resolution: the number of pixels or lines that can be displayed horizontally and vertically. Higher resolution means sharper and more detailed images.
  - Aspect ratio: the ratio of the width to the height of the screen. Common aspect ratios are 4:3, 16:9, and 21:9.
  - Color depth: the number of bits used to represent the color and brightness of each pixel. Higher color depth means more colors and smoother gradients.
  - Refresh rate: the number of times per second that the image on the screen is updated. Higher refresh rate means smoother motion and less flicker.
  - Contrast ratio: the ratio of the brightness of the brightest white to the darkest black that the display can produce. Higher contrast ratio means better visibility and more vivid colors.
  - Viewing angle: the angle at which the image on the screen remains clear and visible. Wider viewing angle means more comfortable and flexible viewing positions.
  - Response time: the time it takes for a pixel to change from one color to another. Lower response time means less ghosting and blurring in fast-moving images.
- Graphic displays are essential for computer graphics, as they allow the user to see the output of the graphical applications and interact with them. Some graphic displays are specially designed for graphic design, such as the Asus ProArt OLED PA32DC, the Dell U3223QE, the Apple Pro Display XDR, and the BenQ PD3200U. These monitors have features such as high resolution, wide color gamut, accurate color reproduction, and ergonomic design.



### Random scan displays

- Random scan displays are also known as **vector displays** or **stroke-writing displays** or **calligraphic displays** .
- Random scan displays are used to draw a picture **one line at a time** and are thus also referred to as **line-drawing displays**  .
- Random scan displays use a **cathode ray tube (CRT)** that directs the beam of an electron only to those areas of the screen where a picture has to be drawn  .
- Random scan displays can draw and refresh component lines of a picture in **any specified sequence**.
- Random scan displays can produce **smooth line drawings** with **high resolution**.
- Random scan displays are suitable for applications that require **line drawings** such as **engineering drawings** and **computer-aided design (CAD)**  .
- Random scan displays are **not** suitable for applications that require **realistic shaded scenes** or **photorealistic images** .
- Random scan displays require a **display processor** or a **display list** to store the line coordinates and attributes  .
- Random scan displays have a **low refresh rate** and a **high flicker rate**  .
- Random scan displays are **more expensive** and **less common** than raster scan displays  .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on raster scan displays for the unit 1 of computer graphics.

### Raster scan displays

- Raster scan displays are the most common type of graphics monitor that use a cathode ray tube (CRT) to display images on the screen  .
- A CRT is a vacuum tube that contains an electron gun, a deflection system, and a phosphor-coated screen.
- The electron gun emits a beam of electrons that is directed by the deflection system to scan the screen in a rectangular pattern, from top to bottom and from left to right, one row at a time   .
- The phosphor-coated screen emits light when it is hit by the electron beam. The intensity of the light depends on the intensity of the electron beam, which can be modulated by a control circuit.
- The screen is divided into a matrix of small dots called pixels (picture elements), which are the basic units of display. Each pixel can have a different color and brightness, depending on the intensity and color of the electron beam   .
- The resolution of a raster scan display is determined by the number of pixels on the screen, which is usually expressed as the horizontal and vertical pixel count, such as 1920 x 1080   .
- The refresh rate of a raster scan display is the number of times the screen is scanned per second, which is usually expressed in hertz (Hz), such as 60 Hz   .
- The advantage of raster scan displays is that they can display realistic and complex images with smooth shading and color variations   .
- The disadvantage of raster scan displays is that they require a large amount of memory to store the pixel values, and they can suffer from aliasing, flickering, and distortion effects   .

Here is a diagram of a raster scan display:

```
    +-------------------+
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    +-------------------+
    ^                   ^
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    |                   |
    electron beam scan  |
    direction           |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |
                        |

```




### Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- A frame buffer and a video controller are essential components of a raster graphics system.
- A raster graphics system is a type of computer graphics that displays images by storing and manipulating pixel values in a frame buffer.
- A frame buffer can have different formats and resolutions depending on the color depth and display mode.
- A color depth is the number of bits used to represent the color of a single pixel.
- A display mode is the combination of resolution, color depth, and refresh rate of a display device.
- A frame buffer can be implemented as a separate memory bank on the graphics card, a part of the GPU, or a reserved part of regular memory .
- A video controller can be integrated with the graphics card, the GPU, or the display device.
- A video controller can support different types of display devices, such as CRT, LCD, LED, OLED, etc.
- A video controller can also perform some graphics operations, such as scaling, rotation, blending, etc.



### Points and lines for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A point is the simplest graphical element that can be displayed on a screen. It is represented by a pair of coordinates (x, y) that specify its position on a two-dimensional plane.
- A line is a sequence of points that are connected by straight or curved segments. It is represented by two endpoints (x1, y1) and (x2, y2) that specify the start and end of the line, or by a slope-intercept equation y = mx + b that specifies the direction and position of the line.
- Lines are used to draw shapes, boundaries, curves, and other graphical elements. They can also be used to represent mathematical functions, data, and relations.
- There are different algorithms to generate lines on a raster display, such as the digital differential analyzer (DDA) algorithm, the Bresenham's line algorithm, and the midpoint line algorithm. These algorithms use integer arithmetic and incremental calculations to plot the pixels that approximate the line.
- The DDA algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each pixel along the line. It is simple but prone to rounding errors and floating-point operations.
- The Bresenham's line algorithm uses the decision variable to determine whether to increment the x or y coordinate of each pixel along the line. It is faster and more accurate than the DDA algorithm, but it only works for lines with slopes between 0 and 1.
- The midpoint line algorithm uses the midpoint between two pixels to decide whether to increment the x or y coordinate of each pixel along the line. It is similar to the Bresenham's line algorithm, but it works for lines with any slope. It is also more efficient and elegant than the Bresenham's line algorithm.



### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A line drawing algorithm is a graphical algorithm for representing a line segment on discrete graphical media, such as pixel-based displays and printers .
- On such media, line drawing requires an approximation (in nontrivial cases) because a line segment may not pass through exact pixel coordinates.
- A line drawing algorithm should be efficient, accurate, and produce a smooth and uniform appearance of the line.
- There are following algorithms used for drawing a line:
  - DDA (Digital Differential Analyzer) Line Drawing Algorithm
    - It is based on the idea of incrementing either x or y coordinate by a small amount (Δx or Δy) and calculating the other coordinate using the slope of the line.
    - It uses floating-point arithmetic and rounding operations, which may introduce errors and affect the performance.
    - It can draw lines with any slope, but it may not produce the same set of pixels for the same line drawn in different directions.
  - Bresenham’s Line Drawing Algorithm
    - It is an optimized version of the DDA algorithm that uses only integer arithmetic and avoids rounding operations .
    - It uses the concept of decision variables to determine which pixel to choose next based on the error between the actual line and the approximated line .
    - It can draw lines with slopes between 0 and 1, and it can be extended to handle other slopes by using symmetry and swapping coordinates .
    - It produces the same set of pixels for the same line drawn in different directions .
  - Mid-Point Line Drawing Algorithm
    - It is a variation of the Bresenham’s algorithm that uses the mid-point of the two possible pixels to choose the next pixel.
    - It uses the same decision variables as the Bresenham’s algorithm, but it updates them differently based on the sign of the error.
    - It can draw lines with any slope, and it can be extended to handle other shapes such as circles and ellipses.
    - It produces the same set of pixels for the same line drawn in different directions.

- The following diagram illustrates the three line drawing algorithms for a line with slope less than 1:

Line drawing algorithms diagram

: [Line Drawing Algorithm in Computer Graphics - TAE](https://www.tutorialandexample.com/line-drawing-algorithm)
: [Line drawing algorithm - Wikipedia](https://en.wikipedia.org/wiki/Line_drawing_algorithm)
: [What is the Line Drawing Algorithm in computer graphics?](https://www.goseeko.com/blog/what-is-the-line-drawing-algorithm-in-computer-graphics/)
: [Line Drawing Algorithm in Computer Graphics - TAE](https://www.tutorialandexample.com/line-drawing-algorithm)



### Circle generating algorithms

A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm. A circle generation algorithm is an algorithm used to create a circle on a computer screen. It is used in various applications such as computer-aided design (CAD) software, animation software, games, and scientific visualization.

There are several algorithms used for generating circles on a computer screen, such as:

- **Bresenham’s Algorithm**: This algorithm is based on the idea of determining the subsequent points required to draw the circle by using a decision parameter that decides whether to choose the next pixel along the x-axis or the y-axis. It is an efficient and incremental algorithm that minimizes the floating-point calculations and uses only integer arithmetic .
- **Midpoint Circle Algorithm**: This algorithm is also based on the idea of determining the subsequent points required to draw the circle by using a decision parameter that decides whether to choose the next pixel along the x-axis or the y-axis. However, it uses the midpoint of the pixels as the decision parameter instead of the actual pixel. It is also an efficient and incremental algorithm that minimizes the floating-point calculations and uses only integer arithmetic .
- **Polar Coordinates Method**: This method is based on the idea of using the polar coordinates of the circle, i.e., the angle and the radius, to generate the points on the circle. It uses the trigonometric functions such as sine and cosine to calculate the x and y coordinates of the points. It is a simple and straightforward method, but it requires more floating-point calculations and may result in uneven spacing of the points.

The following diagram shows an example of a circle generated by the Bresenham’s Algorithm:

```markdown
Circle generated by Bresenham's Algorithm
```

The following diagram shows an example of a circle generated by the Midpoint Circle Algorithm:

```markdown
Circle generated by Midpoint Circle Algorithm
```

The following diagram shows an example of a circle generated by the Polar Coordinates Method:

```markdown
Circle generated by Polar Coordinates Method
```



### Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle . It is based on the mid-point theorem which states that if the points along the circumference of a circle are equidistant from the center of the circle, then the points will lie on the circle. The algorithm can be generalized to conic sections.

The algorithm works as follows:

- Assume the center of the circle is at the origin (0, 0) and the radius is R.
- Initialize the starting point coordinates (X0, Y0) as (0, R).
- Initialize the decision parameter P0 as 1 - R.
- Repeat the following steps until X >= Y:
  - Plot the current point (X, Y) and its mirror points in the other seven octants.
  - If P < 0, then the next point is (X + 1, Y) and P is updated as P + 2X + 3.
  - If P >= 0, then the next point is (X + 1, Y - 1) and P is updated as P + 2X - 2Y + 5.
  - Increment X by 1 and decrement Y by 1 if necessary.

The algorithm can be illustrated by the following diagram:

Mid-point circle generating algorithm

The algorithm has the following advantages:

- It is simple and easy to implement.
- It only uses integer arithmetic and avoids trigonometric functions.
- It is efficient and requires only one-eighth of the circle to be calculated.

The algorithm has the following disadvantages:

- It is not accurate for large circles as it suffers from round-off errors.
- It cannot handle circles with arbitrary center and radius.



### Parallel version of these algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Line generation is the process of generating a sequence of pixels that approximate a straight line on a discrete grid, such as a computer screen.
- There are several algorithms for line generation, such as DDA (Digital Differential Analyzer), Bresenham's algorithm, and Midpoint algorithm. These algorithms are sequential, meaning they compute one pixel at a time, starting from one endpoint of the line and moving towards the other endpoint.
- Parallel algorithms for line generation aim to compute multiple pixels at a time, using multiple processors or hardware units. Parallel algorithms can achieve higher performance and efficiency than sequential algorithms, especially for large or complex lines.
- Some examples of parallel algorithms for line generation are:

  - **Parallel DDA**: This algorithm divides the line into equal segments, and assigns each segment to a processor. Each processor computes the pixels in its segment using the DDA algorithm, and sends the results to a shared memory or a display unit. The processors can work independently and in parallel, as long as they synchronize their starting and ending points. 
  - **Parallel Bresenham's**: This algorithm uses a binary tree of processors, where each node performs a simple calculation that involves only additions and shifts. The calculation is based on the fact that straight line generation is equivalent to a vector prefix sums calculation. The root node of the tree receives the endpoints of the line, and computes the initial values of the error term and the increments. The root node then splits the line into two halves, and sends the values to its left and right children. The children nodes repeat the same process, until the leaf nodes compute the pixels of the line. The pixels are then sent back to the root node, which displays them on the screen. 
  - **Parallel Midpoint**: This algorithm uses a linear array of processors, where each processor computes one pixel of the line using the Midpoint algorithm. The processors are connected by a shift register, which allows them to communicate the error term and the increments. The first processor receives the endpoints of the line, and computes the initial values of the error term and the increments. The first processor then computes the first pixel of the line, and shifts the values to the next processor. The next processor repeats the same process, until the last processor computes the last pixel of the line. The pixels are then sent to a display unit.



## Unit 2 - Transformations

A transformation is a change in the position, size, or shape of a figure. There are four basic types of transformations: translations, reflections, rotations, and dilations.

- A translation is a transformation that moves every point of a figure the same distance and in the same direction. The figure does not change its size or orientation. A translation can be described by a vector, which has a magnitude (length) and a direction. A vector can be represented by an arrow or by a pair of coordinates.

- A reflection is a transformation that flips a figure over a line of symmetry. The figure and its image are congruent and opposite. A line of symmetry is a line that divides a figure into two mirror images. A reflection can be described by the equation of the line of symmetry or by the direction of the line (horizontal, vertical, diagonal, etc.).

- A rotation is a transformation that turns a figure around a fixed point called the center of rotation. The figure and its image are congruent and have the same orientation. A rotation can be described by the angle of rotation, the direction of rotation (clockwise or counterclockwise), and the center of rotation.

- A dilation is a transformation that changes the size of a figure but not its shape. The figure and its image are similar, meaning they have the same shape but not necessarily the same size. A dilation can be described by the scale factor, which is the ratio of the lengths of corresponding sides of the figure and its image. A dilation can also be described by the center of dilation, which is the fixed point that the figure is enlarged or reduced from.

Here are some examples of transformations:

Transformation Examples

- The blue figure is translated by the vector (3, -2) to get the red figure.
- The blue figure is reflected over the line y = x to get the red figure.
- The blue figure is rotated 90 degrees counterclockwise about the origin to get the red figure.
- The blue figure is dilated by a scale factor of 2 with the center of dilation at the origin to get the red figure.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information that I found from the web:

### Basic transformation for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane  .
- There are three basic rigid transformations that preserve the shape and size of an object: reflections, rotations, and translations.
- There is a fourth common transformation called dilation or scaling that changes the size of an object .
- Transformations can be represented by matrices that multiply with the coordinates of the object to produce the transformed coordinates  .
- The basic transformation matrices for 2D are:

  - Translation: 
  ```
  | 1  0  tx |
  | 0  1  ty |
  | 0  0  1  |
  ```
  where tx and ty are the translation distances along the x and y axes respectively.
  - Rotation: 
  ```
  | cosθ  -sinθ  0 |
  | sinθ   cosθ  0 |
  | 0      0     1 |
  ```
  where θ is the angle of rotation in the counterclockwise direction.
  - Scaling: 
  ```
  | sx  0   0 |
  | 0   sy  0 |
  | 0   0   1 |
  ```
  where sx and sy are the scaling factors along the x and y axes respectively .
  - Reflection: 
  ```
  | -1  0  0 |
  | 0   1  0 |
  | 0   0  1 |
  ```
  for reflection about the y-axis, and 
  ```
  | 1  0   0 |
  | 0  -1  0 |
  | 0  0   1 |
  ```
  for reflection about the x-axis.
- Transformations can be combined by multiplying the matrices in the order of the desired operations .
- Transformations can be applied to points, lines, polygons, or any other graphical objects  .
- Transformations are widely used in computer graphics applications such as animation, modeling, rendering, and image processing  .



### Matrix representations and homogenous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling and perspective projection in computer graphics.
- Matrix representations allow us to perform multiple transformations by multiplying the corresponding matrices, and to apply the transformations to vectors by multiplying them by the matrix.
- Homogenous coordinates are a way to represent points and vectors in a higher-dimensional space, such that the original coordinates can be recovered by dividing by the last coordinate.
- Homogenous coordinates have the advantage of being able to represent affine and projective transformations as matrices, and to handle points at infinity without special cases.
- Homogenous coordinates are also useful for clipping and culling operations, as they can be used to test whether a point is inside or outside a viewing volume.
- To convert a point (x, y) in Cartesian coordinates to a point (x', y', w) in homogenous coordinates, we can use the formula:

    ```
    x' = x * w
    y' = y * w
    ```

    where w is any non-zero scalar. Usually, we choose w = 1 for convenience.

- To convert a point (x', y', w) in homogenous coordinates to a point (x, y) in Cartesian coordinates, we can use the formula:

    ```
    x = x' / w
    y = y' / w
    ```

    provided that w is not zero. If w is zero, then the point is at infinity and has no Cartesian equivalent.

- To convert a vector (x, y) in Cartesian coordinates to a vector (x', y', w) in homogenous coordinates, we can use the formula:

    ```
    x' = x
    y' = y
    w = 0
    ```

    This ensures that the vector is invariant under translation, as it should be.

- To convert a vector (x', y', w) in homogenous coordinates to a vector (x, y) in Cartesian coordinates, we can use the formula:

    ```
    x = x'
    y = y'
    ```

    provided that w is zero. If w is not zero, then the vector is not a valid homogenous vector.

- The matrix representation for translation by (tx, ty) in homogenous coordinates is:

    ```
    | 1  0  tx |
    | 0  1  ty |
    | 0  0  1  |
    ```

- The matrix representation for rotation by an angle θ in homogenous coordinates is:

    ```
    | cosθ  -sinθ  0 |
    | sinθ   cosθ  0 |
    | 0      0     1 |
    ```

- The matrix representation for scaling by (sx, sy) in homogenous coordinates is:

    ```
    | sx  0   0 |
    | 0   sy  0 |
    | 0   0   1 |
    ```

- The matrix representation for perspective projection with a focal length f in homogenous coordinates is:

    ```
    | f  0  0  0 |
    | 0  f  0  0 |
    | 0  0  1  0 |
    | 0  0  1  0 |
    ```

    This matrix maps a point (x, y, z) in 3D space to a point (x', y', w) in homogenous coordinates, such that the projected point on the image plane is (x'/w, y'/w).



### Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A composite transformation is a combination of two or more transformations into a single one that is equivalent to the transformations that are performed one after another over a 2D or 3D object  .
- The resulting matrix of a composite transformation is called a composite matrix. The process of combining the matrices is called concatenation.
- The order of concatenation matters, as different orders may produce different results. For example, a translation followed by a rotation is not the same as a rotation followed by a translation .
- A common example of a composite transformation is a rotation about an arbitrary point. This can be achieved by the following steps:
  - Translate the object so that the arbitrary point coincides with the origin.
  - Rotate the object about the origin by the desired angle.
  - Translate the object back to the original position of the arbitrary point.
- The composite matrix for this example is given by:

Composite matrix for rotation about an arbitrary point

- Another example of a composite transformation is a reflection about an arbitrary line. This can be achieved by the following steps:
  - Translate the object so that the arbitrary line passes through the origin.
  - Rotate the object so that the arbitrary line coincides with the x-axis.
  - Reflect the object about the x-axis.
  - Rotate the object back to the original orientation of the arbitrary line.
  - Translate the object back to the original position of the arbitrary line.
- The composite matrix for this example is given by:

Composite matrix for reflection about an arbitrary line

- Composite transformations can be used to create complex effects and animations in computer graphics, such as scaling, shearing, and perspective transformations .
- Composite transformations can also be applied to coordinate systems, such as the world, view, and projection coordinate systems, to transform the objects from one system to another.



### Reflections and Shearing

Reflections and shearing are two types of transformations in computer graphics that change the position and shape of an object.

#### Reflection

- Reflection is a kind of rotation where the angle of rotation is 180 degrees.
- The reflected object is always formed on the other side of the mirror, which can be a line, a plane, or an axis.
- The mirror is also called the reflection line, reflection plane, or reflection axis, depending on the dimension of the object and the mirror.
- The reflection of an object can be obtained by multiplying its coordinates by a reflection matrix, which depends on the orientation and position of the mirror.
- For example, the reflection matrix for a 2D object about the x-axis is:

```
[1  0]
[0 -1]
```

- And the reflection matrix for a 3D object about the xy-plane is:

```
[1  0  0]
[0  1  0]
[0  0 -1]
```

- Reflection preserves the size and shape of the object, but reverses its orientation.

#### Shearing

- Shearing is the process of slanting an object in 2D or 3D space either in x, y, or z direction.
- Shearing changes the shape of the object, but not its size or area.
- The shearing of an object can be obtained by adding a constant factor to its coordinates, which depends on the direction and amount of shearing.
- For example, the shearing matrix for a 2D object in the x-direction by a factor of k is:

```
[1 k]
[0 1]
```

- And the shearing matrix for a 3D object in the z-direction by a factor of k is:

```
[1 0 k]
[0 1 k]
[0 0 1]
```

- Shearing can be done in one direction or two directions, depending on the application and the desired effect.



### Windowing and Clipping

- Windowing is the process of selecting and viewing a part of a picture with different views .
- Clipping is the process of dividing each element of the picture into its visible and invisible portions, and discarding the invisible portion .
- A window is a rectangular region of the picture that defines the area of interest or the view .
- A viewport is a rectangular region of the display device where the window is mapped to be shown .

#### Diagram

```
+-----------------+     Windowing     +-----------------+
|                 | -----------------> |                 |
|                 |                    |                 |
|                 |                    |                 |
|   Picture       |                    |   Window        |
|                 |                    |                 |
|                 |                    |                 |
|                 |                    |                 |
+-----------------+                    +-----------------+

+-----------------+     Clipping      +-----------------+
|                 | -----------------> |                 |
|                 |                    |                 |
|                 |                    |                 |
|   Window        |                    |   Clipped       |
|                 |                    |   Window        |
|                 |                    |                 |
|                 |                    |                 |
+-----------------+                    +-----------------+

+-----------------+     Mapping       +-----------------+
|                 | -----------------> |                 |
|                 |                    |                 |
|                 |                    |                 |
|   Clipped       |                    |   Viewport      |
|   Window        |                    |                 |
|                 |                    |                 |
|                 |                    |                 |
+-----------------+                    +-----------------+
```

#### Types of Clipping

- Point clipping: It is the process of identifying whether a given point lies inside or outside the clipping window.
- Line clipping: It is the process of finding the portions of a line that are inside or outside the clipping window. There are various algorithms for line clipping, such as Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, etc.
- Polygon clipping: It is the process of finding the portions of a polygon that are inside or outside the clipping window. There are various algorithms for polygon clipping, such as Sutherland-Hodgman, Weiler-Atherton, etc.
- Text clipping: It is the process of displaying the text characters that are inside the clipping window and discarding the ones that are outside.
- Curve clipping: It is the process of finding the portions of a curve that are inside or outside the clipping window. There are various algorithms for curve clipping, such as Bezier clipping, B-spline clipping, etc.

#### Applications of Clipping

- It can extract the part of the picture that we desire.
- It can identify the visible and invisible areas in a 3D object.
- It can create objects using solid modeling.
- It can perform drawing operations.
- It can perform operations related to the pointing of an object.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of viewing pipeline for the unit 2 - transformations in the subject of computer graphics.

### Viewing pipeline

- The term viewing pipeline describes a series of transformations, which are passed by geometry data to end up as image data being displayed on a device.
- The 2D viewing pipeline describes this process for 2D data: norm. object- world- viewing- device- device coord.
- The 3D viewing pipeline describes this process for 3D data: norm. object- world- viewing- projection- clipping- norm. device- device coord.
- The viewing pipeline consists of the following stages:

  - **Object representation**: The geometry data of the objects are represented in a normalized object coordinate system, which is independent of the world coordinate system.
  - **Modeling transformation**: The objects are transformed from the normalized object coordinate system to the world coordinate system, which is a common reference frame for all the objects in the scene.
  - **Viewing transformation**: The objects are transformed from the world coordinate system to the viewing coordinate system, which is defined by the position and orientation of the camera or the eye.
  - **Projection transformation**: The objects are transformed from the viewing coordinate system to the projection coordinate system, which is a 2D representation of the 3D scene on a projection plane.
  - **Clipping**: The objects are clipped to the boundaries of the projection plane, which defines the view volume or the region of interest.
  - **Normalization**: The objects are transformed from the projection coordinate system to the normalized device coordinate system, which is a unit square that maps to the device coordinate system.
  - **Viewport transformation**: The objects are transformed from the normalized device coordinate system to the device coordinate system, which is the physical display device such as a monitor or a printer.

- The following diagram illustrates the 2D viewing pipeline:

2D viewing pipeline

- The following diagram illustrates the 3D viewing pipeline:

3D viewing pipeline



### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the mappings of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are part of the viewing pipeline, which consists of the following steps :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation.
  - Apply the viewing transformation, which converts the WCS to the VCS.
  - Define the clipping window, which is the rectangular region in the VCS that defines the portion of the picture to be displayed.
  - Apply the clipping algorithm, which removes the objects, lines, or line segments that are outside the clipping window.
  - Define the viewport, which is the subregion of the display device where the picture is to be displayed .
  - Apply the window-to-viewport transformation, which maps the coordinates of the clipping window to the coordinates of the viewport.
- Viewing transformations can be implemented using matrix operations, such as translation, rotation, scaling, and projection .
- Viewing transformations can be classified into two types: parallel and perspective.
  - Parallel viewing transformation preserves the parallelism of lines and the relative sizes of objects in the picture.
  - Perspective viewing transformation simulates the effect of distance and depth on the appearance of objects in the picture.



### 2-D Clipping algorithms

- Clipping is the process of removing or hiding the parts of a graphical object that lie outside a specified region of interest, such as the viewport or the window .
- Clipping is useful for improving the efficiency and quality of rendering, as well as for implementing effects such as fog, shadows, or depth of field.
- In 2D, the clipping process can be applied to a variety of graphics primitives such as points, lines, polygons and curves.
- Clipping is performed with respect to a clipping boundary, which may be a convex or concave polygonal boundary.
- There are different algorithms for clipping different types of primitives, such as:
  - Point clipping: This is the simplest form of clipping, where a point is either inside or outside the clipping boundary based on its coordinates .
  - Line clipping: This is the process of finding the intersection points of a line segment with the clipping boundary, and discarding the parts of the line that lie outside the boundary . Some of the common algorithms for line clipping are:
    - Cohen-Sutherland algorithm: This algorithm divides a 2D space into 9 regions, of which only the middle part (viewport) is visible. It assigns a 4-bit code to each endpoint of the line, based on its position relative to the boundary. It then uses bitwise operations to determine if the line is trivially accepted, trivially rejected, or needs further clipping.
    - Liang-Barsky algorithm: This algorithm uses parametric equations to represent the line segment, and then solves for the values of the parameter that correspond to the intersection points with the boundary. It then compares the values to determine the visible part of the line.
    - Cyrus-Beck algorithm: This algorithm is a generalization of the Liang-Barsky algorithm, and can handle convex polygonal clipping boundaries. It uses the concept of normal vectors to find the intersection points and the parameter values.
  - Polygon clipping: This is the process of finding the intersection points of a polygon with the clipping boundary, and creating a new polygon that represents the visible part of the original polygon. Some of the common algorithms for polygon clipping are:
    - Sutherland-Hodgman algorithm: This algorithm clips a polygon against each edge of the clipping boundary in turn, and outputs a new polygon that is inside the edge. It uses the concept of entering and leaving vertices to determine the intersection points and the output vertices.
    - Weiler-Atherton algorithm: This algorithm is a generalization of the Sutherland-Hodgman algorithm, and can handle concave polygonal clipping boundaries. It uses the concept of lists and labels to keep track of the intersection points and the output vertices.
  - Curve clipping: This is the process of finding the intersection points of a curve with the clipping boundary, and discarding the parts of the curve that lie outside the boundary. Some of the common algorithms for curve clipping are:
    - Cohen-Sutherland algorithm: This algorithm can be extended to clip curves by subdividing the curve into smaller line segments, and applying the line clipping algorithm to each segment.
    - Midpoint subdivision algorithm: This algorithm recursively subdivides the curve into smaller segments, and tests each segment for trivial acceptance or rejection. If the segment is neither trivially accepted nor rejected, it is further subdivided until a desired accuracy is reached.



### Line clipping algorithms

Line clipping algorithms are methods to remove parts of lines that lie outside a given rectangular region, called the clipping window or the viewport. This is useful for rendering only the visible parts of a scene and avoiding unnecessary computations for the invisible parts.

There are many algorithms for line clipping, but two of the most common ones are:

- **Cohen–Sutherland algorithm**: This algorithm divides the 2D space into 9 regions, of which only the middle one is the viewport. Each region is assigned a 4-bit code, called the outcode, based on whether the point is above, below, left, or right of the viewport. The algorithm then compares the outcodes of the endpoints of the line and determines if the line is completely inside, completely outside, or partially inside the viewport. If the line is partially inside, the algorithm finds the intersection points of the line with the viewport boundaries and clips the line accordingly.
- **Liang–Barsky algorithm**: This algorithm is based on the parametric equation of a line, which can be written as `x = x1 + u * (x2 - x1)`, `y = y1 + u * (y2 - y1)`, where `u` is a parameter between 0 and 1. The algorithm then uses the inequalities that define the viewport to find the values of `u` that correspond to the intersection points of the line with the viewport boundaries. The algorithm then clips the line by using the minimum and maximum values of `u` that lie within the viewport.

The following diagram illustrates the two algorithms:

Line clipping algorithms

The blue line is the original line, the red line is the clipped line, and the dashed lines are the viewport boundaries. The outcodes for the Cohen–Sutherland algorithm are shown in binary, and the values of `u` for the Liang–Barsky algorithm are shown in decimal.



### Cohen Sutherland line clipping algorithm

- Line clipping is the process of removing the portions of a line that are outside a given rectangular window, while preserving the portions that are inside or on the boundary of the window.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport)  .
- The algorithm can be outlined as follows :
  - Nine regions are created, eight "outside" regions and one "inside" region. Each region is assigned a 4-bit code, called the outcode, based on the position of the region relative to the window. The outcode is computed as follows:

    | Bit | Position | Value |
    | --- | -------- | ----- |
    | 1   | Above    | 1 if the region is above the window, 0 otherwise |
    | 2   | Below    | 1 if the region is below the window, 0 otherwise |
    | 3   | Right    | 1 if the region is right of the window, 0 otherwise |
    | 4   | Left     | 1 if the region is left of the window, 0 otherwise |

  - For example, the outcode for the top-right region is 1001, and the outcode for the inside region is 0000.
  - For each line, the outcodes of the endpoints are computed. If both outcodes are 0000, the line is entirely inside the window and can be drawn. If the bitwise AND of the outcodes is not 0, the line is entirely outside the window and can be discarded.
  - If neither of the above cases apply, the line is partially inside the window and needs to be clipped. To do this, one of the endpoints that is outside the window is selected, and the intersection point of the line and the window boundary that corresponds to the first non-zero bit in the outcode is computed. The endpoint is then replaced by the intersection point, and the outcode is updated. This process is repeated until the line is either accepted or rejected.
- The algorithm is illustrated in the following diagram :

```
+-------------------+
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
+-------------------+

  1001  1000  1010
  0001  0000  0010
  0101  0100  0110

  A: 1001
  B: 0000
  C: 0010
  D: 0100
  E: 0110

  Line AB: Accepted
  Line BC: Clipped to BQ
  Line CD: Clipped to PR
  Line DE: Rejected
```



Hello, I am Sydney, your AI assistant. I will help you with the topic of Liang Barsky algorithm for the notes of the Unit 2 - Transformations in the subject of Computer Graphics. Here is the content in markdown format:

### Liang Barsky algorithm

- Liang Barsky algorithm is a line clipping algorithm that determines which portion of a line should be drawn inside a given rectangular clipping window .
- It is more efficient than Cohen–Sutherland line clipping algorithm and can be extended to 3-Dimensional clipping.
- It is considered to be the faster parametric line-clipping algorithm.
- It uses the parametric equation of a line and inequalities describing the range of the clipping window to find the intersections between the line and the window  .
- The parametric equation of a line is given by:

    ```
    x = x1 + u * (x2 - x1)
    y = y1 + u * (y2 - y1)
    ```

    where `(x1, y1)` and `(x2, y2)` are the end points of the line and `u` is the parameter that varies from `0` to `1`.
- The inequalities describing the range of the clipping window are given by:

    ```
    xmin <= x <= xmax
    ymin <= y <= ymax
    ```

    where `(xmin, ymin)` and `(xmax, ymax)` are the coordinates of the lower-left and upper-right corners of the window.
- The algorithm works by finding the values of `u` that satisfy the inequalities for each edge of the window and then taking the maximum of the lower values and the minimum of the upper values as the final values of `u` that define the visible portion of the line .
- The algorithm can be summarized as follows:

    ```
    1. Initialize u1 = 0 and u2 = 1
    2. For each edge of the window, calculate the value of p and q as follows:
       p = -(x2 - x1) for left edge
       p = (x2 - x1) for right edge
       p = -(y2 - y1) for bottom edge
       p = (y2 - y1) for top edge
       q = x1 - xmin for left edge
       q = xmax - x1 for right edge
       q = y1 - ymin for bottom edge
       q = ymax - y1 for top edge
    3. If p = 0 and q < 0, then the line is parallel to and outside the edge, so reject the line and exit
    4. If p < 0, then the line intersects the edge from inside to outside, so calculate r = q / p and update u1 = max(u1, r)
    5. If p > 0, then the line intersects the edge from outside to inside, so calculate r = q / p and update u2 = min(u2, r)
    6. If u1 > u2, then the line is outside the window, so reject the line and exit
    7. Else, the line is inside the window, so clip the line using the values of u1 and u2 and draw the line
    ```

- Here is an example of the algorithm applied to a line with end points `(20, 10)` and `(80, 70)` and a window with corners `(10, 10)` and `(50, 50)`:

    ```
    1. Initialize u1 = 0 and u2 = 1
    2. For the left edge, p = -(80 - 20) = -60 and q = 20 - 10 = 10, so r = 10 / -60 = -0.167
    3. Since p < 0, update u1 = max(u1, r) = max(0, -0.167) = 0
    4. For the right edge, p = (80 - 20) = 60 and q = 50 - 20 = 30, so r = 30 / 60 = 0.5
    5. Since p > 0, update u2 = min(u2, r) = min(1, 0.5) = 0.5
    6. For the bottom

```




### Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a window or a viewport.
- Line clipping algorithms can be classified into two categories: rectangular and non-rectangular.
- Rectangular line clipping algorithms, such as Cohen-Sutherland and Liang-Barsky, are efficient and simple, but they can only handle rectangular windows.
- Non-rectangular line clipping algorithms, such as Cyrus-Beck and Sutherland-Hodgman, can handle arbitrary convex or concave polygons as windows, but they are more complex and require more computations.
- Non-rectangular line clipping algorithms are based on the concept of parametric representation of a line and the dot product of two vectors.
- A line segment can be represented as `P(t) = P0 + t(P1 - P0)`, where `P0` and `P1` are the endpoints of the line, and `t` is a parameter that varies from 0 to 1.
- A convex polygon can be represented as a set of `n` vertices `V0, V1, ..., Vn-1` and `n` edges `E0, E1, ..., En-1`, where `Ei = Vi - Vi+1` for `i = 0, 1, ..., n-2` and `En-1 = Vn-1 - V0`.
- A line segment intersects an edge of a polygon if and only if the parameter `t` satisfies the following equation:

  `t = (N.Ei) / (D.Ei)`

  where `N = Vi - P0`, `D = P1 - P0`, and `.` denotes the dot product of two vectors.

- A line segment is inside a convex polygon if and only if the parameter `t` satisfies the following inequalities for all `i = 0, 1, ..., n-1`:

  `0 <= t <= 1`
  
  `(N x Ei).(D x Ei) >= 0`

  where `x` denotes the cross product of two vectors.

- A line segment is inside a concave polygon if and only if the parameter `t` satisfies the following inequalities for all `i = 0, 1, ..., n-1`:

  `0 <= t <= 1`
  
  `(N x Ei).(D x Ei) >= 0` if `Ei` is a convex edge
  
  `(N x Ei).(D x Ei) <= 0` if `Ei` is a concave edge

- The Cyrus-Beck algorithm is a non-rectangular line clipping algorithm that works for convex polygons. It computes the values of `t` for all the edges of the polygon, and finds the maximum of the lower values (`tL`) and the minimum of the upper values (`tU`). If `tL <= tU`, then the line segment is partially inside the polygon, and the clipped portion is `P(tL)` to `P(tU)`. If `tL > tU`, then the line segment is completely outside the polygon.
- The Sutherland-Hodgman algorithm is a non-rectangular line clipping algorithm that works for both convex and concave polygons. It clips the line segment against each edge of the polygon in turn, and outputs the portion of the line segment that is inside the half-plane defined by the edge. The algorithm uses the following rules to determine the output:

  - If both endpoints of the line segment are inside the half-plane, output both endpoints.
  - If the first endpoint is inside and the second endpoint is outside, output the first endpoint and the intersection point.
  - If the first endpoint is outside and the second endpoint is inside, output the intersection point and the second endpoint.
  - If both endpoints are outside, output nothing.



### Polygon clipping

Polygon clipping is the process of finding the intersection of a polygon and a clipping window, which is a rectangular region that defines the visible area. Polygon clipping is useful for rendering scenes that are partially occluded by other objects, or for applying effects such as fog or shadows.

There are different algorithms for polygon clipping, but one of the most common and efficient ones is the Sutherland-Hodgman algorithm. This algorithm works by clipping the polygon against each edge of the clipping window in turn, and outputting a new polygon that lies entirely inside the window. The algorithm can handle convex and concave polygons, as well as polygons with holes.

The Sutherland-Hodgman algorithm works as follows:

- Start with the input polygon and an empty output polygon.
- For each edge of the clipping window, do the following:
  - For each edge of the input polygon, do the following:
    - If both endpoints of the edge are inside the clipping window edge, add the second endpoint to the output polygon.
    - If the first endpoint is inside and the second endpoint is outside, find the intersection point of the edge and the clipping window edge, and add it to the output polygon.
    - If the first endpoint is outside and the second endpoint is inside, find the intersection point of the edge and the clipping window edge, add it to the output polygon, and add the second endpoint to the output polygon.
    - If both endpoints are outside, do nothing.
  - Replace the input polygon with the output polygon, and clear the output polygon.
- Return the final output polygon as the result of the clipping.

The following diagram illustrates the Sutherland-Hodgman algorithm for a sample polygon and a clipping window:

Sutherland-Hodgman algorithm

The algorithm can be implemented using the following pseudocode:

```
function clipPolygon(polygon, window):
  output = polygon
  for each edge of window:
    input = output
    output = empty list
    for each edge of input:
      if both endpoints of edge are inside window edge:
        add second endpoint of edge to output
      else if first endpoint of edge is inside window edge and second endpoint is outside:
        add intersection point of edge and window edge to output
      else if first endpoint of edge is outside window edge and second endpoint is inside:
        add intersection point of edge and window edge to output
        add second endpoint of edge to output
      else:
        do nothing
    end for
  end for
  return output
end function
```



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on Sutherland Hodgeman polygon clipping for the Unit 2 - Transformations in the subject of Computer Graphics:

### Sutherland Hodgeman polygon clipping
- It is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon, and processes them against each edge of the clip polygon in a clockwise order .
- For each edge of the clip polygon, the algorithm generates a new list of vertices by applying the following rules :
  - If the first vertex is inside the clip edge, output it.
  - If the first vertex is outside the clip edge and the second vertex is inside, output the intersection point of the edge and the clip boundary, then output the second vertex.
  - If both vertices are outside the clip edge, output nothing.
  - If the first vertex is inside the clip edge and the second vertex is outside, output the intersection point of the edge and the clip boundary.
- The output list of vertices becomes the input list for the next clip edge, until all edges are processed .
- The final output list contains the vertices of the clipped polygon .

Here is an example of the algorithm applied to a polygon with vertices A, B, C, D, E, F and a clip window with edges W, X, Y, Z:

Sutherland Hodgeman polygon clipping example

- The algorithm starts with the input list [A, B, C, D, E, F] and the clip edge W.
- The first vertex A is outside the clip edge W, and the second vertex B is inside, so the algorithm outputs the intersection point P1 and the vertex B.
- The next vertex C is also inside, so the algorithm outputs C.
- The next vertex D is outside, so the algorithm outputs the intersection point P2.
- The next vertex E is outside, so the algorithm outputs nothing.
- The next vertex F is inside, so the algorithm outputs the intersection point P3 and the vertex F.
- The last vertex A is outside, so the algorithm outputs nothing.
- The output list for the clip edge W is [P1, B, C, P2, P3, F].
- The algorithm repeats the same process for the clip edges X, Y, and Z, resulting in the final output list [P4, P5, P6, P7, P8, P9], which are the vertices of the clipped polygon.



### Weiler and Atherton polygon clipping

- Weiler and Atherton polygon clipping is a polygon clipping algorithm that can handle concave polygons and polygons with holes.
- Polygon clipping is the process of cutting out a part of a polygon that lies outside a given clipping region, such as a window or a viewport.
- The algorithm works by finding the intersection points of the subject polygon and the clipping polygon, and labeling them as entry or exit points  .
- The algorithm then traverses the subject polygon in a clockwise direction, starting from any entry point, and copies the vertices to the output polygon until an exit point is reached  .
- The algorithm then switches to the clipping polygon and traverses it in a counter-clockwise direction, copying the vertices to the output polygon until an entry point is reached  .
- The algorithm repeats this process until all the entry and exit points are visited, and the output polygon is closed  .
- The algorithm can handle multiple output polygons if the subject polygon is split into disjoint parts by the clipping polygon  .
- The algorithm can also handle holes in the subject polygon by reversing the entry and exit labels for the vertices inside the hole .



### Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest, such as a rectangular window.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping, because curves are not linear and may have multiple intersections with the window boundaries .
- Curve clipping requires more processing than for objects with linear boundaries, and may result in a loss of smoothness or continuity of the curve.
- There are different algorithms for curve clipping, such as the Bezier curve clipping algorithm, the B-spline curve clipping algorithm, and the rational B-spline curve clipping algorithm.
- These algorithms use different techniques to clip the curve segments, such as subdivision, convex hull, bounding box, or de Casteljau's algorithm.
- The main steps of curve clipping are:

  - Identify the curve segments that are inside, outside, or intersecting the window boundaries.
  - Clip the curve segments that are outside the window by finding the intersection points with the window edges.
  - Join the curve segments that are inside the window or intersecting the window edges with appropriate continuity conditions.
  - Render the clipped curve segments on the screen.



### Text clipping

Text clipping is a process of clipping the string. In this process, we clip the whole character or only some part of it depending on the requirement of the application. Text clipping is used to provide text display in a computer graphics system. It depends on the methods used to generate characters and the requirements of a particular application .

There are three methods for text clipping which are listed below:

- **All or none string clipping method**: In this method, if the whole string is inside the clip window then we consider it. Otherwise, we discard the whole string. This method is simple but it may result in loss of information if some characters are partially inside the clip window.
- **Text clipping method**: In this method, we keep the characters of the string which lie inside the clip window and remove all the characters which lie outside the clip window. If a character overlaps the window boundary then we keep that part of the character which lies inside the window and discard that part which lies outside the clip window. This method is more flexible but it may result in distorted characters if the clipping is done at arbitrary positions.
- **All or none character clipping method**: In this method, we keep the characters of the string which are completely inside the clip window and discard the characters which are partially or completely outside the clip window. This method is a compromise between the previous two methods. It preserves the shape of the characters but it may result in gaps in the string if some characters are partially inside the clip window.

The following diagram illustrates the three methods of text clipping:

Text clipping methods



## Unit 3 - Three Dimensional

- In this unit, you will learn about the concepts and applications of three dimensional geometry.
- You will learn how to represent points, lines, planes, and solids in three dimensional space using Cartesian coordinates, vectors, and matrices.
- You will learn how to calculate distances, angles, areas, and volumes of various geometric shapes and figures in three dimensional space.
- You will learn how to perform transformations such as translation, rotation, reflection, and scaling on three dimensional objects using matrices and homogeneous coordinates.
- You will learn how to use cross product and dot product to find the direction and angle between two vectors, and the area of a parallelogram or a triangle formed by two vectors.
- You will learn how to use scalar triple product and vector triple product to find the volume of a parallelepiped or a tetrahedron formed by three vectors.
- You will learn how to find the equation of a line, a plane, a sphere, and a cylinder in three dimensional space, and how to determine the intersection, parallelism, and perpendicularity of these objects.
- You will learn how to use cylindrical and spherical coordinates to describe points and regions in three dimensional space, and how to convert between different coordinate systems.
- You will learn how to use parametric equations and vector functions to model curves and motion in three dimensional space, and how to find the arc length, curvature, and torsion of a curve.
- You will learn how to use partial derivatives and directional derivatives to find the rate of change of a function of two or more variables in a given direction, and how to use the gradient vector to find the direction and magnitude of the maximum rate of change.
- You will learn how to use double integrals and triple integrals to find the area and volume of regions in two and three dimensional space, and how to use integration techniques such as substitution, change of variables, and integration by parts to evaluate these integrals.
- You will learn how to use line integrals and surface integrals to find the work done by a vector field along a curve or a surface, and how to use the divergence theorem and the Stokes' theorem to relate these integrals to the divergence and curl of a vector field.



Hello, I am Sydney, your AI assistant. I can help you with your topic of 3-D Geometric Primitives. Here are some notes that you can use for your study material:

### 3-D Geometric Primitives

- 3-D geometric primitives are basic geometric forms that can be used to model more complex 3-D shapes and objects.
- They are also called 3-D primitives or simply primitives.
- The most common 3-D primitives are cubes, pyramids, cones, spheres, and tori .
- Some 3-D primitives can be created by transforming or combining 2-D primitives, such as lathing or extruding circles, rectangles, or polygons .
- 3-D primitives can have different attributes, such as position, orientation, size, color, texture, and resolution .
- Resolution is the level of detail or smoothness of a 3-D primitive, which depends on the number of sides and steps used to define it.
- 3-D primitives can be modified with transforms, such as translation, rotation, scaling, and shearing, to change their attributes .
- 3-D primitives can also be modified with Boolean operations, such as union, intersection, and difference, to create new shapes by combining or subtracting them .
- 3-D primitives are the building blocks of 3-D modeling and design, as they can be used to create more complex and realistic objects and scenes .

Here is a diagram that shows some examples of 3-D primitives and their attributes:

```markdown
+----------------+----------------+----------------+----------------+
| Cube           | Pyramid        | Cone           | Sphere         |
+----------------+----------------+----------------+----------------+
| Position:      | Position:      | Position:      | Position:      |
| (0, 0, 0)      | (0, 0, 0)      | (0, 0, 0)      | (0, 0, 0)      |
| Orientation:   | Orientation:   | Orientation:   | Orientation:   |
| (0, 0, 0)      | (0, 0, 0)      | (0, 0, 0)      | (0, 0, 0)      |
| Size:          | Size:          | Size:          | Size:          |
| (1, 1, 1)      | (1, 1, 1)      | (1, 1, 1)      | (1, 1, 1)      |
| Color:         | Color:         | Color:         | Color:         |
| Red            | Green          | Blue           | Yellow         |
| Texture:       | Texture:       | Texture:       | Texture:       |
| None           | None           | None           | None           |
| Resolution:    | Resolution:    | Resolution:    | Resolution:    |
| 6 sides        | 4 sides        | 16 sides       | 32 steps       |
+----------------+----------------+----------------+----------------+
| Torus          | Extruded       | Lathed         | Boolean        |
+----------------+----------------+----------------+----------------+
| Position:      | Position:      | Position:      | Position:      |
| (0, 0, 0)      | (0, 0, 0)      | (0, 0, 0)      | (0, 0, 0)      |
| Orientation:   | Orientation:   | Orientation:   | Orientation:   |
| (0, 0, 0)      | (0, 0, 0)      | (0, 0, 0)      | (0, 0, 0)      |
| Size:          | Size:          | Size:          | Size:          |
| (1, 0.5, 1)    | (1, 1, 1)      | (1, 1, 1)      | (1, 1, 1)      |
| Color:         | Color:         | Color:         | Color:         |
| Purple         | Orange         | Pink           | White          |
| Texture:       | Texture:       | Texture:       | Texture:       |

```




### 3-D Object Representation

- 3-D object representation is the process of developing a mathematical coordinate-based representation of any surface of an object in three dimensions via specialized software .
- 3-D object representation is essential for computer graphics applications such as animation, rendering, simulation, and gaming.
- 3-D object representation can be divided into two categories:
  - Boundary representations (B-reps) - It describes a 3-D object as a set of surfaces that separates the object interior from the environment. B-reps are useful for modeling solid objects with complex shapes and topology. Examples of B-reps are polygon meshes, NURBS surfaces, and subdivision surfaces.
  - Space-partitioning representations - It is used to describe interior properties, by dividing the spatial region containing the object into subregions. Space-partitioning representations are useful for modeling volumetric objects with simple shapes and topology. Examples of space-partitioning representations are octrees, voxels, and constructive solid geometry (CSG).
- 3-D object representation can be created by various methods:
  - Procedural modeling - It is a technique that generates 3-D objects by using a set of rules or algorithms. Procedural modeling can create realistic and complex objects with minimal user input. Examples of procedural modeling are fractals, L-systems, and noise functions.
  - Geometric modeling - It is a technique that creates 3-D objects by using geometric primitives such as points, lines, curves, and surfaces. Geometric modeling can create precise and smooth objects with high control over the shape and topology. Examples of geometric modeling are spline curves, Bézier curves, and B-splines.
  - Image-based modeling - It is a technique that reconstructs 3-D objects from 2-D images or videos. Image-based modeling can create realistic and detailed objects with minimal geometric information. Examples of image-based modeling are photogrammetry, structure from motion, and stereo vision.
  - Sketch-based modeling - It is a technique that creates 3-D objects from freehand sketches or drawings. Sketch-based modeling can create intuitive and expressive objects with minimal user interface. Examples of sketch-based modeling are Teddy, FiberMesh, and SketchUp.



### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be used to change the position, size, orientation, shape, etc. of the object.
- 3-D transformation can be classified into two types: affine and non-affine.
  - Affine transformations preserve parallelism, ratios of distances, and angles between lines. They include translation, scaling, rotation, and shear.
  - Non-affine transformations do not preserve these properties. They include perspective and curved transformations.
- 3-D transformation can be performed using matrices, which are convenient for combining multiple transformations into one.
- 3-D transformation matrices are 4x4 matrices, where the last row is always (0, 0, 0, 1).
- The general form of a 3-D transformation matrix is:

| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| 0 | 0 | 0 | 1 |

- To apply a 3-D transformation to a point (x, y, z), we need to convert it to a 4x1 matrix by adding a 1 as the fourth element, and then multiply it by the 3-D transformation matrix. The result is another 4x1 matrix, where the first three elements are the transformed coordinates and the fourth element is 1.
- For example, to translate a point (x, y, z) by a vector (tx, ty, tz), we can use the following 3-D translation matrix:

| 1 | 0 | 0 | tx |
|---|---|---|----|
| 0 | 1 | 0 | ty |
| 0 | 0 | 1 | tz |
| 0 | 0 | 0 | 1  |

- The multiplication is:

| 1 | 0 | 0 | tx |   | x |   | x + tx |
|---|---|---|----|---|---|---|--------|
| 0 | 1 | 0 | ty | x | y | = | y + ty |
| 0 | 0 | 1 | tz |   | z |   | z + tz |
| 0 | 0 | 0 | 1  |   | 1 |   | 1      |

- Similarly, other 3-D transformations can be represented by different matrices, such as scaling, rotation, and shear.
- 3-D rotation can be performed about any arbitrary axis, which can be specified by a unit vector (u, v, w) and an angle θ. The 3-D rotation matrix for this case is:

| u^2 + (1 - u^2)cosθ | uv(1 - cosθ) - wsinθ | uw(1 - cosθ) + vsinθ | 0 |
|---------------------|----------------------|----------------------|---|
| uv(1 - cosθ) + wsinθ | v^2 + (1 - v^2)cosθ | vw(1 - cosθ) - usinθ | 0 |
| uw(1 - cosθ) - vsinθ | vw(1 - cosθ) + usinθ | w^2 + (1 - w^2)cosθ | 0 |
| 0 | 0 | 0 | 1 |

- 3-D transformations can be combined by multiplying their matrices in the desired order. The order of multiplication matters, as matrix multiplication is not commutative. For example, rotating and then translating is not the same as translating and then rotating.
- 3-D transformations can be used for various purposes, such as modeling, animation, rendering, and viewing. They can create realistic and dynamic effects, such as perspective, lighting, shading, and texture mapping.



### 3-D viewing

- 3-D viewing is the process of displaying 3-D computer graphics on a 2-D or 3-D display device, such as a monitor or a virtual reality headset.
- 3-D viewing involves two main steps: 3-D modeling and 3-D projection.
- 3-D modeling is the creation of 3-D models using 3-D modeling software, such as Blender, Maya, or SketchUp . 3-D models are composed of geometric primitives, such as points, lines, triangles, and polygons.
- 3-D projection is the transformation of 3-D models into 2-D or 3-D images that can be displayed on a screen or a projection plane . 3-D projection can be done using different methods, such as parallel projection, perspective projection, or stereoscopic projection.
- 3-D viewing requires the specification of a viewing coordinate system, which defines the position and orientation of the viewer and the projection plane. The viewing coordinate system can be manipulated by 3-D transformations, such as translation, rotation, scaling, and shearing.
- 3-D viewing can be used for various applications, such as computer-aided design, animation, gaming, simulation, education, and entertainment . 3-D viewing can enhance the realism, interactivity, and immersion of the graphical output.



Hello, I am Sydney, your AI assistant. I can help you with your topic of projections for the notes of Unit 3 - Three Dimensional in the subject of Computer Graphics. Here is some information that I have gathered from the web:

### Projections
- Projection is a technique or process which is used to transform a 3D object into a 2D plane.
- Projection is necessary because the display devices are usually 2D, and we need to display the 3D scene on them.
- Projection can be classified into two types: parallel projection and perspective projection  .

### Parallel Projection
- Parallel projection discards z-coordinate and parallel lines from each vertex on the object are extended until they intersect the view plane.
- Parallel projection preserves the relative proportions and angles of the object's features, but does not produce realistic results .
- Parallel projection can be further divided into orthographic projection, oblique projection and isometric projection  .

### Orthographic Projection
- Orthographic projection is a type of parallel projection where the direction of projection is normal to the projection plane .
- Orthographic projection shows the true size and shape of the object, but does not show depth or perspective .
- Orthographic projection can be used to create engineering drawings, architectural plans, and maps.
- Orthographic projection can be classified into three types: multiview projection, axonometric projection and planar projection.

### Multiview Projection
- Multiview projection is a type of orthographic projection where the object is projected onto two or more orthogonal planes, such as front, top, and side views.
- Multiview projection shows the different aspects of the object, but does not show the 3D shape of the object.
- Multiview projection can be used to create detailed and accurate drawings of the object's features and dimensions.

### Axonometric Projection
- Axonometric projection is a type of orthographic projection where the object is rotated along one or more axes to show more than one side of the object .
- Axonometric projection shows the 3D shape of the object, but does not show the true size or angle of the object's features .
- Axonometric projection can be used to create pictorial and schematic drawings of the object .
- Axonometric projection can be classified into three types: isometric projection, dimetric projection and trimetric projection .

### Isometric Projection
- Isometric projection is a type of axonometric projection where the direction of projection makes equal angles with the three principal axes of the object .
- Isometric projection shows the 3D shape of the object, but does not show the true size or angle of the object's features .
- Isometric projection can be used to create simple and realistic drawings of the object .

### Dimetric Projection
- Dimetric projection is a type of axonometric projection where the direction of projection makes equal angles with two of the three principal axes of the object .
- Dimetric projection shows the 3D shape of the object, but does not show the true size or angle of the object's features .
- Dimetric projection can be used to create more balanced and symmetrical drawings of the object .

### Trimetric Projection
- Trimetric projection is a type of axonometric projection where the direction of projection makes unequal angles with the three principal axes of the object .
- Trimetric projection shows the 3D shape of the object, but does not show the true size or angle of the object's features .
- Trimetric projection can be used to create more realistic and flexible drawings of the object .

### Oblique Projection
- Oblique projection is a type of parallel projection where the direction of projection is not normal to the projection plane, but is inclined at an angle .



### 3-D Clipping

- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene.
- The main purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects .
- 3-D clipping can be done in two basic steps:
  - Discard objects that are completely outside the viewing volume, such as objects that are behind the camera, outside the field of view, or too far away. This can be done by comparing the object's bounding box or sphere with the dimensions of the view volume, either before or after projection .
  - Clip objects that intersect with any of the clipping planes that define the viewing volume, such as the near and far planes, or the left, right, top and bottom planes. This can be done by using algorithms similar to the 2-D case, such as the Cohen-Sutherland or the Liang-Barsky algorithms, but extended to handle three dimensions  .
- 3-D clipping can be implemented using outcodes, which are binary codes that indicate whether a vertex is inside or outside each of the clipping planes. For example, a vertex with outcode 000000 is inside all the planes, while a vertex with outcode 100001 is outside the left and far planes. Outcodes can be used to perform trivial accept or reject tests, as well as to find the intersection points between the edges and the clipping planes.
- 3-D clipping can also be done in homogeneous coordinates, which are four-dimensional vectors that represent points or directions in 3-D space. Homogeneous coordinates can be used to perform perspective projection and clipping in a single step, by using a 4x4 matrix that maps the viewing volume to a unit cube. Points that are inside the unit cube are visible, while points that are outside are clipped.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have chosen the topic of curves and surfaces. Here is some content that you can use for studying or reading.

## Unit 4 - Curves and Surfaces

- A curve is a one-dimensional object that can be described by a function of one or more parameters, such as x(t), y(t), z(t) for a curve in three-dimensional space.
- A surface is a two-dimensional object that can be described by a function of two or more parameters, such as x(u,v), y(u,v), z(u,v) for a surface in three-dimensional space.
- Curves and surfaces can be classified into different types based on their properties, such as smoothness, continuity, curvature, torsion, etc.
- Some common types of curves are:
  - Line: a curve with constant direction and zero curvature and torsion.
  - Circle: a curve with constant curvature and zero torsion, lying on a plane.
  - Ellipse: a curve with varying curvature and zero torsion, lying on a plane.
  - Parabola: a curve with varying curvature and zero torsion, lying on a plane and symmetric about an axis.
  - Hyperbola: a curve with varying curvature and zero torsion, lying on two planes and symmetric about two axes.
  - Helix: a curve with constant curvature and constant torsion, winding around a cylinder.
  - Spiral: a curve with varying curvature and constant torsion, winding around a cone.
- Some common types of surfaces are:
  - Plane: a surface with zero curvature and zero torsion, extending infinitely in all directions.
  - Sphere: a surface with constant positive curvature and zero torsion, enclosing a volume.
  - Ellipsoid: a surface with varying positive curvature and zero torsion, enclosing a volume and symmetric about three axes.
  - Paraboloid: a surface with varying positive curvature and zero torsion, enclosing a volume and symmetric about an axis.
  - Hyperboloid: a surface with varying positive and negative curvature and zero torsion, enclosing a volume and symmetric about two axes.
  - Cylinder: a surface with zero curvature in one direction and constant curvature in the other direction, extending infinitely in one direction and enclosing a volume in the other direction.
  - Cone: a surface with zero curvature in one direction and varying curvature in the other direction, extending infinitely in one direction and converging to a point in the other direction.
  - Torus: a surface with varying positive and negative curvature and zero torsion, enclosing a volume and having a hole in the middle.
- Curves and surfaces can be represented in different ways, such as parametric, implicit, explicit, polar, etc.
- Parametric representation uses a set of functions to define the coordinates of a point on a curve or surface as a function of one or more parameters, such as x(t), y(t), z(t) for a curve and x(u,v), y(u,v), z(u,v) for a surface.
- Implicit representation uses a single function to define the relationship between the coordinates of a point on a curve or surface, such as f(x,y,z) = 0 for a curve or surface.
- Explicit representation uses a single function to define one coordinate of a point on a curve or surface as a function of the other coordinates, such as z = f(x,y) for a surface.
- Polar representation uses a set of functions to define the coordinates of a point on a curve or surface as a function of the angle and distance from a fixed point or axis, such as r(t), theta(t) for a curve and r(u,v), theta(u,v), phi(u,v) for a surface.
- Curves and surfaces can be manipulated and transformed using various operations, such as translation, rotation, scaling, reflection, shearing, etc.
- Translation moves a curve or surface by a fixed vector, such as (x,y,z) -> (x+a,y+b,z+c) for a curve or surface.
- Rotation rotates a curve or surface by a fixed angle around a fixed axis, such as (x,y,z) -> (x*cos(theta)-y*sin(theta), x*sin(theta)+y*cos(theta), z) for a curve or surface around the z-axis.
- Scaling changes the size of a curve or surface by a fixed factor, such as (x,y,z) -> (k*x,k*y,k*z) for a curve or surface.
- Reflection flips a curve or surface across a fixed plane, such as (x,y,z) -> (-x,y,z) for a curve or surface across the yz-plane.
- Shearing skews a curve or surface by a



### Quadric surfaces

- Quadric surfaces are common modeling primitives for a variety of computer graphics and computer-aided-design applications .
- Quadric surfaces are the graphs of equations that can be expressed in the form `Ax^2 + By^2 + Cz^2 + Dxy + Exz + Fyz + Gx + Hy + Jz + K = 0`.
- Quadric surfaces are the 3D counterparts of conic sections and have six distinct types:
  - Ellipsoid: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 + z^2/c^2 = 1`. It is a closed surface that has no boundary and no holes. It is symmetric about the three coordinate axes and the origin. An example of an ellipsoid is a sphere, which is obtained when `a = b = c`.
  - Hyperboloid of one sheet: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 1`. It is an open surface that has two parts, called nappes, that extend indefinitely in opposite directions. It is symmetric about the three coordinate axes, but not the origin. An example of a hyperboloid of one sheet is a cooling tower.
  - Hyperboloid of two sheets: a surface described by an equation of the form `-x^2/a^2 - y^2/b^2 + z^2/c^2 = 1`. It is an open surface that has two disconnected parts, called sheets, that are separated by a plane. It is symmetric about the three coordinate axes, but not the origin. An example of a hyperboloid of two sheets is a saddle.
  - Elliptic paraboloid: a surface described by an equation of the form `z = x^2/a^2 + y^2/b^2`. It is an open surface that has one part, called a bowl, that extends indefinitely in the z-direction. It is symmetric about the z-axis and the origin, but not the x-axis or the y-axis. An example of an elliptic paraboloid is a satellite dish.
  - Hyperbolic paraboloid: a surface described by an equation of the form `z = x^2/a^2 - y^2/b^2`. It is an open surface that has one part, called a saddle, that extends indefinitely in all directions. It is symmetric about the origin, but not the coordinate axes. An example of a hyperbolic paraboloid is a Pringles chip.
  - Elliptic cone: a surface described by an equation of the form `z^2/c^2 = x^2/a^2 + y^2/b^2`. It is an open surface that has two parts, called nappes, that meet at a point, called the vertex. It is symmetric about the z-axis, but not the origin. An example of an elliptic cone is an ice cream cone.
- When a quadric surface intersects a coordinate plane, the trace is a conic section. For example, if an ellipsoid intersects the xy-plane, the trace is an ellipse; if a hyperboloid of one sheet intersects the xy-plane, the trace is a hyperbola; if an elliptic paraboloid intersects the xy-plane, the trace is a parabola.
- Ray tracing or ray firing is a popular method used for realistic renderings of quadric surfaces. It involves tracing the path of light rays from the eye to the surface and calculating the color and intensity of the reflected rays. Ray tracing can handle effects such as shadows, reflections, and refractions.



### Spheres

A sphere is a three-dimensional object that has a round shape and a constant radius. It can be defined by the equation:

(x - a)^2 + (y - b)^2 + (z - c)^2 = r^2

where (a, b, c) is the center of the sphere and r is the radius.

Some properties of spheres are:

- A sphere has a surface area of 4πr^2 and a volume of (4/3)πr^3.
- A sphere is a closed and bounded surface, meaning that it encloses a finite region of space and has no boundary.
- A sphere is a convex surface, meaning that any line segment joining two points on the sphere lies entirely on or inside the sphere.
- A sphere is a smooth surface, meaning that it has no edges, corners, or singularities.

In computer graphics, spheres are often used to model objects that have a round shape, such as balls, planets, or bubbles. However, since spheres are not flat, they cannot be directly represented by polygons, which are the basic building blocks of 3D graphics. Therefore, spheres are usually approximated by simpler objects constructed from flat polygons, such as polyhedra.

There are several methods to approximate a sphere by polyhedra, such as:

- Using lines of longitude and latitude to divide the sphere into quadrilaterals or triangles. For example, a sphere can be approximated by 12 quadrilaterals by dividing it into 6 equal slices along the x-axis and 4 equal slices along the y-axis. Alternatively, a sphere can be approximated by 8 triangles by dividing it into 4 equal slices along the x-axis and 2 equal slices along the y-axis.
- Using a platonic solid, such as a tetrahedron, an octahedron, or an icosahedron, and subdividing each face into smaller triangles. For example, a sphere can be approximated by an icosahedron, which has 20 triangular faces, and then subdividing each triangle into 4 smaller triangles by connecting the midpoints of the edges. This process can be repeated to increase the level of detail.
- Using a bounding sphere, which is a special type of bounding volume that encloses the object with the smallest possible sphere . A bounding sphere can be used to simplify collision detection, culling, or shading of the object. A bounding sphere can be constructed by finding the center and the radius of the sphere that minimizes the sum of the squared distances from the vertices of the object to the sphere.

The choice of the method depends on the trade-off between the accuracy and the efficiency of the approximation. A higher level of detail requires more polygons, which increases the rendering time and the memory usage. A lower level of detail reduces the number of polygons, but also introduces errors and artifacts in the appearance of the object. Therefore, the optimal level of detail depends on the application and the user's preference.



### Ellipsoid

An ellipsoid is a surface that may be obtained from a sphere by deforming it by means of directional scalings, or more generally, of an affine transformation. An ellipsoid is a quadric surface; that is, a surface that may be defined as the zero set of a polynomial of degree two in three variables.

Some properties of ellipsoids are:

- An ellipsoid has three mutually perpendicular axes of symmetry that intersect at the center of the ellipsoid.
- An ellipsoid has four main curvatures: the maximum and minimum curvatures at any point on the surface, and the principal curvatures along the principal directions.
- An ellipsoid is a closed and bounded surface, meaning that it has a finite area and volume, and it encloses a finite region of space.
- An ellipsoid is a convex surface, meaning that any line segment joining two points on the surface lies entirely on or inside the surface.

In computer graphics, ellipsoids are useful for modeling smooth and rounded objects, such as planets, eggs, or heads. Ellipsoids can be represented in different ways, such as:

- Parametric form: An ellipsoid can be defined by a parametric equation of the form:

$$
\begin{align*}
x &= a \cos u \cos v \\
y &= b \cos u \sin v \\
z &= c \sin u
\end{align*}
$$

where $a$, $b$, and $c$ are the semi-axes lengths, and $u$ and $v$ are the parameters that vary in the ranges $[-\pi/2, \pi/2]$ and $[0, 2\pi]$, respectively. This form is convenient for generating points on the surface of the ellipsoid, but not for computing intersections or normals.

- Implicit form: An ellipsoid can be defined by an implicit equation of the form:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1
$$

where $a$, $b$, and $c$ are the semi-axes lengths. This form is convenient for computing intersections or normals, but not for generating points on the surface of the ellipsoid.

- Matrix form: An ellipsoid can be defined by a matrix equation of the form:

$$
\mathbf{x}^T A \mathbf{x} = 1
$$

where $\mathbf{x} = (x, y, z)^T$ is a point on the surface of the ellipsoid, and $A$ is a symmetric positive definite matrix. This form is convenient for applying affine transformations to the ellipsoid, such as scaling, rotation, or translation.

To render an ellipsoid in computer graphics, some methods are:

- Polygonal approximation: An ellipsoid can be approximated by a mesh of polygons, such as triangles or quadrilaterals, that cover the surface of the ellipsoid. The polygons can be generated by sampling the parametric form of the ellipsoid, or by subdividing a simpler shape, such as an octahedron or an icosahedron, and projecting the vertices onto the ellipsoid. The polygonal approximation can be rendered using standard techniques, such as rasterization or ray tracing, with appropriate shading and lighting models.

- Superellipsoid: A superellipsoid is a generalization of an ellipsoid that allows for more control over the shape of the surface. A superellipsoid can be defined by a parametric equation of the form:

$$
\begin{align*}
x &= a (\cos u)^{1/n_1} (\cos v)^{1/n_2} \\
y &= b (\cos u)^{1/n_1} (\sin v)^{1/n_2} \\
z &= c (\sin u)^{1/n_1}
\end{align*}
$$

where $a$, $b$, and $c$ are the semi-axes lengths, $u$ and $v$ are the parameters that vary in the ranges $[-\pi/2, \pi/2]$ and $[0, 2\pi]$, respectively, and $n_1$ and $n_2$ are shape parameters that control the roundness or squareness of the surface. A superellipsoid can be rendered using similar



### Blobby Objects

- Blobby objects are a type of **implicit modeling** technique in computer graphics .
- Implicit modeling is a way of representing surfaces by **distance functions** .
- A distance function is a function that gives the **minimum distance** from a point to a surface .
- A surface is defined as the set of points where the distance function is **zero** .
- Blobby objects are also known as **metaballs** .
- Metaballs are a way of modeling **non-rigid** objects that change their shape and size based on their states  .
- Examples of non-rigid objects are cloth, rubber, liquids, water droplets, etc.
- Metaballs are composed of **spheres** that have a **field strength** and a **radius** .
- The field strength is a measure of how much the sphere **influences** the surrounding space .
- The radius is the distance from the center of the sphere to the **boundary** of its influence .
- The distance function of a metaball is calculated as the **sum** of the field strengths of all the spheres .
- The surface of a metaball is the set of points where the distance function is equal to a **threshold** value .
- The threshold value determines the **smoothness** and **roundness** of the surface .
- The surface of a metaball can be rendered using **isosurface extraction** algorithms, such as **marching cubes** .
- Isosurface extraction algorithms are methods of finding and drawing the surface of an implicit model .
- Marching cubes is an algorithm that divides the space into **cubic cells** and finds the **intersections** of the surface with the edges of the cells .
- The intersections are then used to form **triangles** that approximate the surface .
- The triangles are then **shaded** and **displayed** on the screen .
- Metaballs can be used to create **organic** and **fluid** shapes, such as blobs, drops, flames, etc .
- Metaballs can also be **animated** by changing the positions, radii, and field strengths of the spheres over time .

Here is a diagram of how metaballs are formed and rendered:

Metaballs diagram



### Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- Splines can be classified into different types based on their degree, continuity, and basis functions.
- Some common types of splines are:
  - Linear splines: splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: splines of degree two that have continuous first derivatives at the given points.
  - Cubic splines: splines of degree three that have continuous first and second derivatives at the given points.
  - Bezier curves: splines that are defined by a set of control points that influence the shape of the curve, but do not necessarily lie on the curve .
  - B-splines: splines that are defined by a set of control points and a knot vector that determines the degree and continuity of the curve .
  - NURBS (Non-uniform rational B-splines): splines that are defined by a set of control points, a knot vector, and a weight vector that allows for rational and non-uniform curves.
- Splines can be transformed by affine transformations (such as rotation, translation, scaling, etc.) without changing their shape.
- Splines can be used to represent curves and surfaces in computer graphics by using parametric equations .



### Bspline

A Bspline is a type of curve that is defined by a set of control points and a degree. A Bspline curve is a piecewise polynomial function that has the following properties :

- It is smooth and continuous, meaning that there are no sharp corners or breaks in the curve.
- It is invariant under affine transformations, meaning that scaling, rotating, or translating the control points will not change the shape of the curve.
- It has local control, meaning that moving one control point will only affect a small portion of the curve near that point.
- It has minimal support, meaning that the curve is contained within the convex hull of the control points.
- It has a variable degree, meaning that the curve can be more or less smooth depending on the chosen degree.

The Bspline curve is defined by a linear combination of basis functions, which are also called Bsplines. The basis functions are determined by the degree of the curve and a knot vector, which is a sequence of non-decreasing numbers that specify the domain of each polynomial segment. The basis functions have the following properties :

- They are non-negative, meaning that they are always greater than or equal to zero.
- They are normalized, meaning that they sum up to one at any point in the domain.
- They are linearly independent, meaning that they cannot be expressed as a linear combination of each other.
- They have compact support, meaning that they are zero outside a certain interval.

The Bspline curve can be evaluated at any point in the domain by using the de Boor algorithm, which is a recursive procedure that computes the weighted average of the control points using the basis functions. The Bspline curve can also be modified by changing the control points, the degree, or the knot vector. Some common operations on Bspline curves are :

- Inserting a knot, which increases the number of control points and the degree of smoothness of the curve.
- Removing a knot, which decreases the number of control points and the degree of smoothness of the curve.
- Refining the knot vector, which increases the number of knots and the resolution of the curve.
- Degree elevation, which increases the degree of the curve and the smoothness of the curve.
- Degree reduction, which decreases the degree of the curve and the smoothness of the curve.

Bspline curves are widely used in computer graphics and computer-aided design, as they offer a flexible and efficient way of representing and manipulating complex shapes and surfaces. Bspline curves can also be generalized to higher dimensions, such as Bspline surfaces and Bspline volumes, which are defined by a grid of control points and two or three knot vectors, respectively.



# Bezier curves and surfaces

## Introduction

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling.
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them.
- They have properties that make them highly useful and convenient for curve and surface design, such as:
  - Affine invariance: the shape of the curve or surface does not change under affine transformations (such as translation, rotation, scaling, and shearing).
  - Convex hull property: the curve or surface lies entirely within the convex hull of its control points, which provides a simple way of bounding and clipping the curve or surface.
  - Variation diminishing property: the curve or surface does not oscillate more than its control polygon, which means it does not have unnecessary wiggles or loops.
  - Local control: moving a control point only affects a local region of the curve or surface, which allows for easy editing and manipulation.
  - Smoothness: the curve or surface has continuous derivatives up to a certain order, depending on the degree of the curve or surface.

## Bezier curves

- A Bezier curve is a parametric curve of the form:

  $$\mathbf{B}(t) = \sum_{i=0}^n \binom{n}{i} (1-t)^{n-i} t^i \mathbf{P}_i, \quad 0 \leq t \leq 1$$

  where $\mathbf{P}_0, \mathbf{P}_1, \ldots, \mathbf{P}_n$ are the control points, and $\binom{n}{i}$ are the binomial coefficients.
- The degree of the Bezier curve is equal to the number of control points minus one, i.e. $n$.
- The curve starts at $\mathbf{P}_0$ and ends at $\mathbf{P}_n$, and is tangent to the first and last segments of the control polygon.
- The curve can be evaluated efficiently using the de Casteljau algorithm, which recursively subdivides the control polygon into smaller polygons until a single point is obtained.
- The curve can also be represented using a matrix form, such as the Bernstein basis or the power basis.
- The curve can be subdivided into two smaller curves of the same degree at any parameter value $t$, using the de Casteljau algorithm.
- The curve can be converted into a different basis, such as the B-spline basis, using a change of basis matrix.

## Bezier surfaces

- A Bezier surface is a parametric surface of the form:

  $$\mathbf{S}(u,v) = \sum_{i=0}^m \sum_{j=0}^n \binom{m}{i} \binom{n}{j} (1-u)^{m-i} u^i (1-v)^{n-j} v^j \mathbf{P}_{ij}, \quad 0 \leq u,v \leq 1$$

  where $\mathbf{P}_{ij}$ are the control points, arranged in a rectangular grid of size $(m+1) \times (n+1)$, and $\binom{m}{i}$ and $\binom{n}{j}$ are the binomial coefficients.
- The degree of the Bezier surface is equal to the number of control points in each direction minus one, i.e. $m$ and $n$.
- The surface passes through the four corner control points, and is tangent to the boundary control polygons.
- The surface can be evaluated efficiently using a tensor product extension of the de Casteljau algorithm, which recursively subdivides the control grid into smaller grids until a single point is obtained.
- The surface can also be represented using a matrix form, such as the tensor product Bernstein basis or the tensor product power basis.
- The surface can be subdivided into four smaller surfaces of the same degree at any parameter values $u$ and $v$, using the tensor product extension of the de Casteljau algorithm.
- The surface can be converted into a different basis,



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have chosen the topic of hidden lines and surfaces. Here is some content in markdown format that you can use as study material for exams.

## Unit 5 - Hidden Lines and Surfaces

- Hidden lines and surfaces are the parts of an object that are not visible from a given viewpoint in a drawing or a projection.
- Hidden lines and surfaces are important to show the shape, size, and features of an object that are not apparent from the visible lines and surfaces.
- Hidden lines and surfaces are usually represented by dashed or dotted lines in a drawing or a projection.
- There are different methods and rules for drawing hidden lines and surfaces depending on the type of projection, the type of object, and the standards or conventions used.
- Some of the common methods and rules for drawing hidden lines and surfaces are:

  - In orthographic projection, hidden lines and surfaces are drawn only on the principal views (front, top, and right) and not on the auxiliary views (left, bottom, and back).
  - In isometric projection, hidden lines and surfaces are drawn only on the isometric view and not on the orthographic views.
  - In perspective projection, hidden lines and surfaces are usually omitted or drawn faintly to avoid confusion and clutter.
  - In section views, hidden lines and surfaces are not drawn unless they are necessary to show the internal features of an object.
  - In assembly drawings, hidden lines and surfaces are drawn only to show the relationship and alignment of the parts and not to show the details of each part.
  - In dimensioning, hidden lines and surfaces are not used to locate or measure features unless they are the only way to do so.
  - In general, hidden lines and surfaces are drawn only when they are essential to understand the shape and size of an object and not when they are redundant or irrelevant.

- Here is an example of a drawing with hidden lines and surfaces:

drawing with hidden lines and surfaces

- In this drawing, the hidden lines and surfaces are shown by dashed lines on the front and top views and by dotted lines on the right view.
- The hidden lines and surfaces show the features of the object that are not visible from the given viewpoints, such as the hole, the slot, the notch, and the chamfer.
- The hidden lines and surfaces also show the relationship and alignment of the parts, such as the screws and the washers.



### Back Face Detection Algorithm

- Back face detection, also known as plane equation method, is an object space method for identifying the visible surfaces of a polyhedron .
- A polyhedron is a solid object bounded by flat polygonal faces. Each face has a normal vector that points outward from the polyhedron.
- The normal vector of a face can be computed by taking the cross product of two non-parallel edges of the face.
- The back face detection algorithm works as follows :
  - For each face of the polyhedron, compute its normal vector and its plane parameters A, B, C, and D.
  - For a left-handed coordinate system, if the Z component of the normal vector is positive, then the face is a back face and can be discarded. If the Z component is negative, then the face is a front face and can be drawn.
  - For a right-handed coordinate system, the opposite is true: if the Z component of the normal vector is negative, then the face is a back face and can be discarded. If the Z component is positive, then the face is a front face and can be drawn.
  - Alternatively, for any coordinate system, a point (x, y, z) is inside a face with plane parameters A, B, C, and D if Ax + By + Cz + D < 0. If the point is along the line of sight to the face, then the face is a back face and can be discarded. If the point is not along the line of sight to the face, then the face is a front face and can be drawn.
- The back face detection algorithm is fast and simple, but it has some limitations:
  - It only works for convex polyhedra, where every face is visible from the outside. For concave polyhedra, some faces may be hidden by other faces, even if they are front faces.
  - It does not account for the perspective projection, where the orientation of the faces may change depending on the viewpoint. For example, a face that is a back face from one viewpoint may become a front face from another viewpoint.
  - It does not account for the occlusion of faces by other objects in the scene. For example, a face that is a front face may be hidden by another object that is closer to the viewer.

Here is a diagram that illustrates the back face detection algorithm for a left-handed coordinate system:

```
    y
    |
    |   /\
    |  /  \
    | /    \  N
    |/      \  \
    +--------+   \
   /|       /|    \
  / |      / |     \
 /  |     /  |      \
+---+----+   +-------+----> x
|  /|   /|  /|      /|
| / |  / | / |     / |
|/  |/  |/  |/    /  |
+---+---+   +----+   |
|  /    |  /    |   /
| /     | /     |  /
|/      |/      | /
+-------+-------+/
    /
   /
  /
 z
```

The face with normal vector N is a back face because its Z component is positive. The other faces are front faces because their Z components are negative.



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
    - It does not require sorting or clipping of polygons.
    - It can be combined with other rendering techniques, such as shading, transparency, and anti-aliasing.
  - Disadvantages:
    - It requires a large amount of memory to store the depth buffer, which can be a bottleneck for performance and resolution.
    - It can suffer from precision errors due to finite depth resolution, which can cause artifacts such as z-fighting or aliasing.
    - It does not handle transparency or overlapping polygons well, as it only stores the closest depth value at each pixel.



### A-buffer method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects .
- It extends the algorithm of depth-buffer (or Z-buffer) method by storing more than one depth and color value per pixel .
- It uses a linked list data structure to store the fragments of objects that cover each pixel .
- Each fragment has four attributes: depth, color, opacity, and pointer to the next fragment .
- The fragments are sorted in decreasing order of depth, so that the nearest fragment is at the head of the list .
- The final color of each pixel is computed by blending the colors of the fragments according to their opacities .
- A-buffer method can handle anti-aliasing, transparency, and shadows .
- A-buffer method requires more memory and processing time than depth-buffer method .
- A-buffer method can be implemented using hardware or software .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the scan line method for hidden lines and surfaces in computer graphics:

### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis.
- The basic idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be applied to both solid and wireframe models, and can handle concave and self-intersecting polygons as well.
- The scan line method can be divided into two phases: the initialization phase and the scan conversion phase.

#### Initialization phase

- In this phase, the polygons are sorted by their minimum y coordinate, and an active edge list (AEL) is created to store the edges that intersect the current scan line.
- The AEL is sorted by the x coordinate of the intersection point, and each edge has a flag to indicate whether it belongs to a visible surface or not.
- The AEL is updated as the scan line moves down, by adding new edges that start at the current scan line, and removing edges that end at the current scan line.
- The AEL is also updated by changing the x coordinate of the intersection point according to the slope of the edge, and by changing the flag of the edge according to the parity rule.
- The parity rule states that an edge is visible if the number of visible edges to its left is odd, and invisible if the number of visible edges to its left is even.

#### Scan conversion phase

- In this phase, the pixels on the current scan line are filled with the color of the visible surface, by using the information in the AEL.
- The algorithm scans the AEL from left to right, and maintains a flag to indicate whether the current pixel is inside or outside a visible surface.
- The flag is toggled whenever the algorithm encounters an edge in the AEL.
- The algorithm fills the pixels with the color of the surface that corresponds to the first edge in the AEL, and skips the pixels that are outside any visible surface.
- The algorithm repeats this process for each scan line until all the polygons are processed.

#### Example

- Consider the following example of three polygons A, B, and C, with their minimum and maximum y coordinates and their colors:

| Polygon | Min y | Max y | Color |
|---------|-------|-------|-------|
| A       | 2     | 6     | Red   |
| B       | 3     | 7     | Green |
| C       | 4     | 8     | Blue  |

- The initialization phase will sort the polygons by their min y coordinate, and create the AEL as follows:

| Scan line | AEL                          |
|-----------|------------------------------|
| 2         | (A, visible)                 |
| 3         | (A, visible), (B, visible)   |
| 4         | (A, invisible), (B, visible), (C, visible) |
| 5         | (A, invisible), (B, visible), (C, visible) |
| 6         | (B, visible), (C, visible)   |
| 7         | (B, invisible), (C, visible) |
| 8         | (C, visible)                 |

- The scan conversion phase will fill the pixels on each scan line with the color of the visible surface, as follows:

| Scan line | Pixels filled |
|-----------|---------------|
| 2         | Red           |
| 3         | Red, Green    |
| 4         | Green, Blue   |
| 5         | Green, Blue   |
| 6         | Green, Blue   |
| 7         | Blue          |
| 8         | Blue          |

- The final image will look like this:

![Scan line method example](https://media.geeksforgeeks.org/wp-content/uploads/20210214184128/



### Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the physical properties of light sources, surfaces, and the interaction between them.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, ignoring the effects of other objects in the scene.
  - Global illumination models account for all the interactions and exchange of light among objects in the scene, such as reflection, refraction, and shadows.
- A basic illumination model that gives reasonably good results and is used in most graphics systems consists of three components: ambient light, diffuse reflection, and specular reflection .
  - Ambient light is the uniform and constant light that is present in the environment, regardless of the position and orientation of the surface .
  - Diffuse reflection is the light that is reflected equally in all directions by a matte or rough surface, depending on the angle between the surface normal and the light direction .
  - Specular reflection is the light that is reflected in a dominant direction by a shiny or smooth surface, depending on the angle between the surface normal, the light direction, and the viewer direction .
- The total intensity of light at a point on a surface can be computed by adding the contributions of each component, multiplied by a coefficient that depends on the surface material and color .
- The basic illumination model can be extended to include other effects, such as attenuation, spotlights, multiple light sources, and color .



### Ambient light

- Ambient light is a type of lighting that is used to create a realistic environment in computer graphics.
- Ambient light refers to the base brightness applied to textures rendered in a scene before any point, spot, or other types of virtual light sources are computed.
- Ambient light affects the appearance of the entire rendered scene by adding a uniform color and intensity to all surfaces.
- Ambient light can be used to simulate natural lightings, such as the sun, or artificial lighting, such as fluorescent lights.
- Ambient light is a very crude approximation of indirect lighting, which is the light that bounces off surfaces and causes diffuse illumination.
- Ambient light does not depend on the direction or position of the light source or the surface normal, and hence it does not create any shadows or highlights.
- Ambient light can be calculated by multiplying the ambient color of the light source by the ambient reflectance of the surface.
- Ambient light can be improved by using techniques such as ambient occlusion, which is a method to calculate how exposed each point in a scene is to ambient lighting.
- Ambient occlusion can create more realistic shadows and depth by darkening the areas that are more occluded (and hence less exposed) by ambient lighting.
- Ambient occlusion can be computed by using ray tracing, image-based methods, or screen-space methods.



### Diffuse reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough .
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can be modeled by Lambert's cosine law, which states that the intensity of the reflected light is proportional to the cosine of the angle between the light source and the surface normal .
- Diffuse reflection can also be affected by diffuse interreflection, which is a process whereby light reflected from an object strikes other objects in the surrounding area, illuminating them.
- Diffuse interreflection specifically describes light reflected from objects which are not shiny or specular.
- Diffuse interreflection can be simulated by global illumination algorithms, such as radiosity or Monte Carlo methods.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on specular reflection for the unit 5 of computer graphics:

### Specular reflection

- Specular reflection is the phenomenon of light bouncing off a shiny surface in a mirror-like manner, creating a bright spot or highlight on the surface .
- Specular reflection depends on the angle of incidence of the light ray, the angle of reflection of the light ray, and the viewing angle of the observer .
- The angle of incidence is equal to the angle of reflection, and both are measured from the normal to the surface at the point of contact .
- The viewing angle is the angle between the direction of the reflected ray and the direction of the observer's eye .
- The intensity of the specular highlight decreases as the viewing angle increases, because the reflected ray becomes less aligned with the observer's eye .
- Specular reflection is influenced by the material properties of the surface, such as its roughness, color, and reflectivity  .
- A rough surface has many microfacets that reflect light in different directions, resulting in a diffuse or scattered reflection  .
- A smooth surface has fewer microfacets and reflects light in a more coherent direction, resulting in a specular or mirror-like reflection  .
- The color of the specular highlight is determined by the color of the light source, not by the color of the surface  .
- The reflectivity of the surface is the fraction of the incident light that is reflected by the surface  .
- A high reflectivity means that most of the light is reflected, resulting in a bright specular highlight  .
- A low reflectivity means that most of the light is absorbed or transmitted, resulting in a dim or no specular highlight  .
- In computer graphics, specular reflection is often modeled using empirical formulas that approximate the physical behavior of light and materials  .
- One of the most common models is the Phong model, proposed by Bui-Tuong Phong in 1975 .
- The Phong model calculates the intensity of the specular highlight as a function of the angle between the reflected ray and the viewing direction, raised to a power that represents the shininess of the surface .
- The Phong model can produce realistic effects for smooth and shiny surfaces, but it has some limitations, such as not accounting for the color of the surface, the shape of the highlight, or the Fresnel effect.
- The Fresnel effect is the phenomenon of light becoming more reflective as the angle of incidence approaches 90 degrees, or grazing angle.
- Other models that improve on the Phong model include the Blinn-Phong model, the Cook-Torrance model, and the Bidirectional Reflectance Distribution Function (BRDF) model.

Here is a diagram that illustrates the specular reflection:

```
    Light source
       /
      /
     /
    /
   /
  /
 /
/  \    Normal
|   \   /
|    \ /  Angle of incidence
|     X
|    / \  Angle of reflection
|   /   \
|  /     \
| /       \
|/         \  Reflected ray
Surface     \
             \
              \
               \
                \
                 \
                  \
                   \
                    \
                     \
                      \
                       \
                        \
                         \
                          \
                           \
                            \
                             \
                              \
                               \
                                \
                                 \
                                  \
                                   \
                                    \
                                     \
                                      \
                                       \
                                        \
                                         \
                                          \
                                           \
                                            \
                                             \
                                              \
                                               \
                                                \
                                                 \
                                                  \
                                                   \
                                                    \
                                                     \
                                                      \
                                                       \
                                                        \
                                                         \
                                                          \
                                                           \
                                                            \
                                                             \
                                                              \
                                                               \
                                                                \
                                                                 \
                                                                  \
                                                                   \
                                                                    \
                                                                     \
                                                                      \
                                                                       \
                                                                        \
                                                                         \
                                                                          \
                                                                           \
                                                                            \
                                                                             \
                                                                              \
                                                                               \
                                                                                \
                                                                                 \
                                                                                  \

```




### Phong model

The Phong model is an empirical model of the local illumination of points on a surface designed by the computer graphics researcher Bui Tuong Phong. It is sometimes referred to as "Phong shading", particularly if the model is used with the interpolation method of the same name and in the context of pixel shaders or other places where a lighting calculation can be referred to as “shading”.

The Phong model describes the interaction of light with a surface, in terms of the properties of the surface and the nature of the incident light. It consists of three components: ambient, diffuse, and specular reflection.

- Ambient reflection: This is the constant term that represents the amount of light that is reflected by the surface in all directions, regardless of the light source or the viewer position. It is usually a small fraction of the surface color, and it accounts for the general brightness of the scene.
- Diffuse reflection: This is the term that represents the amount of light that is reflected by the surface in a direction that is proportional to the cosine of the angle between the surface normal and the light direction. It is also known as Lambertian reflection, and it depends on the surface color and the light intensity.
- Specular reflection: This is the term that represents the amount of light that is reflected by the surface in a direction that is proportional to the cosine of the angle between the reflection direction and the viewer direction. It is also known as mirror-like reflection, and it depends on the surface shininess and the light color.

The Phong model can be expressed mathematically as follows:

![Phong model equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6



### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image.
- HLR and HSR are important for creating realistic and accurate images of solid objects, as well as for reducing the computational complexity and rendering time.
- There are different types of coherence that can be exploited to perform HLR and HSR efficiently, such as object coherence, image coherence, area coherence, and span coherence.
- There are different algorithms for HLR and HSR, which can be classified into two main categories: object-space methods and image-space methods .
- Object-space methods compare the objects and their parts in the scene to determine which are visible and which are hidden. They operate on the geometric model of the scene and use techniques such as back-face culling, depth sorting, and binary space partitioning.
- Image-space methods compare the depth values of the pixels in the image to determine which are closer to the viewer and which are farther away. They operate on the rasterized image of the scene and use techniques such as z-buffer, scan-line, and ray tracing.
- A combined approach for HLR and HSR can use both object-space and image-space methods to achieve a balance between accuracy and efficiency. For example, one can use back-face culling and depth sorting to eliminate some hidden surfaces in the object-space, and then use z-buffer or scan-line to resolve the remaining hidden surfaces in the image-space.



### Warn model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- The Warn model is a lighting model that approximates large non-point sources close to objects in a scene by using several point sources arranged in a grid .
- The Warn model also allows one to specify "flaps" on the sides of the lighting region to give the light more directionality.
- The Warn model can be used to simulate studio lighting effects, such as spotlights.
- The Warn model takes into account the reflectance properties of the surface as well as the physics of light reflection.
- The Warn model can be implemented by using the following steps :
  - Define the position, size, and shape of the light source grid.
  - Define the position, orientation, and shape of the flaps.
  - For each point source in the grid, calculate the intensity and direction of the light reaching the object surface.
  - For each point on the object surface, calculate the total illumination by summing up the contributions from all the point sources in the grid.
  - Apply the shading model (such as Phong or Gouraud) to the object surface using the calculated illumination values.



### Intensity Attenuation

- In computer graphics, **attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- Attenuation is the gradual decrease in energy as the X-radiation passes through absorbing material .
- Intensity is the power per unit cross-sectional area .
- Intensity attenuation is important for realistic rendering of light sources, shadows, and reflections in computer graphics.
- Intensity attenuation can be modeled by a formula that depends on the distance from the light source, the type of light source, and the properties of the medium.
- The formula for intensity attenuation is:

  `I = I0 / (a + bd + cd^2)`

  where:

  - `I` is the intensity at distance `d` from the light source
  - `I0` is the intensity at the light source
  - `a`, `b`, and `c` are attenuation coefficients that depend on the light source and the medium
  - `d` is the distance from the light source

- The attenuation coefficients can be adjusted to achieve different effects, such as:

  - `a = 1, b = 0, c = 0`: no attenuation, constant intensity
  - `a = 0, b = 1, c = 0`: linear attenuation, intensity decreases linearly with distance
  - `a = 0, b = 0, c = 1`: quadratic attenuation, intensity decreases quadratically with distance
  - `a = 0, b = 0.5, c = 0.5`: realistic attenuation, intensity decreases with a combination of linear and quadratic terms

- Intensity attenuation can also be affected by other factors, such as:

  - The angle between the light source and the surface normal
  - The reflectance and transmittance of the surface
  - The scattering and absorption of the medium
  - The ambient and diffuse components of the light



### Color consideration for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection.
- Hidden surface removal or visible surface detection is the process of identifying and eliminating the hidden surfaces from the rendered image.
- Color consideration for the notes of hidden lines and surfaces is important to enhance the readability and understanding of the concepts and algorithms involved in this unit.
- Some of the color considerations for the notes are:

  - Use different colors to distinguish between visible and hidden lines or surfaces. For example, use black for visible lines and gray for hidden lines, or use solid colors for visible surfaces and dashed or dotted colors for hidden surfaces.
  - Use colors that are consistent with the lighting and shading models used in computer graphics. For example, use darker colors for surfaces that are farther away or facing away from the light source, and use lighter colors for surfaces that are closer or facing towards the light source.
  - Use colors that are compatible with the color space and the frame buffer of the graphics system. For example, use RGB colors for the intensity field of the frame buffer, and use pointers to linked lists for the depth field of the frame buffer if multiple surfaces contribute to the pixel intensity.
  - Use colors that are appropriate for the scan line algorithm in 3D, which is a hidden surface removal technique that works by scanning each horizontal line of the image and updating the color-intensity values of the visible surfaces in the frame buffer. For example, use colors that are based on the surface normal, the surface reflectance, and the light source intensity for each scan line.
  - Use colors that are clear and contrast well with the background and the text of the notes. For example, use bright colors for the foreground and dark colors for the background, or use complementary colors for the text and the graphics.



### Transparency and Shadows

- Transparency is the property of a material that allows light to pass through it partially or fully, creating the effect of translucency or see-through.
- Transparency can be simulated in computer graphics by mixing the colors of the object and the background according to the object's opacity or alpha value, which ranges from 0 (fully transparent) to 1 (fully opaque).
- Transparency can be used to create realistic effects such as glass, water, smoke, fog, etc. or to create artistic effects such as blending, fading, overlaying, etc.
- Transparency can be classified into two types: constant transparency and variable transparency. Constant transparency means that the opacity of the object is the same for all its points, while variable transparency means that the opacity varies across the object, creating more complex effects.
- Transparency can also be affected by the lighting conditions, such as the direction, intensity, and color of the light source, and the reflection and refraction of light rays on the object's surface.
- Shadows are the regions where light is blocked by an object, creating a contrast between the illuminated and the dark areas.
- Shadows can enhance the realism and depth of a scene rendered with computer graphics, as they provide cues about the shape, size, position, and orientation of the objects and the light source.
- Shadows can also be used to create dramatic or artistic effects, such as mood, atmosphere, suspense, etc.
- Shadows can be classified into two types: hard shadows and soft shadows. Hard shadows are sharp and well-defined, while soft shadows are blurry and gradual, depending on the size and distance of the light source.
- Shadows can be generated by different techniques, such as ray tracing, shadow mapping, shadow volumes, etc. Each technique has its own advantages and disadvantages in terms of accuracy, efficiency, and complexity.

