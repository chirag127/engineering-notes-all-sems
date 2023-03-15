### Relational Data Model Concepts

- A relational data model is a way of representing data as a collection of tables, where each table consists of rows and columns .
- The tables are also called relations, and each row in a table is called a tuple .
- Each column in a table is called an attribute, and it represents a property or characteristic of the tuples in the relation .
- A relation schema is the name of the relation and the set of attributes that define it . For example, STUDENT(RollNo, Name, Age, Address) is a relation schema for a table that stores information about students.
- A relation instance is a snapshot of the data in a relation at a given point in time . For example, the following table is a relation instance of the STUDENT relation schema:

| RollNo | Name | Age | Address |
|--------|------|-----|---------|
| 101    | Alice| 20  | A1      |
| 102    | Bob  | 21  | A2      |
| 103    | Carol| 19  | A3      |

- The degree of a relation is the number of attributes in its schema . For example, the degree of the STUDENT relation is 4.
- The cardinality of a relation is the number of tuples in its instance . For example, the cardinality of the STUDENT relation is 3.
- A primary key is an attribute or a set of attributes that uniquely identifies each tuple in a relation . For example, RollNo is a primary key for the STUDENT relation.
- A foreign key is an attribute or a set of attributes in one relation that refers to the primary key of another relation . For example, if there is another relation called COURSE(CourseID, CourseName, Instructor), then CourseID can be a foreign key in a relation called ENROLLMENT(RollNo, CourseID, Grade) that links students and courses.
- A relational database is a collection of relations that are logically connected by primary and foreign keys . For example, the following diagram shows a relational database that consists of four relations: STUDENT, COURSE, ENROLLMENT, and INSTRUCTOR.

![Relational Database Diagram](https://www.guru99.com/images/1/Relational-Model-Concepts.png)

- Relational integrity constraints are rules that ensure the validity and consistency of the data in a relational database . There are two types of relational integrity constraints: domain constraints and referential integrity constraints.
- Domain constraints specify the set of permissible values for each attribute in a relation . For example, the domain constraint for the Age attribute in the STUDENT relation can be that it must be a positive integer.
- Referential integrity constraints ensure that a foreign key value in one relation either matches a primary key value in another relation or is null . For example, the referential integrity constraint for the CourseID attribute in the ENROLLMENT relation can be that it must exist in the COURSE relation or be null.
- Relational data modeling is the process of designing a relational database by identifying the entities, attributes, and relationships that are relevant for the data requirements . Relational data modeling involves the following steps:
  - Define the purpose and scope of the database
  - Identify the entities and their attributes
  - Determine the primary and foreign keys for each relation
  - Normalize the relations to avoid data redundancy and anomalies
  - Draw the entity-relationship diagram to show the logical structure of the database
  - Implement the physical design of the database using a relational database management system (RDBMS)