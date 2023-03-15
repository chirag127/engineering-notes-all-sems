# Basic Structural Modeling

Basic structural modeling is the process of identifying and describing the static structure of an object-oriented system. It involves the following concepts:

- **Class**: A class is a blueprint or template that defines the common attributes and behaviors of a group of similar objects. A class has a name, attributes (data members), and operations (member functions). A class can also have relationships with other classes, such as inheritance, association, aggregation, or composition. A class can be represented by a rectangle with three compartments: the top one for the class name, the middle one for the attributes, and the bottom one for the operations. For example:

![Class diagram example](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Loan_class.svg/320px-Loan_class.svg.png)

- **Object**: An object is an instance or occurrence of a class. It has a unique identity, a state, and a behavior. An object can be created, modified, or destroyed during the execution of a system. An object can be represented by a rectangle with an underlined name, optionally followed by a colon and the class name. For example:

![Object diagram example](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Object_Diagram.png/320px-Object_Diagram.png)

- **Relationship**: A relationship is a connection or link between two or more classes or objects. It specifies how they interact or depend on each other. There are different types of relationships, such as:

  - **Inheritance**: Inheritance is a relationship in which a subclass (child class) inherits the attributes and operations of a superclass (parent class). It is also called generalization or specialization. It represents an "is-a" or "kind-of" relationship. For example, a car is a kind of vehicle, so the class Car inherits from the class Vehicle. Inheritance can be represented by a solid line with a hollow triangle pointing to the superclass. For example:

  ![Inheritance diagram example](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Inheritance_example.svg/320px-Inheritance_example.svg.png)

  - **Association**: Association is a relationship in which two or more classes or objects are related or linked to each other. It represents a "has-a" or "uses-a" relationship. For example, a student has a name, a course has a teacher, a car uses a engine. Association can be represented by a solid line with optional labels for the role, multiplicity, and direction of the relationship. For example:

  ![Association diagram example](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Association_example.svg/320px-Association_example.svg.png)

  - **Aggregation**: Aggregation is a special type of association in which a class or object is composed of or contains other classes or objects. It represents a "part-of" or "whole-part" relationship. For example, a car is composed of wheels, doors, engine, etc. Aggregation can be represented by a solid line with a hollow diamond at the end of the whole. For example:

  ![Aggregation diagram example](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Aggregation_example.svg/320px-Aggregation_example.svg.png)

  - **Composition**: Composition is a stronger type of aggregation in which the lifetime of the part is dependent on the lifetime of the whole. It represents an "owns-a" relationship. For example, a car owns an engine, so if the car is destroyed, the engine is also destroyed. Composition can be represented by a solid line with a filled diamond at the end of the whole. For example:

  ![Composition diagram example](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Composition_example.svg/320px-Composition_example.svg.png)

- **Class diagram**: A class diagram is a diagram that shows the classes and relationships of an object-oriented system. It is a static view of the system structure. It can be used for analysis, design, or documentation purposes. A class diagram can include the following elements:

  - Classes and their attributes, operations, and visibility (public, private, or protected).
  - Relationships and their labels, multiplicity, and direction.
  - Generalization, realization, or dependency relationships between classes or interfaces.
  - Packages, notes, or constraints to group or annotate the elements.

- **Object diagram**: An object diagram is a diagram that shows the objects and relationships of an object-oriented system at a specific point in time. It is a