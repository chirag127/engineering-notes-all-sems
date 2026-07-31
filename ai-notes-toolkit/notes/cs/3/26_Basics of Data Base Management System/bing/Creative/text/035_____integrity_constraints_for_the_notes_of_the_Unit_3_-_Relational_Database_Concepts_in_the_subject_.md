### Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of data in a relational database.
- Integrity constraints can be defined at the schema level (when the database is created) or at the instance level (when the data is inserted or updated).
- Integrity constraints can be classified into four types: domain constraints, key constraints, referential integrity constraints, and general constraints.

#### Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- Domain constraints ensure that the data stored in a relation is of the correct type and format.

#### Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by defining primary keys and candidate keys for the relations.
- Primary keys are the minimal set of attributes that can uniquely identify each tuple in a relation. There can be only one primary key for each relation.
- Candidate keys are the alternative sets of attributes that can also uniquely identify each tuple in a relation. There can be more than one candidate key for each relation.
- Key constraints ensure that the data stored in a relation is unique and non-redundant.

#### Referential Integrity Constraints

- Referential integrity constraints specify the relationships between tuples in different relations.
- Referential integrity constraints can be enforced by defining foreign keys and referential actions for the relations.
- Foreign keys are the attributes or combinations of attributes in a relation that refer to the primary key or a candidate key of another relation. The relation that contains the foreign key is called the referencing relation, and the relation that is referred to by the foreign key is called the referenced relation.
- Referential actions are the actions that are taken when the data in the referenced relation is inserted, updated, or deleted. The referential actions can be: cascade, restrict, set null, set default, or no action.
- Referential integrity constraints ensure that the data stored in a relation is consistent and coherent with the data in other relations.

#### General Constraints

- General constraints are the constraints that cannot be expressed by the other types of integrity constraints.
- General constraints can be enforced by defining triggers, assertions, or check clauses for the relations.
- Triggers are the procedures that are executed automatically when a certain event (such as insert, update, or delete) occurs on a relation.
- Assertions are the conditions that must hold true for the database at all times.
- Check clauses are the conditions that must hold true for each tuple in a relation.
- General constraints ensure that the data stored in a relation satisfies some specific business rules or logic.