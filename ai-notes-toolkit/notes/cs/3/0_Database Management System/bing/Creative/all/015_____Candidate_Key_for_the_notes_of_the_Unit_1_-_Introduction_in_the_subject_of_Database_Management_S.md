# Candidate Key

- A candidate key is a set of attributes that can uniquely identify each tuple (row) in a relation (table) of a database  .
- A candidate key is also a minimal superkey, which means that it has no redundant attributes and removing any attribute from it would make it lose the uniqueness property .
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier of the relation .
- The other candidate keys that are not chosen as the primary key are called alternate keys or secondary keys.
- A candidate key can be a single attribute or a combination of attributes, depending on the data and the functional dependencies in the relation .
- A candidate key should satisfy the following properties:
  - Uniqueness: No two tuples in the relation should have the same values for the candidate key attributes.
  - Irreducibility: No subset of the candidate key attributes should have the uniqueness property.
  - Non-nullability: The candidate key attributes should not have null values in any tuple.