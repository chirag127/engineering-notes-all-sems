### Candidate Key
- A candidate key is a minimal set of attributes that can uniquely identify a tuple (row) in a relation (table) of a database.
- A relation can have more than one candidate key.
- Each candidate key must satisfy two properties: uniqueness and minimality.
- Uniqueness means that no two distinct tuples can have the same values for the candidate key attributes.
- Minimality means that no proper subset of the candidate key attributes is a candidate key.
- One of the candidate keys is chosen as the primary key, which is used to uniquely identify tuples in the relation and to establish relationships with other relations.
- The remaining candidate keys are called alternate keys.
- Candidate keys are important in the process of database normalization, as they help to identify functional dependencies and to eliminate redundancy in the data.