 Here are the notes for unions in SQL for Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

### Unions

- Unions combine the results of two or more SELECT statements into a single result set.
- Each SELECT statement within UNION must have the same number of columns and compatible data types.
- The columns in each SELECT statement must also be in the same order.
- UNION removes duplicate rows, UNION ALL retains duplicate rows.
- The basic syntax is:

SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2

- The columns and data types must match in each SELECT statement.
- The rows are combined and sorted to remove duplicates (UNION) or duplicates are retained (UNION ALL).
- Unions are useful for combining rows from two or more tables when a relationship does not exist between the tables.

The above notes highlight the key points regarding unions in SQL while following a formal tone with bullet points and no emojis or external links as requested. Please let me know if you would like me to modify or expand the notes in any way.