### Keys for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a graphical and conceptual tool for data modeling using entities, attributes, and relationships.
- An entity is a real-world object or concept that can be identified and distinguished from others. Examples of entities are students, courses, books, etc.
- An attribute is a property or characteristic of an entity that describes some aspect of it. Examples of attributes are name, age, address, etc.
- A relationship is an association or connection between two or more entities that expresses some business rule or logic. Examples of relationships are enrolls, teaches, borrows, etc.
- An Entity Relationship Diagram (ERD) is a diagram that shows the entities, attributes, and relationships in a database using symbols and connectors.
- The symbols and connectors used in an ERD are:

  - A rectangle represents an entity. The name of the entity is written inside the rectangle.
  - An oval represents an attribute. The name of the attribute is written inside the oval. An attribute is connected to the entity it belongs to by a line.
  - A diamond represents a relationship. The name of the relationship is written inside the diamond. A relationship is connected to the entities it involves by a line.
  - A line represents a connection between an entity and an attribute or between an entity and a relationship. The line may have a cardinality symbol at one or both ends to indicate the number of occurrences of an entity in a relationship.
  - A cardinality symbol is a number or a letter that indicates the minimum and maximum number of occurrences of an entity in a relationship. The most common cardinality symbols are:

    - 1: one and only one
    - N: zero or more
    - M: one or more
    - C: zero or one

- An example of an ERD is:

![ERD example](https://www.visual-paradigm.com/servlet/editor-content/tutorials/erd/what-is-entity-relationship-diagram/erd-example.png)

- The ERD above shows the entities Student, Course, and Instructor, their attributes, and their relationships. The cardinality symbols indicate the following:

  - A student can enroll in zero or more courses, and a course can have zero or more students enrolled in it.
  - A course can have one and only one instructor, and an instructor can teach one or more courses.
  - A student can have zero or one advisor, and an instructor can advise zero or more students.

- The ER Model can be converted into a relational model, which is a more formal and logical representation of data using tables, columns, and keys.
- A table is a collection of rows and columns that store data about a specific entity or relationship. A table has a name and a set of columns.
- A column is a vertical component of a table that stores data of a specific type and has a name and a domain.
- A domain is a set of values that a column can take. A domain can be a predefined data type (such as integer, string, date, etc.) or a user-defined data type (such as enumeration, range, etc.).
- A key is a column or a set of columns that uniquely identifies a row in a table. A key can be a primary key, a foreign key, or a candidate key.
- A primary key is a key that uniquely identifies a row in a table and cannot be null. A table can have only one primary key, which is usually underlined in the table schema.
- A foreign key is a key that references a primary key of another table and establishes a relationship between the two tables. A foreign key can be null and can appear more than once in a table. A foreign key is usually marked with an asterisk (*) in the table schema.
- A candidate key is a key that can uniquely identify a row in a table but is not chosen as the primary key. A table can have more than one candidate key, which are usually marked with a hash (#) in the table schema.
- An example of a relational model is:

![Relational model example](https://www.cs.rpi.edu/~sibel/csci4380/fall2020/course_notes/er/er_to_relational.png)

- The relational model above shows the tables Student, Course, Instructor, Enrolls, and Advises, their columns, and their keys. The tables are derived from the