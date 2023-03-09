 Here is the content in markdown format for the given topic:

### Integrity Constraints

Integrity constraints are rules enforced on data in a database. They ensure accuracy and consistency of data in a database. There are three main types of integrity constraints:

1. Entity Integrity Constraint: Ensures that each row in a table has a value for the primary key. It prevents the insertion of rows with null primary key values.
2. Referential Integrity Constraint: Ensures that the relationship between two tables is consistent. It prevents actions that would destroy links between data in two related tables. Eg: It prevents deletion of a row in the parent table if there are dependent rows in the child table.
3. Domain Integrity Constraint: Ensures that the values in a column satisfy specific conditions or restrictions. Eg: It can be used to restrict values in a column to a specific range or data type.

The benefits of having integrity constraints are:

- Increased data accuracy and consistency.
- Prevention of anomalous or incorrect data.
- Increased user confidence in data and system integrity.

However, integrity constraints may impact performance as the database has to do additional work to enforce the constraints. It is a trade-off between data integrity and performance.

Here is an ascii diagram showing entity integrity constraint:

[Diagram showing a table with primary key and rows with values for the primary key]

Code example:
CREATE TABLE table_name (
    id INTEGER PRIMARY KEY,
    col_name data_type,
    ...
);

Advantages and applications of integrity constraints were discussed above with examples. Overall, integrity constraints are important to uphold the accuracy and consistency of data in a database.