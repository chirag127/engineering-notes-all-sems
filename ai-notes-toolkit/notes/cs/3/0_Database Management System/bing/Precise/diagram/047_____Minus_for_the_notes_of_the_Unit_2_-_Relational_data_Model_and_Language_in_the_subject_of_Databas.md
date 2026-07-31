### Unit 2 - Relational Data Model and Language

#### Minus

- The `MINUS` operator is used in relational algebra and SQL to return the difference between two sets of tuples.
- It takes two relations as input and returns a new relation that contains all the tuples that are in the first relation but not in the second.
- The two input relations must be union-compatible, meaning they must have the same number of attributes and the corresponding attributes must have the same domain.
- In SQL, the `MINUS` operator is called `EXCEPT`.
- The result of the `MINUS` operation is all the tuples in the first relation that are not in the second relation.
- The order of the input relations matters, as `R MINUS S` is not the same as `S MINUS R`.
- The `MINUS` operator can be used to find the difference between two sets of data, such as finding the customers who have made a purchase in the past but have not made a purchase in the current month.