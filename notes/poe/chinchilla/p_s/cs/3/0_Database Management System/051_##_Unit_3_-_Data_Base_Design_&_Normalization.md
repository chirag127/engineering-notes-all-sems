## Unit 3 - Data Base Design & Normalization

Database design is the process of organizing data into tables and columns in a way that makes it easy to retrieve and manipulate. It involves defining the table structure, relationships between tables, and constraints to ensure data integrity. Normalization is a technique used in database design to eliminate redundant data and improve data integrity.

### Database Design

* Database design involves the following steps:
  * Requirement gathering: This involves understanding the user's needs and the data that needs to be stored.
  * Conceptual design: This involves creating a high-level conceptual model of the database.
  * Logical design: This involves translating the conceptual model into a logical model, including defining tables, columns, and relationships.
  * Physical design: This involves implementing the logical model on a specific database management system.

* The following are important concepts in database design:
  * Tables: A table is a collection of related data. Each table has a unique name and consists of columns and rows.
  * Columns: A column is a data item in a table.
  * Rows: A row is a record in a table.
  * Relationships: A relationship is a connection between two tables.
  * Constraints: Constraints are rules that enforce data integrity, such as primary keys, foreign keys, and unique constraints.

### Normalization

* Normalization is a technique used to eliminate redundant data and improve data integrity.
* It involves dividing larger tables into smaller tables and defining relationships between them.
* The following are the steps involved in normalization:
  * First Normal Form (1NF): Eliminate repeating groups and create a separate table for each set of related data.
  * Second Normal Form (2NF): Eliminate partial dependencies by creating a separate table for each set of related fields that depend on a primary key.
  * Third Normal Form (3NF): Eliminate transitive dependencies by creating a separate table for each set of related fields that do not depend on a primary key.

* Advantages of normalization:
  * Reduces data redundancy
  * Improves data integrity
  * Simplifies data maintenance
  * Facilitates data querying

* Disadvantages of normalization:
  * Can result in more tables and more complex relationships
  * Can make querying more complex

* Example:
  * Consider a database for a library. The following tables could be created:
    * Books (book_id, title, author_id, publisher_id, year_published)
    * Authors (author_id, first_name, last_name)
    * Publishers (publisher_id, name, location)

* Applications of database design and normalization:
  * Any application that requires storing and manipulating data can benefit from database design and normalization.
  * Common applications include customer relationship management, inventory management, and e-commerce websites.

In conclusion, database design and normalization are important techniques for organizing and maintaining data. By following a structured design process and applying normalization, you can improve data integrity, simplify data maintenance, and facilitate data querying.