### Classes

- A class is a blueprint or template for creating objects in Python. An object is an instance of a class that has attributes (data) and methods (functions) associated with it.
- A class definition starts with the keyword `class` followed by the name of the class and a colon. The class name should follow the naming convention of using capital letters for each word and no underscores (e.g. `MyClass`).
- The class body contains the attributes and methods of the class, indented under the class header. The first argument of every method is `self`, which refers to the current object.
- To create an object of a class, we use the class name followed by parentheses (e.g. `obj = MyClass()`). This calls the constructor method `__init__` of the class, which initializes the object with some initial values or parameters.
- To access or modify the attributes or methods of an object, we use the dot notation (e.g. `obj.attr` or `obj.method()`).

### Special Methods

- Special methods are methods that have a special meaning or functionality in Python. They are also called magic methods or dunder methods because they start and end with double underscores (e.g. `__init__`).
- Some of the common special methods are:

  - `__init__(self, ...)` : The constructor method that is called when an object is created. It takes `self` and any other parameters that are needed to initialize the object.
  - `__str__(self)` : The string representation method that is called when an object is printed or converted to a string. It returns a string that describes the object.
  - `__eq__(self, other)` : The equality comparison method that is called when two objects are compared using the `==` operator. It returns `True` if the objects are equal and `False` otherwise.
  - `__lt__(self, other)` : The less than comparison method that is called when two objects are compared using the `<` operator. It returns `True` if the first object is less than the second object and `False` otherwise.
  - `__add__(self, other)` : The addition method that is called when two objects are added using the `+` operator. It returns a new object that is the result of adding the two objects.
  - `__sub__(self, other)` : The subtraction method that is called when two objects are subtracted using the `-` operator. It returns a new object that is the result of subtracting the two objects.

### Class Example

- Here is an example of a class that represents a point in a two-dimensional plane:

```python
class Point:
  # constructor method
  def __init__(self, x, y):
    # attributes
    self.x = x
    self.y = y

  # string representation method
  def __str__(self):
    return f"({self.x}, {self.y})"

  # equality comparison method
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  # less than comparison method
  def __lt__(self, other):
    return self.x < other.x or (self.x == other.x and self.y < other.y)

  # addition method
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  # subtraction method
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)

  # a custom method to calculate the distance from the origin
  def distance(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5
```

- Here are some examples of using the class and its methods:

```python
# create two point objects
p1 = Point(3, 4)
p2 = Point(1, 2)

# print the objects
print(p1) # (3, 4)
print(p2) # (1, 2)

# compare the objects
print(p1 == p2) # False
print(p1 < p2) # False
print(p1 > p2) # True

# add and subtract the objects
print(p1 + p2) # (4, 6)
print(p1 - p2) # (2, 2)

# call the custom method
print(p1.distance()) # 5.0
```

### Inheritance

- Inheritance is a mechanism that allows a class to inherit the attributes and methods of another class. The class that inherits is called the subclass or child class, and the class that