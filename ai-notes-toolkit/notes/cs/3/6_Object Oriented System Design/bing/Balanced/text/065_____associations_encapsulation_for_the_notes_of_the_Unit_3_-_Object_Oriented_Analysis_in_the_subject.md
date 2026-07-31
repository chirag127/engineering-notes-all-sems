### Associations Encapsulation for the Notes of the Unit 3 - Object Oriented Analysis in the Subject of Object Oriented System Design

- Object Oriented Analysis (OOA) is the process of identifying software engineering requirements and developing software specifications in terms of a software system's object model, which consists of interacting objects.
- An object is an entity that has a state (attributes) and a behavior (operations) that are encapsulated within the object's boundary.
- Encapsulation is the concept of hiding the internal details of an object from the outside world, and only exposing the essential features and functionality that are relevant for other objects.
- Encapsulation helps to protect the data and methods of an object from unauthorized access, modification, or misuse, and also enables modularity, reusability, and maintainability of the software system.
- An association is a semantically weak relationship (a semantic dependency) between otherwise unrelated objects that have their own lifetime and no owner.
- An association represents a "using" relationship between objects, where one object uses another object to perform a certain task or function.
- An association can have a name, a direction, and a multiplicity, which specify the meaning, the directionality, and the number of objects involved in the relationship.
- An example of an association is a "drives" relationship between a person object and a car object, where the person object uses the car object to travel from one place to another.
- An aggregation is a special form of association that represents a "has-a" or "part-of" relationship between objects, where one object (the whole) contains or consists of another object (the part), but the part object can exist independently of the whole object.
- An aggregation implies a weaker relationship between the objects than a composition, as the lifetime of the part object is not dependent on the lifetime of the whole object.
- An example of an aggregation is a "contains" relationship between a library object and a book object, where the library object contains the book object, but the book object can exist outside the library object.
- A composition is a special form of aggregation that represents a "has-a" or "part-of" relationship between objects, where one object (the whole) contains or consists of another object (the part), and the part object cannot exist independently of the whole object.
- A composition implies a stronger relationship between the objects than an aggregation, as the lifetime of the part object is dependent on the lifetime of the whole object.
- An example of a composition is a "consists-of" relationship between a car object and a wheel object, where the car object consists of the wheel object, and the wheel object cannot exist without the car object.
- Associations, aggregations, and compositions are important concepts in OOA, as they help to model the relationships and dependencies between the objects in the software system, and also to define the scope and boundaries of the objects.