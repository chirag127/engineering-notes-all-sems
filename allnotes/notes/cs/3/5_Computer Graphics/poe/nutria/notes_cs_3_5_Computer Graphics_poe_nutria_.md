


## Unit 1 - Introduction and Line Generation

* Line generation is a type of computer graphics which involves the use of algorithms to generate a line or a series of lines that connect two or more points. 
* Line generation algorithms can be used to draw lines on a computer screen or to create vector images.
* Line generation algorithms can be classified into two categories: parametric and non-parametric.
* Parametric line generation algorithms use equations to define the line, while non-parametric algorithms use a set of points to define the line.
* Line generation algorithms can be used to draw straight lines, curved lines, or a combination of both.
* Line generation algorithms can be used to draw lines in two dimensions or in three dimensions.
* Line generation algorithms can be used to create images of objects in a scene or to create the illusion of movement in a scene.




### Types of Computer Graphics

1. Vector Graphics: Vector graphics use mathematical equations to draw lines, shapes, and curves. These graphics are resolution-independent and can be resized without losing quality. Examples of vector graphics include logos and illustrations.

2. Bitmap Graphics: Bitmap graphics are made up of a grid of individual pixels. They are resolution-dependent, meaning they cannot be resized without losing quality. Examples of bitmap graphics include photographs and scanned images.

3. 3D Graphics: 3D graphics are computer-generated images that give the illusion of three-dimensional depth. 3D graphics can be used to create realistic scenes, animations, and objects. Examples of 3D graphics include video games and movies.




### Graphic Displays for the Notes of the Unit 1 - Introduction and Line Generation in the Subject of Computer Graphics

- Computer graphics is a field of study that involves the use of computers to create and manipulate visual images.
- It is used to create images for a variety of purposes, such as scientific visualization, entertainment, and advertising.
- Line generation is a fundamental computer graphics technique that is used to draw lines on a computer screen.
- The most common line drawing algorithms are Bresenham’s line algorithm and the Digital Differential Analyzer (DDA).
- Bresenham’s line algorithm is an incremental scan conversion algorithm that can be used to draw straight lines on a raster display.
- The Digital Differential Analyzer (DDA) is an incremental scan conversion algorithm that can be used to draw lines on a raster display.
- Both algorithms are based on the idea of incrementally stepping through each pixel on the line and deciding whether to draw it or not.
- Line drawing algorithms can be used to draw curves as well as lines, by using the same basic principles.
- The use of computer graphics can also be used to create 3D images, which can be used for a variety of purposes, such as scientific visualization, entertainment, and advertising.




### Random Scan Displays

* Random scan displays are a type of display system used in computer graphics in which the image is drawn by a beam of electrons that is randomly directed to scan the display area.
* The beam is moved across the display area in a series of horizontal lines with a raster pattern.
* At each point, the beam is turned on or off to draw the picture.
* The beam is then moved to the next line and the process is repeated until the entire image is drawn.
* Random scan displays are often used in television and computer monitors.
* They are also used in some digital printing machines.
* The advantage of random scan displays is that they can be used to display high-resolution images with a wide range of colors.
* The disadvantage is that they require more power and generate more heat than other types of displays.




### Raster Scan Displays
* A raster scan display is a type of display system that uses a beam of electrons or light to scan across a surface to create an image.
* The image is created by a series of scan lines, each line being composed of a series of pixels, or picture elements.
* The scan lines are generated in a left-to-right, top-to-bottom order and the pixels are illuminated as the beam moves across the screen.
* The raster scan display is the most common type of display system used in computers and television sets.
* The process of creating an image with a raster scan display is known as rasterization.
* The raster scan display is used to generate line and point primitives, as well as to display text, images, and video.
* To generate line primitives, the display system uses an algorithm called the Bresenham line drawing algorithm.
* The Bresenham line drawing algorithm works by plotting the points along the line that are closest to the ideal line.
* To generate point primitives, the display system uses a point plotting algorithm.
* The point plotting algorithm works by plotting a single pixel at the given coordinates.
* To display text and images, the display system uses a raster image processor (RIP).
* The RIP works by converting the text or image into a bitmap and then displaying it on the screen.
* To display video, the display system uses a video processor.
* The video processor works by converting the video signal into a series of scan lines that are then displayed on the screen.




### Frame Buffer and Video Controller 

* A frame buffer is a portion of memory used to store the image to be displayed. It is a two-dimensional array of pixels, with each pixel representing a single color. 
* A video controller is a device that controls the display of the image stored in the frame buffer. It is responsible for controlling the timing of the display, the resolution, and the refresh rate of the image.
* Line generation is the process of generating a line on the screen from two given points. This is done by using various algorithms such as Bresenham's line algorithm, DDA algorithm and Mid-Point algorithm. 
* A line is defined by two points, (x1, y1) and (x2, y2). The line can be represented by the equation y = mx + c, where m is the slope of the line and c is the y-intercept. 
* The Bresenham's line algorithm is an efficient algorithm for drawing a line on a raster display. It is based on the observation that when drawing a line on a raster display, it is only necessary to consider the pixels which lie on the line. 
* The DDA algorithm is an algorithm for drawing a line on a raster display. It is based on the observation that when drawing a line on a raster display, it is only necessary to consider the pixels which lie on the line. 
* The Mid-Point algorithm is an algorithm for drawing a line on a raster display. It is based on the observation that when drawing a line on a raster display, it is only necessary to consider the pixels which lie on the line. It is an efficient algorithm and is used in many graphics packages.




### Points and Lines for the Notes of the Unit 1 - Introduction and Line Generation in the Subject of Computer Graphics

* A point in computer graphics is a precise location on the screen, represented by an X-Y coordinate. 
* A line is a connection between two points.
* Lines can be straight, curved, or a combination of both.
* Lines can also be drawn using different colors, widths, and patterns.
* Line drawing algorithms are used to create lines on the screen.
* The most common line drawing algorithm is the Bresenham line algorithm.
* The Bresenham line algorithm is an efficient way to draw lines on a raster display.
* It is based on the idea of using incremental error terms to determine which pixels to draw.
* The algorithm works by calculating which pixels are closest to the line being drawn and then drawing those pixels.
* The algorithm can also be used to draw circles and other curved shapes.




