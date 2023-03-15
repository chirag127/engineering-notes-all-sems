### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm.
- A circle generation algorithm is an algorithm used to create a circle on a computer screen by determining the subsequent points required to draw the circle .
- There are several algorithms used for generating circles on a computer screen, such as:
  - Bresenham's Algorithm
  - Midpoint Circle Algorithm
  - Polar Coordinates Method
  - Trigonometric Method
- These algorithms have different advantages and disadvantages in terms of accuracy, efficiency, and complexity.
- Bresenham's Algorithm is an efficient and simple algorithm that uses only integer arithmetic and avoids floating-point operations . It is based on the idea of incrementally updating the decision parameter that determines whether to choose the next pixel along the circle or the diagonal.
- Midpoint Circle Algorithm is a modification of Bresenham's Algorithm that reduces the number of calculations by using the symmetry of the circle and the midpoint of the arc as the decision parameter . It is also based on integer arithmetic and avoids floating-point operations.
- Polar Coordinates Method is an algorithm that uses the polar form of the equation of a circle, x = r cos θ and y = r sin θ, where r is the radius and θ is the angle, to generate the points along the circle. It requires floating-point operations and trigonometric functions, which makes it less efficient than the previous algorithms.
- Trigonometric Method is an algorithm that uses the parametric form of the equation of a circle, x = x0 + r cos t and y = y0 + r sin t, where (x0, y0) is the center and t is the parameter, to generate the points along the circle. It also requires floating-point operations and trigonometric functions, which makes it less efficient than the previous algorithms.