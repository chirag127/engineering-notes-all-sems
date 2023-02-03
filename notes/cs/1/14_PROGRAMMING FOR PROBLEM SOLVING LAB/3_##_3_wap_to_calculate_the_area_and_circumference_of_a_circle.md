## 3. WAP to calculate the area and circumference of a circle.

Here's a Python code to calculate the area and circumference of a circle:
```
def circle_area_circumference(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    circumference = 2 * pi * radius
    return area, circumference

radius = float(input("Enter the radius of the circle: "))
area, circumference = circle_area_circumference(radius)
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")
```
Explanation: 
- Define a function `circle_area_circumference` which takes radius as input. 
- Calculate the area using the formula `pi * (radius ** 2)`. 
- Calculate the circumference using the formula `2 * pi * radius`. 
- Return both area and circumference. 
- Take the radius input from the user. 
- Call the function and store the returned values in `area` and `circumference` variables. 
- Print the area and circumference.
