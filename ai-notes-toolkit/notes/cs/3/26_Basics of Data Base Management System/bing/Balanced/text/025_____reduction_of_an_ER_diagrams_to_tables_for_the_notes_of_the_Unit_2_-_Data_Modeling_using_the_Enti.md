### Reduction of an ER diagram to tables

An ER diagram is a graphical representation of the entities and relationships in a database. It shows the structure and constraints of the data. To implement the database, we need to convert the ER diagram into a collection of tables. Each table represents an entity set or a relationship set in the ER diagram. The following are the general rules for converting an ER diagram to tables  :

- For each strong entity set, create a table with the same name and include all the attributes as columns. Declare the primary key attribute(s) of the entity set as the primary key of the table.
- For each weak entity set, create a table with the same name and include all the attributes as columns. Include the primary key attribute(s) of the owner entity set as foreign key(s) in the weak entity set table. Declare the combination of foreign key(s) and partial key attribute(s) of the weak entity set as the primary key of the table.
- For each one-to-one or one-to-many relationship set, identify the entity set that participates as the many side and include the primary key attribute(s) of the other entity set as foreign key(s) in the many side table. If the relationship set has any attributes, include them as columns in the many side table as well. If the relationship set is one-to-one and both entity sets are strong, choose either entity set to include the foreign key.
- For each many-to-many relationship set, create a table with the same name and include the primary key attribute(s) of both participating entity sets as foreign key(s) in the relationship set table. Declare the combination of foreign key(s) as the primary key of the table. If the relationship set has any attributes, include them as columns in the relationship set table as well.
- For each multivalued attribute, create a separate table with the same name and include the attribute as a column. Include the primary key attribute(s) of the entity set or relationship set that the multivalued attribute belongs to as foreign key(s) in the multivalued attribute table. Declare the combination of foreign key(s) and multivalued attribute as the primary key of the table.
- For each derived attribute, do not include it as a column in the table. Instead, use a function or a query to compute its value from the other attributes when needed.

Here is an example of an ER diagram and its corresponding tables:

![ER diagram example](https://www.w3cschoool.com/wp-content/uploads/2020/12/er-diagram.png)

The tables are:

**LECTURE** (Lecture_ID, Lecture_Name, Lecture_Duration, Course_ID)  
Primary key: Lecture_ID  
Foreign key: Course_ID references COURSE(Course_ID)

**STUDENT** (Student_ID, Student_Name, Student_Address, Student_Phone)  
Primary key: Student_ID

**SUBJECT** (Subject_ID, Subject_Name, Subject_Credit)  
Primary key: Subject_ID

**COURSE** (Course_ID, Course_Name, Course_Fee)  
Primary key: Course_ID

**ENROLL** (Student_ID, Subject_ID, Marks)  
Primary key: (Student_ID, Subject_ID)  
Foreign key: Student_ID references STUDENT(Student_ID)  
Foreign key: Subject_ID references SUBJECT(Subject_ID)

**TEACH** (Lecture_ID, Subject_ID)  
Primary key: (Lecture_ID, Subject_ID)  
Foreign key: Lecture_ID references LECTURE(Lecture_ID)  
Foreign key: Subject_ID references SUBJECT(Subject_ID)

**PHONE** (Student_ID, Phone_Number)  
Primary key: (Student_ID, Phone_Number)  
Foreign key: Student_ID references STUDENT(Student_ID)