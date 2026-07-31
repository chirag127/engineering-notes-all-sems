### Integrity Constraints for the Notes of the Unit 3 - Relational Database Concepts

- Integrity constraints are the set of rules that can be used to maintain the data integrity during an insert, delete and update operations into a table.
- Data integrity means that the data in the database is valid, consistent and accurate.
- There are four types of integrity constraints in relational database:
  - Domain constraints
  - Key constraints
  - Entity integrity constraints
  - Referential integrity constraints

#### Domain Constraints
- Domain constraints specify the valid values for a column or an attribute.
- They are defined by the data type, size, range, format and default value of the column.
- For example, a column named AGE can have a domain constraint that only allows integer values between 1 and 120.

#### Key Constraints
- Key constraints identify the unique rows in a table or a relation.
- They are defined by the primary key and the candidate keys of the table.
- A primary key is a column or a combination of columns that uniquely identifies a row in a table.
- A candidate key is a column or a combination of columns that can also uniquely identify a row in a table, but is not chosen as the primary key.
- For example, a table named STUDENT can have a primary key of STUDENT_ID and a candidate key of EMAIL.

#### Entity Integrity Constraints
- Entity integrity constraints ensure that every table has a primary key and that the primary key does not contain null values.
- Null values are used to represent missing or unknown data in a database.
- A primary key with null values cannot uniquely identify a row in a table.
- For example, a table named COURSE can have a primary key of COURSE_ID and an entity integrity constraint that does not allow null values in the COURSE_ID column.

#### Referential Integrity Constraints
- Referential integrity constraints ensure that the foreign key values in a table match the primary key values in another table.
- A foreign key is a column or a combination of columns that references the primary key of another table.
- Referential integrity constraints prevent the insertion of invalid data or the deletion of referenced data in the database.
- For example, a table named ENROLLMENT can have a foreign key of STUDENT_ID that references the primary key of the STUDENT table, and a referential integrity constraint that does not allow the insertion of a STUDENT_ID that does not exist in the STUDENT table, or the deletion of a STUDENT_ID that is referenced by the ENROLLMENT table.