### Mid-point circle generating algorithm for the notes of the Unit 1 - Introduction and Line Generation in the subject of Computer Graphics

- The mid-point circle generating algorithm is a technique to draw a circle on a raster display using only integer arithmetic and pixel plotting.
- The algorithm is based on the observation that a circle with radius r and center (xc, yc) can be defined by the equation x^2 + y^2 = r^2, where x and y are relative to the center.
- The algorithm starts by plotting the point (0, r) on the circle, which corresponds to the topmost pixel. Then, it moves to the next pixel along the circle by incrementing x by 1 and decrementing y by 1, if the mid-point between the two pixels is inside the circle, or by only incrementing x, if the mid-point is outside the circle.
- The mid-point can be determined by evaluating the circle equation at the point (x + 1, y - 0.5). If the result is negative, the mid-point is inside the circle, and if the result is positive, the mid-point is outside the circle. If the result is zero, the mid-point is on the circle.
- The algorithm repeats this process until x is equal to y, which corresponds to the point (r/sqrt(2), r/sqrt(2)) on the circle, or the first octant is completed. Then, the algorithm can use the symmetry of the circle to plot the remaining seven octants by reflecting the points along the x-axis, y-axis, and the line y = x.
- The algorithm can be summarized by the following pseudocode:

```
// Input: radius r and center (xc, yc)
// Output: a circle with radius r and center (xc, yc) on the raster display
x = 0
y = r
p = 1 - r // initial value of the decision parameter
plot(xc + x, yc + y) // plot the first point
while x < y
  x = x + 1 // increment x
  if p < 0 // mid-point is inside the circle
    p = p + 2 * x + 1 // update the decision parameter
  else // mid-point is outside or on the circle
    y = y - 1 // decrement y
    p = p + 2 * (x - y) + 1 // update the decision parameter
  plot(xc + x, yc + y) // plot the point in the first octant
  plot(xc - x, yc + y) // plot the point in the second octant
  plot(xc + x, yc - y) // plot the point in the third octant
  plot(xc - x, yc - y) // plot the point in the fourth octant
  plot(xc + y, yc + x) // plot the point in the fifth octant
  plot(xc - y, yc + x) // plot the point in the sixth octant
  plot(xc + y, yc - x) // plot the point in the seventh octant
  plot(xc - y, yc - x) // plot the point in the eighth octant
end while
```

- The algorithm has the following advantages and disadvantages:
  - Advantages:
    - It uses only integer arithmetic and pixel plotting, which are fast and simple operations on a raster display.
    - It avoids redundant calculations by using the previous value of the decision parameter to update the next value.
    - It exploits the symmetry of the circle to reduce the number of calculations and pixel plotting by a factor of eight.
  - Disadvantages:
    - It can only draw circles with integer radii, which may result in aliasing or jagged edges on the circle.
    - It can only draw circles with the center at an integer coordinate, which may limit the flexibility of positioning the circle on the display.
    - It can only draw circles in one color, which may not be suitable for some applications that require shading or filling the circle.