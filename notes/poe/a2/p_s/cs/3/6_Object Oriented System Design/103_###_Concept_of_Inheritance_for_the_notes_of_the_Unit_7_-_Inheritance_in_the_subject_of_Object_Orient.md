 Here is the content in markdown format for the topic ### Concept of Inheritance for the notes of the Unit 7 - Inheritance in the subject of Object Oriented System Design:

### Concept of Inheritance

- Inheritance is an important concept in Object Oriented Programming (OOP). It allows us to define a class that inherits all the methods and properties from another class.
- The class that inherits the properties and methods is called a *child class* or *subclass* and the class that allows inheritance is called a *parent class* or *superclass*.
- Inheritance allows us to reuse the code from the parent class. We can extend the functionality of the parent class by adding more methods and properties in the child class.
- The child class inherits all the non-private methods and properties of the parent class. However, it can also override methods of the parent class and provide its own implementation.
- The key benefit of inheritance is reusability of code. The child class does not have to implement the methods and properties again that are already defined in the parent class. It can simply inherit them and extend or modify them as needed.
- Inheritance also promotes the DRY (Don't Repeat Yourself) principle as the code is reused and not repeated. It also allows us to logically classify objects into a hierarchy.

**Example:**

```
class Vehicle:
    def __init__(self, wheels, seats):
        self.wheels = wheels
        self.seats = seats

class Car(Vehicle):
    def __init__(self):
        super().__init__(wheels=4, seats=5)

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__(wheels=2, seats=2)
```

Here `Car` and `Motorcycle` inherit from the parent class `Vehicle`. They reuse the `wheels` and `seats` properties and simply pass in values for their specific types of vehicles in the constructor.

[Detailed diagrams and examples can be added here if required]

[Advantages, disadvantages and applications of inheritance can be added here if required]