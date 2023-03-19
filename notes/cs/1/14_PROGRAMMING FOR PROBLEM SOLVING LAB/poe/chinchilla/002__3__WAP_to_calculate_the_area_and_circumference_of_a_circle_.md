## 3. WAP to calculate the area and circumference of a circle.

To calculate the area and circumference of a circle, we need to use the following formulas:

- Area of a circle = πr² (where r is the radius of the circle)
- Circumference of a circle = 2πr (where r is the radius of the circle)

Here's a step-by-step guide on how to write a program in Python to calculate the area and circumference of a circle:

1. First, we need to define the value of π. We can either use a predefined constant value of π in the math module or we can define it ourselves. Here's how to define it ourselves:

```python
pi = 3.141592653589793238
```

2. Next, we need to ask the user to input the radius of the circle. We can use the input() function to do this:

```python
radius = float(input("Enter the radius of the circle: "))
```

Note that we use the float() function to convert the user input (which is a string) to a floating-point number.

3. Now, we can calculate the area and circumference of the circle using the formulas we defined earlier:

```python
area = pi * radius**2
circumference = 2 * pi * radius
```

4. Finally, we can print the results using the print() function:

```python
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
```

Here's the complete program:

```python
pi = 3.141592653589793238

radius = float(input("Enter the radius of the circle: "))

area = pi * radius**2
circumference = 2 * pi * radius

print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
```

Now, when we run this program and enter the value of the radius, it will calculate and print the area and circumference of the circle.