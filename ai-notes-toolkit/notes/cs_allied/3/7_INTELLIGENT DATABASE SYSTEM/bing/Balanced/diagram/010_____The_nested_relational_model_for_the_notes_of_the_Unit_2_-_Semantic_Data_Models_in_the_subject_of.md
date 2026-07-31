### The nested relational model

- The nested relational model is an extension of the relational model in which domains may be either atomic or relation-valued .
- This allows a complex object to be represented by a single tuple of a nested relation, which has a one-to-one correspondence between data items and objects.
- A nested relation can be seen as a relation of relations, where each tuple may contain one or more sub-relations as attribute values.
- A nested relation schema can be defined recursively as follows:

  - A nested relation schema is either an atomic type or a set of attribute-name/type pairs, where the type can be either atomic or a nested relation schema.
  - A nested relation schema can be denoted by R(A1:T1, A2:T2, ..., An:Tn), where R is the relation name, Ai are the attribute names, and Ti are the attribute types.
  - A nested relation schema can also be denoted by R(T1, T2, ..., Tn), where the attribute names are omitted and the attribute types are ordered.

- A nested relation instance can be defined recursively as follows:

  - A nested relation instance is either an atomic value or a set of tuples, where each tuple is a sequence of attribute values that conform to the corresponding attribute types in the nested relation schema.
  - A nested relation instance can be denoted by {t1, t2, ..., tm}, where ti are the tuples.
  - A nested relation instance can also be denoted by {v1, v2, ..., vm}, where vi are the atomic values.

- An example of a nested relation schema and instance is shown below:

  - Schema: Employee(Name, Address, Phone, Projects(SetOf(ProjectNo, Budget, Members(SetOf(EmpNo, Role)))))
  - Instance: {('Alice', '123 Main St', '555-1111', {('P1', 100000, {('E1', 'Manager'), ('E2', 'Analyst')})}), ('Bob', '456 Elm St', '555-2222', {('P2', 50000, {('E3', 'Programmer'), ('E4', 'Tester')})})}

- The nested relational model supports various operations to manipulate nested relations, such as projection, selection, join, union, aggregation, and unnesting .
- The nested relational model can be used to model complex objects, hierarchies, and networks in a relational database system  .
- The nested relational model has some advantages and disadvantages compared to the flat relational model :

  - Advantages:
    - It can represent complex objects and relationships more naturally and compactly.
    - It can avoid data redundancy and inconsistency by avoiding the need to flatten nested structures into multiple relations.
    - It can support more expressive queries and operations on nested structures.
  - Disadvantages:
    - It can introduce more complexity and overhead in the database design, implementation, and management.
    - It can require more sophisticated query processing and optimization techniques to handle nested queries and operations.
    - It can lose some of the desirable properties of the flat relational model, such as normal forms, functional dependencies, and relational algebra.