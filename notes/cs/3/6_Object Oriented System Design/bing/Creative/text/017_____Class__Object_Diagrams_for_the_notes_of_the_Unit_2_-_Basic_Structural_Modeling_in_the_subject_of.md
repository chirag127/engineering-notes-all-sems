### Class and Object Diagrams

- Class and object diagrams are two types of structural diagrams in UML that show the static structure and behavior of a system.
- Class diagrams describe the classes and interfaces that make up the system, along with their attributes, operations, and relationships.
- Object diagrams show the instances of classes and interfaces in a specific situation or scenario, along with their values and links.
- Class and object diagrams are related in the sense that an object diagram is a snapshot of a class diagram at a particular point in time.

#### Class Diagrams

- A class diagram consists of a set of classes and interfaces, represented by rectangles with three compartments: the top one for the name, the middle one for the attributes, and the bottom one for the operations.
- A class can have zero or more attributes, which are the properties or characteristics of the class. An attribute has a name, a type, and optionally a visibility (public, private, protected, or package) and a multiplicity (how many values it can have).
- A class can have zero or more operations, which are the behaviors or functions of the class. An operation has a name, a list of parameters, a return type, and optionally a visibility and a multiplicity.
- A class can also have zero or more stereotypes, which are keywords enclosed in guillemets (« ») that indicate some special characteristics or roles of the class. For example, «abstract» means the class cannot be instantiated, «interface» means the class only defines a set of operations without implementation, and «enumeration» means the class defines a finite set of constants.

- A class diagram can also show the relationships between classes and interfaces, such as associations, generalizations, dependencies, realizations, and aggregations.
- An association is a structural relationship that indicates that two classes are related in some way, such as a student has a name or a car has an engine. An association has a name, a direction, and optionally a role name, a multiplicity, and a visibility for each end. An association can also have attributes and operations, which are shown in a separate compartment attached to the association line.
- A generalization is a relationship that indicates that a class is a kind of another class, such as a dog is a kind of animal or a circle is a kind of shape. A generalization is shown as a solid line with a hollow triangle pointing to the superclass (the more general class).
- A dependency is a relationship that indicates that a class depends on another class for some reason, such as a class uses another class as a parameter or a class creates an instance of another class. A dependency is shown as a dashed line with an open arrowhead pointing to the supplier (the class that is depended on).
- A realization is a relationship that indicates that a class implements an interface, such as a printer realizes a printable interface or a list realizes a collection interface. A realization is shown as a dashed line with a hollow triangle pointing to the interface (the class that is realized).
- An aggregation is a relationship that indicates that a class is a part of another class, such as a wheel is a part of a car or a page is a part of a book. An aggregation is shown as a solid line with a hollow diamond at the end of the whole (the class that contains the parts). An aggregation implies that the parts can exist independently of the whole, unlike a composition, which is a stronger form of aggregation that implies that the parts cannot exist without the whole. A composition is shown as a solid line with a filled diamond at the end of the whole.

#### Object Diagrams

- An object diagram consists of a set of objects and links, represented by rectangles and lines, respectively. An object is an instance of a class or an interface, and a link is an instance of an association or an aggregation.
- An object has a name, which is the name of the class or the interface followed by a colon and a unique identifier. An object can also have a stereotype, which is the same as for a class. An object can also show the values of its attributes, which are the actual data stored in the object.
- A link has a name, which is the name of the association or the aggregation followed by a colon and a unique identifier. A link can also have a stereotype, which is the same as for an association or an aggregation. A link can also show the values of its attributes, which are the actual data stored in the link.
- An object diagram can also show the messages that are exchanged between objects, which are the invocations of the operations defined by the classes