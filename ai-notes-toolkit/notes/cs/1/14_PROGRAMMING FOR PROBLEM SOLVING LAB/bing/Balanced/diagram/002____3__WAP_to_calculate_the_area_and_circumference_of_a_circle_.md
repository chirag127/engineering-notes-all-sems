## 3. WAP to calculate the area and circumference of a circle.

- A circle is a geometric shape that consists of all the points that are equidistant from a fixed point called the center.
- The distance from the center to any point on the circle is called the radius. The diameter of the circle is twice the radius.
- The area of a circle is the amount of space enclosed by the circle. The formula for the area of a circle is A = πr^2, where r is the radius and π is a constant that is approximately equal to 3.14.
- The circumference of a circle is the length of the boundary of the circle. The formula for the circumference of a circle is C = 2πr, where r is the radius and π is a constant that is approximately equal to 3.14.
- To write a program to calculate the area and circumference of a circle, we need to follow these steps:
  - Declare a variable to store the radius of the circle and assign a value to it.
  - Declare two variables to store the area and circumference of the circle and initialize them to zero.
  - Use the formulas A = πr^2 and C = 2πr to calculate the area and circumference of the circle and assign the results to the corresponding variables.
  - Display the values of the area and circumference of the circle on the screen.

- Here is an example of a program to calculate the area and circumference of a circle in Python:

```python
# Declare a variable to store the radius of the circle and assign a value to it
radius = 5

# Declare two variables to store the area and circumference of the circle and initialize them to zero
area = 0
circumference = 0

# Use the formulas A = πr^2 and C = 2πr to calculate the area and circumference of the circle and assign the results to the corresponding variables
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius

# Display the values of the area and circumference of the circle on the screen
print("The area of the circle is", area)
print("The circumference of the circle is", circumference)
```

- The output of the program is:

```
The area of the circle is 78.5
The circumference of the circle is 31.400000000000002
```