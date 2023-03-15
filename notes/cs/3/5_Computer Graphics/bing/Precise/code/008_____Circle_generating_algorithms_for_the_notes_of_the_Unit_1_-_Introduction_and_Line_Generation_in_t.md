### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

1. **Midpoint Circle Algorithm**: This algorithm is an efficient way to draw a circle on a raster grid. It uses the midpoint of the pixels to determine whether to color the pixel inside or outside the circle. The algorithm starts at the top of the circle and moves in a clockwise direction, coloring pixels as it goes.

2. **Bresenham's Circle Algorithm**: This is another efficient algorithm for drawing circles on a raster grid. It is similar to the midpoint circle algorithm, but it uses a decision variable to determine which pixels to color. The algorithm starts at the top of the circle and moves in a clockwise direction, coloring pixels as it goes.

3. **Trigonometric Method**: This method uses trigonometric functions to calculate the coordinates of points on the circle. The points are then plotted on the grid. This method is not as efficient as the previous two algorithms, but it can produce more accurate results.

4. **Polar Coordinates Method**: This method also uses trigonometric functions to calculate the coordinates of points on the circle. However, instead of using Cartesian coordinates, it uses polar coordinates. The points are then converted to Cartesian coordinates and plotted on the grid. This method is also not as efficient as the midpoint circle and Bresenham's circle algorithms, but it can produce more accurate results.

These are some of the common circle generating algorithms used in computer graphics. Each algorithm has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the application.