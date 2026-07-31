# Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when data is inserted, updated, or deleted).
- Integrity constraints can be classified into four types: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

## Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- Domain constraints ensure that the data stored in a relation is of the correct type and format.

## Key Constraints

- Key constraints specify the uniqueness of tuples in a relation.
- Key constraints can be enforced by defining one or more attributes of a relation as the primary key or candidate keys.
- Primary key is a minimal set of attributes that uniquely identifies each tuple in a relation.
- Candidate keys are alternative sets of attributes that can also uniquely identify each tuple in a relation.
- Key constraints ensure that there are no duplicate tuples in a relation.

## Entity Integrity Constraints

- Entity integrity constraints ensure that the primary key of a relation does not contain null values.
- Entity integrity constraints can be enforced by declaring the primary key attributes as not null.
- Entity integrity constraints ensure that each tuple in a relation can be uniquely identified by its primary key.

## Referential Integrity Constraints

- Referential integrity constraints ensure that the foreign key values of a relation are consistent with the primary key values of the referenced relation.
- Referential integrity constraints can be enforced by declaring the foreign key attributes as references to the primary key attributes of another relation.
- Referential integrity constraints ensure that the relationships between relations are valid and consistent.