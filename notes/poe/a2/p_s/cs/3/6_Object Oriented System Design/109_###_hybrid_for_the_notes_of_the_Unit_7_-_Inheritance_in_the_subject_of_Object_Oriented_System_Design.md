 Here is the content in markdown format for the topic ### Inheritance for the notes of Unit 7 - Inheritance in Object Oriented System Design:

### Inheritance

- Inheritance is a key feature of Object Oriented Programming (OOP) that allows us to define a class that inherits all the methods and properties from another class.
- The class which inherits the properties from another class is called the *child class* or *subclass* and the class from which the properties are inherited is called the *parent class* or *superclass*.
- Inheritance allows us to reuse the code from the parent class and prevents duplication. The child class can also modify the properties and methods of the parent class and also add new properties and methods.
- The general form of inheritance is:

```
class Subclass (Parentclass):
    ...
```

- For example:

```
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

d = Dog("Rex")
d.eat("dog food")  # Rex is eating dog food
d.bark()  # Rex is barking
```

- In the above example, the `Dog` class inherits from the `Animal` class. So the `Dog` class will have all the properties and methods of the `Animal` class and can also define additional properties and methods of its own.
- The `__init__()` method is also inherited by the `Dog` class from the `Animal` class. But we can redefine the `__init__()` method in the `Dog` class to include additional properties if required. This is called *method overriding*.
- There are three types of inheritance:

1. Single inheritance - A subclass inherits from only one superclass.
2. Multiple inheritance - A subclass inherits from multiple superclasses.
3. Multilevel inheritance - A subclass inherits from another subclass which in turn inherits from a superclass.

- Advantages of inheritance:
- Code reusability - Common logic can be shared among classes using inheritance.
- Maintainability - Modifications to the parent class automatically reflect in the child class.
- Disadvantages of inheritance:
- Tight coupling - Child class is tightly coupled with the parent class.
- Inappropriate inheritance - Using inheritance when composition is more appropriate can lead to poorly designed systems.