### Line Drawing Algorithms

1. **Bresenham's Line Drawing Algorithm**: This algorithm is an incremental scan-conversion algorithm which is used for drawing lines in a two-dimensional space. It uses integer arithmetic only, which makes it faster and more efficient than other algorithms. It is also capable of drawing circles, ellipses and other curves.

2. **DDA Line Drawing Algorithm**: This algorithm uses floating-point arithmetic and is slower than Bresenham's algorithm. It is an incremental scan-conversion algorithm which is used for drawing lines in a two-dimensional space. It is also capable of drawing circles, ellipses and other curves.

3. **Midpoint Line Drawing Algorithm**: This algorithm is also an incremental scan-conversion algorithm which is used for drawing lines in a two-dimensional space. It is based on the midpoint of the line and uses integer arithmetic only. It is faster than DDA algorithm and is capable of drawing circles, ellipses and other curves.

4. **Xiaolin Wu's Line Drawing Algorithm**: This algorithm is an antialiased line drawing algorithm which is used for drawing lines in a two-dimensional space. It uses floating-point arithmetic and is slower than Bresenham's algorithm. It is capable of drawing circles, ellipses and other curves with smooth antialiased edges.




### Circle Generating Algorithms

1. Bresenham’s Circle Algorithm: This algorithm is used to generate a circle using only integer arithmetic operations. It is an incremental algorithm, which means that it starts at the center of the circle and then works its way outward. It uses the midpoint of the circle to generate the points on the circumference of the circle. 

2. Midpoint Circle Algorithm: This algorithm is based on the same principle as Bresenham’s algorithm, but it is slightly more efficient. It uses the midpoint of the circle to generate the points on the circumference of the circle. It is also an incremental algorithm, which means that it starts at the center of the circle and then works its way outward.

3. Polar Coordinates Algorithm: This algorithm is based on the concept of plotting points in a polar coordinate system. It uses the polar coordinate system to generate the points on the circumference of the circle. It is a non-incremental algorithm, which means that it starts at the circumference of the circle and then works its way inward.

4. Linear Interpolation Algorithm: This algorithm is based on the concept of linear interpolation. It uses linear interpolation to generate the points on the circumference of the circle. It is a non-incremental algorithm, which means that it starts at the circumference of the circle and then works its way inward.





### Mid-point Circle Generating Algorithm

1. The mid-point circle generating algorithm is an algorithm used to draw circles on a computer graphics display. 
2. It is based on the fact that a circle is the locus of points that are equidistant from a given point, called the center. 
3. The algorithm works by calculating the coordinates of points on the circumference of the circle. 
4. The algorithm takes two parameters as input, the center and the radius of the circle. 
5. The algorithm starts by calculating the coordinates of the point on the circumference at angle 0. 
6. Then, it calculates the coordinates of the point on the circumference at angle θ, where θ is the angle between the two points. 
7. The algorithm then calculates the coordinates of the point on the circumference at angle 2θ, and so on. 
8. The coordinates of the points on the circumference are then used to draw the circle on the display. 
9. The algorithm is simple and efficient, and can be used to draw circles of any radius.




### Parallel Version of Algorithms for Unit 1 - Introduction and Line Generation in Computer Graphics

1. Cohen-Sutherland Line Clipping Algorithm: This algorithm is used to clip a line against a rectangular window. It divides the line into four regions and determines which parts of the line should be visible.

2. Liang-Barsky Line Clipping Algorithm: This algorithm is used to clip a line against a rectangular window. It uses a parametric form of the line equation and then determines the parameters that make the line visible.

3. Cyrus-Beck Line Clipping Algorithm: This algorithm is used to clip a line against a convex polygon. It divides the line into two parts and then determines which parts of the line should be visible.

4. Midpoint Line Drawing Algorithm: This algorithm is used to draw a line from one point to another. It uses the midpoint of the line and then determines the next pixel to be plotted based on the decision parameter.

5. Bresenham's Line Drawing Algorithm: This algorithm is used to draw a line from one point to another. It uses the midpoint and then determines the next pixel to be plotted based on the decision parameter.

6. Xiaolin Wu's Line Drawing Algorithm: This algorithm is used to draw a line from one point to another. It uses the midpoint and then determines the next pixel to be plotted based on the decision parameter and the fractional part of the coordinates of the line endpoints.




## Unit 2 - Transformations

1. Transformation is a process of changing the position, size and/or orientation of an object. 
2. Reflection is a type of transformation in which an object is flipped over a line or plane. 
3. Rotation is a type of transformation in which an object is rotated around a point. 
4. Translation is a type of transformation in which an object is moved from one location to another without changing its orientation or size. 
5. Enlargement is a type of transformation in which an object is increased in size. 
6. Reduction is a type of transformation in which an object is decreased in size. 
7. Combination of transformations is a type of transformation in which two or more transformations are combined to form a single transformation.





### Basic Transformations

1. Translation: Translation is a transformation that moves an object in the 2D or 3D space. It can be described using a vector (x, y, z).
2. Rotation: Rotation is a transformation that rotates an object around an axis. The angle of rotation is specified in degrees.
3. Scaling: Scaling is a transformation that changes the size of an object. It can be uniform (all dimensions are scaled by the same factor) or non-uniform (each dimension is scaled by a different factor).
4. Shear: Shear is a transformation that changes the shape of an object. It is typically defined by two shear factors (x, y).
5. Reflection: Reflection is a transformation that reflects an object across an axis. The axis of reflection can be either vertical or horizontal.




### Matrix Representations and Homogenous Coordinates

1. A matrix is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns. Matrices can be used to represent linear transformations, such as rotation, scaling, and shearing.

2. Homogenous coordinates are a special type of coordinates used in computer graphics. They are used to represent points in 3D space as a combination of three numbers, rather than as three separate coordinates.

