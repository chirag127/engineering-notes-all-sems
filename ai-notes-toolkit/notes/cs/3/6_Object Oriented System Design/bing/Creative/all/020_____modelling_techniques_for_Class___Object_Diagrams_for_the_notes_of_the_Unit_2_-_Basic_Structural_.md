# Modelling Techniques for Class & Object Diagrams

## Introduction

Class and object diagrams are two types of structural diagrams in the Unified Modeling Language (UML) that show the static structure of a system. Class diagrams describe the classes, attributes, operations, and relationships of a system, while object diagrams show the instances of classes and their links at a specific point in time. Both diagrams are useful for object-oriented system design and analysis.

## Class Diagrams

A class diagram consists of the following elements:

- **Classes**: A class is a template that defines the properties and behaviors of a set of objects. A class is represented by a rectangle with the class name on the top, followed by the attributes and operations in separate compartments. For example:

![Class Diagram Example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/uml-class-diagram-tutorial/class-diagram-example.png)

- **Attributes**: An attribute is a named property of a class that describes the data stored in an object. An attribute has a name, a type, and an optional visibility and default value. For example, name: String, age: int, balance: double = 0.0.
- **Operations**: An operation is a named behavior of a class that defines the actions that an object can perform. An operation has a name, a list of parameters, a return type, and an optional visibility and body. For example, deposit(amount: double): void, withdraw(amount: double): boolean, getBalance(): double.
- **Associations**: An association is a relationship between two or more classes that indicates how the objects are linked. An association has a name, an optional direction, and multiplicity for each end. For example, a Customer class and a BankAccount class can have a one-to-many association named owns, where a customer can own zero or more bank accounts, and a bank account can be owned by one customer.

![Association Example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/uml-class-diagram-tutorial/association-example.png)

- **Aggregations**: An aggregation is a special type of association that represents a whole-part relationship. An aggregation has a hollow diamond symbol at the end of the association that represents the whole. For example, a Car class and a Wheel class can have a one-to-four aggregation named has, where a car has four wheels, and a wheel is part of one car.

![Aggregation Example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/uml-class-diagram-tutorial/aggregation-example.png)

- **Compositions**: A composition is a stronger form of aggregation that implies ownership and exclusive containment. A composition has a solid diamond symbol at the end of the association that represents the whole. For example, a House class and a Room class can have a one-to-many composition named contains, where a house contains one or more rooms, and a room belongs to one house.

![Composition Example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/uml-class-diagram-tutorial/composition-example.png)

- **Generalizations**: A generalization is a relationship between a general class (superclass) and a specific class (subclass) that indicates inheritance. A generalization has a solid line with a hollow triangle symbol at the end of the association that points to the superclass. For example, a Person class and a Student class can have a generalization named is-a, where a student is a person, and a person can have subclasses such as student, teacher, etc.

![Generalization Example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/uml-class-diagram-tutorial/generalization-example.png)

- **Realizations**: A realization is a relationship between an interface and a class that implements the interface. A realization has a dashed line with a hollow triangle symbol at the end of the association that points to the interface. For example, a Shape interface and a Circle class can have a realization named implements, where a circle implements the shape interface, and the shape interface can have classes that implement it such as circle, square, etc.

![Realization Example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/uml-class-diagram-tutorial/realization-example.png)

## Object Diagrams

An object diagram consists of the following elements:

- **Objects**: An object is an instance of a class that has a specific state and behavior. An object is represented by a rectangle with the object name and class name separated by a colon on the top, followed by the attribute values in a separate compartment. For example:

![