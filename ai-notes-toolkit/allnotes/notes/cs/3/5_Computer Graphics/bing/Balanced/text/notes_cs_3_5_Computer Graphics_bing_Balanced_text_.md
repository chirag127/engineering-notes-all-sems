

## Unit 1 - Introduction and Line Generation

- Computer graphics is the field of study that deals with the creation, manipulation, and display of images using computers.
- Computer graphics can be used for various applications, such as entertainment, education, simulation, visualization, design, and communication.
- Computer graphics can be classified into two types: raster graphics and vector graphics.
  - Raster graphics are composed of pixels, which are small dots of color arranged in a grid. Raster graphics are commonly used for digital photos, videos, and games.
  - Vector graphics are composed of geometric primitives, such as points, lines, curves, and polygons. Vector graphics are commonly used for logos, fonts, diagrams, and illustrations.
- Line generation is one of the basic tasks in computer graphics, as lines are used to draw shapes, curves, and edges.
- Line generation algorithms are methods to determine which pixels should be turned on to display a line on a raster screen.
- Line generation algorithms should be efficient, accurate, and consistent. They should also avoid aliasing, which is the jagged appearance of lines due to pixelation.
- Some of the common line generation algorithms are:
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to increment the x and y coordinates by a small fraction in each step. It is simple, but can be slow and inaccurate due to rounding errors.
  - Bresenham's algorithm: This algorithm uses integer arithmetic and decision variables to determine the next pixel to be turned on. It is faster, more accurate, and more consistent than DDA, but can only handle lines with slopes between 0 and 1.
  - Midpoint algorithm: This algorithm uses the midpoint of the line segment between two pixels to decide which pixel to turn on. It is similar to Bresenham's algorithm, but can handle lines with any slope and can be extended to draw circles and ellipses.



### Types of computer graphics

Computer graphics are the visual representation of data and information using computers and software. Computer graphics can be used for various purposes, such as creating images, animations, simulations, games, user interfaces, and more.

Computer graphics can be broadly classified into two main categories: raster graphics and vector graphics  . Additionally, computer graphics can also be categorized based on the dimensionality of the images: two dimensional (2D) and three dimensional (3D) graphics . Let us examine each of these types in detail.

- Raster graphics: Raster graphics are made up of pixels, which are small squares of color arranged in a grid. Each pixel contains information about its color and brightness. Raster graphics are also known as bitmap images, as they map each pixel to a specific location on the screen. Raster graphics are commonly used for digital photographs, paintings, and scanned images. The quality of raster graphics depends on the resolution, which is the number of pixels per inch (ppi). The higher the resolution, the more detailed and sharp the image. However, raster graphics also have some drawbacks, such as being memory-intensive, losing quality when scaled up or down, and being difficult to edit or manipulate   .

- Vector graphics: Vector graphics are made up of paths, which are defined by mathematical equations that describe the shape, direction, and color of the lines and curves. Vector graphics are also known as object-oriented graphics, as they represent each image element as an object that can be modified independently. Vector graphics are commonly used for logos, icons, diagrams, fonts, and illustrations. The quality of vector graphics does not depend on the resolution, as they can be scaled up or down without losing clarity or detail. Vector graphics also have some advantages, such as being memory-efficient, easy to edit or manipulate, and supporting transparency and animation   .

- 2D graphics: 2D graphics are images that have only two dimensions: width and height. 2D graphics can be either raster or vector, depending on how they are created and stored. 2D graphics are widely used for web design, graphic design, user interfaces, and games. 2D graphics can create the illusion of depth, perspective, and motion by using techniques such as shading, lighting, shadows, gradients, and animation  .

- 3D graphics: 3D graphics are images that have three dimensions: width, height, and depth. 3D graphics are usually created using vector graphics, as they can represent complex shapes and surfaces more easily. 3D graphics are widely used for computer-aided design (CAD), virtual reality, augmented reality, simulations, and games. 3D graphics can create realistic and immersive scenes by using techniques such as modeling, rendering, lighting, shading, texturing, and animation  .

These are the main types of computer graphics that you should know for the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics. I hope this helps you to understand the topic better. If you have any questions, please feel free to ask me.🙂



### Graphic Displays for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A graphic display is a device that can show images or text on a screen, such as a monitor, a projector, or a printer.
- A graphic display can be classified into two types: raster and vector.
  - A raster display consists of a grid of pixels, each of which can have a different color or intensity. Raster displays are commonly used for displaying photographs, videos, and games.
  - A vector display uses mathematical equations to draw lines, curves, and shapes on the screen. Vector displays are commonly used for displaying diagrams, maps, and fonts.
- A graphic display can have different characteristics, such as size, resolution, color depth, refresh rate, and aspect ratio  .
  - The size of a graphic display is measured by the diagonal length of the screen, usually in inches. The size affects the viewing distance and the amount of detail that can be seen on the screen.
  - The resolution of a graphic display is the number of pixels that can be displayed horizontally and vertically, usually in pixels per inch (ppi) or dots per inch (dpi). The resolution affects the sharpness and clarity of the image.
  - The color depth of a graphic display is the number of bits that can be used to represent the color of each pixel, usually in bits per pixel (bpp). The color depth affects the range and accuracy of the colors that can be displayed.
  - The refresh rate of a graphic display is the number of times the image on the screen is updated per second, usually in hertz (Hz). The refresh rate affects the smoothness and responsiveness of the display.
  - The aspect ratio of a graphic display is the ratio of the width to the height of the screen, usually expressed as a fraction or a decimal. The aspect ratio affects the shape and proportion of the image on the screen.
- A graphic display can be connected to a computer or a graphics processing unit (GPU) to receive and process the data that needs to be displayed .
  - A computer is a device that can perform various tasks using software and hardware components, such as a CPU, a RAM, a hard disk, and an operating system.
  - A GPU is a specialized chip that can perform complex calculations and operations related to graphics, such as rendering, shading, and lighting. A GPU can be integrated into the computer's motherboard or attached as a separate card.
  - A graphic display can be connected to a computer or a GPU using different types of cables or ports, such as HDMI, VGA, DVI, or USB-C. The type of connection affects the quality and speed of the data transfer.
- A graphic display can be used for various purposes and applications, such as graphic design, animation, gaming, education, and entertainment  .
  - Graphic design is the process of creating and communicating visual messages using typography, images, colors, and layouts. Graphic design can be used for creating logos, posters, flyers, websites, and magazines.
  - Animation is the process of creating and displaying a sequence of images that create the illusion of movement. Animation can be used for creating cartoons, movies, video games, and simulations.
  - Gaming is the process of playing and interacting with video games that involve challenges, goals, rules, and feedback. Gaming can be used for entertainment, education, socialization, and therapy.
  - Education is the process of acquiring and imparting knowledge, skills, and values. Education can be used for teaching, learning, and researching various subjects and topics.
  - Entertainment is the process of providing and enjoying amusement, pleasure, and relaxation. Entertainment can be used for watching movies, shows, sports, and music.



### Random scan displays

- Random scan displays are also known as vector displays, stroke-writing displays, or calligraphic displays  .
- Random scan displays use a cathode ray tube (CRT) to draw a picture one line at a time in any order or direction given, in a vectorial fashion  .
- Random scan displays direct the electron beam only to those areas of the screen where a picture has to be drawn, and not to the entire screen  .
- Random scan displays can produce smooth line drawings and have high resolution, as they are not limited by the pixel size .
- Random scan displays are suitable for applications that require line drawings, such as engineering and computer-aided design (CAD) .
- Random scan displays cannot display realistic shaded scenes, as they cannot fill the areas between the lines .
- Random scan displays require more memory than raster scan displays, as they need to store the coordinates and attributes of each line.
- Random scan displays are less common than raster scan displays, as they are more expensive and complex.
- Pen plotter is an example of random scan display.



### Raster scan displays

- Raster scan displays are the most common type of graphics monitor that use a cathode ray tube (CRT) to display images on a screen  .
- A raster scan display works by scanning an electron beam across the screen from top to bottom, one row at a time, and turning the beam intensity on and off to create a pattern of illuminated spots called pixels  .
- The pixels are arranged in a rectangular grid called a raster, and each pixel has a specific color and intensity value that determines how it appears on the screen  .
- The resolution of a raster scan display is the number of pixels per unit area, and the refresh rate is the number of times the screen is redrawn per second  .
- The color of a pixel is determined by the combination of three primary colors: red, green, and blue, which are emitted by three separate electron guns in the CRT  .
- The color model used by a raster scan display is called RGB, and each primary color has a range of values from 0 to 255, where 0 means no color and 255 means full color  .
- The color depth of a raster scan display is the number of bits used to store the color value of each pixel, and it affects the number of possible colors that can be displayed  .
- For example, a 1-bit color depth can only display two colors (black and white), a 8-bit color depth can display 256 colors, and a 24-bit color depth can display 16.7 million colors  .
- Raster scan displays are widely used for displaying graphics, images, videos, and animations, as they can produce realistic and detailed images with high color quality  .
- However, raster scan displays also have some limitations, such as aliasing, flickering, and memory consumption  .
- Aliasing is the distortion of edges and curves in an image due to the discrete nature of pixels, and it can be reduced by using anti-aliasing techniques that smooth the edges by blending the colors of adjacent pixels  .
- Flickering is the perceptible change in brightness of the screen due to the finite refresh rate, and it can be reduced by using a higher refresh rate or a double buffering technique that draws the image on a hidden buffer and then displays it on the screen  .
- Memory consumption is the amount of memory required to store the pixel values of an image, and it depends on the resolution and the color depth of the raster scan display  .
- For example, a 1024 x 768 resolution with a 24-bit color depth requires 2.36 MB of memory per image, which can be a challenge for some applications that need to display multiple images or animations  .



### Frame buffer and video controller

- A frame buffer is a portion of random-access memory (RAM) containing a bitmap that drives a video display.
- It is a memory buffer containing data representing all the pixels in a complete video frame.
- A video controller is a device that passes the contents of the frame buffer to the monitor.
- It controls the timing and synchronization of the display signals.
- The frame buffer and video controller are essential components of computer graphics systems, as they enable the display of images on the screen.
- Some of the characteristics of the frame buffer and video controller are:

  - The size of the frame buffer determines the resolution and color depth of the display.
  - The frame buffer can be a separate memory bank on the graphics card, or a reserved part of regular memory.
  - The video controller can have various functions, such as generating the horizontal and vertical sync signals, providing the pixel clock, performing digital-to-analog conversion, and applying gamma correction.
  - The video controller can also support multiple frame buffers, such as double buffering or triple buffering, to reduce flickering and tearing effects.
  - The frame buffer and video controller can be integrated into a single chip, such as a graphics processing unit (GPU), or separated into discrete components.



### Points and lines for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A point is the simplest graphical element that can be displayed on a screen. It is represented by a pair of coordinates (x, y) that specify its position on a two-dimensional plane.
- A line is a sequence of points that are connected by straight or curved segments. It is represented by two endpoints (x1, y1) and (x2, y2) that specify the start and end of the line, or by a slope-intercept equation y = mx + b that specifies the direction and position of the line.
- Lines are used to draw shapes, curves, boundaries, and other graphical elements. They can also be used to represent mathematical functions, data, and relations.
- There are different algorithms to generate lines on a raster display, such as the digital differential analyzer (DDA) algorithm, the Bresenham's line algorithm, and the midpoint line algorithm. These algorithms use integer arithmetic and incremental calculations to plot the pixels that approximate the line.
- The DDA algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each pixel along the line. It is simple but prone to rounding errors and requires floating-point arithmetic.
- The Bresenham's line algorithm uses the decision variable to determine whether to increment the x or y coordinate of each pixel along the line. It is faster and more accurate than the DDA algorithm and only requires integer arithmetic.
- The midpoint line algorithm uses the midpoint between the current pixel and the next pixel to determine whether to increment the x or y coordinate of each pixel along the line. It is similar to the Bresenham's line algorithm but more efficient and can handle lines with any slope.



### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A line drawing algorithm is a method for estimating a line segment on discrete graphical media such as pixel-based screens and printers in computer graphics.
- A line segment is defined by two endpoints, each with an x and y coordinate.
- To draw a line, a computer must work out which pixels need to be filled so that the line looks straight.
- There are different algorithms for drawing a line, each with different advantages and disadvantages in terms of accuracy, efficiency, and simplicity.
- Some of the common line drawing algorithms are:

  - Naive algorithm: This algorithm simply rounds the x and y coordinates of each point on the line to the nearest integer and fills the corresponding pixel. It is easy to implement but produces jagged lines and may skip some pixels.
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each point on the line. It produces smoother lines than the naive algorithm but requires floating-point arithmetic and may be slow .
  - Bresenham's algorithm: This algorithm uses integer arithmetic and error terms to determine which pixel to fill at each step. It is faster and more accurate than the DDA algorithm but more complex to implement .
  - Mid-point algorithm: This algorithm uses the mid-point of the line segment to decide which pixel to fill next. It is similar to Bresenham's algorithm but avoids multiplication and division operations .

- The following diagram illustrates the difference between the naive, DDA, and Bresenham's algorithms for drawing a line with slope 2/3:

```markdown
Line drawing algorithms comparison
```

- The following pseudocode shows the basic steps of the Bresenham's algorithm for drawing a line from (x1, y1) to (x2, y2) with slope less than 1:

```markdown
```pseudocode
Bresenham's algorithm:

Input: x1, y1, x2, y2
Output: A set of pixels to fill

Initialize dx = x2 - x1, dy = y2 - y1
Initialize x = x1, y = y1
Initialize p = 2 * dy - dx
Fill the pixel (x, y)
While x < x2
  If p < 0
    p = p + 2 * dy
  Else
    p = p + 2 * (dy - dx)
    y = y + 1
  End if
  x = x + 1
  Fill the pixel (x, y)
End while
```
```markdown



### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm.
- A circle generation algorithm is an algorithm used to create a circle on a computer screen by determining the subsequent points required to draw the circle .
- There are several algorithms used for generating circles on a computer screen, such as:
  - Bresenham's Algorithm
  - Midpoint Circle Algorithm
  - Polar Coordinates Method
  - Trigonometric Method
- These algorithms have different advantages and disadvantages in terms of accuracy, efficiency, and complexity.
- Bresenham's Algorithm is an efficient and simple algorithm that uses only integer arithmetic and avoids floating-point operations . It is based on the idea of incrementally updating the decision parameter that determines whether to choose the next pixel along the circle or the diagonal.
- Midpoint Circle Algorithm is a modification of Bresenham's Algorithm that reduces the number of calculations by using the symmetry of the circle and the midpoint of the arc as the decision parameter . It is also based on integer arithmetic and avoids floating-point operations.
- Polar Coordinates Method is an algorithm that uses the polar form of the equation of a circle, x = r cos θ and y = r sin θ, where r is the radius and θ is the angle, to generate the points along the circle. It requires floating-point operations and trigonometric functions, which makes it less efficient than the previous algorithms.
- Trigonometric Method is an algorithm that uses the parametric form of the equation of a circle, x = x0 + r cos t and y = y0 + r sin t, where (x0, y0) is the center and t is the parameter, to generate the points along the circle. It also requires floating-point operations and trigonometric functions, which makes it less efficient than the previous algorithms.



### Mid-point circle generating algorithm for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- The mid-point circle generating algorithm is a technique to draw a circle on a raster display using only integer arithmetic and pixel plotting.
- The algorithm is based on the observation that a circle with radius r and center (xc, yc) can be defined by the equation x^2 + y^2 = r^2, where x and y are relative to the center.
- The algorithm starts by plotting the point (0, r) on the circle, which corresponds to the topmost pixel. Then, it moves to the next pixel along the circle by incrementing x by 1 and decrementing y by 1, if the mid-point between the two pixels is inside the circle, or by only incrementing x, if the mid-point is outside the circle.
- The mid-point can be determined by evaluating the circle equation at the point (x + 1, y - 0.5). If the result is negative, the mid-point is inside the circle, and if the result is positive, the mid-point is outside the circle. If the result is zero, the mid-point is on the circle.
- The algorithm repeats this process until x is equal to y, which corresponds to the point (r/sqrt(2), r/sqrt(2)) on the circle, or the first octant is completed. Then, the algorithm can use the symmetry of the circle to plot the remaining seven octants by reflecting the points along the x-axis, y-axis, and the line y = x.
- The algorithm can be summarized by the following pseudocode:

```
// Input: radius r and center (xc, yc)
// Output: a circle with radius r and center (xc, yc) on the raster display
x = 0
y = r
p = 1 - r // initial value of the decision parameter
plot(xc + x, yc + y) // plot the first point
while x < y
  x = x + 1 // increment x
  if p < 0 // mid-point is inside the circle
    p = p + 2 * x + 1 // update the decision parameter
  else // mid-point is outside or on the circle
    y = y - 1 // decrement y
    p = p + 2 * (x - y) + 1 // update the decision parameter
  plot(xc + x, yc + y) // plot the point in the first octant
  plot(xc - x, yc + y) // plot the point in the second octant
  plot(xc + x, yc - y) // plot the point in the third octant
  plot(xc - x, yc - y) // plot the point in the fourth octant
  plot(xc + y, yc + x) // plot the point in the fifth octant
  plot(xc - y, yc + x) // plot the point in the sixth octant
  plot(xc + y, yc - x) // plot the point in the seventh octant
  plot(xc - y, yc - x) // plot the point in the eighth octant
end while
```

- The algorithm has the following advantages and disadvantages:
  - Advantages:
    - It uses only integer arithmetic and pixel plotting, which are fast and simple operations on a raster display.
    - It avoids redundant calculations by using the previous value of the decision parameter to update the next value.
    - It exploits the symmetry of the circle to reduce the number of calculations and pixel plotting by a factor of eight.
  - Disadvantages:
    - It can only draw circles with integer radii, which may result in aliasing or jagged edges on the circle.
    - It can only draw circles with the center at an integer coordinate, which may limit the flexibility of positioning the circle on the display.
    - It can only draw circles in one color, which may not be suitable for some applications that require shading or filling the circle.



### Parallel algorithms for line generation

- Line generation is a fundamental task in computer graphics, where a straight line segment is approximated by a sequence of pixels on a discrete grid.
- A common algorithm for line generation is the Bresenham's algorithm, which uses integer arithmetic and incremental calculations to determine the next pixel along the line.
- However, Bresenham's algorithm is sequential and cannot exploit the parallelism of modern hardware architectures, such as GPUs or multicore CPUs.
- Therefore, parallel algorithms for line generation have been proposed, which can generate multiple pixels of the line simultaneously, using different strategies and data structures.
- Some of the parallel algorithms for line generation are:

  - The coordinate pair algorithm, which derives coordinate pairs from the line equation and uses them as a basis for generating the line pixels in parallel. This algorithm can be implemented on a binary tree of processors, where each node performs simple additions and shifts.
  - The edge function algorithm, which represents each edge of a polygon by a linear function that has a value greater than zero on one side of the edge and less than zero on the opposite side. The value of the function can be interpolated and computed in parallel for adjacent pixels, using hardware similar to that required for color and depth interpolation. This algorithm is suitable for polygon rasterization and Z-buffering.
  - The DDA algorithm, which is a digital differential analyzer that uses floating-point arithmetic and incremental calculations to determine the next pixel along the line. This algorithm can be parallelized by dividing the line into segments and assigning each segment to a different processor, or by using SIMD instructions to compute multiple pixels at once.
  - The parallel prefix sum algorithm, which uses the fact that straight line generation is equivalent to a vector prefix sum calculation. This algorithm can be implemented on a binary tree of processors, where each node performs a simple addition and shift operation. This algorithm can also handle lines with arbitrary slopes and directions.

- These parallel algorithms for line generation can improve the performance and efficiency of computer graphics applications, such as rendering, animation, and image processing, by utilizing the parallelism of modern hardware architectures.



## Unit 2 - Transformations

A transformation is a change in the position, size, or shape of a figure. There are four basic types of transformations: translations, rotations, reflections, and dilations.

- A translation is a transformation that moves every point of a figure the same distance and in the same direction. The figure does not change its size or orientation. A translation can be described by a vector, which has a magnitude (length) and a direction. A vector can be represented by an arrow or by a pair of coordinates.

- A rotation is a transformation that turns a figure around a fixed point called the center of rotation. The figure does not change its size or shape, but it changes its orientation. A rotation can be described by an angle of rotation, which measures how much the figure is turned, and a direction of rotation, which can be clockwise or counterclockwise.

- A reflection is a transformation that flips a figure over a line called the line of reflection. The figure does not change its size or shape, but it changes its orientation. A reflection can be described by the equation of the line of reflection, which can be horizontal, vertical, or diagonal.

- A dilation is a transformation that enlarges or reduces a figure by a scale factor. The figure changes its size, but not its shape or orientation. A dilation can be described by a scale factor, which is a positive number that tells how much the figure is enlarged or reduced, and a center of dilation, which is a point that the figure is stretched or shrunk from.

Some properties of transformations are:

- A transformation maps a figure to its image. The original figure is called the pre-image, and the resulting figure is called the image. The notation for a transformation is T(x, y) = (x', y'), where (x, y) is a point on the pre-image and (x', y') is the corresponding point on the image.

- A transformation is rigid if it preserves the distance and angle measures of the figure. Translations, rotations, and reflections are rigid transformations. A rigid transformation is also called an isometry.

- A transformation is non-rigid if it does not preserve the distance and angle measures of the figure. Dilations are non-rigid transformations. A non-rigid transformation is also called a similarity.

- A transformation is congruent if it preserves the shape and size of the figure. Translations, rotations, and reflections are congruent transformations. Two figures are congruent if there is a congruent transformation that maps one figure to the other.

- A transformation is similar if it preserves the shape, but not the size, of the figure. Dilations are similar transformations. Two figures are similar if there is a similar transformation that maps one figure to the other.



### Basic transformation for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane.
- There are three basic types of transformations: translation, rotation, and scaling.
- Translation is the movement of an object from one location to another without changing its size or orientation. It can be represented by adding a displacement vector to the original coordinates of the object.
- Rotation is the change of orientation of an object around a fixed point or axis. It can be represented by multiplying the original coordinates of the object by a rotation matrix that depends on the angle and direction of rotation.
- Scaling is the change of size of an object without changing its shape or orientation. It can be represented by multiplying the original coordinates of the object by a scaling factor that can be uniform or non-uniform.
- Transformations can be combined to form more complex transformations, such as reflection, shear, and dilation. These can be represented by using a combination of translation, rotation, and scaling matrices.
- Transformations can be applied to individual objects or to a coordinate system. When a coordinate system is transformed, all the objects in that system are transformed accordingly.
- Transformations can be performed using different methods, such as matrix multiplication, homogeneous coordinates, or fixed-point arithmetic. These methods have different advantages and disadvantages in terms of efficiency, accuracy, and simplicity.



### Matrix representations and homogeneous coordinates

