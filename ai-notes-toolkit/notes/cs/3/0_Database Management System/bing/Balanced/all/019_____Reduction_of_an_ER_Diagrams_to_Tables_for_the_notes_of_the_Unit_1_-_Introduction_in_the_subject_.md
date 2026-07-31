# Reduction of an ER Diagram to Tables

An ER diagram is a graphical representation of the entities and relationships in a database. It shows the structure and constraints of the data. A table is a collection of rows and columns that store the data in a relational database. The process of converting an ER diagram to tables is called reduction or mapping. It involves the following steps:

- Convert all the entities in the diagram to tables. All the entities represented in the rectangular box in the ER diagram become independent tables in the database. Each table should have a primary key that uniquely identifies each row. The attributes of the entity become the columns of the table. For example, in the following ER diagram, the entities STUDENT, COURSE, and SUBJECT become tables with the same name and attributes.

![ER diagram example](https://tutorialcup.com/wp-content/uploads/2019/01/ER-diagram-to-tables-1.png)

- Convert all the relationships in the diagram to tables or foreign keys. All the relationships represented by the diamonds in the ER diagram can be mapped to tables or foreign keys depending on the cardinality and participation of the entities involved. There are three types of relationships: one-to-one, one-to-many, and many-to-many.

  - For a one-to-one relationship, choose one of the entities and add the primary key of the other entity as a foreign key in its table. The foreign key references the primary key of the related table. For example, in the following ER diagram, the relationship between STUDENT and LECTURE is one-to-one. We can choose STUDENT as the entity and add the primary key of LECTURE (Lecture_ID) as a foreign key in the STUDENT table.

  ![One-to-one relationship example](https://www.w3schools.blog/wp-content/uploads/2020/12/er-diagram-to-table-conversion-1.png)

  - For a one-to-many relationship, choose the entity on the many side and add the primary key of the entity on the one side as a foreign key in its table. The foreign key references the primary key of the related table. For example, in the following ER diagram, the relationship between COURSE and SUBJECT is one-to-many. We can choose SUBJECT as the entity on the many side and add the primary key of COURSE (Course_ID) as a foreign key in the SUBJECT table.

  ![One-to-many relationship example](https://www.w3schools.blog/wp-content/uploads/2020/12/er-diagram-to-table-conversion-2.png)

  - For a many-to-many relationship, create a new table for the relationship and include the primary keys of both the entities as foreign keys in the new table. The combination of the foreign keys becomes the primary key of the new table. The new table may also have additional attributes that describe the relationship. For example, in the following ER diagram, the relationship between STUDENT and COURSE is many-to-many. We can create a new table for the relationship called ENROLLMENT and include the primary keys of STUDENT (Student_ID) and COURSE (Course_ID) as foreign keys in the ENROLLMENT table. The combination of Student_ID and Course_ID becomes the primary key of the ENROLLMENT table. The new table may also have an attribute called Grade that describes the grade of the student in the course.

  ![Many-to-many relationship example](https://www.w3schools.blog/wp-content/uploads/2020/12/er-diagram-to-table-conversion-3.png)

- Convert all the weak entities in the diagram to tables. A weak entity is an entity that depends on another entity for its existence and identification. It is represented by a double-lined rectangle in the ER diagram. A weak entity has a partial key that distinguishes it from other entities of the same type, but it is not enough to identify it uniquely. A weak entity is associated with a strong entity through an identifying relationship, which is represented by a double-lined diamond in the ER diagram. The strong entity has a primary key that identifies it uniquely. To convert a weak entity to a table, follow these steps:

  - Create a separate table for the weak entity with the same name as the entity.
  - Include all the attributes of the weak entity as columns in the table, including the partial key.
  - Include the primary key of the strong entity as a foreign key in the weak entity table. The foreign key references the primary key of the related table.
  - Declare the combination of the foreign key and the partial key as the primary key of the weak entity table. This ensures that the weak entity is identified uniquely by