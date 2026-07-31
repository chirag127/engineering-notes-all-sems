### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A line drawing algorithm is a method for estimating a line segment on discrete graphical media such as pixel-based screens and printers in computer graphics.
- A line segment is defined by two endpoints, each with an x and y coordinate.
- To draw a line, a computer must work out which pixels need to be filled so that the line looks straight.
- There are different algorithms for drawing a line, each with different advantages and disadvantages in terms of accuracy, efficiency, and simplicity.
- Some of the common line drawing algorithms are:

  - Naive algorithm: This algorithm simply rounds the x and y coordinates of each point on the line to the nearest integer and fills the corresponding pixel. It is easy to implement but produces jagged lines and may skip some pixels.
  - Digital Differential Analyzer (DDA) algorithm: This algorithm uses the slope of the line to incrementally calculate the x and y coordinates of each point on the line. It produces smoother lines than the naive algorithm but requires floating-point arithmetic and may be slow .
  - Bresenham's algorithm: This algorithm uses integer arithmetic and error terms to determine which pixel to fill at each step. It is faster and more accurate than the DDA algorithm but more complex to implement .
  - Mid-point algorithm: This algorithm uses the mid-point of the line segment to decide which pixel to fill next. It is similar to Bresenham's algorithm but avoids multiplication and division operations .

- The following diagram illustrates the difference between the naive, DDA, and Bresenham's algorithms for drawing a line with slope 2/3:

```markdown
![Line drawing algorithms comparison](line_drawing_algorithms.png)
```

- The following pseudocode shows the basic steps of the Bresenham's algorithm for drawing a line from (x1, y1) to (x2, y2) with slope less than 1:

```markdown
```pseudocode
Bresenham's algorithm:

Input: x1, y1, x2, y2
Output: A set of pixels to fill

Initialize dx = x2 - x1, dy = y2 - y1
Initialize x = x1, y = y1
Initialize p = 2 * dy - dx
Fill the pixel (x, y)
While x < x2
  If p < 0
    p = p + 2 * dy
  Else
    p = p + 2 * (dy - dx)
    y = y + 1
  End if
  x = x + 1
  Fill the pixel (x, y)
End while
```
```markdown