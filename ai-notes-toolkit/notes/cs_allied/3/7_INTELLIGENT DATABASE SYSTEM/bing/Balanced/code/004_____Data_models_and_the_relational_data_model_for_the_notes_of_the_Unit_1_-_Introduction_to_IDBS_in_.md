### Data models and the relational data model

- A data model is a way of representing the structure, relationships, and constraints of data in a database system.
- A data model can be conceptual, logical, or physical, depending on the level of abstraction and detail.
- A conceptual data model describes the entities and relationships in the domain of interest, without specifying how they are stored or implemented.
- A logical data model describes the structure and constraints of data in terms of tables, columns, keys, and integrity rules, without specifying the physical implementation details.
- A physical data model describes the physical layout and organization of data in terms of files, records, indexes, and storage devices.
- The relational data model is the most widely used logical data model for database systems.
- The relational data model is based on the concept of a relation, which is a set of tuples (or rows) that share the same attributes (or columns).
- A relation can be represented as a table, where each row corresponds to a tuple and each column corresponds to an attribute.
- A relation has a schema, which defines the name, type, and domain of each attribute, and an instance, which is the current set of tuples in the relation.
- A relation can have one or more keys, which are subsets of attributes that uniquely identify each tuple in the relation.
- A primary key is a key that is chosen to be the main identifier of tuples in a relation.
- A foreign key is a key that references the primary key of another relation, to establish a relationship between the two relations.
- A relational database is a collection of relations that conform to a set of integrity constraints, such as entity integrity, referential integrity, and domain integrity.
- Entity integrity states that no tuple in a relation can have a null value in its primary key attribute(s).
- Referential integrity states that for every tuple in a relation that has a foreign key value, there must exist a tuple in the referenced relation that has the same value in its primary key attribute(s).
- Domain integrity states that every value in a relation must belong to the domain of its corresponding attribute.
- A relational database can be manipulated using a relational algebra, which is a set of operators that can perform operations on relations, such as selection, projection, join, union, intersection, and difference.
- A relational database can also be queried using a declarative language, such as SQL, which allows users to specify what data they want to retrieve, without specifying how to retrieve it.