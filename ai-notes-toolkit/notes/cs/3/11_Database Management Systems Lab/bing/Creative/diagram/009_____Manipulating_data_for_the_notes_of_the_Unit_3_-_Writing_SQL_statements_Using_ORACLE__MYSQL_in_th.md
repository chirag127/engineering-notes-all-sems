Hello, I am Sydney, your AI assistant. I can help you with your topic of manipulating data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab. Here is some information that I have gathered from the web:

### Manipulating data

- Data manipulation language (DML) statements add, change, and delete data in relational database management systems such as Oracle and MySQL .
- The main DML statements are INSERT, UPDATE, DELETE, and MERGE .
- INSERT adds new rows of data to a table .
- UPDATE modifies existing rows of data in a table .
- DELETE removes existing rows of data from a table .
- MERGE combines the data from two tables and updates or inserts the result into a third table.
- DML statements can be used with various clauses, such as WHERE, ORDER BY, GROUP BY, HAVING, and JOIN, to filter, sort, aggregate, and combine data .
- DML statements can also use operators, such as arithmetic, logical, comparison, and string operators, to perform calculations and comparisons on data values .
- DML statements are executed as transactions, which are sequences of one or more SQL statements that are treated as a unit. A transaction can be committed or rolled back, depending on whether the changes are successful or not.

Some examples of DML statements in Oracle and MySQL are:

- To insert a new row into the table `students` with the values `101`, `Alice`, and `3.5` for the columns `id`, `name`, and `gpa`, respectively:

```sql
INSERT INTO students (id, name, gpa) VALUES (101, 'Alice', 3.5);
```

- To update the `gpa` column of the table `students` to `4.0` for the row where the `id` is `101`:

```sql
UPDATE students SET gpa = 4.0 WHERE id = 101;
```

- To delete the row from the table `students` where the `id` is `101`:

```sql
DELETE FROM students WHERE id = 101;
```

- To merge the data from the tables `students` and `courses` based on the `id` column and insert the result into the table `enrollments`:

```sql
MERGE INTO enrollments e
USING (SELECT id, course FROM students JOIN courses ON students.id = courses.student_id) s
ON (e.id = s.id)
WHEN MATCHED THEN
  UPDATE SET e.course = s.course
WHEN NOT MATCHED THEN
  INSERT (id, course) VALUES (s.id, s.course);
```

I hope this information is helpful for your notes. If you have any questions, please let me know.😊