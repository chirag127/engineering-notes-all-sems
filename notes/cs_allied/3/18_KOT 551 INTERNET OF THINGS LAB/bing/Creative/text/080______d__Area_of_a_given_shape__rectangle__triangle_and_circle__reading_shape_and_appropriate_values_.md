#### d) Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the amount of space inside the boundary of the shape. It is measured in square units, such as square centimeters, square meters, square inches, etc.
- To find the area of a given shape, we need to know the shape and the appropriate values from the standard input, such as the length, width, base, height, or radius of the shape.
- The formula for the area of a rectangle is `A = length * width`, where `length` and `width` are the dimensions of the rectangle. For example, if a rectangle has a length of 10 cm and a width of 5 cm, then its area is `A = 10 * 5 = 50 cm^2`.
- The formula for the area of a triangle is `A = (base * height) / 2`, where `base` and `height` are the dimensions of the triangle. For example, if a triangle has a base of 12 cm and a height of 9 cm, then its area is `A = (12 * 9) / 2 = 54 cm^2`.
- The formula for the area of a circle is `A = pi * radius^2`, where `pi` is a constant value approximately equal to 3.14 and `radius` is the distance from the center of the circle to any point on the circle. For example, if a circle has a radius of 7 cm, then its area is `A = pi * 7^2 = 153.86 cm^2`.
- To read the shape and the appropriate values from the standard input, we can use the `input()` function in Python, which returns a string of the user's input. For example, we can write:

```python
# Ask the user to enter the shape
shape = input("Enter the shape (rectangle, triangle, or circle): ")

# Check the shape and calculate the area accordingly
if shape == "rectangle":
  # Ask the user to enter the length and width of the rectangle
  length = float(input("Enter the length of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))
  # Calculate the area of the rectangle
  area = length * width
  # Print the area of the rectangle
  print(f"The area of the rectangle is {area} square units.")
elif shape == "triangle":
  # Ask the user to enter the base and height of the triangle
  base = float(input("Enter the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  # Calculate the area of the triangle
  area = (base * height) / 2
  # Print the area of the triangle
  print(f"The area of the triangle is {area} square units.")
elif shape == "circle":
  # Ask the user to enter the radius of the circle
  radius = float(input("Enter the radius of the circle: "))
  # Calculate the area of the circle
  area = 3.14 * radius**2
  # Print the area of the circle
  print(f"The area of the circle is {area} square units.")
else:
  # Print an error message if the shape is not valid
  print("Invalid shape. Please enter rectangle, triangle, or circle.")
```