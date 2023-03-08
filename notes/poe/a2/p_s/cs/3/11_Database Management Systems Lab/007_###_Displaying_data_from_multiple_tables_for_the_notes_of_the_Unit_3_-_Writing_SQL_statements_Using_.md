 Here is the content in markdown format for the given topic:

### Displaying data from multiple tables

To display data from multiple tables, we use JOIN clauses in SQL. The main types of joins are:

1. Inner join: Returns records that have matching values in both tables.

- Syntax: SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column
- Returns the matching rows from both tables.
- Example: Select * from students inner join courses on students.course_id = courses.id

This will return the student data and course data for students enrolled in courses.

2. Left (outer) join: Returns all records from the left table, and the matched records from the right table.

- Syntax: SELECT columns FROM table1 LEFT JOIN table2 ON table1.column = table2.column
- Returns all rows from the left table, even if there are no matches in the right table.
- Nulls will be returned for each column of the right table if there is no match.
- Example: Select * from students left join courses on students.course_id = courses.id

This will return all student data and course data for enrolled students. For unenrolled students, course data will be null.

3. Right (outer) join: Returns all records from the right table, and the matched records from the left table.

- Syntax: SELECT columns FROM table1 RIGHT JOIN table2 ON table1.column = table2.column
- Returns all rows from the right table, even if there are no matches in the left table.
- Nulls will be returned for each column of the left table if there is no match.
- Example: Select * from students right join courses on students.course_id = courses.id

This will return all course data and student data for enrolled students. For courses without students enrolled, student data will be null.

[Additional details, diagrams, examples, etc. can be added here]