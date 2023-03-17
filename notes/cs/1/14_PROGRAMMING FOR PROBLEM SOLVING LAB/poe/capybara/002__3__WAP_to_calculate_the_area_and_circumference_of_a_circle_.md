## WAP to Calculate the Area and Circumference of a Circle

Here are the steps to write a program in Python to calculate the area and circumference of a circle:

1. First, we need to import the math module in Python by using the following code:

```
import math
```

2. Next, we will take the input of the radius of the circle from the user using the input() function. We will store the value in a variable named ‘r’.

```
r = float(input("Enter the radius of the circle: "))
```

3. Now, we can calculate the area of the circle using the formula:

```
area = math.pi * r * r
```

Here, we are using the value of pi from the math module to calculate the area.

4. Similarly, we can calculate the circumference of the circle using the formula:

```
circumference = 2 * math.pi * r
```

5. Finally, we can print the values of the area and circumference using the print() function.

```
print("The area of the circle is: ", area)
print("The circumference of the circle is: ", circumference)
```

Here is the complete Python program to calculate the area and circumference of a circle:

```
import math

r = float(input("Enter the radius of the circle: "))

area = math.pi * r * r
circumference = 2 * math.pi * r

print("The area of the circle is: ", area)
print("The circumference of the circle is: ", circumference)
```

By following these steps, you can easily write a program in Python to calculate the area and circumference of a circle.