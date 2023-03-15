### Class & Object Diagrams

- Class and object diagrams are two types of structural diagrams in UML that show the static structure of a system.
- Class diagrams describe the classes and interfaces that make up the system, along with their attributes, operations, and relationships.
- Object diagrams show the instances of classes and interfaces in a specific situation or scenario, along with their values and links.
- Class and object diagrams are related, as object diagrams are derived from class diagrams. An object diagram is a snapshot of a class diagram at a certain point in time.

#### Class Diagrams

- A class diagram consists of the following elements:
  - **Class**: A rectangle with three compartments, showing the class name, attributes, and operations. A class represents a set of objects that share the same structure and behavior.
  - **Interface**: A rectangle with the keyword «interface» above the name, showing the interface name and operations. An interface specifies a contract that other classes can implement.
  - **Attribute**: A text line in the second compartment of a class or interface, showing the name, type, and optionally the visibility and default value of an attribute. An attribute is a property or feature of a class or interface.
  - **Operation**: A text line in the third compartment of a class or interface, showing the name, parameters, return type, and optionally the visibility and other modifiers of an operation. An operation is a function or method that can be performed by a class or interface.
  - **Association**: A solid line connecting two classes or interfaces, optionally with an association name, role names, and multiplicity at each end. An association represents a relationship between two or more classes or interfaces that describes how they are linked or connected.
  - **Aggregation**: A type of association with a hollow diamond at the aggregate (whole) end. An aggregation represents a part-of relationship between an aggregate and its components, where the components can exist independently of the aggregate.
  - **Composition**: A type of association with a solid diamond at the composite (whole) end. A composition represents a part-of relationship between a composite and its components, where the components cannot exist without the composite.
  - **Generalization**: A solid line with a hollow triangle at the superclass (parent) end. A generalization represents an inheritance relationship between a superclass and a subclass, where the subclass inherits the features of the superclass.
  - **Realization**: A dashed line with a hollow triangle at the interface (contract) end. A realization represents an implementation relationship between a class and an interface, where the class implements the operations of the interface.

- A class diagram can be used for various purposes, such as:
  - Modeling the domain concepts and terminology.
  - Designing the system architecture and components.
  - Specifying the system behavior and interactions.
  - Documenting the system design and implementation.
  - Visualizing and understanding the system structure and relationships.

- An example of a class diagram is shown below:

![Class diagram example](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/wp-content/uploads/sites/3/2018/11/uml-class-diagram-example.png)

#### Object Diagrams

- An object diagram consists of the following elements:
  - **Object**: A rectangle with the object name and class name separated by a colon, optionally with an underline and an object identifier. An object is an instance of a class that has a state and a behavior.
  - **Link**: A solid line connecting two objects, optionally with a link name, role names, and multiplicity at each end. A link is an instance of an association that represents a connection or relationship between two or more objects.
  - **Value**: A text line in the second compartment of an object, showing the name and value of an attribute. A value is an instance of an attribute that represents a property or feature of an object.

- An object diagram can be used for various purposes, such as:
  - Illustrating a specific scenario or example of a system.
  - Testing and verifying the system functionality and behavior.
  - Debugging and tracing the system execution and state.
  - Exploring and analyzing the system design and implementation.
  - Communicating and presenting the system structure and relationships.

- An example of an object diagram is shown below:

![Object diagram example](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-object-diagram/wp-content/uploads/sites/3/2018/11/uml-object-diagram-example.png)