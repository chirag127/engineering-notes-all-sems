# Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A line drawing algorithm is a method for estimating a line segment on discrete graphical media such as pixel-based screens and printers in computer graphics.
- A line segment is defined by two endpoints, each with an x and y coordinate.
- To draw a line, a computer must work out which pixels need to be filled so that the line looks straight.
- There are different algorithms for drawing a line, each with different advantages and disadvantages in terms of accuracy, efficiency, and simplicity.
- Some of the common line drawing algorithms are:

  - Naive algorithm: This algorithm simply uses the slope-intercept form of the equation of a line (y = mx + b) to calculate the y coordinate for each x coordinate along the line. However, this algorithm is inefficient and inaccurate, as it involves floating-point arithmetic, rounding errors, and gaps or overlaps in the line.
  - Digital Differential Analyzer (DDA) algorithm: This algorithm is similar to the naive algorithm, but it uses integer arithmetic and avoids multiplication and division by incrementing the x and y coordinates by a small amount in each step. This algorithm is faster and more accurate than the naive algorithm, but it still suffers from rounding errors and pixel gaps .
  - Bresenham's line algorithm: This algorithm is an optimized version of the DDA algorithm, which uses only integer arithmetic and avoids multiplication and division by using a decision variable to determine whether to increment the x or y coordinate in each step. This algorithm is faster and more accurate than the DDA algorithm, and it produces a smooth line with no gaps .
  - Mid-point line algorithm: This algorithm is another variation of the DDA algorithm, which uses a mid-point between the current pixel and the next pixel to decide whether to increment the x or y coordinate in each step. This algorithm is also faster and more accurate than the DDA algorithm, and it produces a smooth line with no gaps.