### Mid-point circle generating algorithm for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- The Mid-point circle generating algorithm is an efficient way to draw a circle on a raster grid.
- It is an incremental algorithm, meaning it builds the circle point by point, starting from the topmost point and moving clockwise.
- The algorithm uses the symmetry of the circle to reduce the number of calculations needed.
- The basic idea is to start at the top of the circle, and for each point, calculate the next point using the mid-point between the current point and the next point on the circle.
- The decision parameter is used to determine whether the next point should be above or below the mid-point.
- If the decision parameter is less than or equal to zero, the next point is above the mid-point, otherwise it is below.
- The decision parameter is updated at each step using the difference between the squared distance from the next point to the center of the circle and the squared radius of the circle.
- The algorithm can be optimized by pre-calculating the values of the decision parameter for the first octant of the circle and using symmetry to find the points in the other octants.
- The Mid-point circle generating algorithm is widely used in computer graphics for drawing circles and arcs.