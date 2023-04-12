

## Unit 1 - Introduction and Line Generation

- Computer graphics is the field of study that deals with the creation, manipulation, and display of images using computers.
- Computer graphics can be used for various applications, such as entertainment, education, engineering, medicine, art, and science.
- Computer graphics can be classified into two types: raster graphics and vector graphics.
- Raster graphics are composed of pixels, which are small dots of color arranged in a grid. Raster graphics are commonly used for digital photos, videos, and games.
- Vector graphics are composed of geometric primitives, such as points, lines, curves, and polygons. Vector graphics are commonly used for logos, diagrams, fonts, and illustrations.
- Line generation is one of the basic operations in computer graphics, as lines are used to draw other shapes and objects.
- Line generation algorithms are methods to determine which pixels should be turned on to display a line on a raster screen.
- Line generation algorithms should be efficient, accurate, and consistent. They should also avoid aliasing, which is the jagged appearance of lines due to pixelation.
- Some of the common line generation algorithms are:
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the next pixel position along the line. It is simple, but may be slow and inaccurate due to rounding errors.
  - Bresenham's algorithm: This algorithm uses integer arithmetic and decision variables to determine the next pixel position along the line. It is faster and more accurate than DDA, but may be more complex to implement.
  - Midpoint algorithm: This algorithm uses the midpoint of the line segment between two pixels to decide which pixel to turn on next. It is similar to Bresenham's algorithm, but may be easier to generalize to other shapes, such as circles and ellipses.



### Types of computer graphics

Computer graphics are the visual representation of data and information using computers and software. Computer graphics can be used for various purposes, such as creating images, animations, simulations, games, user interfaces, and more.

Computer graphics can be broadly classified into two main categories: raster graphics and vector graphics  . Additionally, computer graphics can also be categorized based on the dimensionality of the images: two dimensional (2D), three dimensional (3D), and animated graphics .

- **Raster graphics** are made up of pixels, which are small squares of color that form a grid. Each pixel contains information about its color and brightness. Raster graphics are also known as bitmap images, as they map each pixel to a specific location on the screen. Raster graphics are commonly used for digital photographs, paintings, and scanned images. The quality and resolution of raster graphics depend on the number of pixels per inch (ppi) or dots per inch (dpi). The more pixels or dots, the higher the quality and the larger the file size. Raster graphics can be edited using software tools that allow changing the color, brightness, contrast, and other attributes of individual pixels or groups of pixels. However, raster graphics can lose quality and become pixelated when they are enlarged or scaled up, as the pixels become more visible and distorted.

- **Vector graphics** are made up of paths, which are defined by mathematical equations that describe the shape, direction, and color of each line or curve. Vector graphics are also known as object-oriented graphics, as they represent each image element as an object that can be manipulated independently. Vector graphics are commonly used for logos, icons, diagrams, fonts, and illustrations. The quality and resolution of vector graphics do not depend on the number of pixels or dots, but on the complexity and accuracy of the mathematical equations. Vector graphics can be edited using software tools that allow changing the shape, size, color, and other attributes of each path or object. Vector graphics can retain their quality and clarity when they are enlarged or scaled up, as the equations can be recalculated to fit any screen size or resolution.

- **2D graphics** are images that have only two dimensions: width and height. 2D graphics can be either raster or vector, depending on how they are created and stored. 2D graphics are widely used for web design, graphic design, user interfaces, and digital art. 2D graphics can create the illusion of depth, perspective, and realism using techniques such as shading, lighting, shadows, and textures. However, 2D graphics cannot represent the actual depth, distance, and orientation of the objects in the scene.

- **3D graphics** are images that have three dimensions: width, height, and depth. 3D graphics can be either raster or vector, depending on how they are rendered and displayed. 3D graphics are widely used for animation, gaming, simulation, and virtual reality. 3D graphics can create realistic and immersive representations of the objects and environments in the scene, using techniques such as modeling, rendering, shading, lighting, shadows, textures, and transformations. 3D graphics can also represent the actual depth, distance, and orientation of the objects in the scene, using mathematical calculations and coordinates.

- **Animated graphics** are images that change over time, creating the illusion of motion and dynamics. Animated graphics can be either raster or vector, depending on how they are created and stored. Animated graphics can be either 2D or 3D, depending on how they are rendered and displayed. Animated graphics are widely used for entertainment, education, advertising, and storytelling. Animated graphics can create engaging and expressive representations of the characters, actions, and events in the scene, using techniques such as keyframes, frames, frame rate, tweening, interpolation, and motion capture. Animated graphics can also represent the changes in the depth, distance, and orientation of the objects in the scene, using mathematical calculations and coordinates.



# Graphic Displays for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A graphic display is a device that can show images generated by a computer on a screen.
- There are two main types of graphic displays: raster and vector.
- Raster displays use a grid of pixels (picture elements) that can be individually turned on or off to create an image. Each pixel has a color and a brightness value. Examples of raster displays are LCD, LED, OLED, and plasma monitors.
- Vector displays use an electron beam that traces lines on a phosphor-coated screen to create an image. Each line has a color, a brightness, and a start and end point. Examples of vector displays are oscilloscopes and some arcade games.
- Raster displays are more common and versatile than vector displays, as they can show more complex and realistic images, such as photographs, videos, and 3D graphics.
- Vector displays are more suitable for showing simple and geometric images, such as graphs, diagrams, and wireframes. They also have a higher resolution and contrast than raster displays, as they do not have pixelation or aliasing effects.
- The quality of a graphic display depends on several factors, such as the size, resolution, refresh rate, color depth, contrast ratio, brightness, viewing angle, and response time of the screen.
- The size of a graphic display is measured by the diagonal length of the screen, usually in inches. The larger the size, the more comfortable and immersive the viewing experience, but also the more expensive and power-consuming the display.
- The resolution of a graphic display is measured by the number of pixels in the horizontal and vertical dimensions of the screen, usually in pixels per inch (ppi) or dots per inch (dpi). The higher the resolution, the sharper and clearer the image, but also the more memory and processing power required by the computer.
- The refresh rate of a graphic display is measured by the number of times the screen updates the image per second, usually in hertz (Hz). The higher the refresh rate, the smoother and more realistic the motion, but also the more bandwidth and electricity needed by the display.
- The color depth of a graphic display is measured by the number of bits used to represent the color and brightness of each pixel, usually in bits per pixel (bpp). The higher the color depth, the more colors and shades the display can show, but also the more data and storage space required by the computer.
- The contrast ratio of a graphic display is measured by the ratio of the brightest white to the darkest black that the screen can produce, usually in decibels (dB). The higher the contrast ratio, the more vivid and detailed the image, but also the more sensitive the display to ambient light and glare.
- The brightness of a graphic display is measured by the amount of light emitted by the screen, usually in candelas per square meter (cd/m2) or nits. The higher the brightness, the more visible and readable the image, but also the more heat and power generated by the display.
- The viewing angle of a graphic display is measured by the angle at which the image quality starts to degrade, usually in degrees. The wider the viewing angle, the more consistent and accurate the image, but also the more expensive and complex the display technology.
- The response time of a graphic display is measured by the time it takes for a pixel to change from one color to another, usually in milliseconds (ms). The lower the response time, the faster and smoother the image, but also the more prone the display to ghosting and blurring effects.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your notes.

### Random scan displays

- Random scan displays are also known as **vector displays** or **stroke-writing displays** or **calligraphic displays**.
- Random scan displays use a **cathode ray tube (CRT)** to draw a picture one line at a time in any order or direction  .
- Random scan displays direct the electron beam only to those areas of the screen where a picture has to be drawn .
- Random scan displays can produce **smooth line drawings** and have **high resolution**.
- Random scan displays cannot display realistic shades or complex scenes.
- Random scan displays are suitable for applications that require **line drawings** such as engineering and scientific drawings.
- Random scan displays require a **display processor** or a **display list** to store the line coordinates and attributes.
- Random scan displays have a **refresh rate** that depends on the number and complexity of lines.
- Pen plotter is an example of random scan displays.



# Raster scan displays

- Raster scan displays are the most common type of graphics monitor that use a cathode ray tube (CRT) to display images on the screen .
- A raster scan display works by scanning an electron beam across the screen from top to bottom, one row at a time .
- The electron beam is modulated by the video signal, which determines the intensity and color of each pixel on the screen .
- The screen is divided into a matrix of small dots called picture elements or pixels, which are the basic units of display .
- The resolution of a raster scan display depends on the number of pixels on the screen and the number of colors that each pixel can display .
- The refresh rate of a raster scan display is the number of times per second that the electron beam scans the entire screen .
- A higher refresh rate reduces the flickering effect and improves the quality of the display .
- Raster scan displays are based on television technology and use the same standards for video signals, such as NTSC, PAL, and SECAM .
- Raster scan displays are suitable for displaying realistic images, animations, and video games, but they have some limitations, such as aliasing, pixelation, and difficulty in drawing lines and curves .



### Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- The frame buffer and video controller are essential components of computer graphics systems, as they enable the display of graphical output on the screen.

Some points to note about frame buffer and video controller are:

- The size of the frame buffer determines the resolution and color depth of the display.
- The frame buffer can be a separate memory bank on the graphics card, GPU or a reserved part of regular memory.
- The video controller can be integrated with the graphics card, GPU or the motherboard.
- The video controller can support different modes of operation, such as text mode, graphics mode, interlaced mode, etc.
- The video controller can also perform some basic operations on the frame buffer, such as scrolling, copying, filling, etc.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write some notes on the topic of points and lines for the unit 1 of computer graphics. Here is what I have written:

### Points and lines

- A point is the simplest graphical element that can be displayed on a screen. It is represented by a single pixel or a small group of pixels.
- A line is a sequence of points that are connected by straight or curved segments. It is one of the most basic and common shapes in computer graphics.
- To draw a line on a screen, we need to specify the coordinates of its endpoints, or the starting point and the direction and length of the line.
- There are different algorithms for drawing lines on a screen, depending on the type of line and the characteristics of the display device. Some of the most common algorithms are:
  - DDA algorithm: It uses a digital differential analyzer to incrementally calculate the coordinates of the points along the line. It is simple and fast, but it may produce round-off errors and gaps in the line.
  - Bresenham's algorithm: It uses integer arithmetic and decision variables to determine the next point along the line. It is more accurate and efficient than the DDA algorithm, but it only works for lines with slopes between 0 and 1.
  - Midpoint algorithm: It uses the midpoint of the line segment to decide whether to move horizontally or vertically to the next point. It is a generalization of the Bresenham's algorithm that can handle any slope and any direction of the line.
  - Xiaolin Wu's algorithm: It uses anti-aliasing techniques to smooth the edges of the line by varying the intensity of the pixels. It produces high-quality lines, but it is more complex and slower than the other algorithms.



### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A line drawing algorithm is a method for estimating a line segment on discrete graphical media such as pixel-based screens and printers in computer graphics.
- A line segment is defined by two endpoints, each with an x and y coordinate.
- To draw a line, a computer must work out which pixels need to be filled so that the line looks straight.
- There are different algorithms for drawing a line, each with different advantages and disadvantages in terms of accuracy, efficiency, and simplicity.
- Some of the common line drawing algorithms are:

  - Naive algorithm: This algorithm simply rounds the x and y coordinates of each point on the line to the nearest integer and fills the corresponding pixel. It is easy to implement but can produce jagged lines and gaps.
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each point on the line. It is more accurate than the naive algorithm but can be slow and requires floating-point arithmetic .
  - Bresenham's algorithm: This algorithm uses integer arithmetic and error terms to determine which pixel to fill at each step. It is faster and more efficient than the DDA algorithm and produces smooth lines .
  - Mid-point algorithm: This algorithm uses the mid-point of the line segment to decide which pixel to fill at each step. It is similar to Bresenham's algorithm but can handle lines with any slope and avoids multiplication and division operations .

- The following is a pseudocode for the Bresenham's algorithm, which is one of the most widely used line drawing algorithms:

  ```
  Input: x1, y1, x2, y2 // the endpoints of the line segment
  Output: a set of pixels to fill

  // initialize the variables
  dx = x2 - x1 // the change in x
  dy = y2 - y1 // the change in y
  x = x1 // the current x coordinate
  y = y1 // the current y coordinate
  p = 2 * dy - dx // the initial error term

  // loop until the end of the line segment is reached
  while x <= x2
    // fill the pixel at (x, y)
    plot(x, y)
    // increment x by 1
    x = x + 1
    // check the error term
    if p < 0
      // no change in y
      p = p + 2 * dy
    else
      // increment y by 1
      y = y + 1
      // update the error term
      p = p + 2 * (dy - dx)
    end if
  end while
  ```



### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm.
- A circle generation algorithm is an algorithm used to create a circle on a computer screen by determining the subsequent points required to draw the circle .
- There are several algorithms used for generating circles on a computer screen, such as:
  - Bresenham's Algorithm
  - Midpoint Circle Algorithm
  - Trigonometric Method
  - Polar Coordinates Method
- Bresenham's Algorithm :
  - It is an efficient algorithm that uses only integer arithmetic to generate a circle.
  - It is based on the idea of incrementally updating the decision parameter that determines whether to choose the next pixel along the circle or the diagonal.
  - It starts from the topmost point of the circle and moves clockwise in the first octant, then uses symmetry to plot the other points in the other octants.
  - The algorithm is as follows:
    - Input the radius r and the center (xc, yc) of the circle.
    - Initialize the decision parameter as p0 = 3 - 2r.
    - Set x = 0 and y = r.
    - Plot the initial point (xc + x, yc + y) and its symmetric points in the other octants.
    - Repeat until x < y:
      - If p < 0, then set p = p + 4x + 6 and x = x + 1.
      - Else, set p = p + 4(x - y) + 10, x = x + 1 and y = y - 1.
      - Plot the point (xc + x, yc + y) and its symmetric points in the other octants.
- Midpoint Circle Algorithm :
  - It is another efficient algorithm that uses only integer arithmetic to generate a circle.
  - It is based on the idea of testing the midpoint of the line joining the two candidate pixels on either side of the circle and choosing the pixel that is closer to the circle.
  - It also starts from the topmost point of the circle and moves clockwise in the first octant, then uses symmetry to plot the other points in the other octants.
  - The algorithm is as follows:
    - Input the radius r and the center (xc, yc) of the circle.
    - Initialize the decision parameter as p0 = 1 - r.
    - Set x = 0 and y = r.
    - Plot the initial point (xc + x, yc + y) and its symmetric points in the other octants.
    - Repeat until x < y:
      - If p < 0, then set p = p + 2x + 3 and x = x + 1.
      - Else, set p = p + 2(x - y) + 5, x = x + 1 and y = y - 1.
      - Plot the point (xc + x, yc + y) and its symmetric points in the other octants.
- Trigonometric Method:
  - It is a simple but inefficient algorithm that uses trigonometric functions to generate a circle.
  - It is based on the idea of using the parametric equation of a circle, x = r cos θ and y = r sin θ, where θ is the angle from the positive x-axis.
  - It requires a large number of calculations and rounding operations to plot the points on the circle.
  - The algorithm is as follows:
    - Input the radius r and the center (xc, yc) of the circle.
    - Set θ = 0 and increment = 2π / N, where N is the number of points to be plotted on the circle.
    - Repeat N times:
      - Set x = r cos θ and y = r sin θ.
      - Round x and y to the nearest integers.
      - Plot the point (xc + x, yc + y) and its symmetric points in the other octants.
      - Set θ = θ + increment.
- Polar Coordinates Method:
  - It is a variation of the trigonometric method that uses polar coordinates to generate a circle.
  - It is based on the idea of using the polar equation of a circle, r = R cos



# Mid-point circle generating algorithm

The mid-point circle generating algorithm is an algorithm used to determine the points needed for rasterizing a circle. It is based on the following properties of a circle:

- A circle is symmetric about its center, so the points in one octant can be mirrored to the other seven octants.
- A circle has a constant radius, so the distance from any point on the circle to the center is equal to the radius.

The algorithm works as follows:

- Given the center (h, k) and the radius r of the circle, start from the point (0, r) on the positive y-axis and move clockwise along the circle perimeter.
- At each step, calculate the next point (x, y) using the decision parameter p, which is the difference between the squared radius and the squared distance from the center to the current point.
- If p is negative, the next point is (x + 1, y), which is closer to the circle. If p is positive, the next point is (x + 1, y - 1), which is farther from the circle. If p is zero, the next point can be either (x + 1, y) or (x + 1, y - 1).
- Update the value of p using the following formula:

  - p = p + 2x + 3, if p < 0
  - p = p + 2x - 2y + 5, if p >= 0

- Stop when x >= y, which means the algorithm has reached the 45-degree line in the first octant.
- For each point (x, y) generated, plot the corresponding points in the other seven octants using the symmetry property of the circle. The points are:

  - (x, y), (y, x), (-x, y), (-y, x), (x, -y), (y, -x), (-x, -y), (-y, -x)

The following diagram illustrates the algorithm:

Mid-point circle generating algorithm

The algorithm has the following advantages:

- It is simple and easy to implement.
- It only uses integer arithmetic, which is faster and more accurate than floating-point arithmetic.
- It minimizes the number of calculations by using the previous value of p and the symmetry property of the circle.

The algorithm has the following disadvantages:

- It generates redundant points when p is zero, which can be avoided by using a modified formula for p.
- It may produce gaps or overlaps in the circle perimeter, depending on the resolution of the raster device. This can be improved by using anti-aliasing techniques.



### Parallel algorithms for line generation

- Line generation is a fundamental task in computer graphics, where a straight line segment between two points on a discrete grid needs to be approximated by a sequence of pixels.
- A common algorithm for line generation is the Bresenham's algorithm, which uses integer arithmetic and incremental calculations to determine the next pixel along the line.
- However, Bresenham's algorithm is sequential and cannot be easily parallelized, as each pixel depends on the previous one.
- Therefore, some parallel algorithms for line generation have been proposed, which exploit the properties of line equations and vector operations to derive coordinate pairs that approximate the line in parallel.
- Some of the parallel algorithms for line generation are:

  - The parallel prefix sums algorithm, which uses the fact that straight line generation is equivalent to a vector prefix sums calculation. The algorithm executes on a binary tree of processors, where each node performs a simple calculation that involves only additions and shifts.
  - The parallel edge function algorithm, which uses a linear edge function that has a value greater than zero on one side of the edge and less than zero on the opposite side. The value of the function can be interpolated with hardware similar to hardware required to interpolate color and Z pixel values. The edge function of adjacent pixels can be easily computed in parallel, and the coefficients of the edge function can be computed from floating point endpoints with sub-pixel precision.
  - The parallel coordinate pair algorithm, which uses the line equation to derive coordinate pairs that approximate the line on a square grid. The algorithm uses a parallel prefix computation to generate the coordinate pairs, and then maps them to the grid using a parallel mapping function.
  - The parallel DDA algorithm, which is a parallel version of the digital differential analyzer (DDA) algorithm, which uses floating point arithmetic and incremental calculations to determine the next pixel along the line. The algorithm divides the line into segments of equal length, and assigns each segment to a processor. Each processor then computes the pixels of its segment using the DDA algorithm.



## Unit 2 - Transformations

In this unit, you will learn about different types of transformations that can be applied to geometric figures. A transformation is a change in the position, size, or shape of a figure. There are four main types of transformations: translations, rotations, reflections, and dilations.

- A translation is a transformation that moves every point of a figure by the same distance and in the same direction. The figure does not change its size or shape, only its location. A translation can be described by a vector, which has a magnitude (length) and a direction. For example, the vector <2, -3> means to move every point of the figure 2 units to the right and 3 units down. To perform a translation, you can add the vector to the coordinates of each point of the figure.

- A rotation is a transformation that turns a figure around a fixed point, called the center of rotation. The figure does not change its size or shape, only its orientation. A rotation can be described by an angle of rotation, which measures how much the figure is turned, and a direction of rotation, which can be clockwise or counterclockwise. For example, a 90-degree clockwise rotation means to turn the figure 90 degrees in the clockwise direction. To perform a rotation, you can use the following rules to find the new coordinates of each point of the figure:

  - If the center of rotation is the origin (0, 0), then the new coordinates of a point (x, y) are (y, -x) for a 90-degree clockwise rotation, (-y, x) for a 90-degree counterclockwise rotation, (-x, -y) for a 180-degree rotation, and (x, y) for a 360-degree rotation.
  - If the center of rotation is not the origin, then you can first translate the figure so that the center of rotation becomes the origin, then apply the rules above, and then translate the figure back to its original position.

- A reflection is a transformation that flips a figure over a line, called the line of reflection. The figure does not change its size or shape, only its orientation. A reflection can be described by the equation of the line of reflection, which can be horizontal, vertical, or diagonal. For example, the line y = x is a diagonal line that reflects the figure over the line y = x. To perform a reflection, you can use the following rules to find the new coordinates of each point of the figure:

  - If the line of reflection is the x-axis, then the new coordinates of a point (x, y) are (x, -y).
  - If the line of reflection is the y-axis, then the new coordinates of a point (x, y) are (-x, y).
  - If the line of reflection is the line y = x, then the new coordinates of a point (x, y) are (y, x).
  - If the line of reflection is the line y = -x, then the new coordinates of a point (x, y) are (-y, -x).
  - If the line of reflection is not one of the above, then you can use the formula y - y1 = m(x - x1), where (x1, y1) is a point on the line and m is the slope of the line, to find the new coordinates of each point of the figure.

- A dilation is a transformation that changes the size of a figure by a scale factor, which can be greater than 1, equal to 1, or less than 1. The figure does not change its shape, only its size. A dilation can be described by a scale factor and a center of dilation, which is a fixed point that does not change its position. For example, a dilation with a scale factor of 2 and a center of dilation at the origin means to double the distance of every point of the figure from the origin. To perform a dilation, you can use the following rule to find the new coordinates of each point of the figure:

  - If the center of dilation is the origin (0, 0), then the new coordinates of a point (x, y) are (kx, ky), where k is the scale factor.
  - If the center of dilation is not the origin, then you can first translate the figure so that the center of dilation becomes the origin, then apply the rule above, and then translate the figure back to its original position.

These transformations can be combined to create more complex transformations, such as glide reflections, which are translations followed by reflections, or compositions of transformations, which are two or more transformations applied in sequence. To find



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on basic transformation for computer graphics:

### Basic transformation for computer graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane  .
- There are three basic rigid transformations that preserve the distance and angle between the points of an object:
  - Reflection: flipping an object over a line or a plane, creating a mirror image.
  - Rotation: rotating an object around a fixed point or an axis, changing its orientation.
  - Translation: moving an object along a vector, changing its position.
- There is a fourth common transformation called dilation or scaling that changes the size of an object by multiplying its coordinates by a scale factor .
- Transformations can be represented by matrices that can be multiplied with the coordinates of the object to obtain the transformed coordinates  .
- For example, a 2D scaling transformation can be represented by a 2x2 matrix as follows:

```
| Sx  0 |
| 0   Sy|
```

where Sx and Sy are the scale factors along the x and y axes respectively.

- Similarly, a 2D rotation transformation can be represented by a 2x2 matrix as follows :

```
| cosθ  -sinθ |
| sinθ   cosθ |
```

where θ is the angle of rotation in the counterclockwise direction.

- A 2D translation transformation can be represented by a 3x3 matrix as follows :

```
| 1  0  tx |
| 0  1  ty |
| 0  0  1  |
```

where tx and ty are the translation distances along the x and y axes respectively.

- Transformations can be combined by multiplying the corresponding matrices in a specific order .
- For example, to perform a scaling followed by a rotation followed by a translation, the matrix multiplication would be as follows:

```
| 1  0  tx | | cosθ  -sinθ | | Sx  0 |
| 0  1  ty | | sinθ   cosθ | | 0   Sy|
| 0  0  1  | | 0      0    | | 0   0 |
```

- The result of the matrix multiplication is another matrix that represents the combined transformation.
- Transformations can be applied to various objects such as points, lines, polygons, curves, surfaces, etc. in computer graphics  .
- Transformations can be used for various purposes such as animation, modeling, rendering, etc. in computer graphics  .
- Transformations can be implemented using various libraries or frameworks such as OpenGL, DirectX, etc. in computer graphics .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of matrix representations and homogenous coordinates for transformations in computer graphics:

### Matrix representations and homogenous coordinates for transformations in computer graphics

