# Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of data in a relational database.
- Integrity constraints can be defined at the schema level (when the database is created or modified) or at the instance level (when data is inserted, updated, or deleted).
- Integrity constraints can be classified into four types: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

## Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for each attribute.
- Domain constraints ensure that the data stored in a relation conforms to the intended meaning and semantics of the attribute.

## Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by defining primary keys, candidate keys, or alternate keys for each relation.
- Key constraints ensure that there are no duplicate tuples in a relation and that each tuple can be uniquely referenced.

## Entity Integrity Constraints

- Entity integrity constraints ensure that the primary key of a relation does not contain null values.
- Entity integrity constraints can be enforced by declaring the primary key as not null or by using a default value for the primary key.
- Entity integrity constraints ensure that each tuple in a relation represents a distinct entity and that the primary key can be used to identify the entity.

## Referential Integrity Constraints

- Referential integrity constraints ensure that the foreign key of a relation either matches the primary key of another relation or is null.
- Referential integrity constraints can be enforced by declaring the foreign key as a foreign key constraint and specifying the referenced relation and attribute(s).
- Referential integrity constraints ensure that the relationships between entities are consistent and that the foreign key can be used to refer to the related entity.