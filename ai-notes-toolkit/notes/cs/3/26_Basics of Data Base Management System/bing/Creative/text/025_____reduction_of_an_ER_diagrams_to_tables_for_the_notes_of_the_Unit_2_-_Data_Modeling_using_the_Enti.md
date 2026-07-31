### Reduction of an ER diagram to tables

- An ER diagram is a graphical representation of the entities and relationships in a database.
- A table is a collection of rows and columns that store data in a database.
- The process of converting an ER diagram to tables is called reduction or mapping.
- The reduction of an ER diagram to tables involves the following steps:

  - For each entity type in the ER diagram, create a table with the same name and include all the attributes as columns. The primary key of the table is the same as the key attribute of the entity type.
  - For each one-to-one or one-to-many relationship type in the ER diagram, identify the table that corresponds to the entity type on the many side of the relationship. Add a foreign key column to this table that references the primary key of the table on the one side of the relationship. The foreign key column can have the same name as the primary key column or a different name. If the relationship type has any attributes, include them as columns in the table on the many side of the relationship.
  - For each many-to-many relationship type in the ER diagram, create a new table with the same name as the relationship type. Include the primary keys of the tables that correspond to the entity types on both sides of the relationship as foreign key columns in the new table. The primary key of the new table is the combination of the foreign key columns. If the relationship type has any attributes, include them as columns in the new table.
  - For each weak entity type in the ER diagram, create a table with the same name and include all the attributes as columns. Include the primary key of the table that corresponds to the strong entity type that owns the weak entity type as a foreign key column in the weak entity table. Declare the combination of the foreign key column and the partial key attribute of the weak entity type as the primary key of the weak entity table.
  - For each multivalued attribute in the ER diagram, create a new table with the same name as the attribute. Include the primary key of the table that corresponds to the entity type that has the multivalued attribute as a foreign key column in the new table. Include the multivalued attribute as another column in the new table. The primary key of the new table is the combination of the foreign key column and the multivalued attribute column.

- Here is an example of an ER diagram and its corresponding tables:

![ER diagram](https://tutorialcup.com/wp-content/uploads/2019/01/er-diagram-to-tables.png)

| LECTURE | | STUDENT | | SUBJECT | | COURSE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LECTURE_ID | LECTURE_NAME | STUDENT_ID | STUDENT_NAME | SUBJECT_ID | SUBJECT_NAME | COURSE_ID | COURSE_NAME |
| PK | | PK | | PK | | PK | |

| LECTURE_STUDENT | | LECTURE_SUBJECT | | STUDENT_SUBJECT | | STUDENT_COURSE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LECTURE_ID | STUDENT_ID | LECTURE_ID | SUBJECT_ID | STUDENT_ID | SUBJECT_ID | STUDENT_ID | COURSE_ID |
| FK | FK | PK | PK | FK | FK | PK | PK |