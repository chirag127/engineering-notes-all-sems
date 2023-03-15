### Keys Constraints

- A key is a set of one or more attributes that can uniquely identify a tuple in a relation.
- A key constraint is a rule that specifies that the values of a key must be distinct, i.e., no two tuples can have the same key value.
- A key can be either a candidate key or a primary key.
- A candidate key is a minimal set of attributes that can uniquely identify a tuple, i.e., no proper subset of the candidate key can serve as a key.
- A primary key is a candidate key that is chosen by the database designer to identify tuples in a relation.
- A relation can have more than one candidate key, but only one primary key.
- A primary key can be either a simple key or a composite key.
- A simple key is a key that consists of a single attribute.
- A composite key is a key that consists of two or more attributes.
- A foreign key is a set of attributes in a relation that references the primary key of another relation (or the same relation in case of recursive relationships).
- A foreign key constraint is a rule that specifies that the values of a foreign key must either match the values of an existing primary key in the referenced relation, or be null.
- A foreign key constraint enforces the referential integrity of the database, i.e., it ensures that there are no dangling references or orphan tuples.