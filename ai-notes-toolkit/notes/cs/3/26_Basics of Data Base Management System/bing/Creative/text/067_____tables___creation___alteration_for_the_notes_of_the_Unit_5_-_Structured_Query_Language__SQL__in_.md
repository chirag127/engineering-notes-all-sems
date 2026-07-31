Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write some notes on the topic of tables – creation and alteration for the unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here are some points that you can use for your study material:

### Tables – creation and alteration

- A table is a collection of data organized in rows and columns in a relational database.
- A table has a name, a set of attributes (columns), and a set of tuples (rows) that store the data values.
- A table can be created using the CREATE TABLE statement in SQL, which specifies the name of the table, the attributes and their data types, and any constraints on the attributes or the table.
- For example, the following statement creates a table called STUDENT with four attributes: ID, NAME, AGE, and MAJOR.

```sql
CREATE TABLE STUDENT (
  ID INT PRIMARY KEY,
  NAME VARCHAR(50) NOT NULL,
  AGE INT CHECK (AGE > 0),
  MAJOR VARCHAR(20)
);
```

- A table can be modified using the ALTER TABLE statement in SQL, which allows adding, deleting, or changing the attributes or the constraints of the table.
- For example, the following statement adds a new attribute called GPA to the STUDENT table.

```sql
ALTER TABLE STUDENT
ADD GPA DECIMAL(3,2) CHECK (GPA BETWEEN 0 AND 4);
```

- The following statement deletes the attribute MAJOR from the STUDENT table.

```sql
ALTER TABLE STUDENT
DROP COLUMN MAJOR;
```

- The following statement changes the data type of the attribute NAME from VARCHAR(50) to VARCHAR(100) in the STUDENT table.

```sql
ALTER TABLE STUDENT
ALTER COLUMN NAME VARCHAR(100);
```

- A table can be deleted using the DROP TABLE statement in SQL, which removes the table and all its data from the database.
- For example, the following statement deletes the STUDENT table.

```sql
DROP TABLE STUDENT;
```