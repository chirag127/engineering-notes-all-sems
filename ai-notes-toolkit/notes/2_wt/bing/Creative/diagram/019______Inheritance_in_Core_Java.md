Inheritance in Java is one of the core concepts of Object-Oriented Programming. It enables developers to inherit data members and properties from one class to another. Inheritance is used when we have is-a relationship between objects. For example, a Car is a Vehicle, so Car can inherit from Vehicle class. Inheritance in Java is implemented using extends keyword. For example, `class Car extends Vehicle` means Car class inherits from Vehicle class. Inheritance in Java allows for code reuse, abstraction and class hierarchy.

A diagram for inheritance in Java can be drawn using ASCII characters as follows:

#### Inheritance in Core Java

```
    +-----------------+
    |     Vehicle     |
    +-----------------+
    | +speed          |
    | +color          |
    +-----------------+
    | +start()        |
    | +stop()         |
    +-----------------+
           /_\
            |
            |
            |
    +-----------------+
    |       Car       |
    +-----------------+
    | +model          |
    | +brand          |
    +-----------------+
    | +honk()         |
    | +accelerate()   |
    +-----------------+
```

The diagram shows that Car class inherits from Vehicle class using extends keyword. Car class can access the data members and methods of Vehicle class, as well as its own data members and methods. Car class is a subclass or child class of Vehicle class, while Vehicle class is a superclass or parent class of Car class. The arrow indicates the direction of inheritance.