3. Transformation matrices are used to represent linear transformations in computer graphics. These matrices can be used to rotate, scale, and shear objects in 3D space.

4. Homogenous coordinates can be used to represent points in 3D space. These coordinates are represented as a combination of three numbers, rather than as three separate coordinates.

5. Transformation matrices can be multiplied together to represent a sequence of transformations. This is useful for representing complex transformations, such as those used in animation.

6. Transformation matrices can also be used to represent the inverse of a transformation. This is useful for performing inverse transformations, such as those used for collision detection.




### Composite Transformations 

* Composite transformations are a combination of two or more transformations, such as a translation followed by a rotation. 
* The composite transformation can be represented as a single transformation matrix, which is the product of the individual transformation matrices. 
* The order in which the individual transformations are applied is important, as it affects the final result. 
* The composite transformation matrix is calculated by multiplying the individual transformation matrices in the correct order. 
* The composite transformation matrix can be used to transform any point in the plane. 
* The composite transformation matrix can also be used to transform lines, circles and other shapes. 
* The composite transformation matrix can be used to perform a variety of tasks, such as scaling, rotating, translating and shearing.




### Reflections and Shearing

* Reflections are a type of transformation in computer graphics where a line, or plane, is used to create a mirror image of an object. When an object is reflected, its coordinates are reversed across the line or plane of reflection. 
* Shearing is a transformation in computer graphics where an object is moved in a direction that is not parallel to any of its axes. This transformation is used to create an angled or slanted version of an object. 
* In order to apply a reflection or shearing transformation to an object, the object must first be translated to the origin (0,0). Then, the reflection or shearing transformation can be applied. Finally, the object is translated back to its original position. 
* Reflections and shearing transformations can be combined to create more complex transformations, such as rotations.




### Windowing and Clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

* Windowing is the process of selecting a portion of the display area to be displayed. It is used to display a particular portion of the scene on the screen.
* Clipping is the process of removing the objects that lie outside the viewing area. It is used to limit the objects to the viewing area.
* Windowing and Clipping are important operations in Computer Graphics as they help to reduce the time taken to render the scene.
* Windowing and Clipping can be performed in two ways:
    * Viewport Transformation: This method involves transforming the coordinates of the objects in the scene to the coordinates of the viewport.
    * Cohen-Sutherland Algorithm: This algorithm uses a four-bit code to identify whether an object is inside or outside the viewing area. If it is outside, then it is clipped.




### Viewing Pipeline for the Notes of the Unit 2 - Transformations in the Subject of Computer Graphics

1. The viewing pipeline is a sequence of transformations that occur when a 3D object is rendered on a 2D screen.

2. The first step is to transform the 3D object from its model coordinates to the world coordinates. This is done by multiplying the object's vertices with a transformation matrix.

3. The next step is to transform the world coordinates to the camera coordinates. This is done by multiplying the object's vertices with the camera's view matrix.

4. The next step is to transform the camera coordinates to the projection coordinates. This is done by multiplying the object's vertices with the projection matrix.

5. The next step is to transform the projection coordinates to the screen coordinates. This is done by multiplying the object's vertices with the viewport matrix.

6. Finally, the object is rendered on the 2D screen.




### Viewing Transformations 

1. Viewing transformation is a process of converting the 3D world coordinates into 2D screen coordinates. 
2. The 3D world coordinates of an object are represented by its position vector and orientation vector.
3. The 2D screen coordinates are the x,y coordinates on the screen.
4. The viewing transformation is a combination of a translation, rotation and scaling.
5. The translation is used to move the object from its current position to the origin of the 3D world coordinates.
6. The rotation is used to orient the object so that it is aligned with the viewing direction.
7. The scaling is used to project the object onto the 2D screen coordinates.
8. The viewing transformation is also known as the camera transformation or the viewport transformation.
9. The viewing transformation is used to create the illusion of depth in a 3D scene.
10. The viewing transformation can also be used to create the illusion of movement in a 3D scene.




### 2-D Clipping Algorithms

1. The Cohen-Sutherland Line Clipping Algorithm is a computer graphics algorithm used to determine the portion of a line that lies within a given rectangle. This algorithm works by dividing the line into four regions, each with a unique combination of bits. A line is then classified by comparing its endpoints to the four regions.

2. The Cyrus-Beck Line Clipping Algorithm is a variant of the Cohen-Sutherland algorithm that clips a line to a polygon. This algorithm works by calculating the intersection of the line with each side of the polygon. The points of intersection are then compared to the endpoints of the line to determine which portion of the line lies within the polygon.

3. The Sutherland-Hodgman Algorithm is a polygon clipping algorithm used to determine the portion of a polygon that lies within a given rectangle. This algorithm works by dividing the polygon into a series of non-overlapping regions. Each region is then tested against the rectangle to determine which portions of the polygon lie within the rectangle.

4. The Liang-Barsky Algorithm is a line clipping algorithm used to determine the portion of a line that lies within a given rectangle. This algorithm works by calculating the intersection of the line with the four sides of the rectangle. The points of intersection are then compared to the endpoints of the line to determine which portion of the line lies within the rectangle.




### Line Clipping Algorithms

Line clipping algorithms are used to determine which portions of a line segment lie within a specified region. This is a fundamental operation in computer graphics, as it allows for the efficient rendering of lines in a given area. 

The most common line clipping algorithm is the Cohen-Sutherland algorithm, which divides the area into nine regions. Each of the nine regions is associated with a binary code, and the line is clipped based on the code of the region it falls into. 

The algorithm works by first determining the binary codes for the two endpoints of the line. The codes are then compared to determine which endpoints are inside or outside of the region. If both endpoints are inside the region, then the line is trivially accepted. If both endpoints are outside, then the line is rejected. If one endpoint is inside and one is outside, then the line is clipped by finding the intersection between the line and the boundaries of the region.

In addition to the Cohen-Sutherland algorithm, other line clipping algorithms such as the Liang-Barsky algorithm and the Cyrus-Beck algorithm are also used. These algorithms are more efficient than the Cohen-Sutherland algorithm, but they are more complex to implement. 

