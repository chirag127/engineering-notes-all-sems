### Intersection
- Intersection is a set operation that returns only the rows that are common to the result sets of two or more queries.
- In the context of the relational data model, the intersection operation can be performed using the `INTERSECT` keyword in SQL.
- The `INTERSECT` operation returns all rows that are common to the result sets of two or more `SELECT` statements.
- The number and data types of the columns in the result sets of the `SELECT` statements must be the same for the `INTERSECT` operation to be valid.
- The result of the `INTERSECT` operation is a new relation that contains only the rows that are common to the result sets of the `SELECT` statements.
- The order of the columns in the result set of the `INTERSECT` operation is determined by the order of the columns in the first `SELECT` statement.
- Duplicate rows are eliminated from the result set of the `INTERSECT` operation.
- The `INTERSECT` operation can be combined with other set operations such as `UNION` and `EXCEPT` to perform more complex queries.
