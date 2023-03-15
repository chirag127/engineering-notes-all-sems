### Unions

- A union is a set operation that combines the results of two or more queries into one result set.
- The queries used in a union must have the same number of columns and the corresponding columns must have the same or compatible data types.
- A union eliminates any duplicate rows from the result set, unless the keyword ALL is used.
- A union can be used to retrieve data from more than one table or relation simultaneously and then merge the results.
- A union can be expressed in relational algebra as R1 UNION R2, where R1 and R2 are two union-compatible relations.
- A union can be expressed in SQL as SELECT * FROM R1 UNION SELECT * FROM R2, where R1 and R2 are two union-compatible tables.
- A union can be useful for combining data from different sources, such as different databases, files, or web services.