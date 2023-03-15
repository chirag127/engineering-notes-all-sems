### Relationships

Relationships are the connections between classes or objects in object-oriented system design. They describe how the classes or objects interact with each other and what kind of dependencies they have. There are four main types of relationships in object-oriented programming: inheritance, association, composition, and aggregation .

- **Inheritance** is a relationship where a class (called the subclass or child class) inherits the attributes and operations of another class (called the superclass or parent class). This means that the subclass can use the features of the superclass as well as add its own features. Inheritance is based on the "is a" relationship, meaning that the subclass is a specific type of the superclass. For example, a Dog class can inherit from an Animal class, because a dog is an animal.
- **Association** is a relationship where two classes or objects are linked to each other in some way, but they can exist independently. Association is based on the "has a" relationship, meaning that one class or object has a reference to another class or object. For example, a Student class can have an association with a Course class, because a student has a course, but they can exist without each other.
- **Composition** is a relationship where a class (called the composite or whole) contains another class (called the component or part) as a part of its structure. Composition is based on the "part of" relationship, meaning that the component is a part of the composite and cannot exist without it. For example, a Car class can have a composition with an Engine class, because an engine is a part of a car and cannot exist without it.
- **Aggregation** is a relationship where a class (called the aggregate or whole) contains another class (called the constituent or part) as a part of its structure, but the constituent can exist independently. Aggregation is also based on the "part of" relationship, but it is a weaker form of composition. For example, a Library class can have an aggregation with a Book class, because a book is a part of a library, but it can exist without it.

Relationships can be represented in a class diagram using different symbols and lines. A class diagram is a type of static structure diagram that shows the classes, their attributes, operations, and the relationships among them. The following table summarizes the symbols and lines used for each type of relationship in a class diagram.

| Relationship | Symbol | Line |
| ------------ | ------ | ---- |
| Inheritance | A hollow triangle pointing to the superclass | A solid line |
| Association | A solid diamond at the end of the line | A solid line |
| Composition | A filled diamond at the composite end of the line | A solid line |
| Aggregation | A hollow diamond at the aggregate end of the line | A solid line |

Here is an example of a class diagram that shows the relationships among some classes:

![Class diagram example](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/GOF-DesignPatterns-Structure.svg/1200px-GOF-DesignPatterns-Structure.svg.png)

In this diagram, the Shape class is the superclass of the Circle, Rectangle, and Triangle classes, so there is an inheritance relationship between them. The Shape class has an association with the Color class, because a shape has a color, but they can exist independently. The Drawing class has a composition with the Shape class, because a shape is a part of a drawing and cannot exist without it. The Drawing class also has an aggregation with the Paper class, because a paper is a part of a drawing, but it can exist without it.