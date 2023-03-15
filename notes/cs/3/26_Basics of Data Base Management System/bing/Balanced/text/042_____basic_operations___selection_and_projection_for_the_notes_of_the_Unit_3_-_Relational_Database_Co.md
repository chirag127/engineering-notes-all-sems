### Basic operations – selection and projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database.
- Selection is the operation of choosing a subset of rows (tuples) from a relation (table) that satisfy a given condition. The condition is specified by a predicate (a logical expression) that involves the attributes (columns) of the relation.
- Projection is the operation of choosing a subset of columns (attributes) from a relation (table) and eliminating the duplicates. The result is a new relation that contains only the specified attributes.
- In SQL, the SELECT statement combines both selection and projection operations in a single query. The WHERE clause is used to specify the selection condition, and the list of attributes after the SELECT keyword is used to specify the projection attributes.
- For example, the following SQL query performs both selection and projection on the relation Employee:

```sql
SELECT name, salary
FROM Employee
WHERE department = 'Sales';
```

- The query selects only the rows where the department attribute is 'Sales', and projects only the name and salary attributes of those rows. The result is a new relation with two columns and no duplicates.