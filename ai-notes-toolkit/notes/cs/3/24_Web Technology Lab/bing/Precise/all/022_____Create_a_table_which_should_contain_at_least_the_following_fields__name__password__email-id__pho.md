# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

## Creating a table with fields: name, password, email-id, phone number

1. To create a table with the specified fields, you can use the following SQL command:
```
CREATE TABLE users (
    name VARCHAR(255),
    password VARCHAR(255),
    email_id VARCHAR(255),
    phone_number VARCHAR(255)
);
```
2. This command creates a table named `users` with four columns: `name`, `password`, `email_id`, and `phone_number`.
3. Each column is of type `VARCHAR` with a maximum length of 255 characters.
4. You can execute this command using a database management tool or by connecting to the database using a programming language such as Java or Python and executing the command using the appropriate API (JDBC or ODBC).
5. Once the table is created, you can insert, update, and retrieve data from it using standard SQL commands.
