# Circle Generating Algorithms

A circle is one of the fundamental shapes used in computer graphics and it is generated through a circle generation algorithm. A circle generation algorithm is an algorithm used to create a circle on a computer screen. It is used in various applications such as computer-aided design (CAD) software, animation software, games, and scientific visualization.

There are several algorithms used for generating circles on a computer screen, but the most popular ones are:

- **Bresenham's Algorithm**: This algorithm is based on the idea of drawing a circle using eight-way symmetry and using only integer arithmetic. It is efficient and simple to implement. It works by determining the next pixel to be plotted based on the previous pixel and the decision parameter, which is the difference between the actual distance of the pixel from the center and the ideal distance (radius). 

- **Midpoint Circle Algorithm**: This algorithm is similar to Bresenham's algorithm, but it uses the midpoint of the two possible pixels as the decision parameter. It is also based on eight-way symmetry and integer arithmetic. It works by computing the initial value of the decision parameter and then updating it for each pixel based on whether the midpoint is inside or outside the circle. It is more accurate than Bresenham's algorithm, but slightly more complex. 

The following are the steps for both algorithms:

- Step 1: Input the center coordinates (h, k) and the radius r of the circle.
- Step 2: Initialize the starting point (x, y) as (0, r).
- Step 3: Initialize the decision parameter d as 3 - 2r for Bresenham's algorithm and 1 - r for Midpoint Circle Algorithm.
- Step 4: Plot the initial point (h + x, k + y) and its symmetric points using eight-way symmetry.
- Step 5: Repeat the following steps until x >= y:
  - Step 5.1: If d < 0, then the next point is (x + 1, y) and the new value of d is d + 4x + 6 for Bresenham's algorithm and d + 2x + 3 for Midpoint Circle Algorithm.
  - Step 5.2: If d >= 0, then the next point is (x + 1, y - 1) and the new value of d is d + 4(x - y) + 10 for Bresenham's algorithm and d + 2(x - y) + 5 for Midpoint Circle Algorithm.
  - Step 5.3: Plot the new point and its symmetric points using eight-way symmetry.
  - Step 5.4: Increment x by 1 and decrement y by 1 if d >= 0.

The following are the pseudocodes for both algorithms:

```
// Bresenham's Algorithm
Input: center (h, k), radius r
Output: circle pixels

x = 0
y = r
d = 3 - 2r

Plot (h + x, k + y) and its symmetric points

While x < y
  If d < 0
    x = x + 1
    d = d + 4x + 6
  Else
    x = x + 1
    y = y - 1
    d = d + 4(x - y) + 10
  End If
  Plot (h + x, k + y) and its symmetric points
End While
```

```
// Midpoint Circle Algorithm
Input: center (h, k), radius r
Output: circle pixels

x = 0
y = r
d = 1 - r

Plot (h + x, k + y) and its symmetric points

While x < y
  If d < 0
    x = x + 1
    d = d + 2x + 3
  Else
    x = x + 1
    y = y - 1
    d = d + 2(x - y) + 5
  End If
  Plot (h + x, k + y) and its symmetric points
End While
```

The following are the diagrams for both algorithms:

![Bresenham's Algorithm](https://www.geeksforgeeks.org/wp-content/uploads/bresenhamCircle.png)



![Midpoint Circle Algorithm](https://www.ge