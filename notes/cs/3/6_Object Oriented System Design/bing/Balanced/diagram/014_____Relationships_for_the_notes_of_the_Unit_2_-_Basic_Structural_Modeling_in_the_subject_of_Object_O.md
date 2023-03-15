### Relationships

Relationships are the connections between classes or objects in object-oriented system design. They describe how the classes or objects interact with each other and what kind of dependencies they have. There are four main types of relationships in object-oriented programming: inheritance, association, composition, and aggregation .

- **Inheritance** is a relationship where a class (called the subclass or child class) inherits the attributes and operations of another class (called the superclass or parent class). This means that the subclass can use the features of the superclass as well as add its own features. Inheritance is based on the "is a" relationship, meaning that the subclass is a specific type of the superclass. For example, a Dog class can inherit from an Animal class, because a dog is an animal. Inheritance is represented by a solid line with an empty arrowhead pointing from the subclass to the superclass.

- **Association** is a relationship where two classes or objects are linked to each other in some way, but they can exist independently. Association is based on the "has a" relationship, meaning that one class or object has a reference to another class or object. For example, a Student class can have an association with a Course class, because a student has a course. Association is represented by a solid line with no arrowheads between the classes or objects.

- **Composition** is a relationship where a class (called the composite or whole) contains another class (called the component or part) as a part of its structure. Composition is based on the "part of" relationship, meaning that the component is a part of the composite and cannot exist without it. For example, a Car class can have a composition with an Engine class, because an engine is a part of a car and cannot function without it. Composition is represented by a solid line with a filled diamond at the end of the composite.

- **Aggregation** is a relationship where a class (called the aggregate or whole) contains another class (called the member or part) as a part of its structure, but the member can exist independently of the aggregate. Aggregation is also based on the "part of" relationship, but it is a weaker form of composition. For example, a Library class can have an aggregation with a Book class, because a book is a part of a library, but it can also exist outside of it. Aggregation is represented by a solid line with an empty diamond at the end of the aggregate.

Here is a diagram that shows the four types of relationships in UML notation:

![Relationships diagram](https://i.imgur.com/0fZ1w7w.png)