Line clipping algorithms are an important tool in computer graphics and are used in a variety of applications, including 3D graphics, computer aided design (CAD), and image processing.




### Cohen Sutherland Line Clipping Algorithm

The Cohen Sutherland line clipping algorithm is a computer graphics algorithm used to determine whether a line segment is visible in a given viewing window. It is based on the idea of dividing the viewing window into four regions, each of which is assigned a binary code.

1. The algorithm works by comparing the two endpoints of the line segment to the boundary of the viewing window. 
2. Each endpoint is assigned a 4-bit code based on its position relative to the boundary. 
3. If the 4-bit codes of both endpoints are the same, the line segment is either completely inside or completely outside the viewing window, and can be discarded or kept accordingly. 
4. If the codes are different, the line segment must intersect the boundary, and must be clipped at the point of intersection. 
5. This is done by finding the intersection of the line segment and the boundary, and replacing the endpoint with the intersection point. 
6. The algorithm is then repeated for the new line segment until both endpoints have the same code, indicating that the line segment is completely inside the viewing window. 
7. Finally, the visible portion of the line segment is drawn.




### Liang Barsky Algorithm

* Liang Barsky algorithm is an algorithm used in computer graphics to clip a line segment to a rectangular area. 
* It works by testing each side of the rectangular area for the line segment's intersection and then clipping the line segment accordingly.
* The algorithm can be implemented with the following steps:
  1. Calculate the parameters of the line.
  2. Test each side of the rectangular area for intersection.
  3. Calculate the intersection points.
  4. Clip the line segment.
* The algorithm is useful for applications such as computer-aided design (CAD) and computer animation. It can also be used to create a line clipping window in a graphical user interface.




### Line Clipping Against Non-Rectangular Clip Windows

1. Line clipping is a process used in computer graphics to limit the lines that are drawn to the boundaries of a designated area, known as the clip window.
2. Non-rectangular clip windows can be used to clip lines in a more complex way than a rectangular clip window.
3. A polygon clip window can be used to clip lines to the edges of the polygon.
4. A circular clip window can be used to clip lines to the circumference of a circle.
5. A line-based clip window can be used to clip lines to a set of lines.
6. The Cohen-Sutherland algorithm is an algorithm used to clip lines against a rectangular clip window.
7. The Liang-Barsky algorithm is an algorithm used to clip lines against an arbitrary clip window.
8. The Cyrus-Beck algorithm is an algorithm used to clip lines against a polygon clip window.
9. The Midpoint algorithm is an algorithm used to clip lines against a circular clip window.
10. The Weiler-Atherton algorithm is an algorithm used to clip lines against a line-based clip window.




### Polygon Clipping
Polygon clipping is a process used in computer graphics to remove parts of a polygon that are outside of a viewing area. It is used to create a more efficient image by reducing the amount of data that needs to be processed.

Polygon clipping can be used for a variety of purposes, including:

- Creating a more efficient image by reducing the amount of data that needs to be processed
- Reducing the amount of data that needs to be stored in memory
- Creating more realistic images by clipping out parts of the image that are outside of the viewing area
- Improving the performance of a game or application by reducing the amount of data that needs to be processed
- Creating more accurate images by clipping out parts of the image that are outside of the viewing area
- Improving the accuracy of a 3D model by removing parts of the model that are outside of the viewing area

Polygon clipping is an important concept to understand when working with computer graphics. It can help create more efficient images and reduce the amount of data that needs to be processed.




### Sutherland Hodgeman Polygon Clipping

* Sutherland Hodgeman polygon clipping is a technique used in computer graphics to clip a polygon against a clip window.
* It uses the concept of half-space clipping to clip the polygon against the four edges of the clip window.
* The algorithm works by successively clipping the polygon against the four edges of the clip window.
* The first step is to clip the polygon against the left edge of the clip window.
* The second step is to clip the polygon against the top edge of the clip window. 
* The third step is to clip the polygon against the right edge of the clip window. 
* The fourth and final step is to clip the polygon against the bottom edge of the clip window. 
* After all four steps are complete, the resulting polygon will be the clipped polygon. 
* This technique is used in many computer graphics applications, such as 3D modeling, image processing, and game development.




### Weiler and Atherton Polygon Clipping
Weiler and Atherton polygon clipping is a technique used in computer graphics to clip a polygon against one or more other polygons. This technique is useful for applications such as image processing, graphics design, and computer animation.

The technique works by performing a series of line-segment intersections between the polygons. The result of this intersection is a set of output polygons that are the clipped versions of the input polygons.

The algorithm is divided into three steps:
1. Initialization: This step involves setting up the data structures for the algorithm and determining the initial polygon vertices.
2. Scan Conversion: This step involves scanning the polygon edges and determining the intersections between the polygons.
3. Output: This step involves generating the output polygons from the intersection points.

The algorithm is relatively simple and efficient, and it can be used to clip any number of polygons against one another. However, it is important to note that the algorithm does not guarantee the output polygons will be convex, so additional steps may be needed to ensure this.




### Curve Clipping for the Notes of Unit 2 - Transformations in the Subject of Computer Graphics

1. Curve Clipping is a process by which a curve is clipped against a rectangular window. 
2. The rectangular window is defined by the user and can be any size or shape. 
3. The process involves clipping the curve against the edges of the window and then adjusting the curve so that it fits within the window. 
4. This process is used in computer graphics to create a more realistic representation of a scene or object. 
5. Curve clipping can be used to reduce the complexity of a scene and make it easier to render. 
6. It can also be used to create a more aesthetically pleasing image. 
7. The process of curve clipping involves dividing the curve into sections and then clipping each section against the edges of the window. 
8. The resulting curve is then adjusted so that it fits within the window. 
9. Curve clipping can be used to create a more realistic representation of a scene or object. 
10. It can also be used to reduce the complexity of a scene and make it easier to render.




### Text Clipping for the Notes of the Unit 2 - Transformations in the Subject of Computer Graphics

