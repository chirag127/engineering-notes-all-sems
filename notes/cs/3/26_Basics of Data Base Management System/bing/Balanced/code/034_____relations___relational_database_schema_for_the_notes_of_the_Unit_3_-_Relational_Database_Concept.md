# Relations and Relational Database Schema

- A **relation** is a set of tuples that have the same attributes. A tuple is a single row of data in a table. An attribute is a column or field name of a table. A relation can also be called a table or a relation variable.
- A **relational schema** is a collection of relation schemas for a whole database. A relation schema is a description of a relation, which specifies the name of the relation and the name and type of each attribute. A relational schema can also be called a database schema or a schema diagram.
- A relational schema is a collection of **metadata**, which is data about data. It describes the structure and constraints of data representing in a particular domain. It does not contain the actual data values, but only the names and types of the attributes.
- A relational schema acts as a **blueprint** or a design of the datasets within the database. It shows the **connections** between different tables, which contain related data. These connections are called **foreign keys**, which are attributes that refer to the primary key of another table.
- A relational schema can be represented using a **graphical notation** or a **textual notation**. A graphical notation uses symbols and lines to show the tables and their attributes, and the foreign keys and their references. A textual notation uses a list of relation names and their attributes, and the constraints on the attributes.
- A relational schema can have **benefits** such as:
  - It helps to **organize** and **structure** the data in a logical and consistent way.
  - It helps to **avoid** data **redundancy** and **inconsistency**, by ensuring that each data item is stored only once and in one place.
  - It helps to **enforce** data **integrity** and **security**, by defining the rules and restrictions on the data values and operations.
  - It helps to **facilitate** data **manipulation** and **querying**, by providing a common language and interface for accessing and modifying the data.
  - It helps to **document** and **communicate** the data model and design to the users and developers of the database.