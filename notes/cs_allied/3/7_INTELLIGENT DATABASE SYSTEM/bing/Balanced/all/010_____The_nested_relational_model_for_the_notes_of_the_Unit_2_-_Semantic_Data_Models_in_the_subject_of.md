# The nested relational model

- The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued .
- This allows a complex object to be represented by a single tuple of a nested relation, which has a one-to-one correspondence between data items and objects.
- A nested relation can be seen as a relation of relations, where each tuple may contain one or more sub-relations as attribute values.
- A nested relation can be flattened into a conventional relation by applying a join operation on the sub-relations.
- A nested relation can also be constructed from a conventional relation by applying a group operation, which partitions the tuples into sub-relations based on some grouping attributes.
- The nested relational model can support more complex data structures and queries than the standard relational model, such as recursive queries, aggregation, and inheritance .
- The nested relational model can also be seen as a special case of the object-relational model, which allows more general types of attributes and methods .