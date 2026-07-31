# Set-theoretic operations for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

Set-theoretic operations are the standard mathematical operations on sets that can be applied to relations in a relational database. These operations are binary, meaning that they operate on two relations at a time. The two relations must be union compatible, meaning that they have the same number and type of attributes, and the same domain for each attribute. The result of a set-theoretic operation is also a relation that is union compatible with the operands.

The main set-theoretic operations are:

- **Union**: The union of two relations R and S, denoted by R ∪ S, is the relation that contains all the tuples that are either in R or in S or in both. The union operation eliminates any duplicate tuples from the result. For example, if R and S are two relations with the same schema of (name, age), then R ∪ S is the relation that contains all the distinct (name, age) pairs from both R and S.

- **Intersection**: The intersection of two relations R and S, denoted by R ∩ S, is the relation that contains all the tuples that are common to both R and S. For example, if R and S are two relations with the same schema of (name, age), then R ∩ S is the relation that contains all the (name, age) pairs that are present in both R and S.

- **Difference**: The difference of two relations R and S, denoted by R - S, is the relation that contains all the tuples that are in R but not in S. For example, if R and S are two relations with the same schema of (name, age), then R - S is the relation that contains all the (name, age) pairs that are in R but not in S.

- **Cartesian product**: The Cartesian product of two relations R and S, denoted by R × S, is the relation that contains all the possible combinations of tuples from R and S. The schema of the Cartesian product is the concatenation of the schemas of R and S. For example, if R is a relation with the schema of (name, age) and S is a relation with the schema of (city, country), then R × S is the relation with the schema of (name, age, city, country) that contains all the possible (name, age, city, country) tuples from R and S.

Set-theoretic operations are useful for manipulating and combining relations in a relational database. They can be used to express complex queries and operations in a concise and elegant way. They can also be combined with other relational algebra operations, such as selection, projection, and join, to form more powerful expressions.