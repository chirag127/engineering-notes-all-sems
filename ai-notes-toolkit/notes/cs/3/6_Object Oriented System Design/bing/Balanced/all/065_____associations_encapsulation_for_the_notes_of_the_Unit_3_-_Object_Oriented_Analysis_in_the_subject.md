# Associations Encapsulation for the Notes of the Unit 3 - Object Oriented Analysis in the Subject of Object Oriented System Design

- Object Oriented Analysis (OOA) is the process of identifying software engineering requirements and developing software specifications in terms of a software system's object model, which consists of interacting objects.
- An object is an entity that has a state (attributes) and a behavior (operations) that define its identity and role in the system.
- A class is a blueprint or template that defines the common attributes and operations of a group of objects that belong to the same category.
- Encapsulation is a fundamental concept in OOA that involves bundling data and the methods that operate on that data within a single unit, known as a class.
- Encapsulation helps to protect the data and methods from outside interference, as it restricts direct access to them. It also promotes modularity, reusability, and maintainability of the code.
- Encapsulation separates the contractual interface of an abstraction and its implementation. The interface defines the services that an object provides to other objects, while the implementation defines how those services are performed.
- Associations are semantically weak relationships between otherwise unrelated objects that indicate how they use each other.
- Associations can have different types, such as aggregation, composition, inheritance, and dependency.
- Aggregation is a type of association that represents a "part-of" or "has-a" relationship between a whole and its parts. The parts can exist independently of the whole, and the whole does not own the parts.
- Composition is a type of association that represents a "part-of" or "has-a" relationship between a whole and its parts. The parts cannot exist independently of the whole, and the whole owns the parts. The lifetime of the parts is tied to the lifetime of the whole.
- Inheritance is a type of association that represents an "is-a" or "kind-of" relationship between a superclass and its subclasses. The subclasses inherit the attributes and operations of the superclass, and can also add or override them.
- Dependency is a type of association that represents a "uses-a" or "depends-on" relationship between two or more objects. The dependent object relies on the independent object for some functionality, but does not own or contain it.
- Associations can have different properties, such as multiplicity, directionality, and role.
- Multiplicity specifies how many instances of one class can be associated with one instance of another class. It can be expressed as a single number, a range, or a star (*) for unlimited.
- Directionality specifies the direction of the association, which can be unidirectional or bidirectional. Unidirectional means that only one class can access the other, while bidirectional means that both classes can access each other.
- Role specifies the name or function of a class in an association, which can help to clarify the meaning and purpose of the relationship.
- Associations can be represented graphically using Unified Modeling Language (UML) diagrams, which are a standard notation for modeling software systems. UML diagrams use different symbols and lines to depict the classes, objects, and associations in a system.