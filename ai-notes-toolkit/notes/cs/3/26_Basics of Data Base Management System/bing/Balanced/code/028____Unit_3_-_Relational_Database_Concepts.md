```
## Unit 3 - Relational Database Concepts

- A relational database is a collection of data organized into tables, where each table has a fixed number of columns (attributes) and a variable number of rows (records or tuples).
- A relational database follows a set of rules, called the relational model, that ensure the data is consistent, accurate, and accessible.
- The relational model was proposed by Edgar F. Codd in 1970, and is based on the concept of mathematical relations and set theory.
- The main components of the relational model are:

  - Relation: A table with a unique name, where each row represents a fact or an entity, and each column represents an attribute or a property of the entity. A relation can also be called a relation schema or a relation variable.
  - Attribute: A column in a table, where each attribute has a unique name and a domain (a set of possible values). An attribute can also be called a relation attribute or a relation column.
  - Tuple: A row in a table, where each tuple contains a value for each attribute in the relation. A tuple can also be called a relation tuple or a relation record.
  - Degree: The number of attributes in a relation.
  - Cardinality: The number of tuples in a relation.
  - Domain: The set of possible values for an attribute.
  - Primary key: A set of one or more attributes that uniquely identify each tuple in a relation. A primary key can also be called a relation key or a candidate key.
  - Foreign key: A set of one or more attributes in a relation that refer to the primary key of another relation. A foreign key can also be called a relation foreign key or a referential attribute.
  - Referential integrity: A rule that ensures that the values of a foreign key in a relation match the values of the primary key in the referenced relation, or are null.
  - Null: A special value that indicates the absence of a value for an attribute. Null is not the same as zero or blank.
  - Relational algebra: A set of operators that can be applied to one or more relations to produce a new relation. Relational algebra operators include selection, projection, join, union, intersection, difference, and division.
  - Relational calculus: A declarative language that can be used to specify queries on relations. Relational calculus expressions consist of variables, constants, logical operators, and quantifiers.
  - SQL: A standard language for defining, manipulating, and querying data in relational databases. SQL stands for Structured Query Language, and is based on relational algebra and relational calculus.
  - Normalization: A process of decomposing a relation into smaller relations that have less redundancy and anomalies. Normalization is based on the concept of functional dependencies and normal forms.
  - Functional dependency: A constraint that specifies that the value of one or more attributes in a relation depends on the value of another attribute or a set of attributes in the same relation.
  - Normal form: A condition that a relation satisfies if it has a certain level of normalization. The most common normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF).
```