- Most graphics are represented by matrices, and applied for vectors in cartesian form, by taking vectors as column vectors and multiplying them by the transformation’s matrix.
- Homogeneous coordinate systems mean expressing each coordinate as a homogeneous coordinate to represent all geometric transformation equations as matrix multiplication.
- In homogeneous coordinate system, two-dimensional coordinate positions (x, y) are represented by triple-coordinates (xh, yh, h), where h is a non-zero scalar.
- Homogeneous coordinates are generally used in design and construction applications. Here we perform translations, rotations, scaling to fit the picture into proper position.
- Points (x, y, z) in R3 can be identified as a homogeneous vector (xh, yh, zh, h) with h≠0 on the plane in R4. If we convert a 3D point to a 4D vector, we can represent a transformation to this point with a 4 x 4 matrix. The last coordinate is a scalar term.
- Graphics transformations can be classified into two types: affine and projective. Affine transformations preserve parallelism, ratios of distances, and angles. Projective transformations preserve straight lines and ratios of areas. Affine transformations can be represented by 3 x 3 matrices in homogeneous coordinates, while projective transformations require 4 x 4 matrices.
- Some examples of affine transformations are translation, rotation, scaling, shear, and reflection. Some examples of projective transformations are perspective projection, cylindrical projection, and spherical projection.
- To perform a transformation on a point or a vector, we multiply the corresponding matrix by the homogeneous coordinate of the point or vector. For example, to translate a point (x, y) by a vector (tx, ty), we multiply the translation matrix by the homogeneous coordinate of the point:

```
| 1  0  tx |   | x |   | x + tx |
| 0  1  ty | x | y | = | y + ty |
| 0  0  1  |   | 1 |   |   1    |
```

- To perform a sequence of transformations, we multiply the matrices of each transformation in the order they are applied. For example, to rotate a point (x, y) by an angle θ and then scale it by a factor s, we multiply the rotation matrix by the scaling matrix and then by the homogeneous coordinate of the point:

```
| s  0  0 |   | cosθ -sinθ  0 |   | x |   | s(cosθx - sinθy) |
| 0  s  0 | x | sinθ  cosθ  0 | x | y | = | s(sinθx + cosθy) |
| 0  0  1 |   |  0     0     1 |   | 1 |   |        1         |
```

- To perform the inverse of a transformation, we multiply the inverse matrix of the transformation by the homogeneous coordinate of the point or vector. For example, to undo a translation by a vector (tx, ty), we multiply the inverse translation matrix by the homogeneous coordinate of the point:

```
| 1  0  -tx |   | x |   | x - tx |
| 0  1  -ty | x | y | = | y - ty |
| 0  0   1  |   | 1 |   |   1    |
```

- To perform a transformation on a shape or an object, we apply the same transformation to each point or vertex of the shape or object. For example, to rotate a triangle by an angle θ, we multiply the rotation matrix by the homogeneous coordinates of each vertex of the triangle.



### Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A transformation is a process of changing the position, size, shape, or orientation of an object in a coordinate system.
- A composite transformation is a combination of two or more transformations into a single one that is equivalent to applying them one after another.
- A composite transformation can be represented by a matrix that is obtained by multiplying the matrices of the individual transformations in the order of their application.
- The order of the transformations matters, as some transformations are not commutative, meaning that changing the order will change the result.
- For example, rotation and translation are not commutative, as rotating an object and then translating it will produce a different result than translating it and then rotating it.
- However, some transformations are commutative, such as scaling and reflection, meaning that changing the order will not change the result.
- For example, scaling an object and then reflecting it will produce the same result as reflecting it and then scaling it.
- The most common types of transformations in computer graphics are translation, scaling, rotation, and shear.
- Translation is the process of moving an object by a given distance along a given direction.
- Scaling is the process of changing the size of an object by a given factor along a given axis.
- Rotation is the process of rotating an object by a given angle around a given point or axis.
- Shear is the process of distorting an object by a given factor along a given direction.
- Each type of transformation has a corresponding matrix that can be used to perform the transformation on the coordinates of an object.
- For example, the matrix for translation by (tx, ty) is:

```
| 1  0  tx |
| 0  1  ty |
| 0  0  1  |
```

- The matrix for scaling by (sx, sy) is:

```
| sx  0  0 |
| 0  sy  0 |
| 0  0  1  |
```

- The matrix for rotation by θ degrees around the origin is:

```
| cosθ  -sinθ  0 |
| sinθ  cosθ   0 |
| 0     0      1 |
```

- The matrix for shear by (shx, shy) is:

```
| 1  shx  0 |
| shy  1  0 |
| 0   0  1  |
```

- To perform a composite transformation on an object, we multiply the matrices of the individual transformations in the order of their application, and then multiply the resulting matrix with the coordinates of the object.
- For example, to perform a translation by (tx, ty) followed by a rotation by θ degrees around the origin, we multiply the matrices as follows:

```
| 1  0  tx |   | cosθ  -sinθ  0 |   | cosθ  -sinθ  tx |
| 0  1  ty | x | sinθ  cosθ   0 | = | sinθ  cosθ   ty |
| 0  0  1  |   | 0     0      1 |   | 0     0      1  |
```

- Then, we multiply the resulting matrix with the coordinates of the object, such as (x, y, 1), to obtain the transformed coordinates, such as (x', y', 1).
- For example, if x = 2, y = 3, tx = 4, ty = 5, and θ = 90 degrees, then the transformed coordinates are:

```
| cosθ  -sinθ  tx |   | x |   | -3 + 4 |   | 1 |
| sinθ  cosθ   ty | x | y | = |  2 + 5 | = | 7 |
| 0     0      1  |   | 1 |   |    1   |   | 1 |
```

- Therefore, the point (2, 3) is translated by (4, 5) and then rotated by 90 degrees around the origin, resulting in the point (1, 7).



### Reflections and Shearing

- Reflections and shearing are two types of transformations in computer graphics that change the position, orientation, or shape of an object.
- A reflection is a transformation that flips an object over a line or a plane, creating a mirror image of the original object. The line or plane is called the axis or plane of reflection.
- A shearing is a transformation that slants an object in one or more directions, changing the shape of the object. The amount of slanting is called the shear factor.
- Both reflections and shearing can be performed in two-dimensional or three-dimensional space, depending on the number of coordinates involved.

#### Reflections in 2D

- A reflection in 2D is a transformation that flips an object over a line, creating a mirror image of the original object. The line is called the axis of reflection.
- The axis of reflection can be horizontal, vertical, or diagonal, depending on the orientation of the line.
- To perform a reflection in 2D, we need to find the new coordinates of each point of the object after the transformation. This can be done by using the following formulas, depending on the axis of reflection:

  - If the axis of reflection is the x-axis, then the new coordinates of a point (x, y) are (x, -y).
  - If the axis of reflection is the y-axis, then the new coordinates of a point (x, y) are (-x, y).
  - If the axis of reflection is the line y = x, then the new coordinates of a point (x, y) are (y, x).
  - If the axis of reflection is the line y = -x, then the new coordinates of a point (x, y) are (-y, -x).

- For example, consider the following figure, where a triangle ABC is reflected over the x-axis, the y-axis, the line y = x, and the line y = -x.

Reflection in 2D

- The new coordinates of the vertices of the triangle after each reflection are:

  - Over the x-axis: A'(-2, -1), B'(1, -3), C'(4, -2)
  - Over the y-axis: A'(-2, 1), B'(-1, 3), C'(-4, 2)
  - Over the line y = x: A'(1, -2), B'(3, 1), C'(2, 4)
  - Over the line y = -x: A'(-1, 2), B'(-3, -1), C'(-2, -4)

#### Reflections in 3D

- A reflection in 3D is a transformation that flips an object over a plane, creating a mirror image of the original object. The plane is called the plane of reflection.
- The plane of reflection can be any plane that passes through the origin, such as the xy-plane, the yz-plane, or the xz-plane, or any other plane defined by a normal vector.
- To perform a reflection in 3D, we need to find the new coordinates of each point of the object after the transformation. This can be done by using the following formulas, depending on the plane of reflection:

  - If the plane of reflection is the xy-plane, then the new coordinates of a point (x, y, z) are (x, y, -z).
  - If the plane of reflection is the yz-plane, then the new coordinates of a point (x, y, z) are (-x, y, z).
  - If the plane of reflection is the xz-plane, then the new coordinates of a point (x, y, z) are (x, -y, z).
  - If the plane of reflection is defined by a normal vector (a, b, c), then the new coordinates of a point (x, y, z) are (x - 2a(xa + yb + zc) / (a^2 + b^2 + c^2), y - 2b(xa + yb + zc) / (a^2 + b^2 + c^2), z - 2c(xa + yb + zc) / (a^2 + b^2 + c^2)).

- For example, consider the following figure, where a cube ABCDEFG



### Windowing and Clipping

Windowing and clipping are two techniques used in computer graphics to display a part of a scene or an object on the screen. They are useful for zooming, panning, and culling operations.

- Windowing is the process of selecting and viewing a picture with different views. A window is a rectangular region of the world coordinate system that defines the area of interest or the portion of the picture that is to be displayed on the screen. A viewport is a rectangular region of the device coordinate system that specifies where the window is to be mapped on the screen. The mapping from the window to the viewport is called the viewing transformation. Windowing allows the user to change the scale and position of the picture on the screen by adjusting the window and the viewport parameters .

- Clipping is the process of dividing each element of the picture into its visible and invisible portions, and discarding the invisible portion. Clipping is necessary to remove the objects, lines, or line segments that are outside the viewing pane or the window, as they are irrelevant for the display. Clipping can be done in the world coordinate system before the viewing transformation, or in the device coordinate system after the viewing transformation. Clipping can be applied to different types of objects, such as points, lines, polygons, circles, curves, and text .

There are different algorithms for clipping different types of objects, such as Cohen-Sutherland algorithm, Liang-Barsky algorithm, Sutherland-Hodgman algorithm, Cyrus-Beck algorithm, etc. These algorithms usually assign a region code to each endpoint of the object, and use bitwise operations to determine whether the object is inside, outside, or partially inside the window. Then, they compute the intersection points of the object with the window boundaries, and keep only the visible portion of the object .

Here is an example of windowing and clipping a line segment:

Windowing and clipping a line segment

The line segment AB has endpoints A(40, 40) and B(80, 80) in the world coordinate system. The window has coordinates (20, 20) and (60, 60). The viewport has coordinates (0, 0) and (100, 100) in the device coordinate system. The region codes for A and B are 1001 and 1010, respectively. The bitwise AND of the region codes is not zero, so the line segment is partially inside the window. The intersection points of the line segment with the window boundaries are C(20, 20) and D(60, 60). The visible portion of the line segment is CD, which is mapped to the viewport as CD'(0, 0) and D'(100, 100) in the device coordinate system.



### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert geometric data into image data that can be displayed on a device .
- The viewing pipeline consists of the following stages :
  - Object coordinates: The coordinates of the geometric primitives that define the objects in the scene.
  - World coordinates: The coordinates of the objects after applying the modeling transformation, which positions and orientates them in the 3D space.
  - Viewing coordinates: The coordinates of the objects after applying the viewing transformation, which defines the position and orientation of the camera or the eye.
  - Projection coordinates: The coordinates of the objects after applying the projection transformation, which maps the 3D scene onto a 2D plane.
  - Normalized device coordinates: The coordinates of the objects after applying the normalization transformation, which scales and translates the projected scene to fit within a unit cube.
  - Device coordinates: The coordinates of the objects after applying the viewport transformation, which maps the normalized device coordinates to the physical device coordinates.
- The viewing pipeline can be represented by the following diagram :

```
Object coordinates -> World coordinates -> Viewing coordinates -> Projection coordinates -> Normalized device coordinates -> Device coordinates
```

- An example of the viewing pipeline is as follows :
  - Suppose we have a triangle with vertices (1, 1), (2, 3), and (3, 2) in object coordinates.
  - We apply a modeling transformation that translates the triangle by (2, 1) and scales it by 2, resulting in the following world coordinates: (4, 4), (6, 8), and (8, 6).
  - We apply a viewing transformation that rotates the scene by 90 degrees clockwise around the origin, resulting in the following viewing coordinates: (4, -4), (8, -6), and (6, -8).
  - We apply a projection transformation that uses an orthographic projection with a clipping window of (-10, 10) x (-10, 10), resulting in the following projection coordinates: (4, -4), (8, -6), and (6, -8).
  - We apply a normalization transformation that maps the clipping window to the unit square of (-1, 1) x (-1, 1), resulting in the following normalized device coordinates: (0.4, -0.4), (0.8, -0.6), and (0.6, -0.8).
  - We apply a viewport transformation that maps the unit square to the device coordinates of (0, 0) x (100, 100), resulting in the following device coordinates: (40, 60), (80, 70), and (60, 80).
  - The final image is a triangle with vertices (40, 60), (80, 70), and (60, 80) on the device.



### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformation is the mapping of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformation is part of the viewing pipeline, which consists of the following steps :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation.
  - Define the projection type, which can be parallel or perspective, and the projection plane, which is the plane where the picture is projected.
  - Define the window, which is the rectangular region of the projection plane that contains the picture of interest.
  - Define the viewport, which is the rectangular region of the display device where the window is mapped.
  - Apply the viewing transformation, which consists of the following substeps :
    - Translate the WCS origin to the VCS origin.
    - Rotate the WCS axes to align with the VCS axes.
    - Project the VCS coordinates onto the projection plane.
    - Scale the window to the size of the viewport.
    - Translate the window to the position of the viewport.
- Viewing transformation can be represented by a matrix that combines all the substeps into one operation.
- Viewing transformation can be applied to any geometric object, such as points, lines, polygons, curves, or surfaces.
- Viewing transformation can be affected by various factors, such as the viewer's position, orientation, distance, field of view, aspect ratio, and clipping planes.
- Viewing transformation can be implemented using various methods, such as homogeneous coordinates, normalized device coordinates, or clipping algorithms.



### 2-D Clipping algorithms

Clipping is the process of removing or hiding the parts of a graphical object that lie outside a specified region of interest, usually called the clipping window or the clipping region. Clipping is an important operation in computer graphics, as it can improve the performance and efficiency of rendering by discarding the invisible or irrelevant parts of a scene.

There are different types of clipping algorithms, depending on the type of graphical object and the shape of the clipping region. Some of the common 2-D clipping algorithms are:

- Point clipping: This algorithm determines whether a given point lies inside or outside the clipping region, and discards the point if it is outside. The clipping region can be a rectangle, a circle, or a polygon. A simple way to perform point clipping is to compare the coordinates of the point with the boundaries of the clipping region, and check if the point satisfies the inclusion criteria. For example, for a rectangular clipping region with coordinates (xmin, ymin) and (xmax, ymax), a point (x, y) is inside the region if and only if xmin <= x <= xmax and ymin <= y <= ymax.

- Line clipping: This algorithm determines the visible portion of a line segment that lies inside the clipping region, and discards the rest. The clipping region can be a rectangle, a polygon, or a curve. There are several line clipping algorithms, such as the Cohen-Sutherland algorithm, the Liang-Barsky algorithm, the Cyrus-Beck algorithm, and the Nicholl-Lee-Nicholl algorithm. These algorithms use different techniques to find the intersection points of the line segment with the clipping region, and to classify the endpoints of the line segment as inside or outside the region. For example, the Cohen-Sutherland algorithm divides the 2-D space into nine regions, and assigns a 4-bit code to each endpoint based on its position relative to the clipping region. Then, it uses bitwise operations and logical tests to determine if the line segment is trivially accepted, trivially rejected, or partially clipped.

- Polygon clipping: This algorithm determines the visible portion of a polygon that lies inside the clipping region, and discards the rest. The clipping region can be a rectangle, a polygon, or a curve. There are several polygon clipping algorithms, such as the Sutherland-Hodgman algorithm, the Weiler-Atherton algorithm, the Greiner-Hormann algorithm, and the Vatti algorithm. These algorithms use different techniques to find the intersection points of the polygon edges with the clipping region, and to construct a new polygon that represents the clipped portion. For example, the Sutherland-Hodgman algorithm clips a polygon against each edge of the clipping region, and outputs a new polygon that is inside the current edge. It repeats this process for all the edges of the clipping region, and obtains the final clipped polygon.

- Curve clipping: This algorithm determines the visible portion of a curve that lies inside the clipping region, and discards the rest. The clipping region can be a rectangle, a polygon, or a curve. There are several curve clipping algorithms, such as the Bezier clipping algorithm, the B-spline clipping algorithm, and the NURBS clipping algorithm. These algorithms use different techniques to find the intersection points of the curve with the clipping region, and to split the curve into sub-curves that are inside or outside the region. For example, the Bezier clipping algorithm uses a recursive subdivision technique to approximate the Bezier curve by a series of line segments, and then applies a line clipping algorithm to each segment.



### Line clipping algorithms

Line clipping algorithms are methods to remove parts of lines that lie outside a specified region, such as a viewport or a view volume. Line clipping is useful for rendering only the visible parts of a scene and avoiding unnecessary computations for the invisible parts. Line clipping algorithms typically work by testing the endpoints of each line segment against the boundaries of the clipping region and determining whether the line segment is inside, outside, or partially inside the region. If the line segment is partially inside, the algorithm computes the intersection points of the line segment and the clipping boundaries and clips the line segment accordingly. There are several line clipping algorithms, but two of the most common ones are:

- **Cohen–Sutherland algorithm**: This algorithm divides the 2D space into nine regions, of which only the middle one is the viewport. Each region is assigned a 4-bit code, called the outcode, that indicates which boundaries the region lies outside of. For example, the outcode 1001 means that the region is above and to the left of the viewport. The algorithm then compares the outcodes of the endpoints of each line segment and applies the following rules:

  - If both outcodes are zero, the line segment is completely inside the viewport and no clipping is needed.
  - If the bitwise AND of the outcodes is nonzero, the line segment is completely outside the viewport and can be discarded.
  - If neither of the above cases apply, the line segment is partially inside the viewport and the algorithm finds an intersection point of the line segment and one of the clipping boundaries. The algorithm then replaces the endpoint with the nonzero outcode with the intersection point and repeats the process until one of the above cases apply.

- **Liang–Barsky algorithm**: This algorithm is based on the parametric equation of a line segment, which can be written as:

  - `x = x1 + t * (x2 - x1)`
  - `y = y1 + t * (y2 - y1)`

  where `(x1, y1)` and `(x2, y2)` are the endpoints of the line segment and `t` is a parameter that ranges from 0 to 1. The algorithm then uses the inequalities that define the clipping region to find the values of `t` that correspond to the intersection points of the line segment and the clipping boundaries. The algorithm then clips the line segment by using the minimum and maximum values of `t` that lie within the range of 0 to 1.



### Cohen Sutherland line clipping algorithm

- Line clipping is the process of removing the portions of a line that are outside a given rectangular window, while preserving the portions that are inside or on the boundary of the window.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport).
- The algorithm can be outlined as follows:

  - Nine regions are created, eight "outside" regions and one "inside" region. Each region is assigned a 4-bit code, called the outcode, that indicates which of the four boundaries of the window the region is outside of. The outcode for the inside region is 0000, meaning it is not outside any boundary. The outcode for each outside region is obtained by bitwise ORing the codes for each boundary that the region is outside of. For example, the outcode for the top-right region is 1001, meaning it is outside the top and right boundaries.
  - For each line to be clipped, the outcodes of the two endpoints are computed. If both outcodes are 0000, the line is entirely inside the window and can be drawn without clipping. If the bitwise AND of the two outcodes is not 0000, the line is entirely outside the window and can be discarded. Otherwise, the line is partially inside the window and needs to be clipped.
  - To clip the line, one of the endpoints that is outside the window is selected and replaced by the intersection point of the line and the boundary that the endpoint is outside of. The outcode of the new endpoint is then recomputed and the process is repeated until the line is either accepted or rejected.

- The algorithm is efficient because it avoids unnecessary calculations and intersections by using the outcodes to quickly test the visibility of the line or its parts.
- The algorithm works only for rectangular windows. For other shapes of windows, other algorithms such as Cyrus Beck algorithm or Sutherland Hodgman algorithm are needed.
- The algorithm can be implemented using the following pseudocode:

```
function clipLine(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
  // compute the outcodes for the endpoints
  outcode1 = computeOutcode(x1, y1, xmin, ymin, xmax, ymax)
  outcode2 = computeOutcode(x2, y2, xmin, ymin, xmax, ymax)
  // loop until the line is either accepted or rejected
  while true:
    // if both outcodes are zero, the line is inside the window
    if outcode1 == 0 and outcode2 == 0:
      return (x1, y1, x2, y2) // accept the line
    // if the bitwise AND of the outcodes is not zero, the line is outside the window
    elif outcode1 & outcode2 != 0:
      return None // reject the line
    // otherwise, the line is partially inside the window and needs to be clipped
    else:
      // select one of the endpoints that is outside the window
      if outcode1 != 0:
        outcode = outcode1
      else:
        outcode = outcode2
      // find the intersection point of the line and the boundary that the endpoint is outside of
      if outcode & 1000: // top boundary
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
        y = ymax
      elif outcode & 0100: // bottom boundary
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
        y = ymin
      elif outcode & 0010: // right boundary
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
      elif outcode & 0001: // left boundary
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
      // replace the endpoint with the intersection point and recompute the outcode
      if outcode == outcode1:
        x1 = x
        y1 = y
        outcode1 = computeOutcode(x1, y1, xmin, ymin, xmax, ymax

```




### Liang Barsky algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the faster parametric line-clipping algorithm.
- The algorithm uses the parametric equation of a line and inequalities describing the range of the clipping window to find the intersections between the line and the window  .
- The parametric equation of a line is given by:

    ```
    x = x1 + u * (x2 - x1)
    y = y1 + u * (y2 - y1)
    ```

    where `(x1, y1)` and `(x2, y2)` are the endpoints of the line and `u` is a parameter that varies from 0 to 1.
- The inequalities describing the range of the clipping window are given by:

    ```
    xmin <= x <= xmax
    ymin <= y <= ymax
    ```

    where `(xmin, ymin)` and `(xmax, ymax)` are the coordinates of the lower-left and upper-right corners of the window respectively.
- The algorithm works by finding the values of `u` that satisfy the inequalities for each edge of the window and then taking the maximum of the lower values and the minimum of the upper values as the final values of `u` that define the visible portion of the line .
- The algorithm can be summarized by the following steps:

    1. Initialize the lower and upper values of `u` as `u1 = 0` and `u2 = 1`.
    2. For each edge of the window, calculate the value of `p` and `q` as follows:

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
        - If `p < 0`, then the line intersects the edge from inside to outside, so calculate `r = q / p` and update `u1 = max(u1, r)`.
        - If `p > 0`, then the line intersects the edge from outside to inside, so calculate `r = q / p` and update `u2 = min(u2, r)`.
        - If `p = 0` and `q >= 0`, then the line is parallel to and inside the edge, so do nothing.

    4. If `u1 > u2`, then the line is outside the window, so reject the line and exit the algorithm.
    5. Otherwise, the line is partially or completely inside the window, so accept the line and calculate the visible endpoints as follows:

        ```
        x'1 = x1 + u1 * (x2 - x1)
        y'1 = y1 + u1 * (y2 - y1)
        x'2 = x1 + u2 * (x2 - x1)
        y'2 = y1 + u2 * (y2 - y1)
        ```

- The algorithm can be illustrated by the following example:

    Liang Barsky example

    - The line has endpoints `(20, 10)` and `(30, 40)`.
    - The clipping window has coordinates `(10, 10)` and `(40, 30)`.
    - The values of `p` and `q` for each edge are:

        ```
        p = -(30 - 20) = -10 for the left edge
        q =

```




### Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a rectangular window or a convex polygon.
- Line clipping algorithms are useful for computer graphics applications, such as rendering, clipping, and visibility testing.
- There are different algorithms for line clipping, depending on the shape and properties of the clipping region. Some of the common algorithms are:

  - Cohen-Sutherland algorithm: This algorithm is based on dividing the 2D plane into nine regions, and assigning a four-bit code to each region. The code indicates whether the region is above, below, left, or right of the clipping window. The algorithm then compares the codes of the endpoints of the line, and determines whether the line is trivially accepted, trivially rejected, or needs further clipping. The algorithm is efficient for rectangular windows, but not for non-rectangular ones.
  - Cyrus-Beck algorithm: This algorithm is based on finding the parametric values of the intersection points of the line with the edges of the clipping polygon. The algorithm then uses these values to determine the visible portion of the line. The algorithm works for convex polygons, and allows line clipping for non-rectangular windows. The algorithm is more general than Cohen-Sutherland, but also more complex .
  - Liang-Barsky algorithm: This algorithm is an improvement of the Cohen-Sutherland algorithm, that avoids unnecessary intersection calculations. The algorithm uses the parametric equation of the line, and the inequalities that define the clipping window, to find the values of the parameter that correspond to the visible portion of the line. The algorithm is faster and more robust than Cohen-Sutherland, but still only works for rectangular windows.
  - Sutherland-Hodgman algorithm: This algorithm is based on clipping the line against each edge of the clipping polygon, one at a time. The algorithm uses the concept of inside and outside tests, to determine whether a point is inside or outside the clipping edge. The algorithm then generates a new line segment, that is either the same as the original one, or a portion of it, or an intersection point with the edge. The algorithm works for any polygon, but is more efficient for convex ones.
  - Nicholl-Lee-Nicholl algorithm: This algorithm is an extension of the Sutherland-Hodgman algorithm, that avoids redundant calculations and improves the accuracy of the intersection points. The algorithm uses a modified inside and outside test, that takes into account the direction of the line and the edge. The algorithm also uses a special case for horizontal and vertical lines, to avoid division by zero errors. The algorithm works for any polygon, but is more efficient for convex ones.

