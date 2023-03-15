### Keys for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a graphical and conceptual tool for data modeling using entities, attributes, and relationships.
- An entity is a real-world object or concept that can be identified and distinguished from others. Examples of entities are students, courses, employees, products, etc.
- An attribute is a property or characteristic of an entity that describes some aspect of it. Examples of attributes are name, age, address, salary, etc.
- A relationship is an association or connection between two or more entities that expresses some business rule or logic. Examples of relationships are enrolls, teaches, works for, buys, etc.
- An Entity Relationship Diagram (ERD) is a diagram that shows the entities, attributes, and relationships in a database using symbols and connectors.
- The symbols and connectors used in an ERD are:

  - A rectangle represents an entity. The name of the entity is written inside the rectangle.
  - An oval represents an attribute. The name of the attribute is written inside the oval. An attribute is connected to the entity it belongs to by a line.
  - A diamond represents a relationship. The name of the relationship is written inside the diamond. A relationship is connected to the entities it involves by a line.
  - A line represents a connection between an entity and an attribute, or between an entity and a relationship. The line can have different cardinalities and participation constraints to indicate the degree and optionality of the connection.
  - A cardinality is a number or a symbol that shows how many instances of one entity can be associated with one instance of another entity in a relationship. The cardinalities are:

    - One-to-one (1:1): One instance of entity A can be associated with at most one instance of entity B, and vice versa. A single line is used to represent this cardinality.
    - One-to-many (1:N): One instance of entity A can be associated with zero or more instances of entity B, but one instance of entity B can be associated with at most one instance of entity A. A single line with a crow's foot at the end is used to represent this cardinality.
    - Many-to-one (N:1): One instance of entity B can be associated with zero or more instances of entity A, but one instance of entity A can be associated with at most one instance of entity B. A single line with a crow's foot at the start is used to represent this cardinality.
    - Many-to-many (N:M): One instance of entity A can be associated with zero or more instances of entity B, and vice versa. A double line with a crow's foot at both ends is used to represent this cardinality.

  - A participation constraint is a symbol that shows whether the participation of an entity in a relationship is mandatory or optional. The participation constraints are:

    - Total participation: Every instance of an entity must participate in the relationship. A double line is used to represent this constraint.
    - Partial participation: Some instances of an entity may or may not participate in the relationship. A single line is used to represent this constraint.

- An example of an ERD is:

![ERD example](https://www.databasestar.com/wp-content/uploads/2017/02/erd-example.png)

- The ERD above shows the entities Student, Course, and Instructor, and their attributes and relationships. The relationship Enrolls has a many-to-many cardinality between Student and Course, and a total participation of Student and a partial participation of Course. The relationship Teaches has a one-to-many cardinality between Instructor and Course, and a total participation of both entities. The attribute ID is underlined for each entity, which means it is a key attribute that uniquely identifies each instance of the entity.