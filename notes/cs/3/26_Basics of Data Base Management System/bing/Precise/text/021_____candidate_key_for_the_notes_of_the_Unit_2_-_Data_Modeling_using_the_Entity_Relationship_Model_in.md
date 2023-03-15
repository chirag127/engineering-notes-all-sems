### Candidate Key

- A candidate key is a minimal set of attributes that can uniquely identify a tuple in a relation.
- In other words, a candidate key is a combination of attributes that can be uniquely used to identify a database record without any extraneous data.
- Each relation must have at least one candidate key, but can have several.
- A candidate key can consist of a single attribute or multiple attributes.
- The candidate key must be chosen such that its attribute values are never, or very rarely, changed.
- For example, in a relation containing student data, the student ID would be a good candidate key, as it is unique to each student and does not change.
- A candidate key is also known as a primary key.
- A relation can have more than one candidate key, but only one can be designated as the primary key.
- The primary key is used to enforce entity integrity and is used as a reference for foreign keys in other relations.
- A candidate key that is not chosen as the primary key is known as an alternate key.
- It is important to choose the candidate key carefully, as it will be used to enforce referential integrity and ensure the accuracy of the data in the relation.