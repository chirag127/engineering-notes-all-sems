# Combining three models for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design

Object Oriented Analysis (OOA) is the first technical activity performed as part of object-oriented software engineering. OOA introduces new concepts to investigate a problem. It is based on a set of basic principles, which are as follows:

- The information domain is modeled.
- Behavior is represented.
- The function is described.

OOA uses three analysis techniques that are used in conjunction with each other for object-oriented analysis. These are:

- Object Modeling: Object modeling develops the static structure of the software system in terms of objects. It defines the classes of objects, their attributes, operations, and relationships. It also identifies the events that affect the state of the objects.
- Dynamic Modeling: Dynamic modeling describes the behavior of the objects over time. It captures the changes in the state and the interactions of the objects. It uses state diagrams and sequence diagrams to represent the dynamic aspects of the system.
- Functional Modeling: Functional modeling specifies the functionality of the system from the user's perspective. It defines the input and output data flows, the transformations applied on the data, and the external entities that interact with the system. It uses data flow diagrams and data dictionaries to represent the functional model.

The three models are combined to form a complete and consistent representation of the system under analysis. The object model provides the static view, the dynamic model provides the behavioral view, and the functional model provides the functional view of the system. The models are interrelated and should be consistent with each other. The models can be validated and verified using various techniques such as scenario-based testing, walkthroughs, and reviews.

Object Oriented Design (OOD) is the next technical activity performed after OOA. OOD transforms the analysis model created using OOA into a design model that works as a plan for software creation. OOD results in a design having several different levels of modularity i.e.,:

- Subsystems: A subsystem is a collection of classes that collaborate to provide a specific service or function. Subsystems are used to decompose the system into manageable and reusable components.
- Classes: A class is a blueprint for creating objects. It defines the attributes, operations, and relationships of the objects of that class. Classes are used to encapsulate the data and behavior of the system.
- Methods: A method is a sequence of statements that implements an operation of a class. Methods are used to define the logic and algorithms of the system.
- Messages: A message is a request from one object to another object to perform an operation. Messages are used to communicate and coordinate the actions of the objects.

OOD uses the same three models as OOA, but with more details and refinements. The object model is enhanced with inheritance, polymorphism, and aggregation. The dynamic model is refined with more states, transitions, and actions. The functional model is elaborated with more data flows, processes, and data stores. The design model is also validated and verified using various techniques such as design metrics, design patterns, and design reviews.

Object Oriented Data Model (OODM) is a common approach to modeling applications, systems, and business domains by using the object-oriented paradigm throughout the entire development life cycles. OODM is a main technique heavily used by both OOD and OOA activities in modern software engineering. OODM is based on the following concepts:

- Object: An object is an entity that has a unique identity, a state, and a behavior. An object is an instance of a class.
- Class: A class is a collection of objects that share the same structure and behavior. A class defines the attributes, operations, and relationships of its objects.
- Attribute: An attribute is a property or characteristic of an object. An attribute has a name and a value.
- Operation: An operation is a function or a service that an object can perform. An operation has a name and a set of parameters.
- Relationship: A relationship is a connection or an association between two or more objects. A relationship has a name and a cardinality.
- Inheritance: Inheritance is a mechanism that allows a class to inherit the attributes and operations of another class. The class that inherits is called the subclass, and the class that is inherited is called the superclass.
- Polymorphism: Polymorphism is a mechanism that allows an object to behave differently depending on its class or context. Polymorphism enables an object to respond to the same message with different methods.
- Aggregation: Aggregation is a