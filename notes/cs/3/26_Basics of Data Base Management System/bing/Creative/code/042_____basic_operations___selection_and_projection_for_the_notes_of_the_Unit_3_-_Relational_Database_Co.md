### Basic operations – selection and projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database .
- Selection targets records (rows) or specific entities in a relation (table) for which a condition or predicate stands true . It is denoted by the symbol σ and can be written as:

    σ<sub>condition</sub>(relation)

- For example, to select all the employees from the Employee relation who have a salary greater than 50000, we can write:

    σ<sub>salary > 50000</sub>(Employee)

- Projection targets attributes (columns) or specific properties of a relation (table) and eliminates the duplicate tuples (rows) . It is denoted by the symbol π and can be written as:

    π<sub>attribute list</sub>(relation)

- For example, to project the names and departments of all the employees from the Employee relation, we can write:

    π<sub>name, department</sub>(Employee)

- Selection and projection can be combined to perform more complex queries on a relation. For example, to project the names of all the employees who have a salary greater than 50000, we can write:

    π<sub>name</sub>(σ<sub>salary > 50000</sub>(Employee))

- Selection and projection are equivalent to the SQL SELECT statement, which combines these operations in a single statement . For example, the above query can be written in SQL as:

    SELECT name FROM Employee WHERE salary > 50000;