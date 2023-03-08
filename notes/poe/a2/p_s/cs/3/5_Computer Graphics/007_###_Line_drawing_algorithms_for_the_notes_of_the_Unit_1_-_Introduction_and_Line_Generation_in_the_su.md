 Here is the content in markdown format for the topic ### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics:

#### Line Generation Algorithms
The following are the popular line drawing algorithms used in computer graphics:

1. Bresenham's Algorithm:
- It is an efficient line drawing algorithm that draws lines on a raster display.
- It uses only integer arithmetic to calculate the next pixel to plot.
- The algorithm stops when it reaches the end point of the line.
- It gives a fast and close approximation to the true line.
- Examples: Drawing lines at 45° and drawing circles.
- Applications: Used in line art creation and primitive shape drawing.

Advantages:
- Uses only integer arithmetic leading to efficient implementation.
- Continuous approach leading to smooth lines.
- Variants available for circles and other shapes.

Disadvantages:
- Does not give true lines. Gives close approximations.

2. Digital Differential Analyzer (DDA):
- It is a more direct method of line generation.
- It uses real arithmetic to compute the next step along the line after each pixel is plotted.
- It generates lines with sub-pixel accuracy leading to more accurate lines than Bresenham's algorithm.
- Examples: Drawing lines at any angles.
- Applications: Used when high precision is needed like in technical drawings, CAD, etc.

Advantages:
- Generates lines with sub-pixel accuracy leading to more accurate lines.

Disadvantages:
- Requires floating point arithmetic leading to slightly slower implementation than Bresenham's algorithm.

[Include detailed examples, codes, diagrams, etc if required]

The content summarizes the key points about the Line Generation Algorithms - Bresenham's Algorithm and Digital Differential Analyzer (DDA) in a formal way with points for easy understanding as if for exam preparation notes. Let me know if you would like me to elaborate on any part or add more details.