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

![Cohen Sutherland example](https://sighack.com/images/cohen-sutherland-line-clipping-algorithm/cohen-sutherland-line-clipping-algorithm-example.png)

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