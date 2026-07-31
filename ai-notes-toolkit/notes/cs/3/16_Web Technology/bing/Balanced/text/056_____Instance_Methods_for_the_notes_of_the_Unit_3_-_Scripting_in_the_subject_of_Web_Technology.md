### Instance Methods

- Instance methods are functions that are defined inside a class and can be called on an instance of that class.
- Instance methods have access to the instance attributes and the class attributes of the class they belong to.
- Instance methods can modify the state of the instance by changing the values of the instance attributes.
- Instance methods can also call other instance methods or class methods of the same class using the `self` parameter, which refers to the current instance.
- Instance methods are defined using the `def` keyword, followed by the method name and a list of parameters. The first parameter is always `self`, which is automatically passed by Python when the method is called on an instance.
- Instance methods can return a value using the `return` statement, or return `None` by default if no `return` statement is present.
- Instance methods can be invoked on an instance using the dot notation, such as `instance.method(arguments)`, where `instance` is the name of the instance, `method` is the name of the method, and `arguments` are the values passed to the method parameters (excluding `self`).
- Example:

```python
# Define a class called Dog
class Dog:

  # Define a class attribute that is shared by all instances of Dog
  species = "Canis familiaris"

  # Define an instance method called __init__ that is executed when a new instance of Dog is created
  def __init__(self, name, age):
    # Assign the name and age parameters to instance attributes
    self.name = name
    self.age = age

  # Define an instance method called description that returns a string with the name and age of the dog
  def description(self):
    return f"{self.name} is {self.age} years old"

  # Define an instance method called speak that takes a sound parameter and prints a string with the name and sound of the dog
  def speak(self, sound):
    print(f"{self.name} says {sound}")

# Create an instance of Dog called miles
miles = Dog("Miles", 4)

# Call the description method on miles and print the result
print(miles.description())

# Call the speak method on miles and pass "Woof" as the argument
miles.speak("Woof")
```

- Output:

```text
Miles is 4 years old
Miles says Woof
```