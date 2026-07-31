# Relationship of Higher Degree

- A relationship of higher degree is a relationship that involves more than two entities.
- For example, a ternary relationship is a relationship of degree three, which relates three entities.
- A relationship of higher degree can be represented by a diamond-shaped symbol with the name of the relationship and the degree as a subscript.
- The participating entities are connected to the relationship symbol by lines, and the cardinality ratios are indicated by numbers or symbols on the lines.
- For example, the following diagram shows a ternary relationship called **Supplies**, which relates three entities: **Supplier**, **Part**, and **Project**.

![Ternary relationship diagram](https://i.imgur.com/7aKw3qF.png)

- A relationship of higher degree can also be represented by a table, where each row corresponds to an instance of the relationship, and each column corresponds to an attribute of the relationship or an entity involved in the relationship.
- For example, the following table shows a possible instance of the **Supplies** relationship, where each row indicates that a supplier supplies a part to a project with a certain quantity and price.

| Supplier | Part | Project | Quantity | Price |
|----------|------|---------|----------|-------|
| S1       | P1   | A       | 100      | 10    |
| S1       | P2   | B       | 50       | 15    |
| S2       | P3   | A       | 200      | 20    |
| S2       | P4   | C       | 150      | 25    |
| S3       | P5   | B       | 75       | 30    |
| S3       | P6   | C       | 100      | 35    |

- A relationship of higher degree can be converted into a set of binary relationships by introducing a new entity that represents the relationship, and creating a one-to-many relationship between the new entity and each of the original entities.
- For example, the **Supplies** relationship can be converted into a set of binary relationships by introducing a new entity called **Supply**, which has a composite key consisting of the attributes of the original entities, and creating a one-to-many relationship between **Supply** and each of **Supplier**, **Part**, and **Project**.

![Binary relationship diagram](https://i.imgur.com/8Zw8w6R.png)

- The advantage of converting a relationship of higher degree into a set of binary relationships is that it simplifies the data model and avoids the ambiguity of the cardinality ratios of the original relationship.
- The disadvantage of converting a relationship of higher degree into a set of binary relationships is that it introduces redundancy and complexity in the data, and may require additional constraints to ensure the consistency and integrity of the data.