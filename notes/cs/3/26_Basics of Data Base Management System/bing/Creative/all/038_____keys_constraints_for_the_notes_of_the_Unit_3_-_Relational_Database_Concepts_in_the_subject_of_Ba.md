# Key Constraints in Relational Database

Key constraints are rules that ensure the integrity and uniqueness of data in a relational database. They are applied on the columns or attributes that are used as keys to identify and relate the rows in a table. There are different types of key constraints in a relational database, such as:

- **Primary key constraint**: This constraint requires every entry in the given column or set of columns to be both unique and not NULL, and allows you to use that column or set of columns to identify each individual row in the table. A table can have only one primary key constraint, which can be either clustered or nonclustered. For example, in a table of students, the student ID can be a primary key.

- **Foreign key constraint**: This constraint requires every entry in the given column or set of columns to match an existing value in the primary key column or set of columns of another table, and ensures the referential integrity between the two tables. A table can have multiple foreign key constraints, which can reference the same or different tables. For example, in a table of courses, the course ID can be a foreign key that references the primary key of another table of course details.

- **Unique key constraint**: This constraint requires every entry in the given column or set of columns to be unique, but allows NULL values. A table can have multiple unique key constraints, which can be either clustered or nonclustered. For example, in a table of students, the email address can be a unique key.

- **Check key constraint**: This constraint requires every entry in the given column or set of columns to satisfy a specified condition or expression. A table can have multiple check key constraints, which can apply to the same or different columns. For example, in a table of students, the age can be a check key that ensures the value is greater than zero.

- **Not NULL key constraint**: This constraint requires every entry in the given column or set of columns to have a value and not be NULL. A table can have multiple not NULL key constraints, which can apply to the same or different columns. For example, in a table of students, the name can be a not NULL key.