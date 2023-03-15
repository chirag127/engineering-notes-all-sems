Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of tables – creation and alteration for the unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here is the content I have generated for you:

### Tables – creation and alteration

- A table is a collection of related data organized in rows and columns in a database.
- A table has a name, a set of attributes (columns), and a set of tuples (rows).
- Each attribute has a name, a data type, and optionally a constraint that defines the valid values or conditions for that attribute.
- Each tuple has a value for each attribute in the table.
- A table can be created using the `CREATE TABLE` statement in SQL, which has the following syntax:

```sql
CREATE TABLE table_name (
  attribute1 data_type1 [constraint1],
  attribute2 data_type2 [constraint2],
  ...
  attributeN data_typeN [constraintN]
);
```

- For example, to create a table called `student` with attributes `id`, `name`, `age`, and `major`, the following statement can be used:

```sql
CREATE TABLE student (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  major VARCHAR(20)
);
```

- The `PRIMARY KEY` constraint specifies that the `id` attribute is the unique identifier for each tuple in the table.
- The `NOT NULL` constraint specifies that the `name` attribute cannot have a null value, which means unknown or missing.
- The `CHECK` constraint specifies that the `age` attribute must be greater than zero.
- The `major` attribute has no constraint, which means it can have any value of the `VARCHAR(20)` data type, which is a variable-length character string with a maximum of 20 characters.

- A table can be altered using the `ALTER TABLE` statement in SQL, which has the following syntax:

```sql
ALTER TABLE table_name
  action1,
  action2,
  ...
  actionN;
```

- The actions can be one or more of the following:

  - `ADD attribute data_type [constraint]` to add a new attribute to the table with the specified data type and optional constraint.
  - `DROP attribute` to remove an existing attribute from the table.
  - `RENAME TO new_table_name` to change the name of the table.
  - `MODIFY attribute data_type [constraint]` to change the data type and/or constraint of an existing attribute.
  - `ADD CONSTRAINT constraint_name constraint_type (attribute_list)` to add a new constraint to the table with the specified name and type, which can be one of the following:
    - `PRIMARY KEY (attribute_list)` to specify the attributes that form the unique identifier for each tuple in the table.
    - `FOREIGN KEY (attribute_list) REFERENCES other_table (other_attribute_list)` to specify the attributes that reference another table's primary key attributes, creating a relationship between the tables.
    - `UNIQUE (attribute_list)` to specify the attributes that must have unique values in the table.
    - `CHECK (condition)` to specify a condition that must be true for each tuple in the table.
  - `DROP CONSTRAINT constraint_name` to remove an existing constraint from the table.

- For example, to alter the `student` table by adding a new attribute called `email`, dropping the `major` attribute, renaming the table to `students`, modifying the data type of the `name` attribute to `VARCHAR(100)`, adding a unique constraint on the `email` attribute, and dropping the check constraint on the `age` attribute, the following statement can be used:

```sql
ALTER TABLE student
  ADD email VARCHAR(50) NOT NULL,
  DROP major,
  RENAME TO students,
  MODIFY name VARCHAR(100) NOT NULL,
  ADD CONSTRAINT email_unique UNIQUE (email),
  DROP CONSTRAINT age_check;
```