- The choice of the line clipping algorithm depends on the shape and properties of the clipping region, the number and length of the lines, and the desired accuracy and performance. Some of the factors to consider are:

  - Rectangular vs non-rectangular: Some algorithms, such as Cohen-Sutherland and Liang-Barsky, are designed for rectangular windows, and cannot handle non-rectangular ones. Other algorithms, such as Cyrus-Beck and Sutherland-Hodgman, can handle non-rectangular windows, but may be more complex or slower than the rectangular ones.
  - Convex vs non-convex: Some algorithms, such as Cyrus-Beck and Nicholl-Lee-Nicholl, are designed for convex polygons, and may not work correctly for non-convex ones. Other algorithms, such as Sutherland-Hodgman, can handle non-convex polygons, but may be less efficient or more prone to errors than the convex ones.
  - Number and length of lines: Some algorithms, such as Cohen-Sutherland and Liang-Barsky, are more efficient for a large number of short lines, as they can quickly reject the lines that are outside the window. Other algorithms, such as Cyrus-Beck and Sutherland-Hodgman, are more efficient for a small number of long lines, as they can clip the lines with fewer intersection calculations.
  - Accuracy and performance: Some algorithms, such as Cohen-Sutherland and Liang-Barsky, use integer arithmetic and bitwise operations, which are fast and accurate, but may cause rounding errors or overflow. Other algorithms, such as Cyrus-Beck and Sutherland-Hodgman, use floating-point arithmetic and geometric operations, which are more precise and robust, but may cause numerical errors or instability.



### Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - To prevent undesirable effects when displaying polygons on the output device.
  - To render 3D images through hidden surface removal techniques.
  - To produce high-quality surface details using techniques such as beam tracing.
  - To distribute the objects of a scene to appropriate processors in multiprocessor raytracing systems to improve rendering speeds.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against a convex clipping window by processing each polygon edge against each window edge in a sequential manner. The output is a sequence of vertices that define the clipped polygon boundaries .
  - Weiler-Atherton algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersections of the polygon edges and the window edges, and then tracing the boundary of the clipped polygon using a winding number rule.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersections of the polygon edges and the window edges, and then using a parity test to determine the inside and outside regions of the clipped polygon.
- Polygon clipping can be illustrated by the following diagrams:

Polygon clipping example

Figure 1: A polygon and a clipping window

Polygon clipping result

Figure 2: The result of polygon clipping



# Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon, and processes them against each edge of the clip polygon in a clockwise order .
- For each edge of the clip polygon, the algorithm generates a new list of vertices by examining each pair of consecutive vertices in the input list and applying the following rules :
  - If both vertices are inside the clip edge, output the second vertex.
  - If the first vertex is outside and the second vertex is inside, output the intersection point of the edge and the clip boundary, followed by the second vertex.
  - If the first vertex is inside and the second vertex is outside, output the intersection point of the edge and the clip boundary.
  - If both vertices are outside, output nothing.
- The output list of vertices becomes the input list for the next clip edge, until all edges are processed .
- The final output list contains the vertices of the clipped polygon .

The following diagram illustrates the algorithm for a simple example:

Sutherland Hodgeman polygon clipping example

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on Weiler and Atherton polygon clipping for the Unit 2 - Transformations in the subject of Computer Graphics.

# Weiler and Atherton polygon clipping

- Polygon clipping is the process of cutting out a part of a polygon that lies outside a given clipping region, such as a window or a viewport.
- Weiler and Atherton polygon clipping is an algorithm that can clip any polygon, including concave polygons and polygons with holes, by an arbitrarily shaped clipping polygon  .
- The algorithm works by finding the intersection points of the subject polygon and the clipping polygon, and labeling them as entry or exit points depending on the direction of the polygon edges  .
- The algorithm then traverses the subject polygon from any entry point, and switches to the clipping polygon whenever it encounters an exit point, until it returns to the starting point  .
- The algorithm may produce one or more clipped polygons, depending on the number and location of the intersection points  .
- The algorithm can handle cases where the subject polygon is completely inside, completely outside, or partially overlapping the clipping polygon  .

## Example

- Consider the following example of clipping a subject polygon (abcdhHIga) by a clipping polygon (BCDEFGA):

Example of Weiler and Atherton polygon clipping

- The algorithm first finds the intersection points of the two polygons, and labels them as entry or exit points. The entry points are marked with solid circles, and the exit points are marked with hollow circles:

Intersection points of the two polygons

- The algorithm then starts from any entry point, say b, and follows the subject polygon until it reaches an exit point, say d. It then switches to the clipping polygon and follows it until it reaches an entry point, say g. It then switches back to the subject polygon and follows it until it returns to the starting point, b. This forms one clipped polygon (bdgab):

One clipped polygon (bdgab)

- The algorithm then repeats the same process for the remaining entry points, h and I, and forms two more clipped polygons (hdh) and (IgI):

Two more clipped polygons (hdh) and (IgI)

- The algorithm then outputs the three clipped polygons as the result of the clipping operation:

The result of the clipping operation



# Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest, called a clip window.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping, because curves are not linear and may have multiple intersections with the clip window .
- Curve clipping requires more processing than for objects with linear boundaries, and may result in new curves or segments after clipping.
- There are different algorithms for curve clipping, depending on the type of curve and the shape of the clip window. Some examples are:
  - Cohen-Sutherland algorithm for line clipping
  - Sutherland-Hodgman algorithm for polygon clipping
  - Liang-Barsky algorithm for parametric line clipping
  - Cyrus-Beck algorithm for convex polygon clipping
  - Midpoint subdivision algorithm for Bezier curve clipping
  - Nicholl-Lee-Nicholl algorithm for circular arc clipping
- The general steps for curve clipping are:
  - Divide the curve into small segments or sub-curves
  - Test each segment or sub-curve against the clip window
  - Discard the segments or sub-curves that are completely outside the clip window
  - Clip the segments or sub-curves that are partially inside and partially outside the clip window
  - Join the remaining segments or sub-curves that are completely inside the clip window
- The following figure shows an example of curve clipping, where a Bezier curve is clipped against a rectangular clip window:

Curve clipping example



# Text clipping

Text clipping is a process of removing the characters or parts of characters that are outside the clipping window in computer graphics. It depends on the methods used to generate characters and the requirements of a particular application. There are three methods for text clipping which are listed below :

- **All or none string clipping method**: In this method, if the whole string is inside the clipping window, then it is displayed. Otherwise, the entire string is discarded. This method is simple and fast, but it may result in loss of information or incomplete text.

- **Text clipping method**: In this method, only the characters that are completely inside the clipping window are displayed. The characters that overlap the window boundary are partially clipped, meaning that only the portion that is inside the window is displayed. This method preserves more information than the previous one, but it may produce distorted or unreadable characters.

- **Precise character clipping method**: In this method, each character is treated as a polygon and clipped using a polygon clipping algorithm. This method produces the most accurate and readable text, but it is also the most complex and time-consuming one. This method is suitable for applications that require high-quality text rendering.



## Unit 3 - Three Dimensional

- In this unit, you will learn about the concepts and applications of three dimensional geometry.
- You will learn how to represent points, lines, planes and solids in three dimensional space using Cartesian coordinates, vectors and equations.
- You will learn how to calculate distances, angles, areas and volumes of various geometric shapes and figures in three dimensional space.
- You will learn how to perform transformations such as translation, rotation, reflection and scaling on three dimensional objects.
- You will learn how to use matrices and determinants to simplify calculations and solve problems involving three dimensional geometry.
- You will learn how to apply the concepts of three dimensional geometry to real world situations such as engineering, architecture, physics and computer graphics.



Hello, I am Sydney, your AI assistant. I can help you with your topic of 3-D Geometric Primitives. Here are some notes that you can use for your study material:

### 3-D Geometric Primitives

- 3-D geometric primitives are basic geometric forms that can be used to model more complex 3-D shapes and objects.
- They are also called 3-D primitives or simply primitives.
- The most common 3-D primitives are cubes, pyramids, cones, spheres, cylinders, and tori (doughnuts).
- These primitives can be modified with transforms (such as scaling, rotating, and translating) and Booleans (such as union, intersection, and difference) to create new shapes and objects.
- These primitives can also have a resolution level assigned to them, which determines how smooth or faceted they look by changing the number of sides and steps used to define them.
- Some 3-D primitives can be created by lathing or extruding 2-D shapes, such as circles, rectangles, and polygons.
- Some 3-D primitives can be defined by curves, such as Bézier curves, NURBS curves, and splines, which can be used to create smooth and organic shapes and objects.
- Some examples of 3-D primitives and their properties are:

  - Cube: A cube is a 3-D primitive that has six square faces, eight vertices, and twelve edges. It can be defined by its center point and its edge length, or by two opposite vertices. It can also be called a hexahedron.
  - Pyramid: A pyramid is a 3-D primitive that has a polygonal base and triangular faces that meet at a common vertex, called the apex. It can be defined by its base shape, its base center point, its height, and its apex point. It can also be called a polyhedron.
  - Cone: A cone is a 3-D primitive that has a circular base and a curved surface that narrows to a point, called the vertex. It can be defined by its base center point, its base radius, its height, and its vertex point. It can also be called a conic solid.
  - Sphere: A sphere is a 3-D primitive that has a round surface that is equidistant from a fixed point, called the center. It can be defined by its center point and its radius. It can also be called a ball or a globe.
  - Cylinder: A cylinder is a 3-D primitive that has two parallel circular bases and a curved surface that connects them. It can be defined by its base center point, its base radius, its height, and its axis of symmetry. It can also be called a circular prism.
  - Torus: A torus is a 3-D primitive that has a ring-shaped surface that is generated by rotating a circle around an axis that does not intersect the circle. It can be defined by its center point, its major radius (the distance from the center to the circle), its minor radius (the radius of the circle), and its axis of rotation. It can also be called a doughnut or a ring.



### 3-D Object Representation

- In 3D computer graphics, a 3D object is a mathematical representation of any three-dimensional object that can be displayed on a screen.
- A 3D object can be created by using specialized software that allows the user to manipulate edges, vertices, and polygons in a simulated 3D space.
- There are different methods to represent a 3D object, such as:
  - Boundary representations (B-reps): It describes a 3D object as a set of surfaces that separates the object interior from the environment. Examples of B-reps are polygon meshes, NURBS surfaces, and subdivision surfaces.
  - Space-partitioning representations: It describes the interior properties of a 3D object by dividing the space into regions. Examples of space-partitioning representations are octrees, BSP trees, and voxels.
  - Implicit representations: It describes a 3D object as a function that evaluates to a positive or negative value depending on whether a point is inside or outside the object. Examples of implicit representations are algebraic surfaces, metaballs, and level sets.
  - Parametric representations: It describes a 3D object as a function that maps a set of parameters to a point in 3D space. Examples of parametric representations are curves, surfaces, and solids of revolution.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on 3-D Transformation for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics. Here is the content in markdown format:

# 3-D Transformation

## Introduction

- A 3-D transformation is a process of changing the position, orientation, size, or shape of a 3-D object in a 3-D space.
- A 3-D transformation can be represented by a 4x4 matrix that operates on a 3-D point or vector in homogeneous coordinates.
- A 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve parallelism, ratios of distances, and angles between lines, but not lengths or areas. Examples of affine transformations are translation, rotation, scaling, and shear.
- Non-affine transformations do not preserve any of the properties of affine transformations. Examples of non-affine transformations are perspective and curved transformations.

## Translation

- Translation is a 3-D transformation that moves a 3-D object by a given displacement vector.
- Translation can be represented by the following matrix:

```
| 1  0  0  tx |
| 0  1  0  ty |
| 0  0  1  tz |
| 0  0  0  1  |
```

- Where tx, ty, and tz are the components of the displacement vector along the x, y, and z axes, respectively.
- To translate a 3-D point (x, y, z, 1) by the displacement vector (tx, ty, tz), we multiply the point by the translation matrix:

