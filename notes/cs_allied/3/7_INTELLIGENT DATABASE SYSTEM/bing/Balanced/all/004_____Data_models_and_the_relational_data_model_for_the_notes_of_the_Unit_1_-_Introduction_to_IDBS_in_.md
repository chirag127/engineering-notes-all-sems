# Data models and the relational data model

## Data models
- A data model is a **conceptual representation** of the data, their relationships, and the rules that govern them.
- A data model helps to **organize**, **understand**, and **communicate** the data and their meaning.
- A data model also provides a way to **implement** the data in a physical system, such as a database or a data warehouse.
- There are different types of data models, such as **hierarchical**, **network**, **relational**, **entity-relationship**, **object-oriented**, and **dimensional**.

## Relational data model
- The relational data model is the most widely used data model for data storage and processing.
- The relational data model was proposed by **E.F. Codd** in 1970.
- The relational data model is based on the **mathematical concept** of a relation, which is a **set of tuples** (or rows) with the same **attributes** (or columns).
- In the relational data model, data are stored as **tables** (or relations), where each row represents an **entity** (or an instance of data) and each column represents an **attribute** (or a property of the entity).
- The tables are related to each other by **keys**, which are attributes that uniquely identify each row in a table.
- A **primary key** is a key that identifies each row in a table, and a **foreign key** is a key that references a primary key in another table.
- The relational data model supports the operations of **data definition**, **data manipulation**, and **transaction management** .
- Data definition allows the creation, modification, and deletion of tables and their attributes.
- Data manipulation allows the insertion, update, deletion, and retrieval of data from the tables.
- Transaction management ensures the **consistency**, **isolation**, **durability**, and **atomicity** of the data operations.
- The relational data model is based on a set of **relational algebra** operations, such as **selection**, **projection**, **join**, **union**, **intersection**, and **difference**, that can be applied to the tables to manipulate and query the data.
- The relational data model can be expressed using a **relational schema**, which is a **diagram** that shows the tables, their attributes, and their relationships.
- The relational schema can also include **constraints**, which are **rules** that specify the **validity** and **integrity** of the data in the tables.
- An example of a constraint is a **domain constraint**, which defines the **range of values** that an attribute can take.
- Another example is a **referential integrity constraint**, which ensures that a foreign key value in one table matches a primary key value in another table .
- The relational data model can be implemented using a **relational database management system (RDBMS)**, which is a software system that provides the functionality of data definition, data manipulation, and transaction management for the relational data model.
- Some examples of RDBMS are **Oracle**, **MySQL**, **PostgreSQL**, and **SQLite** .