Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here is the content for the topic of Instance Methods for the notes of Unit 3 - Scripting:

### Instance Methods

- Instance methods are functions that are defined inside a class and can be called on the objects of that class.
- Instance methods have access to the instance attributes and the class attributes of the object they are called on.
- Instance methods can modify the state of the object by changing the values of its instance attributes.
- Instance methods can also call other instance methods or class methods of the same class.
- Instance methods are defined by using the `def` keyword followed by the method name and a list of parameters. The first parameter is usually named `self` and represents the object that the method is called on.
- Instance methods are called by using the dot notation, i.e., `object.method(arguments)`.
- Example:

```python
# Define a class called Person
class Person:
  # Define a class attribute called species
  species = "human"

  # Define an instance method called __init__ that sets the name and age of the object
  def __init__(self, name, age):
    self.name = name # Define an instance attribute called name
    self.age = age # Define an instance attribute called age

  # Define an instance method called greet that prints a greeting message
  def greet(self):
    print(f"Hello, I am {self.name}, a {self.species}. I am {self.age} years old.")

  # Define an instance method called celebrate that increments the age of the object by 1 and prints a message
  def celebrate(self):
    self.age += 1 # Modify the instance attribute age
    print(f"Happy birthday, {self.name}! You are now {self.age} years old.")

# Create an object of the class Person
p1 = Person("Alice", 20)

# Call the instance method greet on the object p1
p1.greet()
# Output: Hello, I am Alice, a human. I am 20 years old.

# Call the instance method celebrate on the object p1
p1.celebrate()
# Output: Happy birthday, Alice! You are now 21 years old.
```