```
| 1  0  0  tx |   | x |   | x + tx |
| 0  1  0  ty | * | y | = | y + ty |
| 0  0  1  tz |   | z |   | z + tz |
| 0  0  0  1  |   | 1 |   |   1    |
```

- Translation is a commutative operation, meaning that the order of applying multiple translations does not matter.

## Rotation

- Rotation is a 3-D transformation that rotates a 3-D object around a given axis by a given angle.
- Rotation can be represented by the following matrix:

```
| r11 r12 r13 0 |
| r21 r22 r23 0 |
| r31 r32 r33 0 |
| 0   0   0   1 |
```

- Where r11, r12, r13, r21, r22, r23, r31, r32, and r33 are the elements of the rotation matrix, which depend on the axis and angle of rotation.
- To rotate a 3-D point (x, y, z, 1) around an axis by an angle, we multiply the point by the rotation matrix:

```
| r11 r12 r13 0 |   | x |   | r11*x + r12*y + r13*z |
| r21 r22 r23 0 | * | y | = | r21*x + r22*y + r23*z |
| r31 r32 r33 0 |   | z |   | r31*x + r32*y + r33*z |
| 0   0   0   1 |   | 1 |   |          1            |
```

- Rotation is not a commutative operation, meaning that the order of applying multiple rotations matters.
- There are three common axes of rotation in 3-D space: x-axis, y-axis, and z-axis. The rotation matrices for each axis are:

```
Rotation around x-axis by angle θ:

| 1   0    0   0 |
| 0  cosθ -sinθ 0 |
| 0  sinθ  cosθ 0 |
| 0   0    0   1 |

Rotation around y-axis by angle θ:

|  cosθ 0  sinθ 0 |
|   0   1   0   0 |
| -sinθ 0  cosθ 0 |
|   0   0   0   1 |

Rotation around z-axis by angle θ:

| cosθ -sinθ 0 0 |
| sinθ  cosθ 0 0 |
|  0

```




### 3-D viewing in computer graphics

3-D viewing is the process of displaying 3-D objects on a 2-D screen, such as a monitor or a projector. 3-D viewing involves the following steps:

- **Modeling transformation**: This step defines the shape, size, and position of the 3-D objects in a 3-D coordinate system, called the world coordinate system.
- **Viewing transformation**: This step defines the position and orientation of the virtual camera, or the viewer, in the world coordinate system. The camera has a location, a direction, and a view volume, which is the region of the 3-D space that is visible to the camera.
- **Projection transformation**: This step maps the 3-D objects in the view volume to a 2-D plane, called the projection plane or the view plane. The projection can be either perspective or orthographic, depending on how the view volume is shaped.
- **Viewport transformation**: This step maps the 2-D image on the projection plane to a specific region on the screen, called the viewport. The viewport can have a different size and aspect ratio than the projection plane.

There are different methods and techniques for performing 3-D viewing, such as matrix transformations, clipping algorithms, hidden surface removal, shading, and lighting. 3-D viewing is an essential component of 3-D computer graphics, which is the field of creating and manipulating 3-D objects and scenes using computer software. 3-D computer graphics has many applications, such as animation, video games, virtual reality, computer-aided design, and scientific visualization. 3-D computer graphics also involves the use of artificial intelligence to generate realistic and interactive 3-D images. Some examples of 3-D computer graphics software are Blender, Maya, SketchUp, and Microsoft 3D Viewer.



# Projections for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

## Introduction

Projection is a technique or process which is used to transform a 3D object into a 2D plane. Projection is necessary because the display devices are usually 2D and we need to display the 3D objects on them. Projection can be classified into two types: parallel projection and perspective projection.

## Parallel Projection

Parallel projection discards z-coordinate and parallel lines from each vertex on the object are extended until they intersect the view plane. Parallel projection can be further divided into orthographic projection, oblique projection and isometric projection.

### Orthographic Projection

In orthographic projection, the direction of projection is normal to the projection plane. Orthographic projection can be used to show the true shape and size of the object. Orthographic projection can be subdivided into three types: axonometric projection, dimetric projection and trimetric projection.

#### Axonometric Projection

Axonometric projection is a type of orthographic projection that shows more than one side of an object. In axonometric projection, the direction of projection makes equal angles with all the three principal axes of the object. Axonometric projection can be used to create a realistic view of the object.

#### Dimetric Projection

Dimetric projection is a type of orthographic projection that shows two sides of an object. In dimetric projection, the direction of projection makes equal angles with respect to two principal axes of the object, but not the third one. Dimetric projection can be used to create a balanced view of the object.

#### Trimetric Projection

Trimetric projection is a type of orthographic projection that shows three sides of an object. In trimetric projection, the direction of projection makes unequal angles with respect to all the three principal axes of the object. Trimetric projection can be used to create a general view of the object.

### Oblique Projection

In oblique projection, the direction of projection is not normal to the projection plane, but is inclined to it. Oblique projection can be used to show the depth of the object. Oblique projection can be classified into two types: cavalier projection and cabinet projection.

#### Cavalier Projection

Cavalier projection is a type of oblique projection where the projection lines are perpendicular to the projection plane. In cavalier projection, the length of the projection lines are equal to the actual length of the object. Cavalier projection can be used to create a simple and quick view of the object.

#### Cabinet Projection

Cabinet projection is a type of oblique projection where the projection lines are not perpendicular to the projection plane, but are inclined to it by an angle of 45 degrees. In cabinet projection, the length of the projection lines are half of the actual length of the object. Cabinet projection can be used to create a more realistic and less distorted view of the object.

### Isometric Projection

Isometric projection is a special case of axonometric projection where the direction of projection makes equal angles of 120 degrees with all the three principal axes of the object. In isometric projection, the object appears as if it is rotated by 45 degrees along the vertical axis and then tilted by 35.26 degrees along the horizontal axis. Isometric projection can be used to create a symmetrical and uniform view of the object.

## Perspective Projection

Perspective projection is a type of projection where the projection lines are not parallel, but converge at a single point called the center of projection or the eye point. Perspective projection can be used to create a realistic and natural view of the object. Perspective projection can be classified into two types: one-point perspective and two-point perspective.

### One-Point Perspective

One-point perspective is a type of perspective projection where the projection plane is parallel to one of the principal axes of the object, and the center of projection is on the opposite axis. In one-point perspective, the object appears as if it is receding towards a single vanishing point on the projection plane. One-point perspective can be used to create a dramatic and dynamic view of the object.

### Two-Point Perspective

Two-point perspective is a type of perspective projection where the projection plane is parallel to none of the principal axes of the object, and the center of projection is on a diagonal axis. In two-point perspective, the object appears as



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on 3-D Clipping for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics.

### 3-D Clipping
- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene.
- The purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects.
- 3-D clipping can be done in two basic steps:
  - Discard objects that cannot be viewed, such as objects that are behind the camera, outside the field of view, or too far away. This can be done by comparing the object's bounding box or sphere against the dimensions of the view volume, either before or after projection.
  - Clip objects that intersect with any clipping plane, such as the near and far planes, or the left, right, top and bottom planes of the view volume. This can be done by using algorithms such as Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman, or Cyrus-Beck, which are extensions of the 2-D clipping algorithms to 3-D space.
- 3-D clipping can also be applied to higher dimensions, such as 4-D or 5-D, by using hyperplanes or hyperspheres as clipping regions.
- 3-D clipping can also be used to create effects such as fog, depth of field, or shadows, by modifying the clipping planes or the color and intensity of the clipped fragments.



Hello, I am Sydney, your AI assistant. I can help you with your study material on curves and surfaces. Here is an overview of the topic:

## Unit 4 - Curves and Surfaces

- A curve is a one-dimensional object that can be represented by a function of one or more parameters, such as x(t), y(t), z(t).
- A surface is a two-dimensional object that can be represented by a function of two or more parameters, such as x(u,v), y(u,v), z(u,v).
- Curves and surfaces can be classified into different types based on their properties, such as degree, continuity, smoothness, curvature, etc.
- Some common types of curves are:
  - Line: a curve of degree one that has constant direction and zero curvature.
  - Circle: a curve of degree two that has constant curvature and lies on a plane.
  - Ellipse: a curve of degree two that has varying curvature and lies on a plane.
  - Parabola: a curve of degree two that has varying curvature and lies on a plane that is parallel to the axis of symmetry.
  - Hyperbola: a curve of degree two that has varying curvature and lies on two planes that intersect at the axis of symmetry.
  - Bezier curve: a curve of degree n that is defined by n+1 control points and a polynomial basis function.
  - B-spline curve: a curve of degree n that is defined by a set of control points and a knot vector that determines the domain and continuity of the curve.
  - NURBS curve: a curve of degree n that is defined by a set of control points, a knot vector, and a set of weights that determine the shape of the curve.
- Some common types of surfaces are:
  - Plane: a surface of degree one that has constant normal direction and zero curvature.
  - Sphere: a surface of degree two that has constant curvature and is symmetric about a center point.
  - Ellipsoid: a surface of degree two that has varying curvature and is symmetric about three axes.
  - Paraboloid: a surface of degree two that has varying curvature and is symmetric about an axis of revolution.
  - Hyperboloid: a surface of degree two that has varying curvature and is symmetric about two axes of revolution.
  - Bezier surface: a surface of degree m x n that is defined by (m+1) x (n+1) control points and a tensor product of polynomial basis functions.
  - B-spline surface: a surface of degree m x n that is defined by a set of control points and two knot vectors that determine the domain and continuity of the surface.
  - NURBS surface: a surface of degree m x n that is defined by a set of control points, two knot vectors, and a set of weights that determine the shape of the surface.
- Curves and surfaces can be manipulated by applying transformations, such as translation, rotation, scaling, shearing, etc.
- Curves and surfaces can be analyzed by computing their derivatives, such as tangent, normal, binormal, curvature, torsion, etc.
- Curves and surfaces can be rendered by using various techniques, such as polygonal approximation, subdivision, ray tracing, etc.



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
- When a quadric surface intersects a coordinate plane, the trace is a conic section. For example, a sphere is a quadric surface that has circular traces, and an elliptic paraboloid is a quadric surface that has elliptic or parabolic traces.
- Ray tracing or ray firing is a popular method used for realistic renderings of quadric surfaces. It involves finding the intersection points of a ray with a quadric surface, which can be done by solving a quadratic equation.



### Spheres

- A sphere is a three-dimensional object that has a round shape and a constant radius from its center.
- In computer graphics, spheres are often used to model objects such as balls, planets, bubbles, etc.
- Spheres can be represented mathematically by the equation: x^2 + y^2 + z^2 = r^2, where r is the radius and (x, y, z) are the coordinates of any point on the sphere.
- Spheres can also be defined parametrically by the equations: x = r * cos(u) * sin(v), y = r * sin(u) * sin(v), z = r * cos(v), where r is the radius and (u, v) are the spherical angles.
- Spheres can be approximated by simpler objects constructed from flat polygons (polyhedra) by dividing the sphere into segments along lines of longitude and latitude. The segments can be either quadrilaterals or triangles, depending on the number of divisions.
- Spheres can be rendered in computer graphics by using various techniques, such as ray tracing, rasterization, texture mapping, lighting, shading, etc.
- Spheres have some properties that make them useful in computer graphics, such as:
  - They are easy to transform, rotate, and scale by applying matrix operations to their center and radius.
  - They have a simple normal vector at any point, which is the same as the direction from the center to the point.
  - They have a simple distance function, which is the difference between the radius and the distance from the center to any point.
  - They can be used as bounding volumes, which are simple shapes that enclose more complex objects and can be used for collision detection, culling, etc.



### Ellipsoid

An ellipsoid is a surface that may be obtained from a sphere by deforming it by means of directional scalings, or more generally, of an affine transformation. An ellipsoid is a quadric surface; that is, a surface that may be defined as the zero set of a polynomial of degree two in three variables.

Some properties of an ellipsoid are:

- An ellipsoid is symmetrical about three mutually perpendicular axes that intersect at the center. These axes are called the principal axes of the ellipsoid, and their lengths are called the principal semi-axes.
- The general equation of an ellipsoid with principal semi-axes a, b, and c is:

```math
\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1
```

- If a = b = c, the ellipsoid is a sphere.
- If a = b > c, the ellipsoid is an oblate spheroid (a flattened sphere).
- If a = b < c, the ellipsoid is a prolate spheroid (an elongated sphere).
- If a, b, and c are all different, the ellipsoid is a scalene ellipsoid.

