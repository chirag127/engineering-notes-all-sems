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