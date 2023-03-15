### Class & Object Diagrams

- Class and object diagrams are two types of structural diagrams in the Unified Modeling Language (UML) that show the static structure of a system.
- A class diagram describes the system in terms of its classes, attributes, operations, and relationships among classes.
- An object diagram shows a snapshot of the instances of the classes and their values and relationships at a specific point in time.
- Both class and object diagrams use similar notation, but differ in their level of abstraction and purpose.

#### Class Diagram

- A class diagram is a graphical representation of the classes and interfaces in a system, along with their features, constraints, and associations.
- A class diagram can be used for various purposes, such as:
  - Domain modeling: to capture the concepts and terminology of a problem domain.
  - Design modeling: to specify the structure and behavior of a software system.
  - Implementation modeling: to document the code structure and dependencies of a system.
- A class diagram consists of the following elements:
  - Class: a rectangle with three compartments, showing the class name, attributes, and operations. Optionally, the class name can be preceded by a stereotype, such as <<abstract>>, <<interface>>, or <<enumeration>>.
  - Attribute: a property of a class that describes its state. An attribute has a name, a type, and optionally a visibility (public, private, protected, or package) and a default value.
  - Operation: a behavior or service provided by a class. An operation has a name, a list of parameters, a return type, and optionally a visibility and other modifiers, such as abstract, static, or final.
  - Association: a relationship between two or more classes that indicates how they are connected. An association has a name, a direction, and optionally a multiplicity, a role, and a qualifier for each end.
  - Generalization: a relationship between a more general class (superclass) and a more specific class (subclass) that indicates inheritance. A generalization is shown as a solid line with a hollow triangle pointing to the superclass.
  - Dependency: a relationship between two classes that indicates that one class uses or depends on another class. A dependency is shown as a dashed line with an open arrow pointing to the class that is used or depended on.
  - Realization: a relationship between a class and an interface that indicates that the class implements the interface. A realization is shown as a dashed line with a hollow triangle pointing to the interface.
  - Aggregation: a special type of association that indicates a whole-part relationship between two classes. An aggregation is shown as a solid line with a hollow diamond at the end of the whole.
  - Composition: a special type of aggregation that indicates a strong whole-part relationship between two classes, where the part cannot exist without the whole. A composition is shown as a solid line with a filled diamond at the end of the whole.

#### Object Diagram

- An object diagram is a graphical representation of the objects and their values and relationships in a system at a specific point in time.
- An object diagram can be used for various purposes, such as:
  - Testing: to verify the correctness and completeness of a system's state.
  - Debugging: to locate and fix errors in a system's state.
  - Documentation: to illustrate an example scenario or use case of a system.
- An object diagram consists of the following elements:
  - Object: a rectangle with two compartments, showing the object name and the attribute values. Optionally, the object name can be preceded by a colon and followed by the class name, such as :Customer or order:Order.
  - Link: a solid line connecting two objects, representing an instance of an association. Optionally, a link can have a name, a direction, and a multiplicity, a role, and a qualifier for each end, similar to an association.
  - Link attribute: a property of a link that describes its state. A link attribute is shown as a small rectangle attached to the link, with the attribute name and value.
  - Generalization link: a solid line with a hollow triangle pointing to the superclass object, representing an instance of a generalization.
  - Dependency link: a dashed line with an open arrow pointing to the object that is used or depended on, representing an instance of a dependency.
  - Realization link: a dashed line with a hollow triangle pointing to the interface object, representing an instance of a realization.
  - Aggregation link: a solid line with a hollow diamond at the end of the whole object, representing an instance of an aggregation.
  - Composition link