# Entity Integrity in Relational Database

- Entity integrity is a form of data integrity that ensures that each entity (row or record) in a table has a unique and non-null identifier (primary key).
- Entity integrity is one of the three types of integrity constraints in the relational data model, along with referential integrity and domain integrity.
- Entity integrity prevents duplicate or missing data in a table, and ensures that each entity can be uniquely identified and accessed by the primary key.
- Entity integrity is enforced by the database system by checking the primary key values for each entity before inserting, updating, or deleting data in a table.
- Entity integrity can be violated by:
  - Inserting a new entity with a primary key value that already exists in the table.
  - Inserting a new entity with a null primary key value.
  - Updating an existing entity with a primary key value that already exists in the table.
  - Updating an existing entity with a null primary key value.
  - Deleting an existing entity without specifying its primary key value.
- Entity integrity can be maintained by:
  - Defining a primary key for each table in the relational model, and ensuring that it is not null and unique for each entity.
  - Using a surrogate key (an artificial or generated value) as the primary key if the natural key (an attribute or combination of attributes that uniquely identifies an entity) is not suitable or available.
  - Using a composite key (a combination of two or more attributes) as the primary key if a single attribute is not sufficient or meaningful to identify an entity.
  - Using a foreign key (an attribute or combination of attributes that references the primary key of another table) to link entities across tables and enforce referential integrity.