# Notation for ER diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols that can be used to draw an ER diagram, depending on the level of detail and the type of database. Some of the common notations and symbols are:

- **Entity**: An entity is a real-world object or concept that can be identified and stored in the database. It is represented by a rectangle with the entity name inside. For example, Student, Course, Department, etc.

- **Attribute**: An attribute is a property or characteristic of an entity that can be used to describe or identify it. It is represented by an oval with the attribute name inside, connected to the entity by a line. For example, Name, ID, Age, etc. There are different types of attributes, such as:

  - **Simple attribute**: An attribute that cannot be divided into smaller parts. For example, Name, Age, etc.
  - **Composite attribute**: An attribute that can be divided into smaller parts. For example, Address, which can be composed of Street, City, State, etc.
  - **Single-valued attribute**: An attribute that can have only one value for each entity. For example, ID, Name, etc.
  - **Multi-valued attribute**: An attribute that can have more than one value for each entity. For example, Phone, Email, etc. It is represented by a double oval.
  - **Derived attribute**: An attribute that can be derived or calculated from other attributes. For example, Age, which can be derived from Date of Birth. It is represented by a dashed oval.

- **Relationship**: A relationship is an association or link between two or more entities that share some common information or interact with each other. It is represented by a diamond with the relationship name inside, connected to the entities by lines. For example, Enrolls, Teaches, Belongs to, etc. There are different types of relationships, such as:

  - **One-to-one relationship**: A relationship where each entity in one entity set is associated with at most one entity in another entity set. For example, each student has one advisor, and each advisor advises one student. It is represented by a single line between the entities.
  - **One-to-many relationship**: A relationship where each entity in one entity set is associated with zero or more entities in another entity set, but each entity in the other entity set is associated with at most one entity in the first entity set. For example, each department has many courses, but each course belongs to one department. It is represented by a single line on the side of the one entity and a crow's foot on the side of the many entity.
  - **Many-to-many relationship**: A relationship where each entity in one entity set is associated with zero or more entities in another entity set, and each entity in the other entity set is also associated with zero or more entities in the first entity set. For example, each student can enroll in many courses, and each course can have many students. It is represented by a crow's foot on both sides of the entities.

- **Cardinality**: Cardinality is the number of instances of one entity that can or must be associated with each instance of another entity. It is represented by a number or a symbol on the line connecting the entities. For example, 1, N, M, etc. There are different types of cardinality, such as:

  - **Minimum cardinality**: The minimum number of instances of one entity that must be associated with each instance of another entity. It is represented by a small circle for zero or a small line for one on the line near the entity. For example, a student must enroll in at least one course, so the minimum cardinality is one on the side of the course entity.
  - **Maximum cardinality**: The maximum number of instances of one entity that can be associated with each instance of another entity. It is represented by a number or a crow's foot for many on the line near the entity. For example, a student can enroll in at most four courses, so the maximum cardinality is four on the side of the course entity.

- **Participation**: Participation is the degree to which each entity is involved in a relationship. It can be either total or partial. Total participation means that every entity in an entity set must participate in the relationship, while partial participation means that some entities in an entity set may not participate in the relationship. It is represented by a double line for total