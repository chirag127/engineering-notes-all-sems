# Candidate Key

- A candidate key is a minimal set of attributes that can uniquely identify each tuple in a relation.
- A relation can have more than one candidate key, but each candidate key must be irreducible, meaning that no attribute can be removed from it without losing the uniqueness property.
- A candidate key can be a single attribute or a combination of attributes, depending on the relation schema and the functional dependencies among the attributes.
- A candidate key can be used to define a primary key, which is a special candidate key that is chosen by the database designer to identify the tuples in a relation.
- A candidate key that is not chosen as the primary key is called an alternate key.
- A candidate key can also be used to define a foreign key, which is an attribute or a set of attributes that references a primary key or a candidate key of another relation.
- A candidate key can be derived from the relation schema and the set of functional dependencies by applying the closure test, the minimal cover test, or the canonical cover test. These tests are based on the concept of attribute closure, which is the set of all attributes that are functionally determined by a given set of attributes.