 Here is the content in markdown format for the given topic:

### Defining Constraints

Constraints are rules enforced on data columns to ensure data integrity and consistency. Some common types of constraints are:

- **NOT NULL** - Ensures that a column cannot have NULL value.
- **UNIQUE** - Ensures that all values in a column are different.
- **PRIMARY KEY** - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table.
- **FOREIGN KEY** - Ensures that the value in a column exists in another table. Used to link data between tables.
- **CHECK** - Ensures that all values in a column satisfy a specific condition.
- **DEFAULT** - Sets a default value for a column when no value is specified.

Constraints are specified when creating or altering tables. They can be added to enforce business rules on the data and prevent invalid data entry. Some advantages of using constraints are:

- Increased data integrity and consistency.
- More efficient data storage and processing.
- Fewer anomalies and errors.
- Serve as documentation for the database.

However, constraints may affect performance when updating and deleting data and can be overridden by explicit code. Appropriate constraints should be chosen based on requirements to gain the benefits while minimizing the disadvantages.

The SQL commands to define constraints are:

- `NOT NULL` - `col_name datatype NOT NULL`
- `UNIQUE` - `col_name datatype UNIQUE`
- `PRIMARY KEY` - `col_name datatype PRIMARY KEY`
- `FOREIGN KEY` - `col_name datatype FOREIGN KEY REFERENCES parent_table(parent_col)`
- `CHECK` - `col_name datatype CHECK (condition)`
- `DEFAULT` - `col_name datatype DEFAULT default_value`

[Detailed diagrams and examples can be added here for more clarity.]