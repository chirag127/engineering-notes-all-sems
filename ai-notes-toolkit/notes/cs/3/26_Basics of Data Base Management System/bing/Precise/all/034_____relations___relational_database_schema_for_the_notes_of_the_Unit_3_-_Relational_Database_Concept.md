# Relations & Relational Database Schema

## Unit 3 - Relational Database Concepts

### Basics of Data Base Management System

1. **Relations:** A relation is a table with columns and rows. The columns represent the attributes of the relation and the rows represent the tuples or records.
2. **Relational Database Schema:** A relational database schema is a collection of relation schemas, where each relation schema represents the structure of a relation in the database.
3. **Relation Schema:** A relation schema is defined by its name and a set of attributes. Each attribute has a name and a data type.
4. **Keys:** A key is a set of attributes that uniquely identifies a tuple in a relation. A relation can have multiple keys, but one of them is designated as the primary key.
5. **Foreign Keys:** A foreign key is a set of attributes in a relation that refers to the primary key of another relation. The relation that contains the foreign key is called the referencing relation and the relation that is referred to by the foreign key is called the referenced relation.
6. **Referential Integrity:** Referential integrity is a property of a relational database that ensures that the relationships between relations are maintained. It is enforced by the use of foreign keys and the rules for inserting, updating, and deleting tuples in the referencing and referenced relations.
7. **Normalization:** Normalization is the process of organizing the attributes and relations of a relational database to minimize data redundancy and dependency. It involves decomposing a relation into multiple relations with fewer attributes and establishing relationships between them using foreign keys.