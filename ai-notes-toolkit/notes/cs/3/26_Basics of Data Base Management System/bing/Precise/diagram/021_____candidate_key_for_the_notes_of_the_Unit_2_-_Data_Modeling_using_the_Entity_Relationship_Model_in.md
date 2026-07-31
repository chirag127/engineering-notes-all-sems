### Candidate Key

A candidate key is a minimal set of attributes that can uniquely identify a tuple (row) in a relation (table) of a database. In other words, a candidate key is a combination of attributes that can be uniquely used to identify a database record without any extraneous data.

Here are some key points to remember about candidate keys:

- A relation (table) can have more than one candidate key.
- Each non-prime attribute of the relation (table) must be functionally dependent on every candidate key of the relation.
- The candidate key can be simple (having only one attribute) or composite (having more than one attribute).
- A candidate key can never have null values.
- A candidate key must always be chosen in such a way that its attribute values are never, or very rarely, changed.
- Out of all the candidate keys, one can be selected as the primary key.
