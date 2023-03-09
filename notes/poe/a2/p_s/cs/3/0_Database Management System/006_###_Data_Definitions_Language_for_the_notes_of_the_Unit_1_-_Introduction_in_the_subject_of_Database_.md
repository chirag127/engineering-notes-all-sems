 Here is the content written in markdown format for the topic ### Data Definitions Language for the notes of the Unit 1 - Introduction in the subject of Database Management System:

### Data Definitions Language

- DDL or Data Definition Language refers to the SQL statements that are used to define the database structure.
- It is used to create and modify the structure of database objects in a database.
- The common DDL commands are:

1. CREATE - to create a new database, table, index, etc.
2. ALTER - alters an existing database object
3. DROP - deletes an existing database object
4. TRUNCATE - empties a table of all rows
5. COMMENT - adds comments to the data dictionary

- For example, `CREATE TABLE` is used to create a new table, `ALTER TABLE` is used to add a column to an existing table, `DROP TABLE` is used to delete a table, etc.
- DDL commands are executed when the database is initialized or when structural changes are required.
- Once DDL statements are executed, the structure of the database gets modified and the changes are saved in the data dictionary.
- The data dictionary contains metadata, which is data about the data in the database. It stores information about the database structure and is updated automatically whenever DDL commands are executed.

**Advantages:**
- Defines the database structure efficiently.
- Offers flexibility to change the structure as per requirements.
- Maintains data dictionary to store metadata.

**Disadvantages:**
- Executing DDL commands can be time-consuming for large databases.
- If not executed properly, it can corrupt the database.
- Requires exclusive access to objects which can affect performance at times.

**Examples:**
`CREATE DATABASE exampleDB;`
`CREATE TABLE customers (customer_id INT, customer_name VARCHAR(50));`
`ALTER TABLE customers ADD email VARCHAR(50);`
`DROP TABLE customers;`

**Applications:** DDL is fundamental to any database system to create and modify database objects. It is widely used to design and redesign the database structure based on the requirements.