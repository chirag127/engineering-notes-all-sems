### Concepts of Super Key

A super key is a set of one or more attributes that, taken collectively, allow us to identify uniquely a tuple in the relation. In other words, a super key is a set of attributes that can be used to uniquely identify a row in a table.

- A super key may contain extraneous attributes, meaning attributes that are not necessary to uniquely identify a tuple.
- A candidate key is a minimal super key, meaning it is a super key without any extraneous attributes.
- A primary key is a candidate key chosen by the database designer to uniquely identify tuples in a relation.
- A relation may have more than one candidate key, but it can have only one primary key.
- A super key is a superset of a candidate key.