An ellipsoid is useful for computer graphics modeling because it can represent a variety of shapes with different degrees of roundness and smoothness. Superquadric ellipsoids and toroids are recent geometric shapes that can model more complex objects with sharp edges and corners.



### Blobby objects

- Blobby objects are a type of **implicit modeling** technique in computer graphics  .
- Implicit modeling is a way of representing surfaces by **distance functions**  .
- Distance functions are mathematical functions that assign a scalar value to each point in space, indicating how far or close the point is to the surface  .
- Blobby objects are also known as **metaballs** , which are spherical objects that can merge or split depending on their proximity and influence.
- Blobby objects are used to model **non-rigid** and **fluid-like** objects, such as cloth, rubber, liquids, water droplets, etc  .
- Blobby objects can change their shape and size based on their states, such as temperature, pressure, or external forces  .
- Blobby objects are defined by a set of **parameters**, such as position, radius, and strength.
- Blobby objects are rendered by **evaluating** the distance function at each pixel and applying a **threshold** to determine whether the pixel is inside or outside the surface.
- Blobby objects can create **smooth** and **organic** shapes that are difficult to achieve with other modeling techniques.



# Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points .
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics .
- Splines can be classified into different types based on their degree, continuity, and basis functions.
- Some common types of splines are:
  - Linear splines: splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: splines of degree two that consist of parabolic segments that join at the given points.
  - Cubic splines: splines of degree three that have smooth transitions at the given points and can approximate any smooth curve.
  - Bezier curves: splines that are defined by a set of control points that influence the shape of the curve .
  - B-splines: splines that are defined by a set of basis functions that have local support and can be modified by changing the knot vector .
  - NURBS: non-uniform rational B-splines that are generalizations of B-splines that can represent conic sections and rational curves .
- Splines have many properties and applications in computer graphics, such as:
  - Affine invariance: splines are invariant under affine transformations, such as rotation, translation, scaling, and shearing.
  - Interpolation: splines can pass through the given points exactly or approximate them with some error.
  - Approximation: splines can approximate any smooth curve or surface with arbitrary precision by increasing the number of control points or knots.
  - Subdivision: splines can be subdivided into smaller splines without changing the shape of the curve or surface.
  - Rendering: splines can be rendered efficiently by using algorithms such as de Casteljau's algorithm, de Boor's algorithm, or Cox-de Boor's algorithm.



# Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline or basis spline is a piecewise polynomial function with specific properties that determine the polynomial degree/order .
- The idea behind using a B-spline curve is to determine a unique polynomial representation of a set of data, whether that data be structural points in 3D space or a set of data on a graph.
- A B-spline function is a combination of flexible bands that is controlled by a number of points that are called control points, creating smooth curves .
- These functions are used to create and manage complex shapes and surfaces using a number of points.
- A B-spline curve can be defined by the following equation:

B-spline curve equation

where *n* is the number of control points, *p* is the degree of the curve, *N* is the basis function, and *P* is the control point.

- The basis function *N* is defined by the following recursive formula:

B-spline basis function

where *t* is the parameter, and *u* is the knot vector.

- The knot vector *u* is a non-decreasing sequence of real numbers that determines the domain and the shape of the curve.
- The degree *p* of the curve determines the smoothness and the number of segments of the curve.
- The control points *P* determine the position and the direction of the curve.

- Some properties of B-spline curves are:

  - They are invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - They have local control, meaning that changing one control point affects only a local part of the curve.
  - They have variation diminishing, meaning that the curve does not oscillate more than the control polygon.
  - They have convex hull property, meaning that the curve lies within the convex hull of the control points.
  - They have minimal support, meaning that each basis function has the smallest possible support for a given degree and smoothness.



### Bezier curves and surfaces

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling .
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them .
- They have the properties of continuity, smoothness, and local control, which make them highly useful and convenient for curve and surface design.
- They can be classified into different types based on the degree and number of control points, such as linear, quadratic, cubic, and higher-order Bezier curves and surfaces .
- They can be evaluated using the de Casteljau's algorithm, the Bernstein polynomial basis, or the matrix form.
- They can be modified by changing the position, weight, or number of control points, or by applying geometric transformations.
- They can be combined to form complex shapes, such as meshes, patches, or solids .

: Bézier surface - Wikipedia
: Computer Graphics Curve in Computer Graphics - GeeksforGeeks
: Bézier curve - Wikipedia



## Unit 5 - Hidden Lines and Surfaces

- Hidden lines and surfaces are used to represent the parts of an object that are not visible from a given viewpoint.
- Hidden lines are usually drawn as dashed or dotted lines on a drawing, while hidden surfaces are usually omitted or shaded differently.
- The purpose of hidden lines and surfaces is to show the shape and structure of an object more clearly and completely, and to avoid confusion or ambiguity.
- There are different methods and rules for drawing hidden lines and surfaces, depending on the type of projection, the complexity of the object, and the conventions of the field or industry.
- Some common methods and rules are:

  - In orthographic projection, hidden lines and surfaces are usually drawn on the front, top, and right views, but not on the other views, unless they are necessary for clarity.
  - In isometric projection, hidden lines and surfaces are usually omitted, unless they are essential for understanding the object.
  - In perspective projection, hidden lines and surfaces are usually omitted, as they are implied by the depth and shading of the object.
  - In section views, hidden lines and surfaces are usually omitted, as they are cut by the cutting plane and shown by the cross-hatching of the sectioned area.
  - In auxiliary views, hidden lines and surfaces are usually drawn, as they are projected from the principal views and show the true shape and size of the object.
  - In general, hidden lines and surfaces should be drawn only when they are necessary for clarity, and should be avoided when they clutter the drawing or create confusion.



# Back Face Detection Algorithm

- Back face detection, also known as plane equation method, is an object space method for identifying the visible surfaces of a polyhedron .
- A polyhedron is a solid object bounded by flat polygonal faces. Each face has a normal vector that points outward from the polyhedron.
- The normal vector of a face can be computed by taking the cross product of two non-parallel edges of the face.
- The back face detection algorithm is based on the assumption that the polyhedron is convex, meaning that any line segment joining two points inside or on the polyhedron is entirely contained within or on the polyhedron.
- The algorithm works as follows :
  - For each face of the polyhedron, compute its normal vector and its plane parameters (A, B, C, and D) using the equation Ax + By + Cz + D = 0.
  - For each face of the polyhedron, perform an inside-outside test on a reference point (x, y, z) that is known to be inside the polyhedron. This can be the centroid of the polyhedron or any other point that is guaranteed to be inside.
  - The inside-outside test is done by substituting the reference point into the plane equation and checking the sign of the result. If the result is positive, then the reference point is inside the face and the face is a back face. If the result is negative, then the reference point is outside the face and the face is a front face.
  - Discard all the back faces from the rendering process, as they are hidden by the front faces.
- The back face detection algorithm is a simple and fast way to eliminate hidden surfaces, but it has some limitations:
  - It only works for convex polyhedra. If the polyhedron is concave, some back faces may be visible and some front faces may be hidden.
  - It does not account for occlusion by other objects in the scene. If there are multiple polyhedra in the scene, some front faces may be hidden by other objects that are closer to the viewer.
  - It does not account for perspective projection. If the polyhedron is viewed from a perspective camera, some back faces may appear as front faces and vice versa, depending on the angle of view and the distance from the camera.



### Depth buffer method

- Depth buffer method, also known as z-buffer method, is an image-space technique for hidden surface removal in computer graphics  .
- It is based on the idea of storing the depth or z-coordinate of the closest object at each pixel in a buffer, and comparing the depth of new objects with the existing depth to determine visibility  .
- The depth buffer method has the following steps :
  - Initialize the depth buffer and the frame buffer for each pixel to some predefined values, such as the maximum depth and the background color.
  - For each polygon in the scene, project it onto the view plane and scan-convert it to find the pixels that it covers.
  - For each pixel, calculate the depth of the polygon at that pixel using the plane equation or an incremental method.
  - Compare the depth of the polygon with the depth stored in the depth buffer for that pixel. If the polygon depth is smaller, it means the polygon is closer to the viewer and should be visible. In that case, update the depth buffer with the new depth and the frame buffer with the color or intensity of the polygon. Otherwise, the polygon is farther away and should be hidden, so do nothing.
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
    - It can suffer from precision errors due to finite depth resolution, which can cause artifacts such as aliasing, flickering, and popping.
    - It does not handle transparency or overlapping polygons well, as it only stores the closest depth and color for each pixel.



### A-buffer method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- The A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects.
- It extends the algorithm of depth-buffer (or Z-buffer) method .
- It uses an A-buffer (or accumulation buffer) to store multiple fragments per pixel, each with its own depth and color values .
- It sorts the fragments in each pixel by depth and computes the final color by blending the fragments from front to back .
- It can handle anti-aliasing, area averaging, motion blur, depth of field, translucency, and shadows .
- It requires more memory and processing time than the depth-buffer method .
- It can be implemented using linked lists, arrays, or fixed-size buffers .



### Scan line method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The basic idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image from top to bottom, computing the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons and add newly-visible polygons .
- The scan line method can be applied to both wireframe and solid models, and can handle concave and convex polygons, as well as polygons with holes .
- The scan line method can also be extended to handle hidden surface removal in 3D, by using a depth buffer or a z-buffer to store the depth or z coordinate of the closest visible surface at each pixel, and comparing the depth of the current polygon with the depth buffer to determine if it is occluded or not .
- The scan line method has some advantages and disadvantages compared to other visible surface determination algorithms, such as ray tracing, z-buffer, painter's algorithm, etc. Some of the advantages are :
  - It is fast and efficient, as it exploits the coherence between adjacent scan lines and avoids unnecessary calculations for invisible pixels or polygons.
  - It is easy to implement and can be parallelized, as each scan line can be processed independently.
  - It can handle antialiasing, shading, and texture mapping, by interpolating the color, intensity, and texture coordinates along the scan line.
- Some of the disadvantages are :
  - It requires sorting the polygons by their y coordinates, which can be costly for large or complex scenes.
  - It requires maintaining and updating the active edge list, which can be complicated for polygons with multiple intersections or shared edges.
  - It can produce artifacts or errors for polygons that are nearly horizontal or nearly vertical, as the scan line may miss some pixels or intersect the same polygon twice.



### Basic Illumination Models

Illumination models are used to calculate the intensity and color of light that is reflected by a surface in a computer graphics scene. Illumination models can be classified into two categories: local and global. Local illumination models only consider the direct and local interaction of objects with light sources, while global illumination models account for all the interactions and exchange of light among objects, such as reflection, refraction, and shadows .

A basic local illumination model consists of three components: ambient light, diffuse reflection, and specular reflection .

- Ambient light: This is the background light that is present in the environment, regardless of the position and orientation of the surface. Ambient light is assumed to be constant and uniform, and it affects all surfaces equally. Ambient light is usually modeled as a constant term that is added to the final intensity of the surface .
- Diffuse reflection: This is the light that is reflected by a surface in all directions equally, depending on the angle between the surface normal and the light direction. Diffuse reflection is also known as Lambertian reflection, and it depends on the color and the diffuse reflectance coefficient of the surface. Diffuse reflection is usually modeled as a term that is proportional to the cosine of the angle between the surface normal and the light direction .
- Specular reflection: This is the light that is reflected by a surface in a mirror-like manner, depending on the angle between the surface normal, the light direction, and the viewer direction. Specular reflection is also known as Phong reflection, and it depends on the color, the specular reflectance coefficient, and the shininess of the surface. Specular reflection is usually modeled as a term that is proportional to the cosine of the angle between the reflected light direction and the viewer direction, raised to a power that controls the shininess .

The basic local illumination model can be expressed as:

I = I_a + I_d + I_s

where I is the final intensity of the surface, I_a is the ambient light intensity, I_d is the diffuse reflection intensity, and I_s is the specular reflection intensity .

The basic local illumination model can be applied to each pixel or polygon of a graphics object, depending on the shading technique used. Shading is the process of applying the illumination model to the graphics objects to compute the intensities and colors to display the surface. There are three common shading techniques: flat shading, Gouraud shading, and Phong shading.

