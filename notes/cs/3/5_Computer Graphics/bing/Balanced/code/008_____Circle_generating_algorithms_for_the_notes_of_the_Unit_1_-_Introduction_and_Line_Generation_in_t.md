### Circle generating algorithms for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm.
- A circle generation algorithm is an algorithm used to create a circle on a computer screen.
- It is used in various applications such as computer-aided design (CAD) software, animation software, games, and scientific visualization.
- The equation of a circle is X^2^ + Y^2^ = r^2^, where r is the radius.
- There are several algorithms used for generating circles on a computer screen, such as:
  - Bresenham's Algorithm   
    - It is a simple and efficient algorithm that uses only integer arithmetic.
    - It is based on the idea of determining the subsequent points required to draw the circle by using a decision parameter.
    - It exploits the symmetry of the circle to reduce the computation and memory requirements.
    - It starts from the topmost point of the circle and moves clockwise to generate the octant in the first quadrant.
    - It uses the following steps:
      - Initialize the decision parameter as p = 3 - 2r
      - Set the initial point as (0, r)
      - Repeat until x < y
        - Plot the point (x, y) and its symmetric points in the other octants
        - If p < 0, then set p = p + 4x + 6 and increment x by 1
        - Else, set p = p + 4(x - y) + 10 and increment x by 1 and decrement y by 1
      - If x = y, plot the final point (x, y) and its symmetric points in the other octants
  - Midpoint Circle Algorithm  
    - It is another efficient algorithm that uses only integer arithmetic.
    - It is based on the idea of determining the midpoint of the pixels that lie on the circle.
    - It also exploits the symmetry of the circle to reduce the computation and memory requirements.
    - It starts from the topmost point of the circle and moves clockwise to generate the octant in the first quadrant.
    - It uses the following steps:
      - Initialize the decision parameter as p = 1 - r
      - Set the initial point as (0, r)
      - Repeat until x < y
        - Plot the point (x, y) and its symmetric points in the other octants
        - If p < 0, then set p = p + 2x + 3 and increment x by 1
        - Else, set p = p + 2(x - y) + 5 and increment x by 1 and decrement y by 1
      - If x = y, plot the final point (x, y) and its symmetric points in the other octants
- The following diagram illustrates the Bresenham's and Midpoint Circle Algorithms:

```
    y ^
      |
      |       (x, y)
      |       /  |
      |      /   |
      |     /    |
      |    /     |
      |   /      |
      |  /       |
      | /        |
      |/         |
      +----------+--------> x
     (0, 0)     (x, 0)
```

- The advantages of these algorithms are:
  - They are simple and easy to implement
  - They are fast and efficient
  - They use only integer arithmetic and avoid costly floating-point operations
  - They exploit the symmetry of the circle to reduce the number of calculations and memory usage
- The disadvantages of these algorithms are:
  - They are not accurate and may produce jagged edges or aliasing effects
  - They are not scalable and may not work well for large circles or high-resolution screens
  - They are not general and may not handle other shapes such as ellipses or curves