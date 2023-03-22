### Table for Unit 5 - Design server site applications using JDDC, ODBC and section tracking API in the subject of Web Technology Lab

When designing server site applications, it is important to have a well-structured database to store user information. In this unit, we will learn about designing such databases using JDDC, ODBC, and section tracking API. As a part of preparing for exams, it is important to understand the structure of such a database. Here is a table that should contain at least the following fields: name, password, email-id, phone number:

| Field      | Data Type | Constraints |
| ----------- | ----------- | ----------- |
| name      | VARCHAR(50)      | NOT NULL       |
| password   | VARCHAR(20)   | NOT NULL, encrypted      |
| email-id   | VARCHAR(100)   | UNIQUE, NOT NULL      |
| phone number   | VARCHAR(15)   | UNIQUE, NOT NULL      |

- The table should have four fields: name, password, email-id, and phone number.
- The data type of the name field should be VARCHAR(50).
- The data type of the password field should be VARCHAR(20) and should be encrypted for security reasons.
- The email-id field should be of data type VARCHAR(100) and should be a unique field, i.e., it should not allow duplicate values. It should also not allow null values.
- The phone number field should be of data type VARCHAR(15) and should be a unique field, i.e., it should not allow duplicate values. It should also not allow null values.

Having a well-designed database is crucial for any server site application. By following the above guidelines, we can ensure that our database is well-structured and secure.