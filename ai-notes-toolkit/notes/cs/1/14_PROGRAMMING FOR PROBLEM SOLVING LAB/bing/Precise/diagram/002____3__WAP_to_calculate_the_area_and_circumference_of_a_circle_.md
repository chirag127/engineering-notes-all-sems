## 3. WAP to calculate the area and circumference of a circle.

To calculate the area and circumference of a circle, you need to know the value of the radius of the circle. The radius is the distance from the center of the circle to its edge.

The formula to calculate the area of a circle is `Area = π * r^2`, where `r` is the radius of the circle and `π` is a mathematical constant approximately equal to 3.14.

The formula to calculate the circumference of a circle is `Circumference = 2 * π * r`, where `r` is the radius of the circle and `π` is a mathematical constant approximately equal to 3.14.

Here is an example of a program in Python that calculates the area and circumference of a circle with a given radius:

```python
import math

r = float(input("Enter the radius of the circle: "))

area = math.pi * r**2
circumference = 2 * math.pi * r

print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
```

In this program, the user is prompted to enter the radius of the circle. The program then calculates the area and circumference of the circle using the formulas mentioned above and displays the results. The `math.pi` constant is used to represent the value of `π`.