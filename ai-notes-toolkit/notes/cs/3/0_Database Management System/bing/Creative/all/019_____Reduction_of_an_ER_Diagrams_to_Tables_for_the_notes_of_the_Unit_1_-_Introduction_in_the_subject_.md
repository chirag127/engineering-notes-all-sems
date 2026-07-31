# Reduction of an ER Diagram to Tables

An ER diagram is a graphical representation of the entities and relationships in a database. It shows the structure and constraints of the data. An ER diagram can be converted into a relational table, which is a collection of rows and columns that store the data. The conversion of an ER diagram to tables involves the following steps:

- Convert each entity set in the ER diagram into a table. The table name should be the same as the entity set name. The table should have columns for each attribute of the entity set. The primary key of the table should be the same as the primary key of the entity set. If the entity set has a composite primary key, then the table should have a composite primary key as well.
- Convert each relationship set in the ER diagram into a table. The table name should be the same as the relationship set name. The table should have columns for each attribute of the relationship set. The primary key of the table should be a combination of the foreign keys that reference the tables of the participating entity sets. If the relationship set has a composite primary key, then the table should have a composite primary key as well. If the relationship set is many-to-many, then the table should have only the foreign keys as columns. If the relationship set is one-to-many or one-to-one, then the table can be merged with the table of the entity set that participates in the relationship set as the many or the optional side. The foreign key column should be added to the merged table to reference the table of the entity set that participates in the relationship set as the one or the mandatory side.
- Convert each weak entity set in the ER diagram into a table. The table name should be the same as the weak entity set name. The table should have columns for each attribute of the weak entity set. The primary key of the table should be a combination of the foreign key that references the table of the identifying entity set and the partial key of the weak entity set. The foreign key column should also be part of the primary key. If the weak entity set has a composite partial key, then the table should have a composite primary key as well.

Here is an example of an ER diagram and its corresponding tables:

![ER diagram](https://www.w3cschoool.com/wp-content/uploads/2019/10/er-diagram.png)

The tables are:

**Student** (Student_ID, Name, Address, Phone, Email)  
**Primary Key**: Student_ID

**Course** (Course_ID, Title, Credits)  
**Primary Key**: Course_ID

**Enroll** (Student_ID, Course_ID, Semester, Grade)  
**Primary Key**: (Student_ID, Course_ID)  
**Foreign Key**: Student_ID references Student  
**Foreign Key**: Course_ID references Course

**Department** (Dept_ID, Name, Location, Phone)  
**Primary Key**: Dept_ID

**Instructor** (Instructor_ID, Name, Salary, Dept_ID)  
**Primary Key**: Instructor_ID  
**Foreign Key**: Dept_ID references Department

**Teach** (Instructor_ID, Course_ID, Semester)  
**Primary Key**: (Instructor_ID, Course_ID)  
**Foreign Key**: Instructor_ID references Instructor  
**Foreign Key**: Course_ID references Course

**Project** (Project_ID, Name, Budget, Dept_ID)  
**Primary Key**: Project_ID  
**Foreign Key**: Dept_ID references Department

**Work_On** (Employee_ID, Project_ID, Hours)  
**Primary Key**: (Employee_ID, Project_ID)  
**Foreign Key**: Employee_ID references Employee  
**Foreign Key**: Project_ID references Project

**Employee** (Employee_ID, Name, Address, Phone, Email, Instructor_ID)  
**Primary Key**: Employee_ID  
**Foreign Key**: Instructor_ID references Instructor