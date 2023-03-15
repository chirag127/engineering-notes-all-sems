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