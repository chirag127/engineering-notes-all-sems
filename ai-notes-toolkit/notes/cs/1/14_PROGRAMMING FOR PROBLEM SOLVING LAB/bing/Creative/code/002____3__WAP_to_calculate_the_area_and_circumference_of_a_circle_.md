## 3. WAP to calculate the area and circumference of a circle.

- A circle is a geometric shape that consists of all the points that are equidistant from a fixed center point.
- The distance from the center to any point on the circle is called the radius (r) of the circle.
- The area of a circle is the amount of space enclosed by the circle. It is given by the formula:

```math
A = \pi r^2
```

- where A is the area and \pi is a constant that is approximately equal to 3.14 or 22/7.
- The circumference of a circle is the length of the boundary of the circle. It is given by the formula:

```math
C = 2 \pi r
```

- where C is the circumference and \pi is the same constant as before.
- To write a program to calculate the area and circumference of a circle, we need to follow these steps:
  - Declare a variable to store the radius of the circle and assign it a value.
  - Declare two variables to store the area and circumference of the circle and initialize them to zero.
  - Use the formulas to calculate the area and circumference of the circle and assign them to the respective variables.
  - Print the values of the area and circumference of the circle with appropriate messages.
- Here is an example of a program in Python that calculates the area and circumference of a circle:

```python
# Declare a variable to store the radius of the circle and assign it a value
r = 5

# Declare two variables to store the area and circumference of the circle and initialize them to zero
A = 0
C = 0

# Use the formulas to calculate the area and circumference of the circle and assign them to the respective variables
A = 3.14 * r * r
C = 2 * 3.14 * r

# Print the values of the area and circumference of the circle with appropriate messages
print("The area of the circle is", A, "square units.")
print("The circumference of the circle is", C, "units.")
```

- The output of the program is:

```output
The area of the circle is 78.5 square units.
The circumference of the circle is 31.400000000000002 units.
```