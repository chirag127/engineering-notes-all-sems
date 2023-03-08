 Here is the content in markdown format for the topic ### Mid-point circle generating algorithm for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics:

## Mid-point Circle Generating Algorithm

- The Mid-point Circle Generating Algorithm is an algorithm used to plot points on a circle.
- It makes use of the fact that the radius of a circle is constant to determine the next point to plot.
- The algorithm requires the coordinates of the center of the circle (xc, yc) and the radius (r) as inputs.
- The steps involved in the algorithm are:

1. Start with initial decision parameter (d) as 1 - r
2. Plot the first point (xc + r, yc)
3. Calculate the next decision parameter:
- If d <= 0
   - Set d = d + 2*r + 1
- Else
   - Plot (xc + d, yc + 1)
   - Plot (xc + d, yc - 1)
   - Set d = d + 2*(r - 1)
4. Repeat Step 3 until d > r

- The advantages of this algorithm are:
- It is simple and efficient.
- It produces a smooth circle without any jagged edges.
- It can be easily modified to plot ellipses by varying the radius.
- The coordinates of the center and radius can be varied to produce the circle at the desired position and size.

- Examples and applications: Generating pixel circles on screens, generating boundaries of circular objects in computer graphics, etc.

[Include diagrams, codes, tables, etc. if required to explain the topic better]