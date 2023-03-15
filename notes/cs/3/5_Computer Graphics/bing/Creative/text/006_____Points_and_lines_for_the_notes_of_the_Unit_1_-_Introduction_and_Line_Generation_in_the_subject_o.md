### Points and lines for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A point is the simplest graphical element that can be displayed on a screen. It is represented by a single pixel or a dot.
- A line is a sequence of points that connects two endpoints. It is one of the most basic and common shapes in computer graphics.
- There are different methods to generate lines on a raster display, such as DDA algorithm, Bresenham's algorithm, midpoint algorithm, etc.
- These algorithms are based on the concept of incremental calculation, which means that the next point on the line is computed from the previous point using some arithmetic operations.
- The main criteria to evaluate the performance of these algorithms are accuracy, speed, and simplicity.
- Accuracy refers to how closely the generated line approximates the ideal line, which is defined by the slope and the endpoints.
- Speed refers to how fast the algorithm can generate the line, which depends on the number of calculations and memory accesses required for each point.
- Simplicity refers to how easy the algorithm is to implement and understand, which affects the code size and complexity.
- Some of the advantages and disadvantages of these algorithms are:

  - DDA algorithm: It is simple and accurate, but slow and requires floating-point operations.
  - Bresenham's algorithm: It is fast and efficient, but less accurate and works only for lines with slope less than 1 in magnitude.
  - Midpoint algorithm: It is accurate and works for any slope, but more complex and requires more calculations than Bresenham's algorithm.