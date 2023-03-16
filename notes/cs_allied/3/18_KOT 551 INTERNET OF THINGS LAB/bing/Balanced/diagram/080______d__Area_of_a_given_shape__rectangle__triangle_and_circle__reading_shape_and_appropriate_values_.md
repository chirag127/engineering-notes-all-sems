#### d) Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the amount of space inside the shape. It is measured in square units, such as square centimeters, square meters, square inches, etc.
- To find the area of a given shape, we need to know the shape and the appropriate values from the standard input, such as the length, width, base, height, or radius of the shape.
- The formula for the area of a rectangle is `A = length * width`, where `length` is the longer side and `width` is the shorter side of the rectangle.
- The formula for the area of a triangle is `A = (base * height) / 2`, where `base` is the length of the bottom side and `height` is the perpendicular distance from the base to the opposite vertex of the triangle.
- The formula for the area of a circle is `A = pi * radius^2`, where `pi` is a constant value approximately equal to 3.14 and `radius` is the distance from the center to any point on the circle.
- To read the shape and the appropriate values from the standard input, we can use the `input()` function in Python, which returns a string that the user types in the console. We can then convert the string to a numerical value using the `float()` function, which returns a floating-point number.
- For example, if we want to find the area of a rectangle, we can write the following code in Python:

```python
# Read the shape from the standard input
shape = input("Enter the shape: ")

# Check if the shape is a rectangle
if shape == "rectangle":
  # Read the length and width from the standard input
  length = float(input("Enter the length: "))
  width = float(input("Enter the width: "))

  # Calculate the area using the formula
  area = length * width

  # Print the area to the standard output
  print("The area of the rectangle is", area)
```

- Similarly, we can write the code for the other shapes using the corresponding formulas and values.