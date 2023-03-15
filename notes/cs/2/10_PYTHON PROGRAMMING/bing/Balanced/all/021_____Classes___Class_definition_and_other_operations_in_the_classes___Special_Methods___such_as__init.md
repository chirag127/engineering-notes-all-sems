# Classes

## Class definition and other operations in the classes

- A class is a blueprint or template for creating objects of a certain type.
- A class defines the attributes and methods that the objects of that class will have.
- Attributes are variables that store data for each object of the class.
- Methods are functions that perform actions or operations on the objects of the class.
- To define a class, use the keyword `class` followed by the name of the class and a colon.
- The name of the class should follow the naming convention of using uppercase letters for the first letter of each word and lowercase letters for the rest.
- The body of the class should be indented and contain the attributes and methods of the class.
- To create an object of a class, use the class name followed by parentheses and assign it to a variable.
- To access the attributes and methods of an object, use the dot operator (`.`) followed by the attribute or method name.
- To modify the attributes of an object, use the assignment operator (`=`) to assign a new value to the attribute.
- To delete an object, use the `del` keyword followed by the object name.

## Special Methods

- Special methods are methods that have a special meaning or functionality in Python.
- They are also called magic methods or dunder methods because they are surrounded by double underscores (`__`).
- Some of the common special methods are:

  - `__init__`: This is the constructor method that is automatically called when an object is created. It is used to initialize the attributes of the object with the values passed as arguments.
  - `__str__`: This is the string representation method that is automatically called when an object is printed or converted to a string. It should return a string that describes the object.
  - `__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__`: These are the comparison methods that are automatically called when an object is compared with another object using the operators `==`, `!=`, `<`, `>`, `<=`, `>=`. They should return a boolean value that indicates the result of the comparison.
  - `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`: These are the arithmetic methods that are automatically called when an object is involved in an arithmetic operation using the operators `+`, `-`, `*`, `/`, `//`, `%`, `**`. They should return a new object that is the result of the operation.

## Class Example

- Here is an example of a class that represents a rectangle:

```python
class Rectangle:
  # constructor method
  def __init__(self, length, width):
    # initialize the attributes
    self.length = length
    self.width = width

  # method to calculate the area
  def area(self):
    return self.length * self.width

  # method to calculate the perimeter
  def perimeter(self):
    return 2 * (self.length + self.width)

  # string representation method
  def __str__(self):
    return f"A rectangle with length {self.length} and width {self.width}"

  # comparison method for equality
  def __eq__(self, other):
    return self.length == other.length and self.width == other.width

  # comparison method for less than
  def __lt__(self, other):
    return self.area() < other.area()

  # arithmetic method for addition
  def __add__(self, other):
    return Rectangle(self.length + other.length, self.width + other.width)
```

- Here is an example of how to use the class:

```python
# create two rectangle objects
r1 = Rectangle(3, 4)
r2 = Rectangle(5, 6)

# print the objects
print(r1) # A rectangle with length 3 and width 4
print(r2) # A rectangle with length 5 and width 6

# access the attributes
print(r1.length) # 3
print(r2.width) # 6

# modify the attributes
r1.length = 6
r2.width = 8

# access the methods
print(r1.area()) # 48
print(r2.perimeter()) # 26

# compare the objects
print(r1 == r2) # False
print(r1 < r2) # True

# perform arithmetic operations
r3 = r1 + r2
print(r3) # A rectangle with length 11 and width 12
```

## Inheritance

- Inheritance is a mechanism