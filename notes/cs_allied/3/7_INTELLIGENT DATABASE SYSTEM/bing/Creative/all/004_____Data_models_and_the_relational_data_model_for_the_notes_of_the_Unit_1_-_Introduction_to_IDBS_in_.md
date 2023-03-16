# Data models and the relational data model

## Data models

- A data model is a **conceptual representation** of the data, the relationships between data, and the rules and constraints on the data in an information system.
- A data model helps to **design**, **implement**, **manage**, and **use** databases effectively and efficiently.
- A data model can be represented using different **notations** and **techniques**, such as entity-relationship diagrams, UML class diagrams, relational schemas, etc.
- A data model can be classified into three levels: **conceptual**, **logical**, and **physical**.
  - A conceptual data model is a high-level, abstract, and independent view of the data that captures the essential entities, attributes, and relationships without considering any implementation details.
  - A logical data model is a more detailed and structured view of the data that maps the conceptual data model to a specific data model, such as relational, hierarchical, network, etc.
  - A physical data model is a low-level, concrete, and dependent view of the data that specifies how the data will be stored, accessed, and manipulated in a physical database.

## Relational data model

- The relational data model is the most widely used data model for database systems  .
- The relational data model is based on the **mathematical concept** of a relation, which is a set of tuples (or rows) that have the same attributes (or columns)  .
- The relational data model represents data as a collection of **tables** (or relations), where each table has a unique name and a set of attributes  .
- The attributes of a table are also called **columns** or **fields**, and the tuples of a table are also called **rows** or **records**  .
- Each attribute of a table has a **domain**, which is the set of possible values that the attribute can take  .
- Each tuple of a table has a **primary key**, which is a set of one or more attributes that uniquely identifies the tuple within the table  .
- The tables of a relational data model can have **relationships** with each other, which are established by using **foreign keys**, which are attributes that refer to the primary keys of other tables  .
- The relational data model supports various **operations** on the data, such as data definition, data manipulation, data integrity, data security, and data query  .
- The relational data model uses a **query language**, such as SQL, to perform operations on the data  .
- The relational data model has many **advantages**, such as simplicity, flexibility, scalability, consistency, and independence  .
- The relational data model also has some **disadvantages**, such as complexity, redundancy, performance, and security  .

## Example of a relational data model

- Consider a relational data model for a university information system, which consists of the following tables:

| Student | (SID, Name, Major, GPA) |
| --- | --- |
| Course | (CID, Title, Credits, Instructor) |
| Enrollment | (SID, CID, Semester, Grade) |

- The primary keys of the tables are underlined, and the foreign keys are italicized.
- The tables have the following relationships:

  - A student can enroll in many courses, and a course can have many students enrolled. This is a **many-to-many** relationship, which is represented by the Enrollment table.
  - A course can have only one instructor, and an instructor can teach many courses. This is a **one-to-many** relationship, which is represented by the Instructor attribute in the Course table.

- The tables can be queried using SQL, for example:

  - To find the names and majors of all students who have enrolled in CS101 in Spring 2023, we can use the following SQL query:

  ```sql
  SELECT Student.Name