### Line drawing algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

Line drawing algorithms are used to determine which pixels on a raster grid should be turned on to best approximate a straight line between two given points. There are several line drawing algorithms, including:

1. **Digital Differential Analyzer (DDA) Algorithm**: This algorithm uses a digital differential analyzer to calculate the coordinates of the points along the line. It is an incremental method that calculates the next point based on the previous point.

2. **Bresenham's Line Algorithm**: This algorithm is an efficient and accurate raster line-generating algorithm. It uses integer arithmetic to calculate the coordinates of the points along the line, making it faster than the DDA algorithm.

3. **Midpoint Line Algorithm**: This algorithm is similar to Bresenham's algorithm, but it uses a different decision variable to determine which pixel to turn on. It is also an incremental method that calculates the next point based on the previous point.

These algorithms are commonly used in computer graphics to draw lines on a raster grid. They are important for creating accurate and visually appealing graphics.