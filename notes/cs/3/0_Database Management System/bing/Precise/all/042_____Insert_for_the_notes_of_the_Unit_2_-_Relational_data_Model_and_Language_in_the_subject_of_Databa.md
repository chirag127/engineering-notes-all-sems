# Unit 2 - Relational Data Model and Language

## Relational Data Model
- The relational data model is a way of representing data in the form of tables.
- Each table is called a relation and represents a set of tuples.
- Each tuple represents an object and its attributes.
- The attributes are the columns of the table and the values in the rows represent the values of the attributes for a particular object.

## Relational Algebra
- Relational algebra is a procedural query language for the relational data model.
- It consists of a set of operations that take one or more relations as input and produce a new relation as output.
- The basic operations of relational algebra are selection, projection, union, set difference, Cartesian product, and rename.
- These operations can be combined to form more complex queries.

## Structured Query Language (SQL)
- SQL is a declarative language used to manage and query relational databases.
- It is based on relational algebra and tuple relational calculus.
- SQL consists of a data definition language (DDL) and a data manipulation language (DML).
- The DDL is used to define the structure of the database, while the DML is used to manipulate the data stored in the database.

## Normalization
- Normalization is the process of organizing the data in a database to minimize redundancy and dependency.
- It involves decomposing a relation into smaller relations that satisfy certain normal forms.
- The most commonly used normal forms are first normal form (1NF), second normal form (2NF), and third normal form (3NF).
- Normalization helps to improve the efficiency and maintainability of the database.

## Transaction Management
- A transaction is a logical unit of work that must be either completed in its entirety or not at all.
- Transaction management is the process of ensuring the atomicity, consistency, isolation, and durability (ACID) properties of transactions.
- This is achieved through the use of concurrency control and recovery mechanisms.
- Concurrency control ensures that transactions do not interfere with each other, while recovery mechanisms ensure that the database can be restored to a consistent state in the event of a failure.
