### Unions

- A union is a set operation that combines the tuples of two relations into one relation.
- A union can only be performed on two relations that are union-compatible, meaning they have the same number of attributes and the corresponding attributes have the same data type.
- A union eliminates any duplicate tuples from the result relation.
- A union can be expressed in relational algebra as R1 UNION R2, where R1 and R2 are the two relations to be unioned.
- A union can be expressed in SQL as SELECT * FROM R1 UNION SELECT * FROM R2, where R1 and R2 are the two tables to be unioned.
- A union can be used to retrieve data from more than one table simultaneously and then combine the results into one table.
- A union can be useful for combining data from different sources that have the same schema or structure.