### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Line drawing algorithms are methods for approximating a line segment on discrete graphical media, such as pixel-based displays and printers.
- Line drawing algorithms are important in computer graphics because they are the basis for rendering other geometric primitives, such as polygons, circles, and curves.
- Line drawing algorithms need to balance accuracy, efficiency, and simplicity. They also need to handle different cases of line slopes, orientations, and lengths.
- There are following algorithms used for drawing a line:
  - DDA (Digital Differential Analyzer) Line Drawing Algorithm
    - It is based on the idea of incrementing either x or y coordinate by a small amount and calculating the other coordinate using the line equation y = mx + b.
    - It is simple to implement but suffers from rounding errors and floating-point operations.
  - Bresenham’s Line Drawing Algorithm
    - It is an optimized version of DDA that uses only integer arithmetic and avoids multiplication and division.
    - It is based on the idea of choosing the closest pixel to the ideal line using a decision variable that depends on the error term.
    - It is faster and more accurate than DDA but requires more logic to handle different cases of line slopes.
  - Mid-Point Line Drawing Algorithm
    - It is a variation of Bresenham’s algorithm that uses the mid-point of the two possible pixels as the decision variable.
    - It is simpler and more symmetric than Bresenham’s algorithm but requires more calculations per iteration.
- The following diagram illustrates the three algorithms for drawing a line with slope less than 1:

![Line drawing algorithms](https://www.tutorialandexample.com/wp-content/uploads/2019/06/Line-Drawing-Algorithm-in-Computer-Graphics-1.png)

- The following pseudocode shows the general steps of the three algorithms for drawing a line with slope less than 1:

```
// DDA algorithm
Input: x1, y1, x2, y2 // endpoints of the line
Output: pixels to be filled
dx = x2 - x1
dy = y2 - y1
m = dy / dx // slope of the line
x = x1
y = y1
plot(x, round(y)) // plot the first pixel
while x < x2
  x = x + 1 // increment x by 1
  y = y + m // increment y by slope
  plot(x, round(y)) // plot the next pixel
end while

// Bresenham's algorithm
Input: x1, y1, x2, y2 // endpoints of the line
Output: pixels to be filled
dx = x2 - x1
dy = y2 - y1
d = 2 * dy - dx // initial decision variable
x = x1
y = y1
plot(x, y) // plot the first pixel
while x < x2
  x = x + 1 // increment x by 1
  if d < 0 // the lower pixel is closer
    d = d + 2 * dy // update the decision variable
  else // the upper pixel is closer
    y = y + 1 // increment y by 1
    d = d + 2 * (dy - dx) // update the decision variable
  end if
  plot(x, y) // plot the next pixel
end while

// Mid-point algorithm
Input: x1, y1, x2, y2 // endpoints of the line
Output: pixels to be filled
dx = x2 - x1
dy = y2 - y1
d = dy - dx / 2 // initial decision variable
x = x1
y = y1
plot(x, y) // plot the first pixel
while x < x2
  x = x + 1 // increment x by 1
  if d < 0 // the lower pixel is closer
    d = d + dy // update the decision variable
  else // the upper pixel is closer
    y = y + 1 // increment y by 1
    d = d + (dy - dx) // update the decision variable
  end if
  plot(x, y) // plot the next pixel

```
