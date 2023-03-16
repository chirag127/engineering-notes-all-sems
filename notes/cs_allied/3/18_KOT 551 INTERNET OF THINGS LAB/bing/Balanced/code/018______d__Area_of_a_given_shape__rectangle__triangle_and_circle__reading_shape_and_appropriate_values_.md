#### d) Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

The area of a shape is the amount of space that it covers. Different shapes have different formulas for calculating their areas. To find the area of a given shape, we need to read the shape name and the appropriate values from the standard input, and then apply the corresponding formula.

- Rectangle: A rectangle is a four-sided shape with opposite sides equal and right angles. The area of a rectangle is given by multiplying its length and width. If `l` is the length and `w` is the width, then the area of a rectangle is `A = l * w`.
- Triangle: A triangle is a three-sided shape with the sum of its interior angles equal to 180 degrees. The area of a triangle is given by multiplying its base and height and dividing by two. If `b` is the base and `h` is the height, then the area of a triangle is `A = (b * h) / 2`.
- Circle: A circle is a shape with all points at the same distance from the center. The area of a circle is given by multiplying the square of its radius and the constant pi. If `r` is the radius and `pi` is approximately 3.14, then the area of a circle is `A = pi * r * r`.

Here is an example of how to read the shape and the appropriate values from the standard input and calculate the area using Python code:

```python
# Read the shape name from the standard input
shape = input("Enter the shape: ")

# Check the shape name and read the appropriate values
if shape == "rectangle":
  # Read the length and width of the rectangle
  length = float(input("Enter the length: "))
  width = float(input("Enter the width: "))
  # Calculate the area of the rectangle
  area = length * width
elif shape == "triangle":
  # Read the base and height of the triangle
  base = float(input("Enter the base: "))
  height = float(input("Enter the height: "))
  # Calculate the area of the triangle
  area = (base * height) / 2
elif shape == "circle":
  # Read the radius of the circle
  radius = float(input("Enter the radius: "))
  # Calculate the area of the circle
  area = 3.14 * radius * radius
else:
  # Invalid shape name
  print("Invalid shape")
  # Exit the program
  exit()

# Print the area of the shape
print("The area of the", shape, "is", area)
```