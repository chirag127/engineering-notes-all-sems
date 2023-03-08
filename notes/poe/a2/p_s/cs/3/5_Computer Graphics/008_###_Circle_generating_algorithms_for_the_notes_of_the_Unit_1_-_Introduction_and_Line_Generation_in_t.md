 Here is the content in markdown format for the given topic:

### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in Computer Graphics

1. Midpoint Circle Algorithm
- It is a simple and efficient algorithm to generate a circle.
- It uses the centre (h, k) and radius r of the circle as input.
- It calculates the decision parameter (p) and checks if p < 0 or p >= 0 at each step to determine the next octant to plot.
- For each octant, it calculates the next x and y co-ordinates using the increments in x and y and plots the points.
- This is repeated until the end point (initial point) is reached.
- Advantage: Simple and efficient. Requires only addition and comparison.
- Disadvantage: Plotting is not symmetrical and may result in gaps for large circles.

2. Bresenham's Circle Algorithm
- It is an improved version of the Midpoint Circle Algorithm.
- It uses addition, subtraction and bit shifts instead of multiplication, making it faster.
- It generates a circle with equal spacing between pixels, resulting in a smoother circle.
- The calculation of decision parameter is different and more efficient. It uses the distance between the centre and the circumference in each of the 4 quadrants to determine the points to be plotted.
- It is the most commonly used algorithm to generate circles on a digital display.
- Advantage: Fast, accurate and produces a smooth circle.
- Disadvantage: Calculations are more complex though faster than the Midpoint Circle Algorithm.

[Include detailed diagrams, examples and codes if required]

The content can be expanded with more details and points as per the requirements. Please let me know if you would like me to modify or add any other details to the answer.