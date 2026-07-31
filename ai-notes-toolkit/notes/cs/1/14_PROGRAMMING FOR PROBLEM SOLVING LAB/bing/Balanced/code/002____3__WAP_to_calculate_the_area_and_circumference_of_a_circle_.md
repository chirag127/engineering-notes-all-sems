## 3. WAP to calculate the area and circumference of a circle.

- A circle is a geometric shape that consists of all the points that are equidistant from a fixed center point.
- The distance from the center to any point on the circle is called the radius (r) of the circle.
- The area of a circle is the amount of space enclosed by the circle. It is given by the formula:

```math
A = \pi r^2
```

where A is the area and \pi is a constant that is approximately equal to 3.14.

- The circumference of a circle is the length of the boundary of the circle. It is given by the formula:

```math
C = 2 \pi r
```

where C is the circumference and \pi is the same constant as before.

- To write a program to calculate the area and circumference of a circle, we need to follow these steps:

  - Declare a variable to store the radius of the circle and assign a value to it.
  - Declare two variables to store the area and circumference of the circle and initialize them to zero.
  - Use the formulas above to calculate the area and circumference of the circle and assign the results to the corresponding variables.
  - Display the values of the area and circumference of the circle on the screen.

- Here is an example of a program in Python that implements these steps:

```python
# Declare a variable to store the radius of the circle and assign a value to it
r = 5

# Declare two variables to store the area and circumference of the circle and initialize them to zero
A = 0
C = 0

# Use the formulas to calculate the area and circumference of the circle and assign the results to the corresponding variables
A = 3.14 * r * r
C = 2 * 3.14 * r

# Display the values of the area and circumference of the circle on the screen
print("The area of the circle is", A, "square units.")
print("The circumference of the circle is", C, "units.")
```

- The output of the program is:

```text
The area of the circle is 78.5 square units.
The circumference of the circle is 31.400000000000002 units.
```