- Matrix representations are a convenient way to express geometric transformations such as translation, rotation, scaling, and projection in computer graphics.
- A matrix can be multiplied by a vector to obtain a transformed vector, or by another matrix to obtain a composed transformation.
- Homogeneous coordinates are a way to extend the normal Cartesian coordinates with an extra dimension, usually denoted by w, to allow affine and projective transformations to be represented by matrices.
- Homogeneous coordinates have the property that any multiple of a coordinate vector represents the same point, as long as w is not zero. For example, (x, y, 1) and (2x, 2y, 2) are equivalent in homogeneous coordinates.
- To convert from homogeneous coordinates to Cartesian coordinates, we divide by w. For example, (2x, 2y, 2) becomes (x, y) in Cartesian coordinates.
- To convert from Cartesian coordinates to homogeneous coordinates, we append a 1 as the w component. For example, (x, y) becomes (x, y, 1) in homogeneous coordinates.
- Homogeneous coordinates are useful in computer graphics because they allow us to represent translation, rotation, scaling, and projection as matrix operations, and to compose them easily.
- For example, the matrix representation for translation by (tx, ty) in homogeneous coordinates is:

| 1  0  tx |
| 0  1  ty |
| 0  0  1  |

- To translate a point (x, y, 1) by (tx, ty), we multiply it by the translation matrix:

| 1  0  tx |   | x |   | x + tx |
| 0  1  ty | x | y | = | y + ty |
| 0  0  1  |   | 1 |   |   1    |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by 1.
- Similarly, the matrix representation for rotation by an angle θ in homogeneous coordinates is:

| cosθ  -sinθ  0 |
| sinθ   cosθ  0 |
|  0      0    1 |

- To rotate a point (x, y, 1) by an angle θ, we multiply it by the rotation matrix:

| cosθ  -sinθ  0 |   | x |   | x cosθ - y sinθ |
| sinθ   cosθ  0 | x | y | = | x sinθ + y cosθ |
|  0      0    1 |   | 1 |   |       1         |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by 1.
- Similarly, the matrix representation for scaling by a factor s in homogeneous coordinates is:

| s  0  0 |
| 0  s  0 |
| 0  0  1 |

- To scale a point (x, y, 1) by a factor s, we multiply it by the scaling matrix:

| s  0  0 |   | x |   | sx |
| 0  s  0 | x | y | = | sy |
| 0  0  1 |   | 1 |   |  1 |

- The result is still a homogeneous coordinate, which can be converted back to Cartesian coordinates by dividing by 1.
- Finally, the matrix representation for projection onto a plane z = d in homogeneous coordinates is:

| 1  0  0  0 |
| 0  1  0  0 |
| 0  0  0  0 |
| 0  0  1/d 1 |

- To project a point (x, y, z, 1) onto the plane z = d, we multiply it by the projection matrix:

| 1  0  0  0 |   | x |   |  x  |
| 0  1  0  0 | x | y | = |  y  |
| 0  0  0  0 |   | z |   |  0  |
| 0  0  1/d 1 |   | 1 |   | z/d |

- The result is a homogeneous coordinate, which



### Composite transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- A transformation is a process of changing the position, size, shape, or orientation of an object in a 2D or 3D space.
- A composite transformation is a combination of two or more transformations into a single one that is equivalent to applying the transformations one after another.
- A composite transformation can be represented by a matrix that is obtained by multiplying the matrices of the individual transformations in the order of their application.
- The order of the transformations matters, as some transformations are not commutative, meaning that changing the order of the transformations changes the final result.
- The most common types of transformations are translation, scaling, rotation, and shear.
- Translation is the process of moving an object by a given distance in a given direction. It can be represented by a matrix that adds the translation vector to the original coordinates of the object.
- Scaling is the process of changing the size of an object by a given factor in a given direction. It can be represented by a matrix that multiplies the original coordinates of the object by the scaling factor.
- Rotation is the process of rotating an object by a given angle around a given axis. It can be represented by a matrix that applies a trigonometric function to the original coordinates of the object.
- Shear is the process of distorting an object by a given factor in a given direction. It can be represented by a matrix that adds a fraction of one coordinate to another coordinate of the object.
- Composite transformations can be used to perform complex transformations that are not possible with a single transformation, such as rotating an object around an arbitrary point, reflecting an object across a line, or projecting an object onto a plane.



### Reflections and Shearing

- Reflections and shearing are two types of transformations in computer graphics that change the position and shape of an object respectively.
- A transformation is a process of mapping the coordinates of an object from one coordinate system to another.
- Reflection is a transformation that produces a mirror image of an object with respect to a plane, called the mirror plane or the reflection plane.
- Shearing is a transformation that slants the shape of an object by displacing its points along a fixed direction, called the shearing direction.

#### Reflection

- Reflection can be seen as a special case of rotation, where the angle of rotation is 180 degrees.
- The reflection of an object can be obtained by multiplying its coordinates by a reflection matrix, which depends on the orientation of the mirror plane.
- For example, if the mirror plane is parallel to the x-axis, the reflection matrix is:

```
R_x = | 1  0 |
      | 0 -1 |
```

- This matrix negates the y-coordinate of every point, while keeping the x-coordinate unchanged.
- Similarly, if the mirror plane is parallel to the y-axis, the reflection matrix is:

```
R_y = |-1  0 |
      | 0  1 |
```

- This matrix negates the x-coordinate of every point, while keeping the y-coordinate unchanged.
- If the mirror plane is parallel to the origin, the reflection matrix is:

```
R_o = |-1  0 |
      | 0 -1 |
```

- This matrix negates both the x-coordinate and the y-coordinate of every point, producing the inverse image of the object.
- In general, the reflection matrix for any mirror plane can be derived using the normal vector of the plane and some trigonometric formulas.
- The following figure shows some examples of reflection in 2D:

Reflection in 2D

#### Shearing

- Shearing is a transformation that changes the shape of an object by sliding its layers along a fixed direction, without changing its area or volume.
- Shearing can be done in one direction or two directions, depending on the number of shearing factors involved.
- A shearing factor is a constant that determines the amount of displacement of a point along the shearing direction.
- The shearing of an object can be obtained by multiplying its coordinates by a shearing matrix, which depends on the shearing factors and the shearing direction.
- For example, if the shearing is done along the x-axis, the shearing matrix is:

```
S_x = | 1  sh_x |
      | 0    1  |
```

- This matrix adds the product of the y-coordinate and the shearing factor sh_x to the x-coordinate of every point, while keeping the y-coordinate unchanged.
- Similarly, if the shearing is done along the y-axis, the shearing matrix is:

```
S_y = | 1    0  |
      | sh_y 1 |
```

- This matrix adds the product of the x-coordinate and the shearing factor sh_y to the y-coordinate of every point, while keeping the x-coordinate unchanged.
- If the shearing is done along both the x-axis and the y-axis, the shearing matrix is:

```
S_xy = | 1  sh_x |
       | sh_y 1  |
```

- This matrix adds the product of the y-coordinate and the shearing factor sh_x to the x-coordinate, and the product of the x-coordinate and the shearing factor sh_y to the y-coordinate of every point.
- In general, the shearing matrix for any shearing direction can be derived using the angle of the direction and some trigonometric formulas.
- The following figure shows some examples of shearing in 2D:

Shearing in 2D



### Windowing and Clipping

- Windowing is the process of selecting and viewing a part of a picture with different views .
- Clipping is the process of dividing each element of the picture into its visible and invisible portions, and discarding the invisible portion .
- A window is an opening through which part of the outside world can be seen. It defines the region of interest in the picture.
- A viewport is a rectangular area on the display device where the window is mapped. It defines the output display area .

#### Applications of clipping

- Clipping can be used to extract the desired part of a picture.
- Clipping can be used to identify the visible and invisible area in a 3D object.
- Clipping can be used to create objects using solid modeling.
- Clipping can be used for drawing operations and pointing of an object.

#### Types of clipping

- Point clipping: It is the process of testing whether a given point lies inside or outside the window.
- Line clipping: It is the process of finding the portions of a line that are inside or outside the window.
- Polygon clipping: It is the process of finding the portions of a polygon that are inside or outside the window.
- Text clipping: It is the process of displaying only the characters or strings that are inside the window.
- Curve clipping: It is the process of finding the portions of a curve that are inside or outside the window.

#### Algorithms for line clipping

- Cohen-Sutherland algorithm: It is a simple and fast algorithm that uses region codes for each endpoint of a line to determine whether the line is inside, outside, or partially inside the window.
- Liang-Barsky algorithm: It is an efficient algorithm that uses parametric equations of a line and the inequalities defining the window boundaries to find the intersection points of the line and the window.
- Cyrus-Beck algorithm: It is a general algorithm that can be applied to convex polygons as well as rectangular windows. It uses the normal vectors of the polygon edges to find the intersection points of the line and the polygon.
- Nicholl-Lee-Nicholl algorithm: It is an improved version of the Cohen-Sutherland algorithm that reduces the number of intersection calculations by using additional bits in the region codes to indicate the direction of the line.



### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The term **viewing pipeline** describes a series of transformations, which are passed by geometry data to end up as image data being displayed on a device .
- The 2D viewing pipeline describes this process for 2D data: norm. object- world- viewing- device- device coord.
- The 3D viewing pipeline describes this process for 3D data: norm. object- world- viewing- projection- clipping- device- device coord.
- The viewing pipeline consists of the following stages   :
  - **Normalization**: The object coordinates are transformed into a standard coordinate system, called the normalized device coordinate (NDC) system, which is independent of the device resolution and aspect ratio.
  - **World transformation**: The NDC coordinates are transformed into the world coordinate system, which represents the position and orientation of the objects in the scene relative to a common origin.
  - **Viewing transformation**: The world coordinates are transformed into the viewing coordinate system, which represents the position and orientation of the camera (or the eye) relative to the scene.
  - **Projection transformation**: The viewing coordinates are transformed into the projection coordinate system, which represents the projection of the scene onto a 2D plane, called the view plane or the near clipping plane. The projection can be either parallel or perspective, depending on the type of camera used.
  - **Clipping**: The projection coordinates are clipped against the boundaries of the view plane and the far clipping plane, which define the visible region of the scene. The clipped coordinates are also divided by the homogeneous coordinate to obtain the normalized projection coordinates.
  - **Device transformation**: The normalized projection coordinates are transformed into the device coordinate system, which represents the pixel coordinates on the display device. The device coordinates are usually integer values that correspond to the physical pixels on the screen.
  - **Device rendering**: The device coordinates are used to draw the pixels on the screen, using various techniques such as rasterization, shading, texturing, etc.



### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the mappings of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are part of the viewing pipeline, which consists of the following steps :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation.
  - Define the projection type, which can be parallel or perspective, and the projection plane, which is the plane where the picture is projected.
  - Define the window, which is the rectangular region of the projection plane that contains the part of the picture to be displayed.
  - Define the viewport, which is the rectangular region of the display device where the window is mapped.
  - Apply the window-to-viewport transformation, which is the mapping of the window coordinates to the viewport coordinates.
  - Apply the clipping, which is the removal of objects, lines, or line segments that are outside the window or behind the viewer.
- Viewing transformations can be represented by matrices, which can be composed by multiplying them in the correct order.
- Viewing transformations can be implemented by using various methods and algorithms, such as homogeneous coordinates, Cohen-Sutherland algorithm, Liang-Barsky algorithm, Sutherland-Hodgman algorithm, etc .



### 2-D Clipping algorithms

