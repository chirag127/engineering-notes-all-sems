# The nested relational model

The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued. This allows a complex object to be represented by a single tuple of a nested relation -- one-to-one correspondence between data items and objects.

Some features of the nested relational model are:

- It supports nested relations, which are relations that have attributes of type relation. This enables the representation of complex objects and relationships in a single relation.
- It allows non-first normal form (NFNF) relations, which are relations that have attributes with non-atomic domains. This enables the representation of multi-valued and composite attributes.
- It provides operators for manipulating nested relations, such as unnest, nest, and join. These operators can be used to flatten, group, or combine nested relations.
- It preserves the advantages of the relational model, such as declarative query language, data independence, and integrity constraints.

An example of a nested relation is:

| Student | Courses |
| ------- | ------- |
| Alice   | { (CS101, A), (CS102, B) } |
| Bob     | { (CS101, C), (CS103, A) } |
| Carol   | { (CS102, A), (CS103, B) } |

In this relation, the attribute Courses is a relation-valued attribute, which contains the course code and grade of each student. This relation is in NFNF, since the domain of Courses is not atomic. To convert this relation to first normal form (1NF), we would need to create a separate relation for Courses and use a foreign key to link it to Student. However, this would lose the information about the grouping of courses for each student. The nested relation model allows us to keep this information in a single relation.