 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Mid-point circle generating algorithm for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics.

1. Given the coordinates of center (x0, y0) and radius r, the algorithm to generate points on the circle is:
- Calculate the mid-point (x, y) of the circle:
x = x0 + r
y = y0

- If (x, y) lies within the circle, print (x, y).
- Change the value of y by 1
- Check if (x, y) satisfies the circle equation (x-x0)^2 + (y-y0)^2 = r^2.
If yes, print (x, y) and repeat step 4.
If no, go to step 5.

5. Decrement the value of x by 1
Change the value of y to y0 + r - 1
Go to step 4

This repeats in incrementing/decrementing x and y values and generates points on the circle. The generated points can be used to draw circles on a raster display screen.

The explanation is written in points in a formal manner without any emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.