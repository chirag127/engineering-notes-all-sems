 Here are the key points regarding Constraints for the notes of Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Keys
- Primary Key: Uniquely identifies each row in a table. Contains a single column or set of columns with a unique value for each row. No null values allowed. One table can only have one primary key.
- Candidate Key: A minimal set of columns that can uniquely identify each row in a table. A table can have multiple candidate keys, one of which is chosen as the primary key.
- Alternate Key: A key that is not chosen as the primary key. A table can have multiple alternate keys.
- Foreign Key: A column or set of columns in a table that references the primary key of another table. Ensures referential integrity between two tables.

### Constraints
- NOT NULL: Ensures a column cannot have a NULL value.
- UNIQUE: Ensures all values in a column are different.
- PRIMARY KEY: A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table.
- FOREIGN KEY: Prevents actions that would destroy links between data in two tables. Ensures referential integrity.
- CHECK: Ensures all values in a column satisfy a specific condition.
- DEFAULT: Sets a default value for a column when no value is specified.

The constraints and keys help ensure data integrity, accuracy, and reliability in a database. They aid in maintaining the relationships between data in tables and preventing unwanted data entry. Markdown diagrams and examples can be included for better understanding. The points can be elaborated in detail for an in-depth study material.