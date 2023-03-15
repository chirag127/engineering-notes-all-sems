### Mid-point circle generating algorithm for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

The Mid-point circle generating algorithm is an efficient way to draw a circle on a raster grid. It is an incremental algorithm that uses the mid-point between the pixels to determine the next pixel to be drawn. Here are the key points to remember about this algorithm:

1. The algorithm starts at the top of the circle and moves in a clockwise direction, drawing pixels at each octant of the circle.
2. The decision parameter is used to determine whether the next pixel should be above or below the mid-point.
3. If the decision parameter is less than or equal to zero, the next pixel is drawn above the mid-point. Otherwise, it is drawn below the mid-point.
4. The decision parameter is updated at each step using the formula `p = p + 2*dx + 1` if the next pixel is above the mid-point, and `p = p + 2*dx - 2*dy + 1` if it is below the mid-point.
5. The algorithm uses 8-way symmetry to reduce the number of calculations required to draw the circle.
6. The Mid-point circle generating algorithm is more efficient than other circle drawing algorithms because it only requires integer calculations.
