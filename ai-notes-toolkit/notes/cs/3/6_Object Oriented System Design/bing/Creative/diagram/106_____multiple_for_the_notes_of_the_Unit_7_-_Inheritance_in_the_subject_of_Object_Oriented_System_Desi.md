### Multiple Inheritance

- Multiple inheritance is a feature of some object-oriented programming languages in which a class can inherit attributes and methods from more than one superclass.
- Multiple inheritance allows a class to combine the functionality and characteristics of different superclasses, which can be useful for modeling complex systems or domains.
- However, multiple inheritance also introduces some challenges and complexities, such as the diamond problem, ambiguity, and conflicts among inherited members.
- Not all object-oriented programming languages support multiple inheritance. Some languages, such as Java and C#, use single inheritance with interfaces to achieve a similar effect. Other languages, such as Python and C++, allow multiple inheritance with some restrictions or rules to resolve potential issues.
- An example of multiple inheritance in Python is:

```python
# Define a base class Animal with a method sound
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Define another base class Bird with a method fly
class Bird:
    def fly(self):
        print("Bird can fly")

# Define a derived class Parrot that inherits from both Animal and Bird
class Parrot(Animal, Bird):
    def speak(self):
        print("Parrot can speak")

# Create an instance of Parrot and call its methods
p = Parrot()
p.sound() # Animal makes a sound
p.fly() # Bird can fly
p.speak() # Parrot can speak
```