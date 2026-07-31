# Unit 2 - Relational Data Model and Language

- Relational Data Model and Language is a way of representing and manipulating data in a relational database.
- A relational database is a type of database that stores data in the form of relations (tables), where each row represents a tuple (record) and each column represents an attribute (field).
- A relational database may use SQL (Structured Query Language) as its language, but SQL is not the same as the relational model. SQL is a set of commands and syntax that can be used to query, manipulate, and define data in a relational database.
- The relational model has some basic concepts and principles, such as:

  - Entity: An entity is a real-world object or concept that can be identified and distinguished from others. For example, a student, a course, or a book are entities.
  - Attribute: An attribute is a property or characteristic of an entity that describes some aspect of it. For example, name, age, or title are attributes of a student, a course, or a book, respectively.
  - Domain: A domain is a set of possible values for an attribute. For example, the domain of the name attribute of a student entity could be a set of strings, such as "Alice", "Bob", or "Charlie".
  - Relation: A relation is a set of tuples that share the same attributes. A relation can be represented as a table, where each row is a tuple and each column is an attribute. For example, a relation called Student could have the attributes name, age, and major, and store the tuples ("Alice", 19, "Math"), ("Bob", 20, "CS"), and ("Charlie", 18, "Biology").
  - Key: A key is an attribute or a set of attributes that can uniquely identify a tuple in a relation. For example, the name attribute could be a key for the Student relation, as no two students have the same name. A key can also be a combination of attributes, such as name and age, if they are sufficient to distinguish a tuple. A key that consists of a single attribute is called a simple key, and a key that consists of more than one attribute is called a composite key.
  - Primary Key: A primary key is a key that is chosen to be the main identifier of a tuple in a relation. A relation can have only one primary key, and it cannot have null values. For example, the name attribute could be the primary key for the Student relation. A primary key is usually underlined in a table to indicate its importance.
  - Foreign Key: A foreign key is an attribute or a set of attributes in a relation that refers to the primary key of another relation. A foreign key establishes a link or a relationship between two relations. For example, the major attribute in the Student relation could be a foreign key that references the name attribute of another relation called Department, which stores the information about different academic departments. A foreign key is usually italicized in a table to indicate its reference.
  - Schema: A schema is a description or a definition of the structure and constraints of a relation. A schema specifies the name, attributes, domains, keys, and foreign keys of a relation. For example, the schema of the Student relation could be written as:

    Student(name, age, major)

    name is the primary key

    major references Department.name

  - Instance: An instance is a snapshot or a state of a relation at a given point in time. An instance contains the actual data or values that are stored in a relation. For example, the instance of the Student relation could be the table that shows the tuples ("Alice", 19, "Math"), ("Bob", 20, "CS"), and ("Charlie", 18, "Biology").
  - Degree: The degree of a relation is the number of attributes it has. For example, the degree of the Student relation is 3, as it has three attributes: name, age, and major.
  - Cardinality: The cardinality of a relation is the number of tuples it has. For example, the cardinality of the Student relation is 3, as it has three tuples: ("Alice", 19, "Math"), ("Bob", 20, "CS"), and ("Charlie", 18, "Biology").
  - Relational Algebra: Relational algebra is a set of operations that can be applied to relations to manipulate and query data. Relational algebra operations can be classified into two categories: unary operations and binary operations. Unary operations take one relation as input and produce one relation