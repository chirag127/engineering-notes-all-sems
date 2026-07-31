# Notation for ER Diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols used to draw an ER diagram, depending on the modeling methodology and the level of abstraction. Some of the common notations and symbols are:

- **Entities**: Entities are the basic units of data in a database. They are represented by rectangles with the entity name inside. For example, Student, Course, Department, etc. Entities can have different types, such as strong, weak, associative, etc.

- **Attributes**: Attributes are the properties or characteristics of an entity. They are represented by ovals with the attribute name inside, connected to the entity by a line. For example, Name, ID, Age, etc. Attributes can have different types, such as simple, composite, derived, multivalued, etc.

- **Relationships**: Relationships are the associations or interactions between entities. They are represented by diamonds with the relationship name inside, connected to the entities by lines. For example, Enrolls, Teaches, Belongs to, etc. Relationships can have different types, such as one-to-one, one-to-many, many-to-many, etc.

- **Cardinality and Participation**: Cardinality and participation are the constraints that specify the number and optionality of occurrences of entities in a relationship. They are represented by symbols or numbers on the lines connecting the entities and the relationship. For example, 1, N, M, 0, etc. There are different notations for cardinality and participation, such as arrow, crow's foot, Chen, etc.

- **Keys**: Keys are the attributes that uniquely identify an entity or a relationship. They are represented by underlining the attribute name or by adding a key symbol next to it. For example, ID, SSN, etc. Keys can have different types, such as primary, foreign, candidate, etc.

- **Generalization and Specialization**: Generalization and specialization are the concepts of inheritance and subtyping in ER diagrams. They are represented by a triangle with the word "is a" inside, connected to the parent entity and the child entities by lines. For example, Employee is a Person, Manager is an Employee, etc.

- **Aggregation and Composition**: Aggregation and composition are the concepts of grouping and part-whole relationships in ER diagrams. They are represented by a circle with the word "has" inside, connected to the whole entity and the part entities by lines. For example, Department has Employees, Course has Modules, etc.

Here is an example of an ER diagram using the arrow notation:

![ER diagram example](https://www.guru99.com/images/1/092118_0610_ERDiagramTut1.png)