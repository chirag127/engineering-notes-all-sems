### Creating a Table for Web Technology Lab

In the Unit 5 of Web Technology Lab, we will be learning about designing server site applications using JDDC, ODBC, and section tracking API. As a part of this study, we need to create a table that contains the following fields:

- **Name**: This field will store the name of the user. It will be a string data type with a maximum length of 50 characters.
- **Password**: This field will store the password of the user. It will be a string data type with a maximum length of 20 characters.
- **Email-id**: This field will store the email address of the user. It will be a string data type with a maximum length of 100 characters.
- **Phone Number**: This field will store the phone number of the user. It will be a string data type with a maximum length of 15 characters.

We can create this table in any Relational Database Management System (RDBMS) like MySQL, Oracle, or Microsoft SQL Server. The following is an example of how we can create this table in MySQL using SQL query:

```
CREATE TABLE user_details (
    name VARCHAR(50),
    password VARCHAR(20),
    email_id VARCHAR(100),
    phone_number VARCHAR(15)
);
```

In this query, we have specified the name of the table as "user_details" and defined the four fields with their respective data types and maximum lengths.

After creating the table, we can insert data into it using the following SQL query:

```
INSERT INTO user_details (name, password, email_id, phone_number)
VALUES ('John Doe', 'password123', 'johndoe@example.com', '1234567890');
```

In this query, we have inserted the data for one user into the table.

We can also retrieve data from the table using the SELECT statement as follows:

```
SELECT * FROM user_details;
```

This query will return all the data stored in the "user_details" table.

In conclusion, creating a table with the specified fields is an important aspect of designing server site applications using JDDC, ODBC, and section tracking API. By understanding the data types and lengths of the fields, we can create an efficient and effective table to store user data.