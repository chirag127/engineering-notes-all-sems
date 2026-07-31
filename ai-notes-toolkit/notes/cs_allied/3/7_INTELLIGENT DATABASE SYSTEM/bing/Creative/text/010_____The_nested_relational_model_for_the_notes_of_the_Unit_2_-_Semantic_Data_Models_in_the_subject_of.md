### The nested relational model

- The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued .
- This allows a complex object to be represented by a single tuple of a nested relation, which has a one-to-one correspondence between data items and objects.
- A nested relation can be seen as a relation of relations, where each tuple may contain one or more sub-relations as attribute values.
- A nested relation schema can be defined recursively as follows:
  - An atomic type is a nested relation schema.
  - If R1, R2, ..., Rn are nested relation schemas, then (R1, R2, ..., Rn) is a nested relation schema.
  - If R is a nested relation schema, then {R} is a nested relation schema.
- A nested relation instance can be defined recursively as follows:
  - An atomic value is a nested relation instance.
  - If t1, t2, ..., tn are nested relation instances, then (t1, t2, ..., tn) is a nested relation instance.
  - If r is a set of nested relation instances, then {r} is a nested relation instance.
- A nested relation can be flattened into a conventional relation by applying a join operation on the sub-relations.
- A nested relation can be reconstructed from a flattened relation by applying a group operation on the atomic attributes.
- The nested relational model can support complex data types, such as sets, lists, arrays, and records, as well as object identity and inheritance .
- The nested relational model can also support hierarchical data structures, such as trees or graphs, by using the nested set model.
- The nested relational model can be implemented using object-relational database systems, which extend the relational model with object-oriented features .