1. Text clipping is a technique used in computer graphics to limit the area of a picture that is visible.
2. It is used to clip a text from an image or to clip a text from a scene.
3. It helps to make a scene more efficient by limiting the area of the picture that needs to be rendered.
4. Transformations are used to manipulate objects in a scene.
5. Transformations can include scaling, rotating, translating, and shearing.
6. Scaling changes the size of an object, rotating changes the orientation of an object, translating moves an object, and shearing changes the shape of an object.
7. Transformations are used to create realistic scenes in computer graphics.
8. Transformations can also be used to create special effects in movies and video games.




## Unit 3 - Three Dimensional

1. Three-dimensional (3D) objects are objects that have three dimensions: length, width, and height. 
2. 3D objects can be represented in two-dimensional (2D) space, such as on a computer screen, by using a process called 3D rendering. 
3. 3D rendering is the process of taking a 3D object and representing it in a 2D format, usually using a computer program. 
4. 3D rendering can be used to create images of objects that are difficult to represent in 2D, such as complex shapes or curved surfaces. 
5. 3D rendering is used in many industries, such as architecture, engineering, and video game development. 
6. 3D printing is a process of using a 3D printer to create a physical object from a 3D model. 
7. 3D printing can be used to create objects with complex shapes and intricate details that would be difficult or impossible to create with traditional manufacturing methods. 
8. 3D printing is used in a variety of industries, such as aerospace, automotive, and medical.




### 3-D Geometric Primitives

* A 3-D geometric primitive is a basic shape used to construct 3-D models.
* Primitives include cubes, spheres, cylinders, cones, pyramids, tori and more.
* Primitives can be combined and manipulated to create complex 3-D objects.
* Primitives are typically defined by a set of parameters, such as size, position, orientation and material properties.
* Primitives are used to create 3-D models for computer graphics applications, such as animation, virtual reality and video games.




### 3-D Object Representation

* 3-D objects can be represented in two ways: wireframe and surface representation.
* Wireframe representation is the simplest form of 3-D object representation. It consists of a set of points connected by lines that define the edges of the object.
* Surface representation involves representing the object with a set of polygons. These polygons are connected together to form the surface of the object.
* In order to represent a 3-D object accurately, it is necessary to define the position and orientation of the object in the 3-D space.
* The position and orientation of the object can be specified using a transformation matrix. This matrix defines the transformation from the object's local coordinate system to the global coordinate system.
* In addition to the transformation matrix, other parameters such as color, texture, shading, and lighting can also be specified in order to accurately represent a 3-D object.




### 3-D Transformation 

* 3-D transformation is the process of manipulating a 3-dimensional object in a virtual space. 
* It involves translating, rotating, scaling, and skewing the object. 
* Translating an object involves moving it along the x, y and z axes. 
* Rotating an object involves rotating it around an axis. 
* Scaling an object involves changing its size. 
* Skewing an object involves changing its shape. 
* All of these transformations can be combined to create complex objects. 
* 3-D transformation is used in computer graphics to create realistic images and animations.




### 3-D Viewing for the Notes of the Unit 3 - Three Dimensional in the Subject of Computer Graphics 

1. 3-D viewing is the process of displaying a 3-dimensional object or scene on a 2-dimensional surface.
2. 3-D viewing relies on the use of a virtual camera, which is used to capture the 3-D scene from a specific point of view.
3. The virtual camera can be manipulated to create different views of the 3-D object or scene.
4. The most common type of 3-D viewing is called perspective viewing, which uses a single virtual camera to create a realistic view of an object or scene.
5. Other types of 3-D viewing include orthographic viewing, which uses multiple virtual cameras to create an abstract view of the 3-D object or scene, and stereo viewing, which uses two virtual cameras to create a 3-D effect.
6. 3-D viewing is important for computer graphics, as it allows for the creation of realistic images and animations.




### Projections for the Notes of the Unit 3 - Three Dimensional in the Subject of Computer Graphics

1. Projection is the process of mapping a 3D object onto a 2D surface. This process is used to create drawings, diagrams, and other representations of 3D objects.

2. There are three types of projection: orthographic, oblique, and perspective. Orthographic projection is a type of parallel projection, where objects are projected onto a plane without any distortion. Oblique projection is a type of parallel projection, where objects are projected onto a plane with some distortion. Perspective projection is a type of parallel projection, where objects are projected onto a plane with extreme distortion.

3. Orthographic projection is used to create technical drawings. It is the most accurate type of projection, as it does not distort the object.

4. Oblique projection is used to create diagrams and sketches. It is less accurate than orthographic projection, but it is more aesthetically pleasing.

5. Perspective projection is used to create realistic images. It is the least accurate type of projection, as it distorts the object.

6. In order to create a projection, the object must first be rotated in three-dimensional space. This is done by manipulating the object's x, y, and z coordinates.

7. After the object is rotated, the projection is created by tracing the object's outline onto the projection plane.

8. Projections can be used to create accurate representations of 3D objects, which can be used for a variety of purposes, such as engineering, architecture, and design.




### 3-D Clipping 

* 3-D clipping is a computer graphics technique used to limit the rendering of objects to a particular region of a 3-D space. 
* It is used to reduce the amount of data that needs to be processed and increase the rendering speed.
* 3-D clipping is used to determine which parts of an object are visible in a particular view of a 3-D space.
* It is used to determine which parts of an object should be rendered and which should be hidden.
* It is also used to determine which parts of an object should be shaded and which should not.
* 3-D clipping can be used to create a more realistic rendering of a 3-D scene.
* Clipping planes are used to define the boundaries of the viewable region of a 3-D space.
* Clipping planes can be used to limit the rendering of objects to a particular region of a 3-D space.
* Clipping planes can also be used to limit the rendering of objects to a particular region of a 3-D space based on their position and orientation in the 3-D space.





## Unit 4 - Curves and Surfaces

1. Curves are lines that are bent or curved in two-dimensional space. They can be described using equations and can be classified into different types, such as parabolas, circles, ellipses, and hyperbolas.

