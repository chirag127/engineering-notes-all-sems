### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Line drawing algorithms are methods for approximating a line segment on discrete graphical media, such as pixel-based displays and printers.
- Line drawing algorithms are important for computer graphics because they are used to render basic shapes, such as polygons, curves, and fonts.
- Line drawing algorithms need to be efficient, accurate, and smooth, meaning that they should minimize the number of pixels used, avoid gaps and jagged edges, and produce a visually pleasing result.
- There are several algorithms for drawing a line, each with different advantages and disadvantages. Some of the most common ones are :
  - Naive algorithm: This algorithm simply rounds the x and y coordinates of each point on the line to the nearest integer and plots the corresponding pixel. It is simple to implement, but it can produce gaps and jagged edges, especially for steep lines.
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each point on the line. It avoids gaps, but it can be slow and inaccurate due to the use of floating-point arithmetic.
  - Bresenham's algorithm: This algorithm uses integer arithmetic and error terms to determine which pixel to plot for each step along the line. It is fast and accurate, but it can produce jagged edges for steep lines.
  - Mid-point algorithm: This algorithm uses a decision variable based on the mid-point between two possible pixels to choose which one to plot for each step along the line. It is similar to Bresenham's algorithm, but it can handle any slope and produce smoother lines.
- The following diagram illustrates the difference between some of the line drawing algorithms for a line with slope 2/3:

![Line drawing algorithms comparison](https://www.tutorialandexample.com/wp-content/uploads/2019/08/Line-Drawing-Algorithm-1.png)

- The following pseudocode shows the basic steps of the naive, DDA, and Bresenham's algorithms for drawing a line from (x1, y1) to (x2, y2) :

```
// Naive algorithm
function naive_line(x1, y1, x2, y2)
  // Calculate the slope of the line
  m = (y2 - y1) / (x2 - x1)
  // Loop over the x coordinates from x1 to x2
  for x from x1 to x2
    // Calculate the corresponding y coordinate using the slope
    y = m * (x - x1) + y1
    // Round the y coordinate to the nearest integer
    y = round(y)
    // Plot the pixel at (x, y)
    plot(x, y)
  end for
end function

// DDA algorithm
function dda_line(x1, y1, x2, y2)
  // Calculate the absolute difference between x1 and x2, and between y1 and y2
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  // Choose the larger of dx and dy as the number of steps
  steps = max(dx, dy)
  // Calculate the increment for x and y for each step
  x_inc = dx / steps
  y_inc = dy / steps
  // Initialize the current x and y coordinates to x1 and y1
  x = x1
  y = y1
  // Loop over the number of steps
  for i from 0 to steps
    // Plot the pixel at the current x and y coordinates
    plot(x, y)
    // Increment x and y by x_inc and y_inc
    x = x + x_inc
    y = y + y_inc
  end for
end function

// Bresenham's algorithm
function bresenham_line(x1, y1, x2, y2)
  // Calculate the absolute difference between x1 and x2, and between y1 and y2
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  // Initialize the error term to zero
  error = 0
  // Choose the initial y coordinate based on the sign of the slope
  if y1 < y2 then
    y = y1
    y_inc = 1

```
