### Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when data is inserted, updated, or deleted).
- Integrity constraints can be classified into four categories: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

#### Domain Constraints
- Domain constraints specify the set of permissible values for an attribute or a column of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for each attribute or column.
- Domain constraints ensure that the data stored in a relation conforms to the expected domain of values.

#### Key Constraints
- Key constraints specify the attributes or columns that uniquely identify a tuple or a row of a relation.
- Key constraints can be enforced by defining primary keys, candidate keys, or alternate keys for each relation.
- Key constraints ensure that the data stored in a relation is unique and non-redundant.

#### Entity Integrity Constraints
- Entity integrity constraints specify that the primary key of a relation cannot have null values.
- Entity integrity constraints can be enforced by declaring the primary key as not null for each relation.
- Entity integrity constraints ensure that the data stored in a relation can be uniquely identified and referenced.

#### Referential Integrity Constraints
- Referential integrity constraints specify the consistency between two relations that are related by a foreign key.
- Referential integrity constraints can be enforced by declaring the foreign key as a reference to the primary key of another relation, and specifying the actions to be taken when the referenced data is modified or deleted (such as cascade, restrict, set null, or set default).
- Referential integrity constraints ensure that the data stored in a relation is consistent with the data stored in another relation.