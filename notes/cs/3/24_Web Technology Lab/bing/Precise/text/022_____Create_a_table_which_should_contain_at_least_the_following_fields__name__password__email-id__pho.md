### Unit 5 - Design server site applications using JDDC, ODBC and section tracking API in the subject of Web Technology Lab

To create a table with the fields `name`, `password`, `email-id`, and `phone number`, you can use the following SQL statement:

```sql
CREATE TABLE users (
    name VARCHAR(255),
    password VARCHAR(255),
    email_id VARCHAR(255),
    phone_number VARCHAR(255)
);
```

This statement creates a new table called `users` with four columns: `name`, `password`, `email_id`, and `phone_number`. Each column is of type `VARCHAR` with a maximum length of 255 characters.

It is important to note that the `password` field should be encrypted before being stored in the database for security reasons. Additionally, the `email_id` and `phone_number` fields should be validated to ensure that they contain valid email addresses and phone numbers, respectively.