### Line clipping algorithms

Line clipping algorithms are methods to remove parts of lines that lie outside a given rectangular region, called the clipping window or the viewport. This is useful for rendering only the visible parts of a scene and avoiding unnecessary computations for the invisible parts.

There are many algorithms for line clipping, but two of the most common ones are:

- **Cohen–Sutherland algorithm**: This algorithm divides the 2D space into 9 regions, of which only the middle one is the viewport. Each region is assigned a 4-bit code, called the outcode, based on whether the point is above, below, left, or right of the viewport. The algorithm then compares the outcodes of the endpoints of the line and determines if the line is completely inside, completely outside, or partially inside the viewport. If the line is partially inside, the algorithm finds the intersection points of the line with the viewport boundaries and clips the line accordingly.
- **Liang–Barsky algorithm**: This algorithm is based on the parametric equation of a line, which can be written as `x = x1 + u * (x2 - x1)`, `y = y1 + u * (y2 - y1)`, where `u` is a parameter between 0 and 1. The algorithm then uses the inequalities that define the viewport to find the values of `u` that correspond to the intersection points of the line with the viewport boundaries. The algorithm then clips the line by using the minimum and maximum values of `u` that lie within the viewport.

The following diagram illustrates the two algorithms:

![Line clipping algorithms](https://i.imgur.com/5y5w5yM.png)

The blue line is the original line, the red line is the clipped line, and the dashed lines are the viewport boundaries. The outcodes for the Cohen–Sutherland algorithm are shown in binary, and the values of `u` for the Liang–Barsky algorithm are shown in decimal.