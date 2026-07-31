### Relational Algebra

Relational Algebra is a procedural query language used to manipulate and retrieve data from relational databases. It provides a theoretical foundation for relational databases and is used to express queries in a formal and precise way.

Here are some important concepts and operators of Relational Algebra:

- **Relations:** A relation is a table with rows and columns. In Relational Algebra, relations are represented as capital letters, such as R, S or T.

- **Selection (σ):** Selection is used to retrieve a subset of rows from a relation that satisfy a specific condition. It is represented by the Greek letter sigma (σ) and is written as follows: 

  σ<sub>condition</sub>(R)

- **Projection (π):** Projection is used to retrieve a subset of columns from a relation. It removes duplicate rows and is represented by the Greek letter pi (π) and is written as follows:

  π<sub>list of columns</sub>(R)

- **Union (⋃):** Union combines two relations with the same schema and returns a relation that contains all the rows from both relations. Duplicate rows are removed. It is represented by the symbol ⋃ and is written as follows:

  R ⋃ S

- **Intersection (⋂):** Intersection returns a relation that contains only the rows that are common to both relations. It is represented by the symbol ⋂ and is written as follows:

  R ⋂ S

- **Difference (−):** Difference returns a relation that contains all the rows from one relation that are not in the other relation. It is represented by the symbol − and is written as follows:

  R − S

- **Cartesian Product (×):** Cartesian product combines two relations and returns a new relation that contains all possible combinations of rows from both relations. It is represented by the symbol × and is written as follows:

  R × S

These are the most commonly used operators in Relational Algebra. By combining these operators, complex queries can be expressed in a concise and formal way. Understanding and mastering Relational Algebra is essential for working with relational databases and querying them efficiently.