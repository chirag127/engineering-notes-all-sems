### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- Line drawing algorithms are methods for approximating a line segment on discrete graphical media, such as pixel-based displays and printers.
- Line drawing algorithms are important in computer graphics because they are the basis for drawing other geometric primitives, such as polygons, circles, and curves.
- Line drawing algorithms need to balance accuracy, efficiency, and simplicity. They also need to handle different cases of line slopes, orientations, and lengths.
- There are following algorithms used for drawing a line:
  - DDA (Digital Differential Analyzer) Line Drawing Algorithm
    - It is based on the idea of incrementing either x or y coordinate by a small amount and calculating the other coordinate using the equation of the line.
    - It uses floating-point arithmetic and rounding operations, which may introduce errors and reduce performance.
    - It can draw lines with any slope, but it may produce gaps or jagged edges.
  - Bresenham’s Line Drawing Algorithm
    - It is based on the idea of using an error term to decide whether to increment x or y coordinate by 1 and keeping the other coordinate constant.
    - It uses only integer arithmetic and addition operations, which improve accuracy and efficiency.
    - It can draw lines with slopes between 0 and 1, but it needs to be modified for other cases.
  - Mid-Point Line Drawing Algorithm
    - It is based on the idea of using the mid-point of the current pixel and the next pixel to decide whether to increment x or y coordinate by 1 and keeping the other coordinate constant.
    - It uses only integer arithmetic and addition and subtraction operations, which improve accuracy and efficiency.
    - It can draw lines with slopes between 0 and 1, but it needs to be modified for other cases.
- The following diagram illustrates the steps of the DDA, Bresenham’s, and Mid-Point algorithms for drawing a line with slope 0.5 :

![line drawing algorithms diagram](https://i.imgur.com/8W0Z4fP.png)