2. Surfaces are three-dimensional objects that can be described using equations. They can be classified into different types, such as planes, cylinders, cones, and spheres.

3. Parametric equations are equations that can be used to describe curves and surfaces. They involve two or more variables, and the values of these variables can be used to calculate the coordinates of a point on the curve or surface.

4. Vector equations are equations that can be used to describe curves and surfaces. They involve two or more vectors, and the values of these vectors can be used to calculate the coordinates of a point on the curve or surface.

5. Differential equations are equations that can be used to describe the properties of curves and surfaces. They involve derivatives of the equations that describe the curves and surfaces, and can be used to calculate the curvature and other properties of the curves and surfaces.




### Quadric Surfaces 

A quadric surface is a surface described by an equation of the form: 

$$ Ax^2 + By^2 + Cz^2 + 2Dxy + 2Eyz + 2Fxz + 2Gx + 2Hy + 2Iz + J = 0 $$

Quadric surfaces are often used in computer graphics for modeling curved objects such as spheres, cylinders, and cones. They have the advantage of being easy to work with and can be used to create smooth surfaces. 

The equation of a quadric surface can be written in matrix form as: 

$$ \begin{bmatrix} A & D & F & G \\ D & B & E & H \\ F & E & C & I \\ G & H & I & J \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} = 0 $$

The matrix on the left is known as the Quadric Matrix and contains all the information needed to define the quadric surface. The matrix can be used to determine the type of quadric surface, as well as its properties such as its orientation, center, and radius. 

The most common types of quadric surfaces are: 
* Spheres
* Ellipsoids
* Hyperboloids
* Paraboloids
* Cylinders
* Cones

Each of these can be described by a quadric matrix. For example, the quadric matrix for a sphere is: 

$$ \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -r^2 \end{bmatrix} $$

where $r$ is the radius of the sphere. 

Quadric surfaces can also be used to approximate curved surfaces. By using a quadric matrix, a surface can be approximated by a series of quadric surfaces. This is known as quadric surface approximation and is commonly used in computer graphics for modeling curved objects.




### Spheres for the Notes of the Unit 4 - Curves and Surfaces in the Subject of Computer Graphics

* A sphere is a three-dimensional shape that is made up of all points in a three-dimensional space equidistant from a given point. 
* A sphere can be described as a set of points in a three-dimensional space that are equidistant from a given point, called the center. 
* A sphere can also be described as the surface of a solid object whose volume is equal to the cube of its radius. 
* The equation of a sphere is given by: x² + y² + z² = r², where r is the radius of the sphere.
* Spheres are commonly used in computer graphics to represent objects such as planets, moons, and other celestial bodies. 
* Spheres can also be used to represent other objects such as balls, globes, and the human head. 
* The mathematical properties of a sphere can be used to calculate the surface area, volume, and other properties of objects. 
* Spheres are also used to represent curved surfaces in computer graphics, such as the surface of a cylinder or a cone.




### Ellipsoid for Unit 4 - Curves and Surfaces in Computer Graphics

* Ellipsoids are three-dimensional shapes that can be described as the locus of points in three-dimensional space that satisfy the equation: $$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$$

* Here, $a, b,$ and $c$ are the lengths of the three semi-axes of the ellipsoid. 

* Ellipsoids are a type of conic section, and are closely related to circles, ellipses, parabolas, and hyperbolas. 

* In computer graphics, ellipsoids are often used to represent objects in 3D space, such as spheres, cylinders, and other curved shapes. 

* Ellipsoids can also be used to represent the surface of a 3D object, allowing for realistic lighting and shading effects. 

* Ellipsoids can be used to create realistic terrain and landscapes in computer graphics, as well as to simulate the behavior of liquids and other materials. 

* Ellipsoids can also be used to create 3D models of objects, such as cars, buildings, and other structures.




### Blobby Objects

* Blobby objects are a class of mathematical objects used in computer graphics.
* They are defined by a set of control points, which define the shape and appearance of the object.
* Blobby objects are made up of a set of primitives, such as spheres, cubes, and cylinders, which are connected to form a single object.
* The shape and appearance of the object is determined by the relative size, position, and orientation of the primitives.
* Blobby objects are often used for creating organic shapes and textures, such as those found in nature.
* They can also be used to create complex shapes, such as those found in architectural designs.
* Blobby objects are typically rendered using ray tracing algorithms, which allow for realistic lighting and shading effects.




### Introductory Concepts of Spline for the Notes of Unit 4 - Curves and Surfaces in the Subject of Computer Graphics

1. Spline is a mathematical function used to create smooth curves and surfaces in computer graphics.
2. Splines are generally composed of multiple polynomial segments, each of which is connected at the endpoints.
3. Splines can be used to represent a variety of shapes, including circles, ellipses, and parabolas.
4. Splines are used in a variety of applications, such as 3D modeling, animation, and image processing.
5. Splines can be divided into two categories: uniform and non-uniform.
6. Uniform splines are composed of uniform polynomial segments, while non-uniform splines are composed of non-uniform polynomial segments.
7. Splines can be further divided into two types: interpolating and approximating.
8. Interpolating splines are used to interpolate data points, while approximating splines are used to approximate a given curve.
9. Splines can be represented in a variety of ways, including Bezier curves, B-splines, and NURBS.
10. Splines are used in a variety of computer graphics applications, such as 3D modeling, animation, and image processing.




### Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

* B-splines are a type of parametric curve that are widely used in computer graphics.
* B-splines are defined by a set of control points and a degree, which determines the shape of the curve.
* B-splines can be used to represent a variety of shapes, including circles, ellipses, and arbitrary curves.
* B-splines can be used to create smooth surfaces, such as Bezier surfaces.
* B-splines can be used to create complex shapes, such as NURBS curves and surfaces.
* B-splines can be used to create animation, such as motion paths and character animation.




### Bezier Curves and Surfaces 

