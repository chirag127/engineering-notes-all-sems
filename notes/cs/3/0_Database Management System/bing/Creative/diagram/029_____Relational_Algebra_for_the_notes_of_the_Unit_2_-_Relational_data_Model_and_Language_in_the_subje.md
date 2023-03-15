### Relational Algebra

Relational algebra is a theory that uses algebraic structures for modeling data, and defining queries on it with a well founded semantics. It is a procedural query language where the user tells the system to carry out a set of operations to obtain the desired results. Relational algebra provides a theoretical foundation for relational databases, particularly query languages for such databases, chief among which is SQL.

The basic elements of relational algebra are:

- Relations: A relation is a set of tuples or records that represent a table in a database. Each tuple consists of a set of attributes or columns that describe the entity. A relation has a name and a schema that defines the name and type of each attribute. For example, a relation STUDENT with attributes Name, RollNo, and Marks can be represented as:

| Name | RollNo | Marks |
|------|--------|-------|
| Alice | 101 | 85 |
| Bob | 102 | 90 |
| Charlie | 103 | 80 |

- Operators: An operator is a symbol or a function that takes one or more relations as input and produces another relation as output. Operators are designed to do the most common things that we need to do with relations in a database. Some of the basic operators are:

  - SELECT (σ): The SELECT operation is used for selecting a subset of the tuples according to a given selection condition. For example, σ(Marks > 80)(STUDENT) will return the tuples where Marks is greater than 80.

  - PROJECT (π): The PROJECT operation is used for selecting a subset of the attributes of a relation and discarding the rest. For example, π(Name, Marks)(STUDENT) will return the tuples with only Name and Marks attributes.

  - UNION (∪): The UNION operation is used for combining two relations that have the same schema and eliminating any duplicate tuples. For example, if we have another relation STUDENT2 with the same schema as STUDENT, then STUDENT ∪ STUDENT2 will return the tuples that are in either STUDENT or STUDENT2 or both.

  - INTERSECTION (∩): The INTERSECTION operation is used for finding the common tuples between two relations that have the same schema. For example, STUDENT ∩ STUDENT2 will return the tuples that are in both STUDENT and STUDENT2.

  - DIFFERENCE (-): The DIFFERENCE operation is used for finding the tuples that are in one relation but not in another relation that have the same schema. For example, STUDENT - STUDENT2 will return the tuples that are in STUDENT but not in STUDENT2.

  - CARTESIAN PRODUCT (×): The CARTESIAN PRODUCT operation is used for combining every tuple of one relation with every tuple of another relation. The result is a relation with the schema that is the concatenation of the schemas of the input relations. For example, STUDENT × STUDENT2 will return a relation with attributes Name, RollNo, Marks, Name2, RollNo2, Marks2, where each tuple is a combination of a tuple from STUDENT and a tuple from STUDENT2.

  - JOIN (⋈): The JOIN operation is used for combining tuples from two relations that satisfy a join condition. The result is a relation with the schema that is the union of the schemas of the input relations, and the tuples that satisfy the join condition. For example, STUDENT ⋈ (RollNo = RollNo2) STUDENT2 will return a relation with attributes Name, RollNo, Marks, Name2, Marks2, where each tuple is a combination of a tuple from STUDENT and a tuple from STUDENT2 that have the same RollNo.

There are also other operators such as RENAME (ρ), DIVIDE (÷), AGGREGATE (γ), etc. that can be used to perform more complex queries on relations.

Relational algebra is a powerful and expressive language that can be used to manipulate and query data in relational databases. It can also be used to prove the correctness and equivalence of queries, and to optimize query execution.