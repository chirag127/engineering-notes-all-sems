# Unions

- A union is a set operation that combines the results of two or more queries into one result set.
- A union can be used to retrieve data from more than one table simultaneously and then merge the results.
- A union requires that the queries involved have the same number of columns and that the corresponding columns have the same data type.
- A union eliminates any duplicate rows from the result set, unless the keyword ALL is used.
- A union can be expressed in relational algebra as R1 UNION R2, where R1 and R2 are union-compatible relations.
- A union can be expressed in SQL as SELECT * FROM R1 UNION SELECT * FROM R2, where R1 and R2 are union-compatible tables.