* Bezier curves are a type of mathematical curve used in computer graphics and related fields. They are named after Pierre Bézier, who used them in the 1960s for designing curves for the bodywork of Renault cars. 
* Bezier curves are defined by a set of control points. These points define the shape of the curve. The more control points, the more complex the curve. 
* Bezier surfaces are a type of mathematical surface used in computer graphics and related fields. They are named after Pierre Bézier, who used them in the 1960s for designing surfaces for the bodywork of Renault cars. 
* Bezier surfaces are defined by a set of control points. These points define the shape of the surface. The more control points, the more complex the surface. 
* Bezier curves and surfaces can be used to create complex shapes, such as those found in 3D models. They are also used in animation, where they are used to create smooth, natural-looking movements.




## Unit 5 - Hidden Lines and Surfaces

* Hidden lines and surfaces are lines and surfaces that are not visible in a drawing.
* Hidden lines are used to represent edges, curves, and surfaces that are not visible in the drawing.
* Hidden lines are usually drawn with a dashed line.
* Hidden surfaces are used to represent surfaces that are not visible in the drawing.
* Hidden surfaces are usually drawn with a cross-hatched pattern.
* Hidden lines and surfaces are used to show the shape of an object more accurately.
* Hidden lines and surfaces can be used to create a 3D effect in a drawing.




### Back Face Detection Algorithm

1. Back Face Detection (BFD) is an algorithm used to determine which surfaces of a 3D object are visible from a given viewpoint.

2. BFD is important in computer graphics as it determines which surfaces of an object can be seen and which should be hidden from view.

3. The algorithm works by calculating the dot product of the surface normal and the vector from the viewpoint to the surface vertex.

4. If the dot product is less than zero, then the surface is facing away from the viewpoint and should be hidden.

5. BFD is often used in conjunction with hidden line removal algorithms to improve the efficiency of rendering 3D scenes.




### Depth Buffer Method

1. The depth buffer method is a computer graphics technique used to determine visibility of surfaces by storing the depth of each pixel in a buffer. 
2. This method works by writing the depth of each pixel in a frame buffer as the scene is rendered. 
3. During the rendering process, the depth of a pixel is compared to the stored depth value in the buffer. 
4. If the depth of the pixel is less than the stored value, then the pixel is visible and the stored value is updated to the new depth. 
5. This method is used to determine which surfaces are visible and which are hidden. 
6. This technique is commonly used in 3D computer graphics to prevent objects that are behind other objects from being visible. 
7. It is also used to determine which objects are in front of others and which objects are occluded by other objects.




### A-Buffer Method

A-Buffer is a method used in computer graphics to render 3D scenes. It is an efficient algorithm for hidden line and surface removal.

1. The A-Buffer works by storing the depth of each pixel in a buffer.
2. The depth values are compared to the depth of the object being rendered.
3. If the depth of the object is greater than the depth stored in the buffer, the object is visible.
4. If the depth of the object is less than the depth stored in the buffer, the object is hidden.
5. The A-Buffer is a fast algorithm for hidden line and surface removal, as it only needs to compare the depths of the object and the buffer.
6. It is also memory efficient, as it only needs to store the depths of the pixels in the buffer.
7. The A-Buffer is commonly used in 3D computer graphics applications, such as games, CAD, and virtual reality.




### Scan Line Method

1. Scan line method is a computer graphics technique that is used to render two-dimensional images from 3D models.
2. It works by creating a line of pixels from left to right across the screen, one line at a time.
3. As the scan line is created, it is compared to the 3D model to determine which pixels should be drawn and which should be hidden.
4. This technique is used to render hidden lines and surfaces in a 3D model, as well as to create shadows and highlights.
5. The algorithm is relatively simple and can be implemented in a few lines of code.
6. It is also relatively fast, making it a popular choice for rendering 3D graphics.




### Basic Illumination Models

1. Ambient Illumination: Ambient illumination is a type of illumination that is used to simulate the effect of light reflecting off of multiple surfaces in an environment. It is a uniform, omnidirectional light source that is used to simulate the effect of indirect light.

2. Diffuse Illumination: Diffuse illumination is a type of illumination that is used to simulate the effect of light reflecting off of a single surface. It is a non-directional light source that is used to simulate the effect of direct light.

3. Specular Illumination: Specular illumination is a type of illumination that is used to simulate the effect of light reflecting off of a single surface in a specific direction. It is a directional light source that is used to simulate the effect of reflected light.

4. Phong Illumination Model: The Phong Illumination Model is a type of illumination model that is used to simulate the effect of light reflecting off of multiple surfaces in an environment. It is a combination of ambient, diffuse, and specular illumination models.




### Ambient Light

* Ambient light is a form of illumination that is present in the environment. It is usually a low-level light that is evenly distributed in all directions.
* Ambient light is used to create a general illumination in a scene and to provide a base level of illumination for all objects in the scene.
* Ambient light is not affected by the position of objects in the scene, and so it is not affected by shadows or occlusions.
* The color and intensity of ambient light can be adjusted to create a desired effect in the scene.
* Ambient light is used in computer graphics to create a more realistic lighting environment and to simulate the effects of indirect lighting.
* Ambient light can be used to create a more realistic lighting environment by providing a base level of illumination for all objects in the scene.
* Ambient light can also be used to simulate the effects of indirect lighting, such as bounced light from other objects in the scene.




### Diffuse Reflection

* Diffuse reflection is a type of reflection that occurs when light is scattered in many directions due to the irregular surface of the reflecting object. 
* This type of reflection is most commonly observed when light reflects off of a matte or dull surface. 
* Diffuse reflection is the most common type of reflection and is responsible for the majority of the light that is seen in our everyday lives. 
* Diffuse reflection is also known as Lambertian reflection and is characterized by a uniform intensity of reflected light in all directions. 
* The intensity of the diffuse reflection is proportional to the cosine of the angle between the surface normal and the incident light. 
* The light that is reflected off of a diffuse surface is not directional, meaning that the reflected light will not be focused in one specific direction. 
* Diffuse reflection is an important concept in the field of computer graphics, as it is used to simulate the appearance of surfaces in 3D environments.




### Specular Reflection

