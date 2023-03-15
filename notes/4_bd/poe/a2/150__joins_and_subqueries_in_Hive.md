 Here is the formal content on the given topic in Markdown format:

#### Joins and Subqueries in Hive

1. Joins in Hive can be performed using the JOIN keyword. The basic syntax is:

```SELECT column1, column2...
FROM table1
[INNER|LEFT|RIGHT|FULL] JOIN table2
ON table1.column = table2.column;```

The different types of joins in Hive are:

- INNER JOIN: Returns records that have matching values in both tables
- LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
- RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
- FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

2. Subqueries in Hive can be used to extract data from tables and use the results in another query. The subquery is enclosed within parentheses and is used in the WHERE clause. For example:

```SELECT column1, column2
FROM table1
WHERE column3 IN (SELECT column4 FROM table2 WHERE condition);```

The subquery is executed first and the results are used by the outer query. Subqueries can be correlated or non-correlated based on whether they reference the outer query table or not.

3. Joins and subqueries in Hive provide more powerful ways to retrieve data from tables and enable complex data extraction logic. They improve the readability and maintainability of queries compared to using only filtering and conditional expressions.

The content summarizes the key points around joins and subqueries in Hive in a formal tone with points and code snippets. No emojis or external links have been included as requested. The content is written in Markdown format.