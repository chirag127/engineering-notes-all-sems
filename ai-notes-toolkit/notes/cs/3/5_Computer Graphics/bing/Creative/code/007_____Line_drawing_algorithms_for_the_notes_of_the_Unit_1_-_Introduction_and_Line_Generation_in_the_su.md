### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A line drawing algorithm is a method for estimating a line segment on discrete graphical media such as pixel-based screens and printers in computer graphics.
- A line segment is defined by two endpoints, each with an x and y coordinate.
- To draw a line, a computer must work out which pixels need to be filled so that the line looks straight.
- There are different algorithms for drawing a line, each with different advantages and disadvantages in terms of accuracy, efficiency, and simplicity.
- Some of the common line drawing algorithms are:

  - Naive algorithm: This algorithm simply rounds the x and y coordinates of each point on the line to the nearest integer and fills the corresponding pixel. It is easy to implement but can produce jagged lines and gaps.
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each point on the line. It is more accurate than the naive algorithm but can be slow and requires floating-point arithmetic .
  - Bresenham's algorithm: This algorithm uses integer arithmetic and error terms to determine which pixel to fill at each step. It is faster and more efficient than the DDA algorithm and produces smooth lines .
  - Mid-point algorithm: This algorithm uses the mid-point of the line segment to decide which pixel to fill at each step. It is similar to Bresenham's algorithm but can handle lines with any slope and avoids multiplication and division operations .

- The following is a pseudocode for the Bresenham's algorithm, which is one of the most widely used line drawing algorithms:

  ```
  Input: x1, y1, x2, y2 // the endpoints of the line segment
  Output: a set of pixels to fill

  // initialize the variables
  dx = x2 - x1 // the change in x
  dy = y2 - y1 // the change in y
  x = x1 // the current x coordinate
  y = y1 // the current y coordinate
  p = 2 * dy - dx // the initial error term

  // loop until the end of the line segment is reached
  while x <= x2
    // fill the pixel at (x, y)
    plot(x, y)
    // increment x by 1
    x = x + 1
    // check the error term
    if p < 0
      // no change in y
      p = p + 2 * dy
    else
      // increment y by 1
      y = y + 1
      // update the error term
      p = p + 2 * (dy - dx)
    end if
  end while
  ```