- Flat shading: This is the simplest shading technique, where each polygon of the object is assigned a single intensity and color, based on the illumination model applied to the polygon's normal. Flat shading produces a faceted appearance of the object, and it does not account for the variation of the surface normal within the polygon.
- Gouraud shading: This is a shading technique that interpolates the intensities and colors of the vertices of the polygons, based on the illumination model applied to the vertex normals. Gouraud shading produces a smoother appearance of the object, and it accounts for the variation of the surface normal within the polygon. However, Gouraud shading does not handle specular highlights well, as they may be missed or distorted by the interpolation.
- Phong shading: This is a shading technique that interpolates the surface normals of the vertices of the polygons, and then applies the illumination model to each pixel of the polygon, based on the interpolated normal. Phong shading produces the most realistic appearance of the object, and it accounts for the variation of the surface normal and the specular highlights within the polygon. However, Phong shading is more computationally expensive than Gouraud shading, as it requires more calculations per pixel.

The basic illumination model and the shading techniques are the foundation of computer graphics, as they allow the creation of realistic and visually appealing images of 3D objects. However, the basic illumination model has some limitations, such as:

- It does not account for the global effects of light, such as shadows, reflection, refraction, and transparency .
- It does not account for the physical properties of light, such as wavelength, polarization, and interference .
- It does not account for the human perception of light, such as color, brightness, and contrast .

To overcome these limitations, more advanced illumination



### Ambient light

- Ambient light is a type of lighting that is used to create a realistic environment in computer graphics.
- It is usually a soft, warm light that is used to fill in the shadows and create a more natural look.
- It is the base brightness applied to textures rendered in a scene before any point, spot, or other types of virtual light sources are computed.
- It is made up of light that has been reflected many times and is no longer coming from a specific direction.
- It affects the appearance of the entire rendered scene by adding a uniform color and intensity to all surfaces.
- It can be used to simulate natural lightings, such as the sun, or artificial lighting, such as fluorescent lights.
- It is a very crude approximation of indirect lighting, which is the light that bounces off other surfaces and objects in the scene.
- It is often combined with other lighting techniques, such as ambient occlusion, which is a method to calculate how exposed each point in a scene is to ambient lighting.
- It is a simple and fast way to add some realism to computer graphics, but it can also create unrealistic results if not used carefully or combined with other lighting effects.



### Diffuse reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough .
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by the surrounding objects, which can reflect light onto the surface.
- This phenomenon is called diffuse interreflection and it adds more realism to the scene.
- Diffuse reflection can be modeled by the Lambertian reflectance, which assumes that the light intensity is proportional to the cosine of the angle between the light direction and the surface normal .
- The Lambertian reflectance can be expressed by the formula:

```math
I = k_d I_L \cos \theta
```

where:

- `I` is the reflected light intensity
- `k_d` is the diffuse reflection coefficient
- `I_L` is the incident light intensity
- `\theta` is the angle between the light direction and the surface normal

- The diffuse reflection coefficient `k_d` can be different for different wavelengths of light, resulting in different colors for the surface.
- The diffuse reflection coefficient can also vary across the surface, creating textures or patterns.



### Specular reflection

- Specular reflection is the phenomenon of light bouncing off a smooth and shiny surface in a single direction, creating a bright spot or highlight on the surface  .
- Specular reflection depends on the angle of incidence of the light ray, the angle of reflection of the light ray, and the viewing angle of the observer .
- The angle of incidence is equal to the angle of reflection, and both are measured with respect to the normal vector of the surface .
- The viewing angle is the angle between the normal vector of the surface and the line of sight of the observer .
- The intensity of the specular reflection is highest when the viewing angle is equal to the angle of reflection, and decreases as the viewing angle deviates from the angle of reflection .
- Specular reflection is influenced by the material properties of the surface, such as its reflectivity, roughness, and color  .
- Reflectivity is the fraction of incident light that is reflected by the surface  .
- Roughness is the degree of variation or irregularity of the surface microstructure .
- Color is the wavelength or frequency of the light that is reflected by the surface  .
- Specular reflection is modeled by various empirical formulas in computer graphics, such as the Phong model, the Blinn-Phong model, and the Cook-Torrance model   .
- These models use different mathematical functions to approximate the specular reflection intensity as a function of the angle of incidence, the angle of reflection, the viewing angle, and the material properties   .
- Specular reflection is important in computer graphics, as it provides a strong visual cue for the shape of an object and its location with respect to light sources in the scene  .



### Phong model

The Phong model is a widely used model for the local illumination of points on a surface in computer graphics. It was designed by Bui Tuong Phong in 1973 and is based on the empirical observation that the reflection of light from a surface can be divided into three components: ambient, diffuse, and specular.

- Ambient component: This represents the constant background light that is present in the environment and affects all surfaces equally. It is independent of the surface orientation and the light direction. It is usually modeled as a constant color multiplied by a surface reflectivity factor.
- Diffuse component: This represents the light that is scattered uniformly in all directions by a rough or matte surface. It depends on the angle between the surface normal and the light direction. It is usually modeled as the product of the light color, the surface color, and the cosine of the angle between the surface normal and the light direction, also known as the Lambertian cosine law.
- Specular component: This represents the light that is reflected in a preferred direction by a shiny or glossy surface. It depends on the angle between the surface normal, the light direction, and the view direction. It is usually modeled as the product of the light color, the surface specular color, and a power function of the cosine of the angle between the reflection direction and the view direction, also known as the Phong specular term.

The Phong model can be expressed mathematically as follows:

`I = k_a I_a + k_d I_d (N ⋅ L) + k_s I_s (R ⋅ V)^n`

where

- `I` is the resulting color of the surface point
- `k_a`, `k_d`, and `k_s` are the surface reflectivity factors for ambient, diffuse, and specular components, respectively
- `I_a`, `I_d`, and `I_s` are the light colors for ambient, diffuse, and specular components, respectively
- `N` is the unit surface normal vector
- `L` is the unit light direction vector
- `R` is the unit reflection direction vector, computed as `R = 2(N ⋅ L)N - L`
- `V` is the unit view direction vector
- `n` is the shininess exponent, which controls the size and sharpness of the specular highlight

The Phong model can produce realistic results for a variety of materials and lighting conditions, but it also has some limitations. For example, it does not account for the interreflection of light between surfaces, the shadowing and occlusion effects, the wavelength-dependent reflection and refraction, and the polarization of light. These effects require more advanced models, such as global illumination, ray tracing, and physically based rendering.



### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image.
- HLR and HSR are important for creating realistic and accurate images of solid objects, as well as for reducing the computational complexity and rendering time.
- There are different types of coherence that can be exploited to perform HLR and HSR efficiently, such as object coherence, image coherence, surface coherence, and temporal coherence.
- Object coherence refers to the spatial relationship among the objects in the scene, such as occlusion, containment, and proximity.
- Image coherence refers to the spatial relationship among the pixels in the image, such as scan-line order, adjacency, and continuity.
- Surface coherence refers to the properties of the surfaces in the scene, such as planarity, convexity, and orientation.
- Temporal coherence refers to the relationship between successive frames in an animation, such as motion, deformation, and visibility.
- There are different algorithms for HLR and HSR, such as back-face culling, depth-buffer method, scan-line method, painter's algorithm, z-buffer algorithm, BSP-tree method, ray-tracing method, and area-subdivision method.
- Back-face culling is a simple technique that eliminates the faces that are facing away from the viewer, based on the surface normal vector and the viewing direction vector.
- Depth-buffer method is a technique that assigns a depth value to each pixel in the image, and compares it with the depth values of the objects in the scene, to determine the visible pixel.
- Scan-line method is a technique that processes the image one scan-line at a time, and maintains a list of active edges and surfaces, to determine the visible pixel.
- Painter's algorithm is a technique that sorts the surfaces in the scene from back to front, and paints them in that order, to create the final image.
- Z-buffer algorithm is a technique that maintains a z-buffer (or depth buffer) and a frame buffer for each pixel in the image, and updates them with the depth and color values of the closest surface, to create the final image.
- BSP-tree method is a technique that partitions the scene into convex regions using binary space partitioning (BSP) trees, and traverses the tree in a back-to-front or front-to-back order, to determine the visible surfaces.
- Ray-tracing method is a technique that traces a ray from the eye to each pixel in the image, and finds the closest intersection with the objects in the scene, to determine the visible pixel.
- Area-subdivision method is a technique that divides the image into smaller regions, and tests the visibility of the surfaces in each region, to determine the visible pixels.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the Warn model for the unit 5 of computer graphics:

### Warn model

- The Warn model is a technique to simulate the effect of large non-point light sources close to objects in a scene, such as studio lights or windows  .
- The Warn model approximates a large light source by using several point sources arranged in a grid, and allows the user to specify "flaps" on the sides of the lighting region to give the light more directionality.
- The Warn model can produce soft shadows and highlights on the objects, as well as varying the intensity and color of the light depending on the distance and angle of the surface  .
- The Warn model can be implemented by using the following steps :
  - Divide the large light source into a grid of n x m point sources, and assign each point source a position, color, and intensity.
  - For each point source, calculate the angle of incidence and the distance to the surface point, and apply the intensity attenuation and color consideration formulas.
  - For each point source, check if the surface point is in shadow by using a shadow ray or a shadow buffer, and if so, reduce the intensity to zero.
  - Sum up the contributions of all the point sources to get the final color and intensity of the light at the surface point.
- The Warn model can be modified by using different shapes, sizes, and arrangements of the point sources, as well as different attenuation and color formulas, to achieve different lighting effects   .



### Intensity Attenuation

- In computer graphics, **intensity attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- Intensity attenuation is important for realistic rendering of scenes with light sources, shadows, and reflections.
- The intensity of a light source at a point on a surface depends on the distance from the light source, the angle of incidence, and the properties of the medium.
- The intensity attenuation formula in computer graphics is:

```
I = I0 / (a + bd + cd^2)
```

where:

- `I` is the intensity at the point on the surface
- `I0` is the intensity at the light source
- `a`, `b`, and `c` are attenuation coefficients that depend on the medium
- `d` is the distance from the light source to the point on the surface

- The attenuation coefficients `a`, `b`, and `c` can be used to model different types of attenuation, such as constant, linear, or quadratic.
- Constant attenuation (`a > 0`, `b = c = 0`) means that the intensity does not depend on the distance, but only on the angle of incidence.
- Linear attenuation (`b > 0`, `a = c = 0`) means that the intensity decreases linearly with the distance.
- Quadratic attenuation (`c > 0`, `a = b = 0`) means that the intensity decreases quadratically with the distance.
- In general, the attenuation coefficients can be chosen to fit the desired effect or the physical properties of the medium.



### Color consideration for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection.
- Hidden surface removal or visible surface detection is the process of identifying and eliminating the hidden surfaces from the rendered image.
- Color consideration for the notes of this unit is important because it can help to distinguish the visible and hidden parts of the objects, as well as to convey the depth, shading, and lighting effects of the scene.
- Some of the color consideration for the notes are:

  - Use different colors for the visible and hidden lines and surfaces, such as black for visible and gray for hidden, or solid and dashed lines.
  - Use colors that are consistent with the natural or artificial light sources in the scene, such as white for sunlight, yellow for incandescent light, or blue for fluorescent light.
  - Use colors that are proportional to the distance or depth of the objects from the viewpoint, such as darker for closer and lighter for farther, or use a depth buffer to store the depth information for each pixel .
  - Use colors that are influenced by the surface properties of the objects, such as diffuse, specular, or ambient reflection, or use a shading algorithm to calculate the color intensity for each pixel based on the surface normal and the light direction.
  - Use colors that are compatible with the color model and the color space of the computer graphics system, such as RGB, CMYK, HSV, or HSL, and avoid using colors that are out of the gamut or the range of the display device.

- These are some of the color consideration for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics. I hope this helps you to learn and prepare for your exams.👍



### Transparency and Shadows

- Transparency is the property of a material that allows light to pass through it partially or fully, creating the effect of translucency or see-through.
- Transparency can be simulated in computer graphics by mixing the colors of the object and the background according to the object's opacity or alpha value, which ranges from 0 (fully transparent) to 1 (fully opaque).
- Transparency can be used to create realistic effects such as glass, water, smoke, fog, etc. or to create artistic effects such as overlays, blending, fading, etc.
- Transparency can also affect the lighting and shading of an object, as transparent objects can reflect and refract light, as well as cast shadows on themselves or other objects.
- Shadows are the regions where light is blocked by an object, creating a contrast between the illuminated and the dark areas.
- Shadows can be simulated in computer graphics by tracing the paths of light rays from the light source to the eye, and determining whether they are occluded by any object in the scene.
- Shadows can be used to create realistic effects such as depth, shape, texture, mood, etc. or to create artistic effects such as silhouettes, outlines, patterns, etc.
- Shadows can also affect the lighting and shading of an object, as shadows can create soft or hard edges, penumbra or umbra regions, ambient occlusion, etc.

