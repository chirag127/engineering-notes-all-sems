## 3. WAP to calculate the area and circumference of a circle.

- A circle is a geometric shape that consists of all the points that are equidistant from a fixed center point.
- The distance from the center to any point on the circle is called the radius (r) of the circle.
- The longest distance across the circle, passing through the center, is called the diameter (d) of the circle. The diameter is twice the radius, i.e., d = 2r.
- The area of a circle is the amount of space enclosed by the circle. The formula for the area of a circle is A = πr^2, where π is a constant that is approximately equal to 3.14 or 22/7.
- The circumference of a circle is the length of the boundary of the circle. The formula for the circumference of a circle is C = 2πr or C = πd, where π is the same constant as above.
- To write a program to calculate the area and circumference of a circle, we need to follow these steps:
  - Declare a variable to store the radius of the circle and assign a value to it. For example, r = 5.
  - Declare a variable to store the value of π and assign a value to it. For example, pi = 3.14.
  - Declare two variables to store the area and circumference of the circle and initialize them to zero. For example, area = 0 and circum = 0.
  - Use the formulas A = πr^2 and C = 2πr to calculate the area and circumference of the circle and assign the results to the respective variables. For example, area = pi * r * r and circum = 2 * pi * r.
  - Print the values of the area and circumference of the circle. For example, print("Area of the circle is", area) and print("Circumference of the circle is", circum).
- Here is an example of a program in Python that calculates the area and circumference of a circle:

```python
# Declare a variable to store the radius of the circle and assign a value to it
r = 5

# Declare a variable to store the value of pi and assign a value to it
pi = 3.14

# Declare two variables to store the area and circumference of the circle and initialize them to zero
area = 0
circum = 0

# Use the formulas A = pi * r * r and C = 2 * pi * r to calculate the area and circumference of the circle and assign the results to the respective variables
area = pi * r * r
circum = 2 * pi * r

# Print the values of the area and circumference of the circle
print("Area of the circle is", area)
print("Circumference of the circle is", circum)
```

- Here is the output of the program:

```
Area of the circle is 78.5
Circumference of the circle is 31.400000000000002
```

- Here is an example of a program in C that calculates the area and circumference of a circle:

```c
#include <stdio.h>
#define PI 3.14 // Define a macro to store the value of pi

int main()
{
    // Declare a variable to store the radius of the circle and assign a value to it
    float r = 5;

    // Declare two variables to store the area and circumference of the circle and initialize them to zero
    float area = 0;
    float circum = 0;

    // Use the formulas A = PI * r * r and C = 2 * PI * r to calculate the area and circumference of the circle and assign the results to the respective variables
    area = PI * r * r;
    circum = 2 * PI * r;

    // Print the values of the area and circumference of the circle
    printf("Area of the circle is %f\n", area);
    printf("Circumference of the circle is %f\n", circum);

    return 0;
}
```

- Here is the output of the program:

```
Area of the circle is 78.500000
Circumference of the circle is 31.400000
```

- Here is an example of a program in Java that calculates the area and circumference of a circle:

```java
public class Circle {

    public static void main(String[] args) {
        // Declare a constant to store the value of pi
        final double PI = 3.14;

        // Declare a variable to store the radius of the circle and assign a value to it