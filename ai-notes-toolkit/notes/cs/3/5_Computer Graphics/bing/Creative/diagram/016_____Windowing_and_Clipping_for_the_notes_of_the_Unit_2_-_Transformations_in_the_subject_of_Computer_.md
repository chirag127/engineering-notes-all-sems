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