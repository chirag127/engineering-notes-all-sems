### Relational Algebra

Relational algebra is a procedural query language used to manipulate relations in a relational database. It consists of a set of operations that take one or two relations as input and produce a new relation as output. The fundamental operations in relational algebra are:

1. **Selection**: The selection operation selects rows from a relation that satisfy a given condition. It is denoted by the sigma symbol (σ).
2. **Projection**: The projection operation selects columns from a relation and discards the other columns. It is denoted by the pi symbol (π).
3. **Union**: The union operation combines two relations into a single relation, removing any duplicate rows. It is denoted by the union symbol (⋃).
4. **Intersection**: The intersection operation returns the rows that are common to both input relations. It is denoted by the intersection symbol (⋂).
5. **Difference**: The difference operation returns the rows that are in the first relation but not in the second relation. It is denoted by the minus symbol (-).
6. **Cartesian Product**: The Cartesian product operation combines each row of the first relation with each row of the second relation. It is denoted by the cross symbol (×).
7. **Join**: The join operation combines rows from two relations based on a common attribute. There are several types of join operations, including inner join, outer join, and theta join.

These operations can be combined to form complex queries. Relational algebra provides a foundation for the Structured Query Language (SQL), which is the standard language used to interact with relational databases.