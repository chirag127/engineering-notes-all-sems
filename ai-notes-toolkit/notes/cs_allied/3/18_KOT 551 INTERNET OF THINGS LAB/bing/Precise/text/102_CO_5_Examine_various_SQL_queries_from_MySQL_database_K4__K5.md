# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL (Structured Query Language) is a standard language used to manage and manipulate data stored in relational databases. MySQL is one of the most popular open-source relational database management systems that use SQL.

Here are some common SQL queries that can be used in a MySQL database:

1. **SELECT**: Used to retrieve data from a database table. For example, to retrieve all data from a table named 'students', the query would be: `SELECT * FROM students;`

2. **INSERT**: Used to insert data into a database table. For example, to insert a new student record into the 'students' table, the query would be: `INSERT INTO students (name, age) VALUES ('John', 25);`

3. **UPDATE**: Used to update data in a database table. For example, to update the age of a student named 'John' in the 'students' table, the query would be: `UPDATE students SET age = 26 WHERE name = 'John';`

4. **DELETE**: Used to delete data from a database table. For example, to delete a student record with the name 'John' from the 'students' table, the query would be: `DELETE FROM students WHERE name = 'John';`

5. **CREATE**: Used to create a new database table. For example, to create a new table named 'courses' with columns 'id', 'name', and 'credits', the query would be: `CREATE TABLE courses (id INT, name VARCHAR(255), credits INT);`

6. **ALTER**: Used to modify the structure of an existing database table. For example, to add a new column named 'description' to the 'courses' table, the query would be: `ALTER TABLE courses ADD COLUMN description TEXT;`

7. **DROP**: Used to delete a database table. For example, to delete the 'courses' table, the query would be: `DROP TABLE courses;`

These are just a few examples of the various SQL queries that can be used in a MySQL database. It is important to have a good understanding of these queries to effectively manage and manipulate data in a MySQL database.