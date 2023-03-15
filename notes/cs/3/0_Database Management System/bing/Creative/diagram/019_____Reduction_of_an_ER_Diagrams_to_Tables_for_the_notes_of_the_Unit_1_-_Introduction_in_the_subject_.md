# Reduction of an ER Diagram to Tables

An ER diagram is a graphical representation of the entities and relationships in a database. It shows the structure and constraints of the data. An ER diagram can be converted into a set of tables in a relational model, which can be implemented by a relational database management system (RDBMS).

The basic rules for converting an ER diagram into tables are:

- Convert all the entities in the diagram to tables. All the entities represented in the rectangular box in the ER diagram become independent tables in the database.
- Convert all the attributes of the entities to columns of the tables. All the attributes represented in the oval shape in the ER diagram become columns of the corresponding tables. The primary key of each table is underlined.
- Convert all the relationships in the diagram to tables or foreign keys. All the relationships represented in the diamond shape in the ER diagram can be converted in two ways:
  - If the relationship is one-to-one or one-to-many, then the primary key of the entity on the one side of the relationship becomes a foreign key in the table of the entity on the many side of the relationship. A foreign key is a column that references the primary key of another table.
  - If the relationship is many-to-many, then a separate table is created for the relationship, with the primary keys of both the entities as foreign keys in the table. The primary key of the relationship table is the combination of the foreign keys.
- Convert all the weak entities and identifying relationships in the diagram to tables. A weak entity is an entity that depends on another entity for its existence and identification. An identifying relationship is a relationship that connects a weak entity to its owner entity. A weak entity is represented by a double rectangular box and an identifying relationship is represented by a double diamond shape in the ER diagram. The rules for converting a weak entity and an identifying relationship are:
  - Create a separate table for the weak entity with the same name.
  - Include all the attributes of the weak entity as columns of the table.
  - Include the primary key of the owner entity as a foreign key in the table of the weak entity.
  - Declare the combination of the foreign key and the partial key of the weak entity as the primary key of the table. A partial key is an attribute that can uniquely identify a weak entity within the scope of its owner entity.

Here is an example of an ER diagram and its corresponding tables:

![ER diagram](https://www.w3cschoool.com/wp-content/uploads/2019/12/er-diagram-to-table.png)

The tables are:

**Student** (Student_ID, Name, Address, Phone)

**Course** (Course_ID, Title, Duration, Fee)

**Enroll** (Student_ID, Course_ID, Date, Grade)

**Subject** (Subject_ID, Name, Syllabus)

**Teach** (Course_ID, Subject_ID, Teacher)

**Lecture** (Lecture_ID, Topic, Date, Time, Room)

**Attend** (Student_ID, Lecture_ID, Attendance)