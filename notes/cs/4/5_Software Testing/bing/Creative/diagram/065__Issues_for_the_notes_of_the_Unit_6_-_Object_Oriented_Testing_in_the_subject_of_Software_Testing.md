### Issues for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

Object Oriented Testing (OOT) is a testing approach that is applied to software systems that are developed using the object-oriented paradigm. OOT aims to test the functionality and behavior of classes, objects, methods, inheritance, polymorphism, and other object-oriented features. OOT faces some challenges and issues that are different from conventional testing methods. Some of these issues are:

- **Unit testing**: A unit in an object-oriented system can be either a class or a method within a class. Testing a class as a unit requires testing its methods, attributes, constructors, and interactions with other classes. Testing a method as a unit requires testing its input-output behavior, its state changes, and its exceptions. Unit testing can be difficult when the class or method depends on inheritance, polymorphism, or composition. Unit testing can also be affected by the level of encapsulation, which may limit the access to the internal structure of the class or method.

- **Integration testing**: Integration testing is the process of testing the interactions and interfaces among different classes or components of the system. Integration testing can be challenging in object-oriented systems due to the dynamic binding, message passing, and loose coupling features. Dynamic binding allows the selection of the appropriate method at run time, depending on the type of the object. Message passing allows the communication among objects through method invocation. Loose coupling means that the classes are designed to be independent and self-contained. These features make it hard to predict and control the flow of execution and the data exchange among the classes or components.

- **Inheritance and polymorphism**: Inheritance and polymorphism are two key features of object-oriented systems that allow the reuse and extension of existing classes. Inheritance allows a subclass to inherit the attributes and methods of a superclass, and to override or add new ones. Polymorphism allows a subclass to be treated as an instance of its superclass, and to behave differently depending on its type. These features introduce some issues for testing, such as:

  - How to test a subclass without retesting the superclass?
  - How to test the overridden or added methods in the subclass?
  - How to test the polymorphic behavior of the subclass?
  - How to test the interactions among different subclasses of the same superclass?

- **Composition and encapsulation**: Composition and encapsulation are two design principles that aim to improve the modularity and maintainability of object-oriented systems. Composition allows a class to be composed of other classes, and to delegate some of its responsibilities to them. Encapsulation means that a class hides its internal details and exposes only its public interface. These principles introduce some issues for testing, such as:

  - How to test a class that is composed of other classes?
  - How to test the delegation of responsibilities among the composed classes?
  - How to test the class without violating its encapsulation?
  - How to test the public interface of the class?

The following diagram illustrates the basic architecture of a object-oriented system and some of the testing issues that arise from it:

```
+-----------------+       +-----------------+       +-----------------+
|    Subclass A   |       |    Subclass B   |       |    Subclass C   |
+-----------------+       +-----------------+       +-----------------+
| - attribute a   |       | - attribute b   |       | - attribute c   |
| + method a()    |       | + method b()    |       | + method c()    |
| + overridden()  |       | + overridden()  |       | + overridden()  |
+-----------------+       +-----------------+       +-----------------+
         ^                       ^                       ^
         |                       |                       |
         |                       |                       |
         +-----------------------+-----------------------+
                                 |
                                 |
                                 v
                         +-----------------+
                         |    Superclass   |
                         +-----------------+
                         | - attribute     |
                         | + method()      |
                         | + overridden()  |
                         +-----------------+
                                 ^
                                 |
                                 |
                                 v
                         +-----------------+
                         |    Component    |
                         +-----------------+
                         | - attribute     |
                         | + method()      |
                         | + composed()    |
                         +-----------------+
                                 ^
                                 |
                                 |
                                 v
                         +-----------------+
                         |    System       |
                         +-----------------+
                         | - attribute     |
                         | + method()      |
                         | + interface()   |
                         +-----------------+
```

Some of the testing issues are:

- How to test the