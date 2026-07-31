# Points and Lines for the Notes of the Unit 1 - Introduction and Line Generation in the Subject of Computer Graphics

- A point is the fundamental element of picture representation. It is the position in the plane defined as either pair or triplets of numbers depending upon the dimension.
- A line is a basic element in graphics. To draw a line, you need two points between which you can draw a line. In the following three algorithms, we refer the one point of line as X0, Y0 and the second point of line as X1, Y1.
- A line function is used to generate a straight line between any two end points. Usually a line function is provided with the location of two pixel points called the starting point and the end point and it is up to the computer to decide what pixels fall between these two points so that a straight line is generated.
- There are different algorithms to draw a line, such as:
  - DDA algorithm: It is an incremental scan-conversion method. It is based on calculating either delta x or delta y, depending on the slope of the line, and then using the equation of the line to calculate the other value.
  - Bresenham’s Line Algorithm: It is an algorithm that determines the points of an n-dimensional raster that should be selected in order to form a close approximation to a straight line between two points. It is commonly used to draw lines on a computer screen, as it uses only integer addition, subtraction and bit shifting, all of which are very cheap operations in standard computer architectures.
  - Mid-point Line algorithm: It is an algorithm used to determine the points needed for rasterizing a line. It uses only integer addition and subtraction and comparison operations. It is a type of Bresenham’s algorithm that is optimized for drawing circles.
- A line can have different attributes, such as:
  - Color: It is the property of the line that determines its hue and intensity. It can be set using the setcolor() function.
  - Width: It is the property of the line that determines its thickness. It can be set using the setlinestyle() function.
  - Pattern: It is the property of the line that determines its style, such as solid, dashed, dotted, etc. It can be set using the setlinestyle() function.
- A line can also be represented by an equation of the form ax + by + c = 0, where a, b and c are constants. The slope of the line is given by -a/b and the intercept is given by -c/b.
- A line can also be represented by a parametric equation of the form x = x0 + t(x1 - x0) and y = y0 + t(y1 - y0), where x0, y0 and x1, y1 are the end points of the line and t is a parameter that varies from 0 to 1.
- A line can also be represented by a vector equation of the form r = r0 + t(v), where r0 is the position vector of a point on the line, v is the direction vector of the line and t is a scalar parameter.