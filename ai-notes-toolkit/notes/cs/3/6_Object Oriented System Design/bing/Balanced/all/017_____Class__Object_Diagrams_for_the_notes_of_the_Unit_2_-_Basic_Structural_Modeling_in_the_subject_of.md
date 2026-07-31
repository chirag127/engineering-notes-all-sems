# Class and Object Diagrams

## Introduction

- Class and object diagrams are two types of structural diagrams in the Unified Modeling Language (UML) that show the static structure of a system.
- Class diagrams describe the classes and interfaces in a system, their attributes, operations, and relationships.
- Object diagrams show the instances of classes and interfaces in a system, their values, and links.
- Class and object diagrams are closely related and can be derived from each other.

## Class Diagrams

- A class diagram consists of the following elements:
  - **Class**: A class is a template that defines the common properties and behaviors of a set of objects. A class is represented by a rectangle with the class name on the top, followed by the attributes and operations sections.
  - **Attribute**: An attribute is a named property of a class that describes the data stored in an object. An attribute is shown as a text line in the attributes section of the class, with the format `name: type [multiplicity] = default value`.
  - **Operation**: An operation is a named function or procedure that can be performed by an object or a class. An operation is shown as a text line in the operations section of the class, with the format `name(parameter list): return type [multiplicity]`.
  - **Interface**: An interface is a collection of abstract operations that a class can implement. An interface is represented by a circle with the interface name on it, or a rectangle with the stereotype `<<interface>>` above the name.
  - **Relationship**: A relationship is a connection between two or more classes or interfaces that indicates some kind of dependency or association. There are different types of relationships, such as inheritance, association, aggregation, composition, and dependency. A relationship is represented by a line or an arrow between the related elements, with optional labels and symbols to indicate the type and properties of the relationship.

- A class diagram can be used to model the structure of a system at different levels of abstraction, such as conceptual, specification, or implementation.
- A class diagram can also be used to show the collaboration of classes and interfaces in a use case or a scenario.

## Object Diagrams

- An object diagram consists of the following elements:
  - **Object**: An object is an instance of a class or an interface that has a unique identity and a state. An object is represented by a rectangle with the object name and class name separated by a colon on the top, followed by the attribute values section.
  - **Attribute value**: An attribute value is the data stored in an object for a specific attribute. An attribute value is shown as a text line in the attribute values section of the object, with the format `name = value`.
  - **Link**: A link is an instance of a relationship between two or more objects that reflects their association or dependency. A link is represented by a line or an arrow between the linked objects, with optional labels and symbols to indicate the type and properties of the link.

- An object diagram can be used to show the state of a system at a specific point in time, or the interaction of objects in a scenario.
- An object diagram can also be used to illustrate the examples or test cases of a system.

## Example

- The following is an example of a class diagram and an object diagram for a simple bank system.

![Class diagram for bank system](https://www.visual-paradigm.com/servlet/editor-content/tutorials/uml-class-diagram-tutorial/bank-system-class-diagram.png)

- The class diagram shows that there are four classes: Bank, Account, Customer, and Transaction. 
- Bank has an attribute name and an operation createAccount. 
- Account has attributes number, balance, and interestRate, and operations deposit, withdraw, and transfer. 
- Customer has attributes name, address, and email, and an operation getAccounts. 
- Transaction has attributes date, amount, and type, and an operation execute. 
- There are also several relationships between the classes: 
  - Bank has a one-to-many composition relationship with Account, meaning that a bank owns many accounts and an account belongs to one bank. 
  - Account has a one-to-many aggregation relationship with Transaction, meaning that an account has many transactions and a transaction is part of one account. 
  - Customer has a many-to-many association relationship with Account, meaning that a customer can have many accounts and an account can have many customers. 
  - Transaction has a dependency relationship with Account, meaning that a transaction uses the operations of an account.

![Object diagram for bank system](https://www.visual-paradigm