Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of integrity constraints for the notes of the unit 2 - relational data model and language in the subject of database management system.

# Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when the data is inserted or updated).
- Integrity constraints can be classified into four types: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

## Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- Domain constraints ensure that the data stored in the relation conforms to the intended meaning and semantics of the attributes.

## Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by declaring primary keys or candidate keys for the relations.
- Key constraints ensure that the data stored in the relation is free of duplication and ambiguity.

## Entity Integrity Constraints

- Entity integrity constraints specify that the primary key attributes of a relation must not have null values.
- Entity integrity constraints can be enforced by declaring primary keys as not null for the relations.
- Entity integrity constraints ensure that the data stored in the relation can be uniquely referenced and identified.

## Referential Integrity Constraints

- Referential integrity constraints specify the consistency and validity of the data across two or more relations that are related by foreign keys.
- Referential integrity constraints can be enforced by declaring foreign keys as references to the primary keys of the referenced relations, and by specifying the actions to be taken when the referenced data is modified or deleted (such as cascade, restrict, set null, or set default).
- Referential integrity constraints ensure that the data stored in the relation is consistent with the data stored in the referenced relations, and that the relationships among the data are maintained.