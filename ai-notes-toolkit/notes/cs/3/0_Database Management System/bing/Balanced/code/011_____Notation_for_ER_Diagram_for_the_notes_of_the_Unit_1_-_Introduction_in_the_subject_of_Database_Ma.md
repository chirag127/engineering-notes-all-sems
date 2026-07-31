### Notation for ER Diagram

An ER diagram is a graphical representation of the entities, attributes and relationships in a database. It helps to explain the logical structure and design of the database. There are different notations and symbols used to draw an ER diagram, depending on the modeling methodology and the level of abstraction. Some of the common notations and symbols are:

- **Entity**: An entity is a real-world object or concept that can be identified and stored in the database. It is represented by a rectangle with the entity name inside. For example, Student, Course, Department, etc.

- **Attribute**: An attribute is a property or characteristic of an entity that can have a value. It is represented by an oval with the attribute name inside, connected to the entity by a line. For example, Name, Age, ID, etc. There are different types of attributes, such as:

  - **Simple attribute**: An attribute that cannot be divided into sub-attributes. For example, Name, Age, etc.
  - **Composite attribute**: An attribute that can be divided into sub-attributes. For example, Address, which can have Street, City, State, etc.
  - **Single-valued attribute**: An attribute that can have only one value for each entity. For example, ID, Gender, etc.
  - **Multi-valued attribute**: An attribute that can have more than one value for each entity. For example, Phone, Email, etc. It is represented by a double oval.
  - **Derived attribute**: An attribute that can be derived from other attributes or entities. For example, Age, which can be calculated from Date of Birth. It is represented by a dashed oval.

- **Relationship**: A relationship is an association or link between two or more entities. It is represented by a diamond with the relationship name inside, connected to the entities by lines. For example, Enrolls, Teaches, Belongs to, etc. There are different types of relationships, such as:

  - **One-to-one relationship**: A relationship where each entity in one entity set is associated with at most one entity in another entity set. For example, each student has one advisor, and each advisor advises one student. It is represented by a single line between the entities.
  - **One-to-many relationship**: A relationship where each entity in one entity set is associated with zero or more entities in another entity set, but each entity in the other entity set is associated with at most one entity in the first entity set. For example, each department has many courses, but each course belongs to one department. It is represented by a single line on the side of the one entity and a crow's foot on the side of the many entity.
  - **Many-to-many relationship**: A relationship where each entity in one entity set is associated with zero or more entities in another entity set, and each entity in the other entity set is associated with zero or more entities in the first entity set. For example, each student enrolls in many courses, and each course has many students enrolled. It is represented by a crow's foot on both sides of the entities.

- **Cardinality**: Cardinality is the number of instances of one entity that can or must be associated with each instance of another entity. It is represented by a number or a symbol on the line connecting the entities. For example, 1, N, M, etc. There are different types of cardinality, such as:

  - **Minimum cardinality**: The minimum number of instances of one entity that must be associated with each instance of another entity. It is also known as **participation** or **existence dependency**. For example, each student must enroll in at least one course, and each course must have at least one student enrolled. It is represented by a double line or a solid circle on the line.
  - **Maximum cardinality**: The maximum number of instances of one entity that can be associated with each instance of another entity. It is also known as **degree** or **multiplicity**. For example, each student can enroll in at most four courses, and each course can have at most 30 students enrolled. It is represented by a number or a crow's foot on the line.

- **Key**: A key is an attribute or a set of attributes that can uniquely identify an entity in the database. It is represented by an underline under the attribute name. For example, ID, SSN, etc. There are different types of keys, such as:

  - **Primary key**: A key that can uniquely identify each entity in an entity set. It is also known as