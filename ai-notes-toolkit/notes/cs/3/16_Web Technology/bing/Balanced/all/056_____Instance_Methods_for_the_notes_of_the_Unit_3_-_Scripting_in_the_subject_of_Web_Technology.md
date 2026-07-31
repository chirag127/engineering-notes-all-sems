# Instance Methods

- Instance methods are functions that are defined inside a class and can be called on the objects of that class.
- Instance methods have access to the instance attributes and the class attributes of the object on which they are called.
- Instance methods can modify the state of the object by changing the values of its attributes or calling other instance methods.
- Instance methods can also return values or other objects as the result of their computation.
- Instance methods are defined by using the `def` keyword followed by the method name and a list of parameters. The first parameter is usually named `self` and represents the object on which the method is called.
- Instance methods are called by using the dot notation, i.e. `object.method(arguments)`, where `object` is an instance of the class, `method` is the name of the instance method, and `arguments` are the values passed to the parameters of the method.
- Example:

```python
# Define a class named Point
class Point:
    # Define a class attribute named origin
    origin = (0, 0)

    # Define an instance method named __init__ that initializes the instance attributes x and y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define an instance method named distance that calculates the distance between the point and another point
    def distance(self, other):
        # Use the Pythagorean theorem to calculate the distance
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5

    # Define an instance method named move that changes the position of the point by adding some values to x and y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Create two objects of the class Point
p1 = Point(3, 4)
p2 = Point(6, 8)

# Call the instance method distance on p1 and pass p2 as an argument
d = p1.distance(p2)
print(d) # 5.0

# Call the instance method move on p2 and pass 2 and -1 as arguments
p2.move(2, -1)
print(p2.x, p2.y) # 8 7
```