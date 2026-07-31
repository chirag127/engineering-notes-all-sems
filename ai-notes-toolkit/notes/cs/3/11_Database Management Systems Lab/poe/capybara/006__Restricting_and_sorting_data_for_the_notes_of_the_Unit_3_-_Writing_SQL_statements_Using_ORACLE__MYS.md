### Restricting and sorting data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

In SQL, we can restrict and sort data using various commands. In this unit, we will learn about how to restrict and sort data using ORACLE/MYSQL.

#### Restricting Data

Restricting data means selecting only a specific subset of data from a table. This can be achieved using the SELECT statement along with the WHERE clause. The WHERE clause is used to filter data based on a specific condition.

##### Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

##### Example

Suppose we have a table named 'students' with columns 'name', 'age', and 'gender'. We want to select all the male students who are above the age of 18.

```sql
SELECT name, age, gender
FROM students
WHERE age > 18 AND gender = 'male';
```

#### Sorting Data

Sorting data means arranging data in a particular order. This can be achieved using the ORDER BY clause. The ORDER BY clause sorts data based on one or more columns in ascending or descending order.

##### Syntax

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC/DESC;
```

##### Example

Suppose we have the same 'students' table as before. We want to select all the students and sort them in ascending order based on their age.

```sql
SELECT name, age, gender
FROM students
ORDER BY age ASC;
```

#### Combining Restriction and Sorting

We can also combine restriction and sorting to select a specific subset of data and sort it in a particular order.

##### Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
ORDER BY column1, column2, ... ASC/DESC;
```

##### Example

Suppose we want to select all female students who are above the age of 20 and sort them in descending order based on their age.

```sql
SELECT name, age, gender
FROM students
WHERE age > 20 AND gender = 'female'
ORDER BY age DESC;
```

By using these commands, we can easily restrict and sort data in SQL, making it easier to analyze and understand large datasets.