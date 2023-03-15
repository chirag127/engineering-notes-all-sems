### Candidate Key

A candidate key is a minimal set of attributes that can uniquely identify a tuple in a relation. In other words, a candidate key is a combination of attributes that can be uniquely used to identify a database record without any extraneous data.

Here are some important points to remember about candidate keys:

1. A relation can have more than one candidate key.
2. Each non-prime attribute of the relation must be functionally dependent on every candidate key of the relation.
3. The candidate key can be simple (having only one attribute) or composite (having more than one attribute).
4. A candidate key can never have null values.
5. A candidate key is a superkey, meaning that it is a set of attributes that can uniquely identify a tuple, but it is minimal, meaning that no proper subset of the candidate key is a superkey.

In the process of designing a database, it is important to identify all the candidate keys of a relation, so that one of them can be selected as the primary key. The primary key is then used to uniquely identify each tuple in the relation and to establish relationships with other relations in the database.