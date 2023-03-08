### DML for the notes of the Unit 1 - Introduction in the subject of Database Management System

Database Management Systems (DBMS) are computer software applications that interact with the user, other applications and the database itself to capture and analyze data. There are various types of languages used in Database Management Systems, one of which is Data Manipulation Language (DML). In this section, we will learn about DML in detail.

#### What is Data Manipulation Language?

Data Manipulation Language (DML) is a language used for managing data within the database. This language allows users to interact with the data stored in the database and modify it as per their requirements. DML is used to insert, update, delete and retrieve data from the database. 

#### Types of DML commands

Following are the types of DML commands:

1. **SELECT**: It is used to retrieve data from the database. The syntax for SELECT command is as follows:

   ```
   SELECT column1, column2, column3
   FROM table_name
   WHERE condition;
   ```

2. **INSERT**: It is used to insert data into the database. The syntax for INSERT command is as follows:

   ```
   INSERT INTO table_name (column1, column2, column3)
   VALUES (value1, value2, value3);
   ```

3. **UPDATE**: It is used to modify existing data in the database. The syntax for UPDATE command is as follows:

   ```
   UPDATE table_name
   SET column1 = value1, column2 = value2
   WHERE condition;
   ```

4. **DELETE**: It is used to delete data from the database. The syntax for DELETE command is as follows:

   ```
   DELETE FROM table_name
   WHERE condition;
   ```

#### Advantages of DML

- DML is easy to use and understand.
- It provides a flexible and efficient way to manage data.
- It allows users to retrieve and modify data as per their requirements.
- It is widely used in modern database management systems.

#### Disadvantages of DML

- DML commands can be complex and difficult to understand for novice users.
- DML commands can be slow if the database is large.
- DML commands can be prone to errors if not used correctly.

#### Examples of DML commands

```
-- Example of SELECT command
SELECT * FROM employees WHERE age > 30;

-- Example of INSERT command
INSERT INTO employees (name, age, salary) VALUES ('John Doe', 35, 50000);

-- Example of UPDATE command
UPDATE employees SET salary = 55000 WHERE name = 'John Doe';

-- Example of DELETE command
DELETE FROM employees WHERE name = 'John Doe';
```

#### Applications of DML

DML is widely used in various applications such as:

- Banking and finance
- Healthcare
- Retail
- Transportation
- Education
- Government

In conclusion, Data Manipulation Language (DML) is an important part of Database Management Systems (DBMS) as it allows users to interact with the data stored in the database and modify it as per their requirements. DML commands are easy to use and widely used in modern database management systems.