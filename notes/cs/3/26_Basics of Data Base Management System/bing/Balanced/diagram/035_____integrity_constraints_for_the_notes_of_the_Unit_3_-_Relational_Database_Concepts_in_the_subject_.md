### Integrity Constraints for the Notes of the Unit 3 - Relational Database Concepts

- Integrity constraints are the set of rules that can be used to maintain the data integrity during an insert, delete and update operations into a table.
- Data integrity means that the data present in the database table is valid, consistent and accurate.
- There are four types of integrity constraints in relational database:
  - Domain constraints
  - Key constraints
  - Entity integrity constraints
  - Referential integrity constraints

#### Domain Constraints
- Domain constraints specify the valid values for a column or an attribute of a table.
- Domain constraints can be defined by using data types, ranges, formats, patterns, etc.
- For example, a column named Age can have a domain constraint that only allows integer values between 18 and 65.

#### Key Constraints
- Key constraints identify the unique rows in a table or a relation.
- Key constraints can be defined by using primary keys, candidate keys, alternate keys, etc.
- For example, a table named Student can have a key constraint that only allows one row for each student ID.

#### Entity Integrity Constraints
- Entity integrity constraints ensure that every table has a primary key and that the primary key does not contain null values.
- Entity integrity constraints prevent duplicate rows and missing values in a table.
- For example, a table named Employee can have an entity integrity constraint that requires every employee to have a non-null employee ID as the primary key.

#### Referential Integrity Constraints
- Referential integrity constraints ensure that the foreign key values in a table match the primary key values in another table.
- Referential integrity constraints maintain the consistency and validity of the relationships between tables.
- For example, a table named Order can have a referential integrity constraint that requires every order to have a valid customer ID that matches the primary key of the Customer table.