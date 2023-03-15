## 3. WAP to calculate the area and circumference of a circle

To calculate the area and circumference of a circle, you need to know the radius of the circle. The radius is the distance from the center of the circle to its edge.

The formula for calculating the area of a circle is `A = πr^2`, where `A` is the area, `π` is approximately equal to 3.14, and `r` is the radius of the circle.

The formula for calculating the circumference of a circle is `C = 2πr`, where `C` is the circumference, `π` is approximately equal to 3.14, and `r` is the radius of the circle.

Here is an example of a program that calculates the area and circumference of a circle with a radius of 5 units:

```python
radius = 5
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"The area of the circle is {area} square units.")
print(f"The circumference of the circle is {circumference} units.")
```

This program calculates the area and circumference of the circle using the formulas mentioned above and prints the results. The output of this program would be:

```
The area of the circle is 78.5 square units.
The circumference of the circle is 31.400000000000002 units.
```

You can modify the value of the `radius` variable to calculate the area and circumference of a circle with a different radius. You can also use the `math.pi` constant from the `math` module to get a more accurate value of `π`.