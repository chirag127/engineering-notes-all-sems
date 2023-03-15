# Principles of Modelling for Object Oriented System Design

- Modelling is the process of creating a simplified and abstract representation of a system using a set of concepts, rules and symbols.
- Modelling helps to understand, communicate, analyze, design and implement a system in a systematic and consistent way.
- Modelling can be done at different levels of abstraction, such as conceptual, logical and physical, depending on the purpose and scope of the system.
- Modelling can also be done from different perspectives, such as structural, behavioral and functional, depending on the aspects and features of the system.
- Object oriented modelling is a type of modelling that uses the concepts of objects, classes, attributes, methods, associations, inheritance, polymorphism and encapsulation to represent a system.
- Object oriented modelling is based on the following principles:

  - Abstraction: Modelling the relevant attributes and interactions of entities as classes to define an abstract representation of a system .
  - Encapsulation: Hiding the internal state and functionality of an object and only allowing access through a public set of functions .
  - Inheritance: Ability to create new abstractions based on existing abstractions, reusing and extending the attributes and methods of parent classes .
  - Polymorphism: Ability to use the same name or symbol for different types of objects, allowing them to behave differently depending on their actual type .
- Object oriented modelling can be done using various techniques and tools, such as Unified Modeling Language (UML), Object Modeling Technique (OMT), Object Constraint Language (OCL), etc.
- Object oriented modelling can benefit from following some design principles and strategies, such as:

  - Single-responsibility principle: Each class or module should have one and only one reason to change, meaning that it should have a single well-defined responsibility.
  - Open-closed principle: Classes or modules should be open for extension but closed for modification, meaning that they should allow adding new features without changing the existing code.
  - Liskov substitution principle: Subtypes should be substitutable for their supertypes, meaning that they should preserve the behavior and contracts of their parent classes.
  - Interface segregation principle: Clients should not be forced to depend on interfaces that they do not use, meaning that interfaces should be small and specific rather than large and general.
  - Dependency inversion principle: High-level modules should not depend on low-level modules, but both should depend on abstractions, meaning that the design should be based on interfaces rather than concrete implementations.
  - Dependency injection: The basic idea is that if an object depends upon having an instance of some other object then the dependency should be provided to it rather than the object creating or finding the dependency itself .
  - Acyclic dependencies principle: The dependency graph of packages or components should not contain any cycles, meaning that there should be no circular references or mutual dependencies.