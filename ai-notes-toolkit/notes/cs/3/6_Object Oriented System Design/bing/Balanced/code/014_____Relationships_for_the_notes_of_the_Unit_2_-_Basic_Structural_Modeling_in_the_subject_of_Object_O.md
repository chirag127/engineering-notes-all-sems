### Relationships

Relationships are the connections between classes or objects in object-oriented system design. They describe how the classes or objects interact with each other and what kind of dependencies they have. Relationships can be classified into four types: inheritance, association, composition, and aggregation .

- **Inheritance** is a relationship where a class (called the subclass or child class) inherits the attributes and operations of another class (called the superclass or parent class). Inheritance is based on the "is a" relationship, meaning that the subclass is a specific type of the superclass. For example, a Dog class can inherit from an Animal class, because a dog is an animal. Inheritance allows for code reuse and polymorphism .
- **Association** is a relationship where two classes or objects are linked by some concept or idea. Association is based on the "has a" relationship, meaning that one class or object has a reference to another class or object. For example, a Student class can have an association with a Course class, because a student has a course. Association can be unidirectional or bidirectional, meaning that one or both classes or objects can access each other. Association can also have a multiplicity, meaning that one class or object can have one or many references to another class or object .
- **Composition** is a relationship where a class or object is composed of other classes or objects. Composition is based on the "part of" relationship, meaning that the composed class or object is a part of the composing class or object. For example, a Car class can have a composition with an Engine class, because a car is composed of an engine. Composition implies a strong dependency and ownership, meaning that the composed class or object cannot exist without the composing class or object. Composition can also have a multiplicity, meaning that one class or object can have one or many parts of another class or object .
- **Aggregation** is a relationship where a class or object is a collection of other classes or objects. Aggregation is also based on the "part of" relationship, but it implies a weaker dependency and ownership, meaning that the aggregated class or object can exist without the aggregating class or object. For example, a Library class can have an aggregation with a Book class, because a library is a collection of books. Aggregation can also have a multiplicity, meaning that one class or object can have one or many collections of another class or object .

Relationships can be represented in a class diagram using different symbols and notations. A class diagram is a type of static structure diagram that shows the classes, their attributes, operations, and the relationships among them. A class diagram is the main building block of object-oriented modeling. The following table summarizes the symbols and notations for the four types of relationships in a class diagram :

| Relationship | Symbol | Notation |
| ------------ | ------ | -------- |
| Inheritance | A solid line with a hollow triangle pointing to the superclass | Subclass **extends** Superclass |
| Association | A solid line with an optional arrow indicating the direction | Class1 **has a** Class2 |
| Composition | A solid line with a filled diamond pointing to the composed class | Class1 **is composed of** Class2 |
| Aggregation | A solid line with a hollow diamond pointing to the aggregated class | Class1 **is a collection of** Class2 |

Here is an example of a class diagram that shows the relationships among some classes related to a university system:

![Class diagram example](https://www.c-sharpcorner.com/article/types-of-relationships-in-object-oriented-programming-oops/Images/image001.jpg)

: https://www.linkedin.com/pulse/types-relationships-object-oriented-programming-oop-sarah-el-dawody
: https://www.c-sharpcorner.com/article/types-of-relationships-in-object-oriented-programming-oops/
: https://en.wikipedia.org/wiki/Object-oriented_design
: https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)
: https://www.infoworld.com/article/3029325/exploring-association-aggregation-and-composition-in-oop.html
: https://en.wikipedia.org/wiki/Class_diagram