- Clipping is the process of removing parts of an object that are outside a specified region, such as a window or a viewport.
- Clipping is useful for rendering only the visible parts of a scene, reducing the computational cost and improving the performance of graphics applications.
- Clipping can be applied to different types of objects, such as points, lines, polygons, curves, and surfaces.
- In this topic, we will focus on the algorithms for clipping 2-D lines against a rectangular window, which is a common case in computer graphics.
- There are several algorithms for 2-D line clipping, each with different advantages and disadvantages. Some of the most well-known algorithms are:

  - **Cohen-Sutherland algorithm** : This algorithm uses a simple and efficient technique to classify the endpoints of a line segment into nine regions, based on their relative position to the window. Then, it applies a series of logical operations to determine whether the line segment is trivially accepted, trivially rejected, or needs further clipping. This algorithm is fast for lines that are mostly outside the window, but it may require multiple iterations for lines that cross the window boundaries.
  - **Liang-Barsky algorithm** : This algorithm is based on the parametric equation of a line segment, and it uses four inequalities to find the intersection points of the line segment with the window boundaries. Then, it compares the parameter values of the intersection points to determine the visible portion of the line segment. This algorithm is more efficient than the Cohen-Sutherland algorithm for lines that are mostly inside the window, but it involves more arithmetic operations.
  - **Cyrus-Beck algorithm**: This algorithm is a generalization of the Liang-Barsky algorithm, and it can handle convex polygonal windows as well as rectangular windows. It uses the normal vectors of the window edges to compute the parameter values of the intersection points, and then applies the same comparison technique as the Liang-Barsky algorithm. This algorithm is more versatile than the previous ones, but it requires more computations and storage.
  - **Nicholl-Lee-Nicholl algorithm**: This algorithm is a modification of the Cohen-Sutherland algorithm, and it aims to reduce the number of iterations and comparisons. It uses a different encoding scheme for the regions, and it applies a bitwise shifting operation to find the next candidate edge for clipping. This algorithm is faster than the Cohen-Sutherland algorithm, but it is more complex and less intuitive.

- The following figure shows an example of applying the Cohen-Sutherland algorithm to clip a line segment against a rectangular window. The line segment has endpoints P1 and P2, and the window has vertices A, B, C, and D. The algorithm assigns a 4-bit code to each endpoint, based on its position relative to the window. The code is 0000 for inside, 1000 for above, 0100 for below, 0010 for right, and 0001 for left. The code can also be a combination of these values, such as 1010 for above and right. The algorithm then performs a bitwise OR operation on the codes of the endpoints, and checks the result. If the result is 0000, the line segment is trivially accepted. If the result is non-zero, the algorithm performs a bitwise AND operation on the codes of the endpoints, and checks the result. If the result is non-zero, the line segment is trivially rejected. If the result is zero, the algorithm finds the intersection point of the line segment with one of the window boundaries, and replaces the endpoint with the intersection point. The algorithm repeats this process until the line segment is either accepted or rejected.

Figure 1: Example of Cohen-Sutherland algorithm

- In this example, the codes of P1 and P2 are 1001 and 0010, respectively. The bitwise OR operation gives 1011, which is non-zero, so the line segment is not trivially accepted. The bitwise AND operation gives 0000, which is zero, so the line segment is not trivially rejected. The algorithm then finds the intersection point Q1 of the line segment with the left boundary of the window, and replaces P1 with Q1. The code of Q1 is 0000, which means it is inside the window. The algorithm then performs



### Line clipping algorithms

- Line clipping is the process of removing (clipping) lines or portions of lines outside an area of interest (a viewport or view volume) in computer graphics.
- Line clipping is useful for rendering only the visible parts of a scene, reducing the computational cost and improving the performance of graphics applications.
- There are many algorithms for line clipping, but two of the most common ones are Cohen–Sutherland and Liang–Barsky.
- Cohen–Sutherland algorithm:
  - It divides a 2D space into 9 regions, of which only the middle part (viewport) is visible.
  - It assigns a 4-bit code to each endpoint of a line, based on its position relative to the viewport boundaries (top, bottom, left, right).
  - It uses bitwise operations to determine if a line is trivially accepted (both endpoints inside the viewport), trivially rejected (both endpoints outside the viewport and on the same side), or needs further clipping.
  - It uses the parametric equation of a line to find the intersection points of the line with the viewport edges, and updates the endpoint codes accordingly.
  - It repeats the process until the line is either accepted or rejected.
- Liang–Barsky algorithm:
  - It uses the parametric equation of a line and the inequalities that define the viewport boundaries to find the values of the parameter t that correspond to the intersection points of the line with the viewport edges.
  - It uses these values to determine the minimum and maximum values of t that lie inside the viewport, which define the visible portion of the line.
  - It accepts the line if the minimum value of t is less than or equal to the maximum value of t, and rejects it otherwise.
  - It is more efficient than Cohen–Sutherland algorithm, as it requires fewer computations and comparisons.



### Cohen Sutherland line clipping algorithm

- Line clipping is the process of removing lines or portions of lines that are outside a given region of interest, such as a rectangular window or a viewport.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into nine regions: one inside region and eight outside regions, each corresponding to a bit code of four bits.
- The bit code of a point is determined by comparing its x and y coordinates with the boundaries of the window. The four bits represent the top, bottom, right and left positions of the point relative to the window, as shown below:

```
  1001 | 1000 | 1010
  -----+------+-----
  0001 | 0000 | 0010
  -----+------+-----
  0101 | 0100 | 0110
```

- The algorithm can be summarized as follows:

  - Assign a bit code to each endpoint of the line.
  - If both endpoints have a bit code of 0000, the line is entirely inside the window and can be drawn.
  - If the logical AND of the bit codes of the endpoints is not 0000, the line is entirely outside the window and can be discarded.
  - If neither of the above cases apply, the line is partially inside the window and needs to be clipped. To do this, find an intersection point of the line with one of the window boundaries, and replace the endpoint that is outside the window with the intersection point. Repeat this process until the line is either accepted or rejected.



### Liang Barsky algorithm

- The Liang Barsky algorithm is a line clipping algorithm that is used to determine which portion of a line should be drawn inside a given rectangular clipping window .
- The algorithm is more efficient than the Cohen–Sutherland algorithm and can be extended to 3-Dimensional clipping. It is considered to be the faster parametric line-clipping algorithm.
- The algorithm uses the parametric equation of a line and inequalities describing the range of the clipping window to find the intersections between the line and the window  .
- The parametric equation of a line is given by:

    `x = x1 + u * (x2 - x1)`

    `y = y1 + u * (y2 - y1)`

    where `(x1, y1)` and `(x2, y2)` are the end points of the line and `u` is a parameter that varies from 0 to 1.
- The inequalities describing the range of the clipping window are given by:

    `xwmin <= x <= xwmax`

    `ywmin <= y <= ywmax`

    where `(xwmin, ywmin)` and `(xwmax, ywmax)` are the lower-left and upper-right corners of the window respectively.
- The algorithm works by finding the values of `u` that satisfy the inequalities for each edge of the window and then taking the maximum of the lower values and the minimum of the upper values as the final values of `u` that define the visible portion of the line .
- The algorithm can be summarized by the following steps:

    1. Initialize `u1 = 0` and `u2 = 1` as the lower and upper values of `u`.
    2. For each edge of the window, calculate the values of `p` and `q` as follows:

        `p = -(x2 - x1)` for the left edge

        `p = (x2 - x1)` for the right edge

        `p = -(y2 - y1)` for the bottom edge

        `p = (y2 - y1)` for the top edge

        `q = x1 - xwmin` for the left edge

        `q = xwmax - x1` for the right edge

        `q = y1 - ywmin` for the bottom edge

        `q = ywmax - y1` for the top edge

    3. For each edge, if `p = 0`, the line is parallel to the edge. If `q < 0`, the line is outside the window and can be rejected. If `q >= 0`, the line is inside or intersects the edge and can be clipped.
    4. For each edge, if `p < 0`, the line intersects the edge from inside to outside. Calculate `r = q / p` and update `u2 = min(u2, r)` as the upper value of `u`.
    5. For each edge, if `p > 0`, the line intersects the edge from outside to inside. Calculate `r = q / p` and update `u1 = max(u1, r)` as the lower value of `u`.
    6. If `u1 > u2`, the line is outside the window and can be rejected. Otherwise, the line is inside or partially inside the window and can be clipped using the values of `u1` and `u2` to find the new end points of the line as follows:

        `x'1 = x1 + u1 * (x2 - x1)`

        `y'1 = y1 + u1 * (y2 - y1)`

        `x'2 = x1 + u2 * (x2 - x1)`

        `y'2 = y1 + u2 * (y2 - y1)`

