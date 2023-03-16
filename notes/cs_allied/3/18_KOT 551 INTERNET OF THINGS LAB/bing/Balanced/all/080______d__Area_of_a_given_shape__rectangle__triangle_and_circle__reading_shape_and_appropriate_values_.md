#### d) Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the amount of space that it covers in a two-dimensional plane.
- To calculate the area of a given shape, we need to know the shape and the appropriate values from the standard input, such as the length, width, base, height, or radius of the shape.
- The formula for the area of a rectangle is `A = length * width`, where `length` is the longer side and `width` is the shorter side of the rectangle.
- The formula for the area of a triangle is `A = (base * height) / 2`, where `base` is the length of the bottom side and `height` is the perpendicular distance from the base to the opposite vertex of the triangle.
- The formula for the area of a circle is `A = pi * radius^2`, where `pi` is a constant value approximately equal to 3.14 and `radius` is the distance from the center to any point on the circle.
- To read the shape and the appropriate values from the standard input, we can use the `input()` function in Python, which returns a string that the user enters.
- We can convert the string to a numeric value using the `float()` function, which returns a floating-point number that can represent decimals.
- We can use conditional statements such as `if`, `elif`, and `else` to check the shape and apply the corresponding formula for the area.
- We can use the `print()` function to display the result of the calculation to the standard output.

- Here is an example of a Python program that calculates the area of a given shape (rectangle, triangle, or circle) reading shape and appropriate values from standard input:

```python
# Ask the user to enter the shape
shape = input("Enter the shape (rectangle, triangle, or circle): ")

# Check the shape and calculate the area
if shape == "rectangle":
  # Ask the user to enter the length and width of the rectangle
  length = float(input("Enter the length of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))
  # Calculate the area using the formula A = length * width
  area = length * width
  # Print the result
  print("The area of the rectangle is", area)
elif shape == "triangle":
  # Ask the user to enter the base and height of the triangle
  base = float(input("Enter the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  # Calculate the area using the formula A = (base * height) / 2
  area = (base * height) / 2
  # Print the result
  print("The area of the triangle is", area)
elif shape == "circle":
  # Ask the user to enter the radius of the circle
  radius = float(input("Enter the radius of the circle: "))
  # Calculate the area using the formula A = pi * radius^2
  area = 3.14 * radius**2
  # Print the result
  print("The area of the circle is", area)
else:
  # Print an error message if the shape is not valid
  print("Invalid shape")
```