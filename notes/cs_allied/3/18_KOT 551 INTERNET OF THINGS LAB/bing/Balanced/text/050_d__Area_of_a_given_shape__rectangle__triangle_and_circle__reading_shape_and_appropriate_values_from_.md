# Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the measure of how much space it occupies in a plane.
- Different shapes have different formulas for calculating their areas, depending on their properties and dimensions.
- To find the area of a given shape, we need to identify the shape and read the appropriate values from the standard input, such as length, width, base, height, or radius.
- Here are some common formulas for the area of a rectangle, triangle and circle:

  - Rectangle: A = lw, where l is the length and w is the width.
  - Triangle: A = (1/2)bh, where b is the base and h is the height.
  - Circle: A = pi*r^2, where r is the radius and pi is approximately 3.14.

- For example, if we want to find the area of a rectangle with length 10 cm and width 5 cm, we can use the formula A = lw and plug in the values:

  - A = 10 * 5
  - A = 50 cm^2

- Similarly, if we want to find the area of a triangle with base 8 cm and height 6 cm, we can use the formula A = (1/2)bh and plug in the values:

  - A = (1/2) * 8 * 6
  - A = 24 cm^2

- And if we want to find the area of a circle with radius 4 cm, we can use the formula A = pi*r^2 and plug in the values:

  - A = 3.14 * 4^2
  - A = 50.24 cm^2

- To read the shape and the appropriate values from the standard input, we can use the input() function in Python, which returns a string that the user types in the console. For example:

  - shape = input("Enter the shape: ")
  - if shape == "rectangle":
    - l = float(input("Enter the length: "))
    - w = float(input("Enter the width: "))
    - A = l * w
    - print("The area of the rectangle is", A, "cm^2")
  - elif shape == "triangle":
    - b = float(input("Enter the base: "))
    - h = float(input("Enter the height: "))
    - A = (1/2) * b * h
    - print("The area of the triangle is", A, "cm^2")
  - elif shape == "circle":
    - r = float(input("Enter the radius: "))
    - A = 3.14 * r^2
    - print("The area of the circle is", A, "cm^2")
  - else:
    - print("Invalid shape")

- This code will ask the user to enter the shape and the appropriate values, and then calculate and print the area of the shape. For example, if the user enters "circle" and "4", the output will be:

  - Enter the shape: circle
  - Enter the radius: 4
  - The area of the circle is 50.24 cm^2