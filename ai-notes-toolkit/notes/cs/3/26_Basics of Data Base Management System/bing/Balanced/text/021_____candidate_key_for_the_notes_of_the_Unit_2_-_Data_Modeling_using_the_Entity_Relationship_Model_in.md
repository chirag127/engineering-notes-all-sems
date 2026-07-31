### Candidate Key

- A candidate key is a set of attributes that can uniquely identify each tuple (row) in a relation (table) of a database  .
- A candidate key is also a minimal superkey, which means that it has no redundant attributes and removing any attribute from it would make it lose the uniqueness property .
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier of the relation .
- The other candidate keys that are not chosen as the primary key are called alternate keys or unique keys, and they can also enforce uniqueness constraints on the relation.
- To find the candidate keys of a relation, one can use the following steps:
  - Identify all the attributes that are unique by themselves, and mark them as candidate keys.
  - Identify all the attributes that are part of a functional dependency, where they determine the values of other attributes, and mark them as candidate keys.
  - Identify all the combinations of two or more attributes that are unique together, and mark them as candidate keys.
  - Eliminate any candidate key that is a proper subset of another candidate key, as it is not minimal.
  - Choose one of the remaining candidate keys as the primary key, and label the others as alternate keys.