- The algorithm can be illustrated by the following example:

    Liang Barsky example

    In this example, the line has end points `(x1, y1) = (50, 50)` and `(x2, y2) = (150,



### Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a window or a polygon.
- Line clipping algorithms can be classified into two categories: rectangular and non-rectangular.
- Rectangular line clipping algorithms, such as Cohen-Sutherland and Liang-Barsky, are efficient and simple, but they can only handle rectangular windows.
- Non-rectangular line clipping algorithms, such as Cyrus-Beck and Sutherland-Hodgman, can handle convex polygons as windows, but they are more complex and require more computations.
- Cyrus-Beck is a non-rectangular line clipping algorithm that is based on the following steps :
  - Define the convex polygon window by a set of vertices given in a clockwise order.
  - Assign a normal vector to each edge of the polygon, pointing outward from the window.
  - For each line to be clipped, calculate the parameter t for each intersection point with the polygon edges, using the formula: t = (P - P0) . n / D . n, where P is the intersection point, P0 is the starting point of the line, n is the normal vector of the edge, and D is the direction vector of the line.
  - Discard the intersection points that have negative values of t or that lie outside the edge boundaries.
  - Sort the remaining intersection points by increasing values of t.
  - Determine the visible portion of the line by finding the largest interval of t that lies within the window, using the following rules:
    - If the line enters the window at an edge, the value of t at that edge is the lower bound of the interval.
    - If the line exits the window at an edge, the value of t at that edge is the upper bound of the interval.
    - If the line is parallel to an edge and lies inside the window, the value of t at that edge is ignored.
    - If the line is parallel to an edge and lies outside the window, the line is completely invisible.
  - Draw the visible portion of the line by interpolating the points corresponding to the lower and upper bounds of the interval.
- Sutherland-Hodgman is another non-rectangular line clipping algorithm that is based on the following steps :
  - Define the convex polygon window by a set of vertices given in a clockwise order.
  - For each edge of the polygon, clip the line against that edge, using the following rules:
    - If both endpoints of the line are inside the edge, output the line as it is.
    - If both endpoints of the line are outside the edge, discard the line.
    - If one endpoint of the line is inside the edge and the other is outside, output the portion of the line that lies inside the edge, and calculate the intersection point with the edge as the new endpoint.
    - If one endpoint of the line is outside the edge and the other is inside, calculate the intersection point with the edge as the new endpoint, and output the portion of the line that lies inside the edge.
  - Repeat the clipping process for each edge of the polygon, until the line is either completely visible or completely invisible.



### Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - To prevent undesirable effects when rendering polygons that extend beyond the output device's window.
  - To perform hidden surface removal and generate realistic 3D images by clipping polygons against other polygons or planes.
  - To produce high-quality surface details using techniques such as beam tracing or texture mapping by clipping polygons against light sources or textures.
  - To distribute the objects of a scene to appropriate processors in multiprocessor ray tracing systems to improve rendering speeds by clipping polygons against the processor's boundaries.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against a convex clipping window by processing each edge of the polygon against each edge of the window in a clockwise order. The output of this algorithm is a sequence of vertices that define the clipped polygon boundaries. This algorithm is simple and efficient, but it can only handle convex clipping windows and it may introduce degenerate cases such as zero-area polygons or self-intersecting polygons.
  - Weiler-Atherton algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersection points of the polygon edges and the window edges and sorting them along the polygon boundary. The output of this algorithm is a list of polygons that represent the clipped regions. This algorithm can handle concave clipping windows and it preserves the winding order of the polygon vertices, but it is more complex and requires more memory than the Sutherland-Hodgman algorithm.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersection points of the polygon edges and the window edges and marking them as entry or exit points. The output of this algorithm is a list of polygons that represent the clipped regions. This algorithm can handle concave clipping windows and it does not introduce degenerate cases, but it requires more computations than the Sutherland-Hodgman algorithm and it may fail in some cases such as when the polygon is completely inside or outside the window.



### Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon, and processes the boundary of the polygon against each window edge.
- For each window edge, the algorithm generates a new list of vertices by examining each pair of consecutive vertices in the input list and applying the following rules:
  - If both vertices are inside the window, the second vertex is added to the output list.
  - If the first vertex is outside and the second vertex is inside, the intersection point of the edge and the window boundary is added to the output list, followed by the second vertex.
  - If both vertices are outside, no vertices are added to the output list.
  - If the first vertex is inside and the second vertex is outside, the intersection point of the edge and the window boundary is added to the output list.
- The output list becomes the input list for the next window edge, and the process is repeated until all window edges are processed.
- The final output list contains the vertices of the clipped polygon.

The following diagram illustrates the algorithm for a sample polygon and a window:

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
- The algorithm can also handle holes in the subject polygon by using a special flag to indicate whether a vertex is inside or outside a hole .
- The algorithm is more efficient than the Sutherland-Hodgman algorithm for concave polygons, but it requires more preprocessing and sorting of the intersection points .



### Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping .
- Curve clipping requires more processing than for objects with linear boundaries.
- The region of interest, also called the clip window, can be curved or rectangular in shape.
- There are different algorithms for curve clipping, such as the Bezier clipping algorithm, the B-spline clipping algorithm, and the rational B-spline clipping algorithm.
- The Bezier clipping algorithm is based on the convex hull property of Bezier curves, which states that the curve lies entirely within the convex hull of its control points.
- The B-spline clipping algorithm is based on the convex hull property of B-splines, which states that the curve lies entirely within the convex hull of its control points and knots.
- The rational B-spline clipping algorithm is based on the convex hull property of rational B-splines, which states that the curve lies entirely within the convex hull of its weighted control points and knots.
- The general steps of curve clipping algorithms are:
  - Divide the curve into segments using the control points and knots.
  - Test each segment against the clip window boundaries.
  - If the segment is entirely inside the clip window, accept it.
  - If the segment is entirely outside the clip window, reject it.
  - If the segment intersects the clip window boundaries, subdivide it and repeat the process.
- An example of curve clipping is shown below:

Curve clipping example

: https://www.javatpoint.com/computer-graphics-text-clipping
: https://www.javatpoint.com/computer-graphics-clipping
: https://en.wikipedia.org/wiki/Clipping_(computer_graphics)
: https://www.geeksforgeeks.org/computer-graphics-curve-in-computer-graphics/
: https://www.geeksforgeeks.org/polygon-clipping-sutherland-hodgman-algorithm/



### Text clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Text clipping is a process of clipping the string, which means removing the characters or parts of characters that are outside the clipping window.
- Text clipping is dependent on the method of generation used for characters and the requirements of a particular application .
- There are three methods for text clipping which are listed below:

  - All or none string clipping method: In this method, if the whole string is inside the clip window then we consider it, otherwise we discard it . This method is simple but may result in loss of information.
  - Text clipping method: In this method, we keep the characters of the string which lie inside the clip window and remove all the characters which lie outside the clip window . If a character overlaps the window boundary then we keep that part of the character which lies inside the window and discard that part which lies outside the clip window. This method is more flexible but may result in distorted characters.
  - Character clipping method: In this method, we clip each character individually using the same algorithm as for line clipping. This method is more accurate but may result in more computation.

- An example of text clipping is shown below:

Text clipping example

- The image shows a string "COMPUTER GRAPHICS" clipped by a window. The all or none string clipping method would discard the whole string, the text clipping method would keep the characters "PUTER GRAP" and clip the rest, and the character clipping method would clip each character partially.



## Unit 3 - Three Dimensional

- This unit covers the concepts and applications of three dimensional geometry, such as vectors, dot product, cross product, lines, planes, and distances.
- The objectives of this unit are to:
  - Understand the basic properties and operations of vectors in three dimensional space.
  - Calculate the dot product and cross product of two vectors and use them to find angles, areas, and volumes.
  - Write the parametric and symmetric equations of a line in three dimensional space and find the distance between two lines or a point and a line.
  - Write the equation of a plane in three dimensional space and find the distance between two planes or a point and a plane.
  - Identify and sketch the graphs of common three dimensional surfaces, such as cylinders, cones, spheres, and quadric surfaces.
- The main topics of this unit are:
  - Vectors in Three Dimensional Space
    - Definition and notation of vectors
    - Magnitude and direction of vectors
    - Unit vectors and standard basis vectors
    - Vector addition, subtraction, and scalar multiplication
    - Position vectors and displacement vectors
  - The Dot Product and the Cross Product
    - Definition and properties of the dot product
    - Angle between two vectors and orthogonality
    - Projection of a vector onto another vector
    - Work done by a force
    - Definition and properties of the cross product
    - Area of a parallelogram and a triangle
    - Volume of a parallelepiped and a tetrahedron
    - Right-hand rule and orientation
  - Lines and Planes in Three Dimensional Space
    - Parametric equations of a line
    - Symmetric equations of a line
    - Vector equation of a line
    - Parallel and perpendicular lines
    - Distance between a point and a line
    - Distance between two skew lines
    - Equation of a plane
    - Normal vector and constant term of a plane
    - Parallel and perpendicular planes
    - Angle between two planes
    - Distance between a point and a plane
    - Distance between two parallel planes
    - Intersection of a line and a plane
    - Intersection of two planes
  - Graphing in Three Dimensional Space
    - Coordinate system and axes in three dimensional space
    - Plotting points and vectors in three dimensional space
    - Traces and level curves of surfaces
    - Cylindrical coordinates and cylindrical surfaces
    - Spherical coordinates and spherical surfaces
    - Quadric surfaces and their standard forms
    - Ellipsoids, hyperboloids, paraboloids, and cones
    - Rotation of axes and principal axes



### 3-D Geometric Primitives

- 3-D geometric primitives are basic geometric forms that can be used to model more complex 3-D shapes and objects.
- They are the building blocks of 3-D modeling and design.
- Some common 3-D geometric primitives are cubes, pyramids, cones, spheres, cylinders, and tori (doughnuts).
- 3-D geometric primitives can be modified with transforms (such as scaling, rotating, and translating) and Booleans (such as union, intersection, and difference) to create new shapes and objects.
- 3-D geometric primitives can also have a resolution level assigned to them, which determines how smooth or faceted they look by changing the number of sides and steps used to define them.
- 3-D geometric primitives can be represented in different ways, such as by using vertices and edges (polygons), by using curves (such as Bézier curves or circles), or by using mathematical equations (such as parametric or implicit surfaces).
- Different representations of 3-D geometric primitives may have different advantages and disadvantages for different geometric queries and operations. For example, polygons are easy to render and manipulate, but may not capture smooth surfaces well. Curves can represent smooth surfaces better, but may be harder to render and manipulate. Mathematical equations can describe complex shapes precisely, but may be difficult to compute and visualize.



### 3-D Object Representation

- A 3-D object is a mathematical representation of any three-dimensional shape that can be displayed on a computer screen or printed on a paper.
- A 3-D object can be created by using specialized software that allows the user to manipulate edges, vertices, and polygons in a simulated 3-D space.
- There are two main categories of 3-D object representation: boundary representation and space-partitioning representation.
  - Boundary representation (B-rep) describes a 3-D object as a set of surfaces that separates the object interior from the environment. The surfaces can be defined by curves, patches, or meshes. B-rep is useful for modeling solid objects with complex shapes and details.
  - Space-partitioning representation describes the interior properties of a 3-D object by dividing the 3-D space into regions. The regions can be defined by voxels, octrees, or BSP trees. Space-partitioning representation is useful for modeling volumetric objects with homogeneous or heterogeneous materials.
- Some examples of 3-D object representation methods are:
  - Wireframe model: a 3-D object is represented by a set of lines that connect the vertices of the object. Wireframe model is simple and fast to display, but it does not show the surface properties or the hidden parts of the object.
  - Surface model: a 3-D object is represented by a set of patches that cover the surface of the object. Surface model can show the surface properties and the hidden parts of the object, but it does not capture the interior structure or the topology of the object.
  - Solid model: a 3-D object is represented by a set of primitives that define the interior and the exterior of the object. Solid model can show the surface properties, the hidden parts, and the interior structure of the object, but it is more complex and computationally expensive to create and manipulate.



### 3-D Transformation

- In computer graphics, transformation is a process of modifying and re-positioning the existing graphics.
- 3-D transformation takes place in a three dimensional plane, where each point is represented by a triplet of coordinates (x, y, z).
- 3-D transformation can be classified into two types: affine and non-affine.
- Affine transformations preserve the parallelism and ratios of distances between points, but not the angles or lengths. Examples of affine transformations are translation, scaling, rotation, and shear.
- Non-affine transformations do not preserve any of the properties of the original shape. Examples of non-affine transformations are perspective and distortion.
- 3-D transformation can be performed using matrices, which are convenient for combining multiple transformations into one.
- A 3-D transformation matrix is a 4x4 matrix that operates on a 4D homogeneous coordinate vector, where the fourth coordinate is 1 for a point and 0 for a vector.
- The general form of a 3-D transformation matrix is:

| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| m | n | o | p |

- The matrix can be decomposed into four parts: a 3x3 linear transformation matrix, a 3x1 translation vector, a 1x3 perspective vector, and a scalar value.
- The linear transformation matrix can be further decomposed into three parts: a rotation matrix, a scaling matrix, and a shear matrix.
- The rotation matrix can be obtained by rotating the coordinate axes around an arbitrary axis by a given angle. The rotation matrix can be expressed as:

| cosθ + u<sub>x</sub><sup>2</sup>(1 - cosθ) | u<sub>x</sub>u<sub>y</sub>(1 - cosθ) - u<sub>z</sub>sinθ | u<sub>x</sub>u<sub>z</sub>(1 - cosθ) + u<sub>y</sub>sinθ |
|---|---|---|
| u<sub>y</sub>u<sub>x</sub>(1 - cosθ) + u<sub>z</sub>sinθ | cosθ + u<sub>y</sub><sup>2</sup>(1 - cosθ) | u<sub>y</sub>u<sub>z</sub>(1 - cosθ) - u<sub>x</sub>sinθ |
| u<sub>z</sub>u<sub>x</sub>(1 - cosθ) - u<sub>y</sub>sinθ | u<sub>z</sub>u<sub>y</sub>(1 - cosθ) + u<sub>x</sub>sinθ | cosθ + u<sub>z</sub><sup>2</sup>(1 - cosθ) |

where θ is the angle of rotation and u<sub>x</sub>, u<sub>y</sub>, u<sub>z</sub> are the components of the unit vector along the axis of rotation.

- The scaling matrix can be obtained by multiplying the coordinate axes by different factors. The scaling matrix can be expressed as:

| s<sub>x</sub> | 0 | 0 |
|---|---|---|
| 0 | s<sub>y</sub> | 0 |
| 0 | 0 | s<sub>z</sub> |

where s<sub>x</sub>, s<sub>y</sub>, s<sub>z</sub> are the scaling factors along the x, y, and z axes respectively.

- The shear matrix can be obtained by shifting the coordinate axes by different amounts. The shear matrix can be expressed as:

| 1 | sh<sub>x</sub>y | sh<sub>x</sub>z |
|---|---|---|
| sh<sub>y</sub>x | 1 | sh<sub>y</sub>z |
| sh<sub>z</sub>x | sh<sub>z</sub>y | 1 |

where sh<sub>x</sub>y, sh<sub>x</sub>z, sh<sub>y</sub>x, sh<sub>y</sub>z, sh<sub>z</sub>x, sh<sub>z</sub>y are the shearing factors along the xy, xz, yx, yz, zx, and zy



### 3-D viewing for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

- 3-D viewing is the process of displaying 3-D computer graphics on a 2-D or 3-D display device, such as a monitor or a virtual reality headset.
- 3-D viewing involves two main steps: 3-D modeling and 3-D projection.
- 3-D modeling is the creation of 3-D objects using 3-D modeling software, such as Blender, Maya, or SketchUp . 3-D modeling software allows the user to define the shape, color, texture, and other properties of 3-D objects using various methods, such as drawing points, lines, triangles, and other polygonal patches.
- 3-D projection is the transformation of 3-D objects into 2-D or 3-D images that can be displayed on a screen or a projection plane . 3-D projection involves two sub-steps: modeling transformation and viewing transformation.
- Modeling transformation is the manipulation of 3-D objects in the 3-D world coordinate system, such as translation, rotation, scaling, and shearing. Modeling transformation allows the user to change the position, orientation, size, and shape of 3-D objects according to their needs.
- Viewing transformation is the specification of the observer's position, orientation, and view volume in the 3-D world coordinate system. Viewing transformation allows the user to define the perspective from which the 3-D objects are viewed and the region of interest that is projected onto the screen or the projection plane.
- There are different types of 3-D projection, such as parallel projection and perspective projection. Parallel projection preserves the relative sizes and shapes of 3-D objects, but does not create a realistic sense of depth. Perspective projection creates a realistic sense of depth, but distorts the relative sizes and shapes of 3-D objects.
- 3-D viewing is an important and challenging topic in computer graphics, as it requires a lot of mathematical calculations, algorithms, and data structures to perform efficiently and accurately . 3-D viewing is also widely used in various applications, such as video games, animation, simulation, virtual reality, and augmented reality   .



### Projections for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics

- Projection is a technique or process which is used to transform a 3D object into a 2D plane.
- Projection is used to map the view of a 3D object onto the projecting display panel where the viewing volume is specified by the world coordinate and then map these world coordinate over the view port.
- There are two main types of projection: parallel projection and perspective projection .
- Parallel projection discards z-coordinate and parallel lines from each vertex on the object are extended until they intersect the view plane.
- Parallel projection can be further classified into orthographic projection, oblique projection and isometric projection .
- Orthographic projection is a type of parallel projection where the direction of projection is normal to the projection of the plane .
- Orthographic projection can be used to represent the true shape and size of the object.
- Oblique projection is a type of parallel projection where the direction of projection is not normal to the projection of the plane .
- Oblique projection can be used to show the depth of the object.
- Isometric projection is a type of oblique projection where the angle between the projection of the x, y and z axes are equal to 120 degrees .
- Isometric projection can be used to show the three-dimensional view of the object.
- Perspective projection is a type of projection where the lines of projection are not parallel but converge at a single point called the center of projection or the eye point  .
- Perspective projection can be used to show the realistic view of the object as seen by the human eye.
- Perspective projection can be further classified into one-point, two-point and three-point perspective projection depending on the number of vanishing points.
- One-point perspective projection is a type of perspective projection where the projection plane is parallel to two of the principal axes and perpendicular to the third one.
- One-point perspective projection can be used to show the object with one face parallel to the view plane.
- Two-point perspective projection is a type of perspective projection where the projection plane is parallel to one of the principal axes and perpendicular to the other two.
- Two-point perspective projection can be used to show the object with two faces parallel to the view plane.
- Three-point perspective projection is a type of perspective projection where the projection plane is not parallel to any of the principal axes.
- Three-point perspective projection can be used to show the object with no faces parallel to the view plane.
- The following diagram shows the different types of projection:

Diagram of projection types



### 3-D Clipping

- 3-D clipping is the process of removing objects or parts of objects that are outside the viewing volume or the region of interest in a 3-D scene.
- The purpose of 3-D clipping is to reduce the computational effort and improve the rendering performance by discarding invisible or irrelevant objects .
- 3-D clipping can be done in two basic steps:
  - Discard objects that cannot be viewed, such as objects that are behind the camera, outside the field of view, or too far away.
  - Clip objects that intersect with any clipping plane, such as the near and far planes, or the left, right, top and bottom planes of the viewing volume.
- 3-D clipping can be done before or after projection, depending on the coordinate system and the clipping algorithm used .
- 3-D clipping algorithms can be classified into two categories:
  - Point clipping: clipping a single point against a clipping region, such as a cube or a sphere.
  - Polygon clipping: clipping a polygon, such as a triangle or a quadrilateral, against a clipping region, such as a pyramid or a frustum.
- Some common 3-D clipping algorithms are  :
  - Cohen-Sutherland algorithm: a point clipping algorithm that uses outcodes to determine the position of a point relative to a clipping region.
  - Liang-Barsky algorithm: a line clipping algorithm that uses parametric equations to find the intersection points of a line segment with a clipping region.
  - Sutherland-Hodgman algorithm: a polygon clipping algorithm that uses a series of 2-D clipping operations to clip a polygon against a convex clipping region.
  - Cyrus-Beck algorithm: a line clipping algorithm that uses normal vectors to find the intersection points of a line segment with a convex clipping region.
  - Weiler-Atherton algorithm: a polygon clipping algorithm that uses a doubly-linked list to store the vertices of a polygon and clip it against a convex or concave clipping region.



## Unit 4 - Curves and Surfaces

- A curve is a one-dimensional object that can be represented by a function of one or more parameters, such as x(t), y(t), z(t) for a curve in three-dimensional space.
- A surface is a two-dimensional object that can be represented by a function of two or more parameters, such as x(u,v), y(u,v), z(u,v) for a surface in three-dimensional space.
- Curves and surfaces are important in computer graphics, computer-aided design, and geometric modeling, as they can be used to create and manipulate complex shapes and objects.
- Some common types of curves and surfaces are:
  - Line: a curve that has constant direction and magnitude, such as x(t) = a + bt, y(t) = c + dt, z(t) = e + ft.
  - Circle: a curve that has constant distance from a fixed point, such as x(t) = a + r cos(t), y(t) = b + r sin(t), z(t) = c.
  - Ellipse: a curve that has constant sum of distances from two fixed points, such as x(t) = a + r cos(t), y(t) = b + s sin(t), z(t) = c.
  - Parabola: a curve that has constant distance from a fixed line, such as x(t) = a + bt, y(t) = c + dt + et^2, z(t) = f.
  - Hyperbola: a curve that has constant difference of distances from two fixed points, such as x(t) = a + r cosh(t), y(t) = b + s sinh(t), z(t) = c.
  - Bezier curve: a curve that is defined by a set of control points and a polynomial basis function, such as x(t) = sum(i=0 to n) B_i^n(t) P_i_x, y(t) = sum(i=0 to n) B_i^n(t) P_i_y, z(t) = sum(i=0 to n) B_i^n(t) P_i_z, where B_i^n(t) are the Bernstein polynomials and P_i are the control points.
  - B-spline curve: a curve that is defined by a set of control points and a knot vector, such as x(t) = sum(i=0 to n) N_i,k(t) P_i_x, y(t) = sum(i=0 to n) N_i,k(t) P_i_y, z(t) = sum(i=0 to n) N_i,k(t) P_i_z, where N_i,k(t) are the B-spline basis functions and P_i are the control points.
  - NURBS curve: a curve that is defined by a set of control points, a knot vector, and a weight vector, such as x(t) = sum(i=0 to n) w_i N_i,k(t) P_i_x / sum(i=0 to n) w_i N_i,k(t), y(t) = sum(i=0 to n) w_i N_i,k(t) P_i_y / sum(i=0 to n) w_i N_i,k(t), z(t) = sum(i=0 to n) w_i N_i,k(t) P_i_z / sum(i=0 to n) w_i N_i,k(t), where w_i are the weights and N_i,k(t) and P_i are the same as in B-spline curves.
  - Plane: a surface that has constant normal vector, such as x(u,v) = a + bu + cv, y(u,v) = d + eu + fv, z(u,v) = g + hu + iv.
  - Sphere: a surface that has constant distance from a fixed point, such as x(u,v) = a + r cos(u) cos(v), y(u,v) = b + r cos(u) sin(v), z(u,v) = c + r sin(u).
  - Ellipsoid: a surface that has constant sum of squared distances from three fixed points, such as x(u,v) = a + r cos(u) cos(v), y(u,v) = b + s cos(u) sin(v), z(u,v) = c + t sin(u).
  - Cylinder: a surface that has constant distance from a fixed line, such as x(u,v) = a + r cos(u), y(u,v) = b + r sin(u), z(u,v) = c + v.
  - Cone: a surface that has constant ratio of distance from a fixed point to distance from a fixed line, such as x(u,v) = a + v



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
- Quadric surfaces can be rendered using ray tracing or ray firing, which is a method that simulates the path of light rays from the eye to the surface.
- Quadric surfaces can also be rendered using polygonal approximation, which is a method that divides the surface into small flat polygons that can be easily displayed.



### Spheres

- A sphere is a three-dimensional object that has a round shape and a constant radius from its center.
- In computer graphics, spheres are often used to model natural objects such as planets, balls, bubbles, etc.
- However, spheres are not easy to represent on a computer screen, which is made of pixels arranged in a grid. Therefore, spheres are usually approximated by simpler objects constructed from flat polygons (polyhedra).
- There are different methods to approximate a sphere by polygons, such as:
  - Using lines of longitude and latitude to divide the sphere into quadrilaterals or triangles.
  - Using a subdivision algorithm to recursively split an initial polyhedron (such as a tetrahedron, an octahedron, or an icosahedron) into smaller triangles that converge to the sphere.
  - Using a ray tracing technique to compute the intersection of a ray from the camera to the pixel with the sphere equation and shade the pixel accordingly.
- The quality of the approximation depends on the number and size of the polygons used. The more polygons, the smoother and more realistic the sphere looks, but the more computation and memory are required.
- Some properties of spheres that are useful for computer graphics are:
  - The equation of a sphere centered at the origin with radius r is x^2 + y^2 + z^2 = r^2.
  - The normal vector at any point on the sphere is the same as the position vector of that point, normalized to unit length.
  - The surface area of a sphere is 4πr^2 and the volume is (4/3)πr^3.
  - The sphere is a closed and convex surface, which means that any ray that intersects the sphere does so at exactly two points, and that any point inside the sphere is closer to the center than any point outside the sphere.



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
- An ellipsoid can be used in computer graphics to model smooth and symmetric objects, such as planets, eggs, or balloons .
- An ellipsoid can be rendered in computer graphics by dividing it into small triangles or polygons, and applying shading and lighting effects to them .
- An ellipsoid can be generalized to a superellipsoid, which is a surface that can have different degrees of roundness or squareness along different axes.
- A superellipsoid can be defined by the equation:

$$\left(\left(\frac{x}{a}\right)^{2/n_1} + \left(\frac{y}{b}\right)^{2/n_1}\right)^{n_1/n_2} + \left(\frac{z}{c}\right)^{2/n_2} = 1$$

where $n_1$ and $n_2$ are shape parameters that control the roundness or squareness of the surface.
- A superellipsoid can be used in computer graphics to model more complex and varied shapes, such as furniture, buildings, or organic forms .



### Blobby objects

- Blobby objects are a type of implicit modeling technique in computer graphics that can represent non-rigid and fluid-like objects, such as cloth, rubber, liquids, water droplets, etc.  
- Blobby objects are defined by a set of points, called **metaballs**, that have a scalar field associated with them. The scalar field represents the influence or intensity of each metaball at a given point in space.
- The surface of a blobby object is determined by an **isovalue**, which is a threshold that defines the boundary of the object. The surface is the set of points where the sum of the scalar fields of all the metaballs is equal to the isovalue.
- Blobby objects can change their shape and size based on their states, such as temperature, pressure, or interaction with other objects. For example, when two blobby objects come close to each other, they can merge or blend together to form a single object. 
- Blobby objects can be rendered using various techniques, such as ray tracing, polygonization, or splines. Ray tracing is a method that traces rays of light from the eye to the object and calculates the color and shading of each pixel. Polygonization is a method that approximates the surface of the object by a mesh of polygons. Splines are a method that uses curves or patches to define the surface of the object.



### Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- Splines can be classified into different types based on their degree, continuity, and basis functions.
- Some common types of splines are:
  - Linear splines: Splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: Splines of degree two that have continuous first derivatives at the given points.
  - Cubic splines: Splines of degree three that have continuous first and second derivatives at the given points.
  - Bezier curves: Splines that are defined by a set of control points that influence the shape of the curve, but do not necessarily lie on the curve.
  - B-splines: Splines that are defined by a set of control points and a knot vector that determines the degree and continuity of the curve.
  - NURBS: Non-uniform rational B-splines that are a generalization of B-splines that can represent conic sections and other rational curves.
- Splines have many properties and applications in computer graphics, such as:
  - Affine invariance: Splines are invariant under affine transformations, such as rotation, translation, scaling, and shearing.
  - Local control: Splines can be modified locally by changing only a few control points or knots, without affecting the rest of the curve.
  - Interpolation or approximation: Splines can either pass through the given points (interpolation) or lie close to them (approximation), depending on the choice of control points and knots.
  - Smoothness and continuity: Splines can have different levels of smoothness and continuity at the given points, which affect the appearance and behavior of the curve.
  - Subdivision and refinement: Splines can be subdivided or refined into smaller segments or higher degrees, without changing the shape of the curve.



### Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline or basis spline is a piecewise polynomial function with specific properties that determine the polynomial degree/order .
- The idea behind using a B-spline curve is to determine a unique polynomial representation of a set of data, whether that data be structural points in 3D space or a set of data on a graph.
- A B-spline function is a combination of flexible bands that is controlled by a number of points that are called control points, creating smooth curves .
- These functions are used to create and manage complex shapes and surfaces using a number of points.
- A B-spline curve is defined by the following parameters:
  - A set of control points P0, P1, ..., Pn that define the shape of the curve.
  - A degree p that determines the order of the polynomial segments.
  - A knot vector U = {u0, u1, ..., um} that determines the domain and continuity of the curve.
- A B-spline curve has the following properties :
  - It is a linear combination of B-spline basis functions of degree p, which are defined recursively using the Cox-de Boor formula.
  - It is invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - It has local control, meaning that changing one control point only affects the curve in a local region.
  - It has variation diminishing, meaning that the curve does not oscillate more than the control polygon.
  - It has convex hull property, meaning that the curve lies within the convex hull of the control points.
  - It has minimal support, meaning that each basis function has the smallest possible domain for a given degree and knot vector.
  - It has smoothness, meaning that the curve is continuous and has continuous derivatives up to order p - 1, where p is the degree of the curve. The smoothness can be reduced by repeating knots in the knot vector.
  - It has approximation and interpolation capabilities, meaning that the curve can approximate or interpolate a given set of data points by choosing appropriate control points and knot vector.



### Bezier curves and surfaces

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling .
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them .
- They have the properties of continuity, smoothness, and local control, which make them highly useful and convenient for curve and surface design.
- Bezier curves can be classified into simple, quadratic, and cubic curves, depending on the number of control points.
- Simple curves have two control points and are straight lines.
- Quadratic curves have three control points and are parabolic.
- Cubic curves have four control points and are the most commonly used in computer graphics.
- Bezier surfaces are formed by two sets of Bezier curves, one in the u-direction and one in the v-direction.
- The degree of the surface is determined by the number of control points in each direction.
- Bezier surfaces can be used to model complex shapes such as spheres, cylinders, tori, and organic forms.
- Bezier curves and surfaces were patented and popularized by Pierre Bezier, a French engineer who worked for Renault in the 1960s and 1970s.



## Unit 5 - Hidden Lines and Surfaces

- Hidden lines and surfaces are used to represent the parts of an object that are not visible from a given viewpoint.
- Hidden lines are usually drawn as dashed or dotted lines on a 2D drawing or a 3D model.
- Hidden surfaces are usually removed or shaded differently on a 3D model or a rendering.
- The purpose of hidden lines and surfaces is to show the shape and structure of the object more clearly and accurately, and to avoid confusion or ambiguity.
- There are different methods and conventions for drawing hidden lines and surfaces, depending on the type of object, the projection system, the level of detail, and the industry standards.
- Some common methods and conventions are:
  - Parallel projection: Hidden lines are drawn parallel to the projection plane, and are usually dashed or dotted with equal or unequal spacing.
  - Perspective projection: Hidden lines are drawn as if they were visible, but are usually dashed or dotted with decreasing spacing as they recede from the viewer.
  - Isometric projection: Hidden lines are drawn at 30 degrees to the horizontal, and are usually dashed or dotted with equal spacing.
  - Orthographic projection: Hidden lines are drawn perpendicular to the projection plane, and are usually dashed or dotted with equal spacing.
  - Axonometric projection: Hidden lines are drawn at an angle to the projection plane, and are usually dashed or dotted with equal or unequal spacing, depending on the type of axonometry (dimetric, trimetric, etc.).
  - Oblique projection: Hidden lines are drawn parallel or at an angle to the projection plane, and are usually dashed or dotted with equal or unequal spacing, depending on the type of obliquity (cavalier, cabinet, etc.).
  - Sectional views: Hidden lines are omitted or shown as thin solid lines on the cut plane, and are usually dashed or dotted on the adjacent views.
  - Shaded or rendered views: Hidden surfaces are removed or shaded differently from the visible surfaces, using techniques such as ray tracing, z-buffering, occlusion culling, etc.



### Back Face Detection algorithm for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Back face detection (or back face culling) is a technique to eliminate hidden surfaces or faces that are not visible to the viewer.
- It is based on the assumption that the object is a convex polyhedron, which means that any line segment joining two points on the surface of the object lies entirely within the object.
- A face of a convex polyhedron is said to be back facing if it is oriented away from the viewer, or equivalently, if its surface normal is pointing away from the viewer.
- The back face detection algorithm can be summarized as follows:

  1. For each face of the polyhedron, compute its surface normal vector by taking the cross product of two adjacent edges.
  2. Transform the surface normal vector to the view coordinate system using the model-view matrix.
  3. If the z-component of the transformed surface normal vector is positive, then the face is back facing and can be discarded. Otherwise, the face is front facing and should be rendered.

- The back face detection algorithm can improve the rendering efficiency by reducing the number of faces that need to be processed by the hidden surface removal algorithm, such as the z-buffer algorithm or the painter's algorithm.
- However, the back face detection algorithm is not applicable to non-convex polyhedra, such as a torus or a concave cube, because some of their faces may be partially visible and partially hidden. In such cases, a more sophisticated hidden surface removal algorithm is needed.



### Depth buffer method

- Depth buffer method, also known as z-buffer method, is an image-space technique for hidden surface removal in computer graphics  .
- It is based on the idea of storing the depth (or z-coordinate) of the closest object at each pixel in a buffer, and comparing the depth of new objects with the existing depth to determine visibility  .
- The depth buffer method has the following steps :
  - Initialize the depth buffer and the frame buffer for each pixel to some predefined values, such as the maximum depth and the background color.
  - For each polygon in the scene, project it onto the view plane and scan-convert it to find the pixels that it covers.
  - For each pixel, calculate the depth of the polygon at that pixel using the plane equation of the polygon.
  - Compare the depth of the polygon with the depth stored in the depth buffer for that pixel. If the polygon depth is smaller, it means the polygon is closer to the viewer and should be visible. In that case, update the depth buffer and the frame buffer with the new depth and color values. Otherwise, ignore the polygon and move on to the next pixel.
  - Repeat the above steps for all the polygons in the scene, in any order.
  - Display the frame buffer as the final image.
- The depth buffer method has some advantages and disadvantages :
  - Advantages:
    - It is simple and easy to implement, especially in hardware.
    - It can handle any number of polygons and any polygon shapes, including concave and intersecting polygons.
    - It does not require sorting or clipping of polygons.
    - It can be combined with other rendering techniques, such as shading and anti-aliasing.
  - Disadvantages:
    - It requires a large amount of memory to store the depth buffer, which may limit the resolution and precision of the image.
    - It may suffer from aliasing artifacts, such as jagged edges and popping, due to the discrete nature of pixels and depth values.
    - It may not handle transparency or translucency effects correctly, as it only stores the closest depth and color at each pixel.



### A-buffer method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- The A-buffer method is a general hidden surface mechanism that can handle opaque, transparent, and intersecting objects  .
- The A-buffer method extends the depth-buffer (or Z-buffer) method by storing more than one depth value and color value per pixel .
- The A-buffer method uses a linked list data structure to store the depth and color values of each fragment that contributes to a pixel .
- The A-buffer method sorts the fragments in each pixel by their depth values and computes the final color by blending the colors of the visible fragments .
- The A-buffer method can produce anti-aliased images by averaging the colors of the fragments within a pixel  .
- The A-buffer method requires more memory and computation than the depth-buffer method, but it can handle complex scenes with transparency and overlapping objects  .



### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The main idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be applied to both solid and wireframe models, and can handle concave and convex polygons, as well as polygons with holes.
- The scan line method has several advantages, such as:
  - It is efficient and fast, as it avoids unnecessary calculations for hidden pixels or polygons.
  - It is easy to implement and can be parallelized.
  - It can handle shading, texture mapping, and anti-aliasing techniques by interpolating the attributes of the vertices along the scan line.
- The scan line method has some disadvantages, such as:
  - It requires sorting and updating the polygon list, which can be costly for complex scenes.
  - It can produce artifacts or errors when dealing with polygons that share edges or vertices, or when the scan line coincides with a polygon edge.
  - It can be difficult to handle non-planar polygons, as they may need to be subdivided into smaller planar polygons.
- The scan line method can be extended to handle 3D hidden surface removal by using a depth buffer or a z-buffer, which stores the depth or distance of each pixel from the viewpoint, and compares it with the depth of the incoming polygon fragments.
- The scan line method can also be combined with other algorithms, such as ray tracing or radiosity, to produce more realistic images with shadows, reflections, and global illumination effects.



### Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the physical properties of light and the interaction of light with different types of materials.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, such as ambient, diffuse, and specular reflection.
  - Global illumination models consider all the interactions and exchange of light among objects, such as reflection, refraction, shadows, and interreflections.
- In this unit, we will focus on the local illumination models, which are simpler and faster to compute than global illumination models.
- The basic local illumination model consists of three components: ambient light, diffuse reflection, and specular reflection .
  - Ambient light is the uniform and constant light that is present in the environment, regardless of the position and orientation of the objects . Ambient light is used to simulate the effect of indirect illumination that is not captured by the other components .
  - Diffuse reflection is the light that is reflected equally in all directions by a matte or rough surface . Diffuse reflection depends on the angle between the surface normal and the light direction, and the color and reflectivity of the surface .
  - Specular reflection is the light that is reflected in a dominant direction by a shiny or smooth surface . Specular reflection depends on the angle between the surface normal, the light direction, and the view direction, and the color, reflectivity, and shininess of the surface .
- The basic local illumination model can be expressed as a linear combination of the three components :

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - where I is the total intensity of the reflected light, I<sub>a</sub> is the ambient component, I<sub>d</sub> is the diffuse component, and I<sub>s</sub> is the specular component.
- The basic local illumination model can be extended to include other effects, such as attenuation, spotlights, multiple light sources, and colored lights .
- The basic local illumination model can be implemented using different shading techniques, such as flat shading, Gouraud shading, and Phong shading. Shading techniques determine how the illumination model is applied to the pixels or polygons of the graphics objects.



### Ambient light

- Ambient light is the base brightness applied to textures rendered in a scene before any point, spot, or other types of virtual light sources are computed.
- Ambient light affects the appearance of the entire rendered scene by adding a uniform amount of light to every point, regardless of its position, orientation, or material .
- Ambient light can be used to simulate natural or artificial lighting, such as the sun or fluorescent lights, by adjusting its color and intensity.
- Ambient light is a gross oversimplification of the complex interaction between the light sources and the surfaces in the scene, but it works well enough for creating a realistic environment in computer graphics.
- Ambient occlusion is a technique that calculates how exposed each point in a scene is to ambient lighting, and darkens the points that are more occluded (and hence less illuminated) by other objects in the scene.



### Diffuse reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough .
- This type of reflection is what gives an object its matte finish .
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by the color and texture of the surface, as well as the position and intensity of the light source.
- Diffuse interreflection is a process whereby light reflected from an object strikes other objects in the surrounding area, illuminating them.
- Diffuse interreflection specifically describes light reflected from objects which are not shiny or specular.
- Diffuse interreflection can create complex lighting effects, such as color bleeding and soft shadows.
- Diffuse interreflection can be simulated by using radiosity or global illumination techniques.



### Specular reflection

- Specular reflection is the phenomenon of light reflecting off a smooth surface in a mirror-like way, creating a bright spot or highlight on the surface .
- Specular reflection depends on the angle of incidence of the light ray, the angle of reflection of the light ray, and the viewing angle of the observer.
- Specular reflection is modeled by the Phong reflection model, which consists of three components: ambient, diffuse, and specular.
- The ambient component represents the constant background illumination of the scene, independent of the light source or the surface orientation.
- The diffuse component represents the Lambertian reflection of the light source, which is proportional to the cosine of the angle between the light ray and the surface normal.
- The specular component represents the mirror-like reflection of the light source, which is proportional to the cosine of the angle between the reflected light ray and the viewing direction, raised to some power called the shininess.
- The shininess determines how sharp or blurry the specular highlight is, with higher values resulting in sharper highlights and lower values resulting in blurrier highlights.
- The Phong reflection model can be expressed as:

![Phong reflection model formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/8c2c2d0f0b9f0f9c9b2f2e0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9



### Phong model

The Phong model is a widely used model for the local illumination of points on a surface in computer graphics. It was designed by Bui Tuong Phong in 1973 and is based on the empirical observation of how light interacts with different materials.

The Phong model consists of three components: ambient, diffuse, and specular. Each component represents a different aspect of the light reflection from a surface.

- Ambient component: This is the constant term that accounts for the background or indirect illumination of the surface. It is independent of the light source and the viewing direction and is usually set to a small value to avoid completely dark areas.
- Diffuse component: This is the term that models the diffuse reflection of light from a surface. It is proportional to the cosine of the angle between the light direction and the surface normal and depends on the color and the reflectivity of the surface. It is also known as Lambertian reflection, as it follows Lambert's cosine law.
- Specular component: This is the term that models the specular reflection of light from a surface. It is proportional to the cosine of the angle between the viewing direction and the reflection direction and depends on the color, the reflectivity, and the shininess of the surface. It is also known as Phong reflection, as it follows Phong's empirical formula.

The Phong model can be expressed mathematically as follows:

I = I_a + I_d + I_s

where I is the total intensity of the reflected light, I_a is the ambient component, I_d is the diffuse component, and I_s is the specular component.

The ambient component can be calculated as:

I_a = k_a I_a

where k_a is the ambient reflectivity of the surface and I_a is the ambient light intensity.

The diffuse component can be calculated as:

I_d = k_d I_d (N ⋅ L)

where k_d is the diffuse reflectivity of the surface, I_d is the diffuse light intensity, N is the unit surface normal, and L is the unit light direction.

The specular component can be calculated as:

I_s = k_s I_s (R ⋅ V)^n

where k_s is the specular reflectivity of the surface, I_s is the specular light intensity, R is the unit reflection direction, V is the unit viewing direction, and n is the shininess exponent of the surface.

The Phong model can be implemented in different ways, such as:

- Phong shading: This is the technique of applying the Phong model at each pixel of the surface, using the interpolated normals and the actual light and viewing directions. This produces smooth and realistic shading effects, but it is computationally expensive.
- Gouraud shading: This is the technique of applying the Phong model at each vertex of the surface, using the vertex normals and the average light and viewing directions. This produces fast and smooth shading effects, but it can cause artifacts such as Mach bands or specular highlights.
- Flat shading: This is the technique of applying the Phong model at each polygon of the surface, using the polygon normal and the average light and viewing direction. This produces fast and simple shading effects, but it can cause discontinuities and faceted appearance.



### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image.
- HLR and HSR are important for creating realistic and accurate images of solid objects and scenes.
- There are different types of coherence that can be exploited to reduce the computation required for HLR and HSR, such as object coherence, image coherence, area coherence, and span coherence.
- There are different algorithms for HLR and HSR, such as back-face culling, depth-buffer method, scan-line method, painter's algorithm, z-buffer algorithm, and BSP-tree method  .
- Each algorithm has its own advantages and disadvantages in terms of complexity, accuracy, and efficiency.
- A combined approach for HLR and HSR can use multiple algorithms to achieve the best results for different types of scenes and objects.
- A possible combined approach is to use back-face culling to eliminate the faces that are facing away from the viewer, then use the z-buffer algorithm to compare the depth values of the remaining faces and determine the visible ones, and finally use the scan-line method to fill the visible faces with colors and shading.
- This combined approach can handle concave and convex objects, overlapping and intersecting objects, and perspective and parallel projections.
- This combined approach can also be optimized by using coherence techniques, such as sorting the objects by their distance from the viewer, dividing the image into regions, and skipping the pixels that are already filled .



### Warn model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection direction in a 3D scene.
- Hidden line and surface elimination is the problem of determining which lines or edges, vertices, surfaces or volumes are visible or invisible to the observer at a specified point.
- Hidden line and surface elimination can be classified into two categories: object space methods and image space methods.
- Object space methods operate on the object definitions and apply geometric or spatial coherence to eliminate hidden parts. Examples of object space methods are back-face detection, depth sorting, BSP trees, octrees, etc.
- Image space methods operate on the projection image and apply pixel or area coherence to eliminate hidden parts. Examples of image space methods are Z-buffer, A-buffer, scan-line, ray tracing, etc.
- Warn model is an image space method that uses area subdivision algorithm to compute the visible surface in the scene. It was proposed by John Warnock in 1969.
- Warn model divides the projection window into smaller subareas recursively until each subarea is either fully visible, fully invisible, or contains a single object.
- Warn model uses four rules to determine the visibility of a subarea:
  - Rule 1: If the subarea contains only one object, then the object is visible and the subarea is painted with the object color.
  - Rule 2: If the subarea is empty, then the subarea is invisible and the subarea is painted with the background color.
  - Rule 3: If the subarea contains more than one object, and all the objects are at the same depth, then the subarea is visible and the subarea is painted with the color of the nearest object.
  - Rule 4: If the subarea contains more than one object, and the objects are at different depths, then the subarea is divided into four equal subareas and the algorithm is applied recursively to each subarea.
- Warn model can handle transparency, shadows, and reflections by using the A-buffer technique, which stores the depth and color information of all the objects in a subarea in a linked list.
- Warn model can also simulate studio lighting effects by controlling the light intensity in different directions, using the Phong model for the surface points.



### Intensity Attenuation

- In computer graphics, **attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- **Intensity** is the power per unit cross-sectional area.
- Intensity attenuation is the gradual decrease in energy as the radiation passes through absorbing material .
- Intensity attenuation can affect the appearance of objects in a scene, especially when using point light sources or spotlights.
- The intensity of a point light source or a spotlight at a given distance from the source can be calculated using the **attenuation formula**:

  `I = I0 / (a + bd + cd^2)`

  where `I` is the intensity at distance `d`, `I0` is the intensity at distance zero, `a` is the constant attenuation factor, `b` is the linear attenuation factor, and `c` is the quadratic attenuation factor.
- The attenuation factors can be adjusted to create different effects, such as soft or hard shadows, or realistic or stylized lighting.
- Intensity attenuation can also be applied to other types of flux, such as sound, heat, or electric current .



### Color consideration for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection.
- Hidden line and surface removal is an important problem in computer graphics, as it helps to create realistic and uncluttered images of 3D scenes.
- There are different algorithms and techniques for hidden line and surface removal, such as z-buffering, scan-line, painter's, ray tracing, etc   .
- Color consideration for the notes of this unit is important, as it can help to highlight the different aspects of hidden line and surface removal, such as:
  - The depth or distance of the objects from the viewpoint or projection plane, which determines their visibility and occlusion  .
  - The intensity or brightness of the objects, which depends on their surface color, light sources, and shading models.
  - The percent of pixel coverage or the fraction of the pixel area that is covered by a surface, which affects the final color of the pixel.
- Some possible color choices for the notes of this unit are:
  - Use different shades of the same color (such as blue) to represent the depth of the objects, with darker shades for closer objects and lighter shades for farther objects.
  - Use different colors (such as red, green, and blue) to represent the intensity of the objects, with brighter colors for more illuminated objects and darker colors for less illuminated objects.
  - Use different patterns (such as solid, dashed, or dotted) to represent the percent of pixel coverage of the objects, with more dense patterns for higher coverage and less dense patterns for lower coverage.
- These color choices can help to make the notes more clear, attractive, and informative, as they can show the different aspects of hidden line and surface removal in a visual and intuitive way.



### Transparency and Shadows

- Transparency is the property of a material that allows light to pass through it partially or fully, creating the effect of translucency or see-throughness.
- Transparency can be simulated in computer graphics by mixing the colors of the transparent object and the background object, according to the degree of opacity or alpha value of the transparent object.
- Transparency can be used to create realistic effects such as glass, water, smoke, fog, etc. in computer graphics.
- Shadows are the regions where light is blocked by an opaque object, creating a contrast between the illuminated and the dark areas.
- Shadows can be simulated in computer graphics by tracing the paths of light rays from the light source to the eye, and determining whether they are occluded by any object in the scene.
- Shadows can be used to create realistic effects such as depth, perspective, mood, etc. in computer graphics.
- There are different techniques to create transparency and shadows in computer graphics, such as ray tracing, alpha blending, shadow mapping, shadow volumes, etc. Each technique has its own advantages and disadvantages in terms of accuracy, efficiency, and complexity.

