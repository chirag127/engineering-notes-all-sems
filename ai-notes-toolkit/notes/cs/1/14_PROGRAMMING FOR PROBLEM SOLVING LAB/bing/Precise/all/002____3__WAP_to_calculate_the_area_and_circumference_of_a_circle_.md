## 3. WAP to calculate the area and circumference of a circle.

The area of a circle is calculated using the formula `A = πr^2`, where `A` is the area, `π` is approximately equal to 3.14, and `r` is the radius of the circle.

The circumference of a circle is calculated using the formula `C = 2πr`, where `C` is the circumference, `π` is approximately equal to 3.14, and `r` is the radius of the circle.

Here is an example of a program that calculates the area and circumference of a circle with a given radius:

```python
import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
```

This program prompts the user to enter the radius of the circle, then calculates the area and circumference using the formulas above and displays the results.