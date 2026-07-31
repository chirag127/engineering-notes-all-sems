### Relations and Relational Database Schema

- A **relation** is a set of tuples that have the same attributes. A tuple is a single row of data in a table. An attribute is a column or field name of a table. A relation can also be called a table or a file.
- A **relational database** is a collection of relations that store data in a structured and organized way. A relational database follows the principles of the relational data model, which is based on mathematical set theory and logic.
- A **relational database schema** is a blueprint or plan that a database uses to store and organize information. It describes the structure of the data within the database and shows the connections between different tables, which contain related data.
- A **relation schema** is a part of the relational database schema that defines the name, attributes, and constraints of a relation. A relation schema can be written as R(A1, A2, ..., An), where R is the name of the relation and A1, A2, ..., An are the attributes of the relation.
- A **database schema** is the collection of relation schemas for a whole database. A database schema is a collection of meta-data, which means data about data. A database schema describes the structure and constraints of data representing in a particular domain.
- A **database instance** is a snapshot of the data in a database at a given point in time. A database instance can change as the data in the database is inserted, updated, deleted, or queried. A database instance is also called a database state.

#### Example of a relational database schema

Consider a relational database schema for a university that contains the following relation schemas:

- Student(SID, Name, Major, GPA)
- Course(CID, Title, Instructor, Credits)
- Enroll(SID, CID, Grade)

The relation schemas define the name, attributes, and constraints of each relation. For example, the Student relation schema defines that each student has a unique SID (student ID), a name, a major, and a GPA (grade point average).

The relational database schema also shows the connections between the relations. For example, the Enroll relation schema connects the Student and Course relations by using the SID and CID attributes as foreign keys, which refer to the primary keys of the other relations. A foreign key is a constraint that ensures that the values in one relation match the values in another relation. A primary key is a constraint that ensures that each tuple in a relation has a unique identifier.

The following diagram shows the relational database schema for the university database:

![Relational database schema for university database](https://i.imgur.com/6w7Zlq3.png)

The diagram uses the following notation:

- The name of each relation is written in a box, followed by the attributes in parentheses.
- The primary key attribute of each relation is underlined.
- The foreign key attribute of each relation is marked with an asterisk (*).
- The lines between the boxes indicate the connections between the relations.