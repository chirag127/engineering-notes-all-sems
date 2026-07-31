# Keys for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a type of data model that uses graphical symbols and connectors to depict the entities and their relationships in a database.
- An entity is a real-world object or concept that can be identified and distinguished from others. Examples of entities are students, courses, books, etc.
- A relationship is an association or link between two or more entities. Examples of relationships are enrolls, teaches, borrows, etc.
- An attribute is a property or characteristic of an entity or a relationship. Examples of attributes are name, age, grade, etc.
- An ER diagram is a graphical representation of an ER model, using the following symbols:

  - Rectangles for entities
  - Diamonds for relationships
  - Ovals for attributes
  - Lines for connections
  - Cardinality symbols for indicating the number of occurrences of an entity in a relationship

- An example of an ER diagram is shown below:

![ER diagram example](https://www.cs.rpi.edu/~sibel/csci4380/fall2020/course_notes/er_files/er1.png)

- The ER model can be used to design and normalize a database, by following these steps:

  - Identify the entities and their attributes
  - Identify the relationships and their attributes
  - Draw the ER diagram using the symbols and conventions
  - Assign primary keys and foreign keys to the entities and relationships
  - Convert the ER diagram into a relational schema
  - Apply the normalization rules to the relational schema

- The ER model has some limitations, such as:

  - It does not capture the dynamic behavior or operations of the entities and relationships
  - It does not support some complex data types, such as arrays, lists, or multimedia
  - It does not handle the inheritance or generalization of entities
  - It does not specify the physical implementation or storage details of the database

- To overcome these limitations, some extensions or variations of the ER model have been proposed, such as:

  - Enhanced ER model, which introduces the concepts of subclasses, superclasses, and inheritance
  - Object-relational model, which integrates the features of object-oriented and relational models
  - Semantic data model, which captures the meaning and context of the data
  - Conceptual data model, which focuses on the high-level and abstract view of the data