* Specular reflection is a type of reflection that occurs when light is reflected off of a surface in a smooth, mirror-like fashion.
* The angle of incidence of the light ray is equal to the angle of reflection.
* This type of reflection is common in surfaces such as glass, polished metal, and water.
* Specular reflection is used in computer graphics to create realistic looking surfaces and objects.
* It is used to simulate the reflection of light from a surface and can be used to create the illusion of depth and texture.
* The intensity of the specular reflection is determined by the material and the angle of incidence of the light.
* For example, a surface that is highly reflective will have a brighter specular reflection than a surface that is less reflective.
* The specular reflection of a surface can also be adjusted by changing the angle of incidence of the light.
* By changing the angle of incidence, the intensity of the specular reflection can be increased or decreased.
* This can be used to create realistic looking surfaces and objects in computer graphics.




### Phong Model

The Phong Model is a lighting model used in computer graphics to simulate the interaction of light with surfaces. It is used to calculate the intensity of light reflected from a surface at a given point, and is based on the concept of local illumination. It is named after Bui Tuong Phong, who developed the model in 1973.

The Phong Model consists of three components: 
* Ambient Light: This is the light that is present in the environment, and is independent of the light source. It is usually modelled as a constant color.
* Diffuse Reflection: This is the light that is reflected off of the surface in all directions. It is modelled as a Lambertian reflectance.
* Specular Reflection: This is the light that is reflected off of the surface in a specific direction. It is modelled as a Phong reflectance.

In the context of hidden lines and surfaces, the Phong Model is used to calculate the intensity of light that is reflected off of a surface, and thus determine which parts of the surface are visible. This is used to render objects that have hidden lines and surfaces, such as a cube or a sphere.




### Combined Approach for the Notes of the Unit 5 - Hidden Lines and Surfaces in the Subject of Computer Graphics

1. Hidden line algorithms are used to determine which parts of a 3D object are visible to the viewer. This is done by calculating which lines of the object are not obscured by other objects in the scene.

2. The hidden line algorithm works by tracing a line from the eye of the viewer to each point on the object. If the line is blocked by another object, then the point is hidden.

3. Hidden surface algorithms are used to determine which parts of a 3D object are visible to the viewer. This is done by calculating which surfaces of the object are not obscured by other objects in the scene.

4. The hidden surface algorithm works by tracing a ray from the eye of the viewer to each point on the object. If the ray is blocked by another object, then the point is hidden.

5. The hidden line and hidden surface algorithms are often combined to create a more accurate picture of the scene. This combined algorithm is often used in computer graphics applications.

6. The combined algorithm is also used to create 3D images that are more realistic and detailed. This is done by using the hidden line and hidden surface algorithms together to create a more complete picture of the scene.




### Warn Model for Unit 5 - Hidden Lines and Surfaces in Computer Graphics

1. The Warn model is an algorithm for hidden surface removal in 3D computer graphics. 
2. It is based on the Painter's algorithm, which renders objects in the order of their distance from the viewer. 
3. The Warn model adds a few more steps to the Painter's algorithm to improve its accuracy. 
4. First, the algorithm sorts objects according to their depth. 
5. Then, it checks for objects that are partially hidden by other objects and marks them for removal. 
6. Finally, it renders the objects in the order of their depth, taking into account the objects that were marked for removal. 
7. This results in a more accurate rendering of the scene, with hidden surfaces being correctly removed.




### Intensity Attenuation for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Intensity attenuation is the process of decreasing the intensity of light or color in a scene as a result of distance or other factors.
- It is often used to create a more realistic and believable environment in computer graphics.
- Intensity attenuation can be simulated using a simple linear equation, where the intensity of the light or color is decreased by a constant factor over a certain distance.
- Intensity attenuation can also be simulated using more complex equations, such as the inverse square law, which states that the intensity of light or color decreases by a factor of the square of the distance.
- Intensity attenuation can be used to create more realistic shadows and reflections, as well as to simulate the effects of fog, smoke, and other atmospheric effects.
- Intensity attenuation can also be used to simulate the effects of ambient occlusion, which is the effect of objects obscuring the light from other objects in a scene.




### Color Consideration for the Notes of the Unit 5 - Hidden Lines and Surfaces in the Subject of Computer Graphics

1. Color is an important element in the graphics of a 3D scene. It can be used to enhance the realism of a scene, add emphasis to certain objects, and provide a more aesthetically pleasing experience overall. 

2. Color can be used to represent different types of surfaces, such as metal, wood, or plastic. Colors can also be used to distinguish between different types of hidden lines and surfaces.

3. Color can be used to represent the depth of a surface, with darker colors representing surfaces that are further away and lighter colors representing surfaces that are closer.

4. Color can also be used to represent the direction of a surface. For example, a surface that is facing away from the camera can be represented by a darker color, while a surface that is facing towards the camera can be represented by a lighter color.

5. Color can also be used to represent the texture of a surface, with different colors being used to represent different types of textures.

6. Finally, color can be used to represent the transparency of a surface, with lighter colors representing more transparent surfaces and darker colors representing more opaque surfaces.




### Transparency and Shadows 

1. Transparency is the effect of making an object appear to be partially transparent. It is used to create realistic effects in computer graphics, such as glass, water, and other translucent objects. 
2. Shadows are used to give the illusion of depth to a scene. They are created by simulating the effect of light being blocked by an object. 
3. Transparency and shadows can be used together to create more realistic scenes. For example, a transparent object will cast a shadow on the objects behind it, and the shadow will be partially transparent as well. 
4. When modeling objects with transparency and shadows, it is important to consider how the light will interact with the object. For example, a transparent object may block some of the light, while a shadow may be cast in a different direction. 
5. Transparency and shadows can also be used to create interesting effects in 3D graphics. For example, a transparent object can be used to create a refractive effect, or a shadow can be used to create a silhouette. 
6. Finally, transparency and shadows can be used to create more believable animations. For example, a transparent object can be used to simulate a character walking through a door, or a shadow can be used to create a dynamic light source.

