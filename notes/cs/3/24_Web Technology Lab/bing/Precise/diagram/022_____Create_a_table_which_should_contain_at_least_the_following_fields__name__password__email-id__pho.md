### Unit 5 - Design server site applications using JDDC, ODBC and section tracking API in the subject of Web Technology Lab

To create a table with the fields `name`, `password`, `email-id`, and `phone number`, you can use the following SQL statement:

```SQL
CREATE TABLE users (
    name VARCHAR(255),
    password VARCHAR(255),
    email_id VARCHAR(255),
    phone_number VARCHAR(255)
);
```

This table can be used to store user information for server-side applications that use JDBC, ODBC, or session tracking APIs.

- `name`: This field stores the name of the user.
- `password`: This field stores the password of the user.
- `email_id`: This field stores the email address of the user.
- `phone_number`: This field stores the phone number of the user.

It is important to note that the data types and constraints used in the table may vary depending on the specific requirements of the application. Additionally, it is recommended to use proper hashing and encryption techniques to securely store the user's password.