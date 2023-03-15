### Unions

- A union is a set operation that combines the results of two or more queries into one result set that contains all the rows that belong to any of the queries .
- A union is performed using the `UNION` keyword in SQL, which tells the database to merge two separate result sets retrieved through individual `SELECT` queries.
- A union can only be applied to two relations that are union-compatible, which means they have the same number of attributes and the corresponding attributes have the same or compatible domains .
- A union eliminates any duplicate rows from the result set, unless the `UNION ALL` keyword is used, which preserves all the rows .
- A union is different from a join, which combines data into separate columns based on a matching column between the two relations.
- A union can be used to combine data from different tables that have a similar structure, such as different branches of a company or different categories of products .
- A union can also be used to perform complex queries that involve multiple conditions or criteria, such as finding customers who have ordered products from different categories or regions .