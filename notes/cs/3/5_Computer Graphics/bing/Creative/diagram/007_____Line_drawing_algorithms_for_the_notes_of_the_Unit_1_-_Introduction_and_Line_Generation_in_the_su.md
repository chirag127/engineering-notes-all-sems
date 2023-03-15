### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A line drawing algorithm is a graphical algorithm for representing a line segment on discrete graphical media, such as pixel-based displays and printers .
- On such media, line drawing requires an approximation (in nontrivial cases) because a line segment may not pass through exact pixel coordinates.
- A line drawing algorithm should be efficient, accurate, and produce a smooth and uniform appearance of the line.
- There are following algorithms used for drawing a line:
  - DDA (Digital Differential Analyzer) Line Drawing Algorithm
    - It is based on the idea of incrementing either x or y coordinate by a small amount (Δx or Δy) and calculating the other coordinate using the slope of the line.
    - It uses floating-point arithmetic and rounding operations, which may introduce errors and affect the performance.
    - It can draw lines with any slope, but it may not produce the same set of pixels for the same line drawn in different directions.
  - Bresenham’s Line Drawing Algorithm
    - It is an optimized version of the DDA algorithm that uses only integer arithmetic and avoids rounding operations .
    - It uses the concept of decision variables to determine which pixel to choose next based on the error between the actual line and the approximated line .
    - It can draw lines with slopes between 0 and 1, and it can be extended to handle other slopes by using symmetry and swapping coordinates .
    - It produces the same set of pixels for the same line drawn in different directions .
  - Mid-Point Line Drawing Algorithm
    - It is a variation of the Bresenham’s algorithm that uses the mid-point of the two possible pixels to choose the next pixel.
    - It uses the same decision variables as the Bresenham’s algorithm, but it updates them differently based on the sign of the error.
    - It can draw lines with any slope, and it can be extended to handle other shapes such as circles and ellipses.
    - It produces the same set of pixels for the same line drawn in different directions.

- The following diagram illustrates the three line drawing algorithms for a line with slope less than 1:

![Line drawing algorithms diagram](https://www.tutorialandexample.com/wp-content/uploads/2019/10/Line-Drawing-Algorithm-in-Computer-Graphics-1.png)

: [Line Drawing Algorithm in Computer Graphics - TAE](https://www.tutorialandexample.com/line-drawing-algorithm)
: [Line drawing algorithm - Wikipedia](https://en.wikipedia.org/wiki/Line_drawing_algorithm)
: [What is the Line Drawing Algorithm in computer graphics?](https://www.goseeko.com/blog/what-is-the-line-drawing-algorithm-in-computer-graphics/)
: [Line Drawing Algorithm in Computer Graphics - TAE](https://www.tutorialandexample.com/line-drawing-algorithm)