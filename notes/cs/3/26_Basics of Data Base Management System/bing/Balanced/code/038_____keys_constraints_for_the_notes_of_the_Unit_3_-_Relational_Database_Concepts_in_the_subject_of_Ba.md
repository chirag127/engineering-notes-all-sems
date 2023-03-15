### Key Constraints in Relational Database

- Key constraints are rules that are defined for primary keys in a relational database. A primary key is a column or a set of columns that uniquely identifies each row in a table. 
- Key constraints ensure that the data in the primary key column(s) is unique and not null, and that each row can be referenced by other tables using foreign keys. 
- Key constraints can be classified into two types: single-attribute and composite. A single-attribute key constraint is applied on a single column, while a composite key constraint is applied on a combination of two or more columns. 
- Key constraints can be specified using the PRIMARY KEY keyword in the CREATE TABLE or ALTER TABLE statements. For example, to create a table named Student with a single-attribute primary key on the column StudentID, the following SQL statement can be used:

```sql
CREATE TABLE Student (
  StudentID INT PRIMARY KEY,
  Name VARCHAR(50),
  Age INT
);
```

- To create a table named Course with a composite primary key on the columns CourseID and Semester, the following SQL statement can be used:

```sql
CREATE TABLE Course (
  CourseID VARCHAR(10),
  Semester VARCHAR(10),
  Title VARCHAR(50),
  Instructor VARCHAR(50),
  PRIMARY KEY (CourseID, Semester)
);
```

- Key constraints can also be defined using the CONSTRAINT keyword and a constraint name. For example, to create a table named Enrollment with a composite primary key on the columns StudentID and CourseID, and a foreign key constraint on the column StudentID that references the Student table, the following SQL statement can be used:

```sql
CREATE TABLE Enrollment (
  StudentID INT,
  CourseID VARCHAR(10),
  Grade CHAR(1),
  CONSTRAINT PK_Enrollment PRIMARY KEY (StudentID, CourseID),
  CONSTRAINT FK_Student FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);
```

- Key constraints have some limitations and rules that must be followed. For example, a table can have only one primary key constraint, a primary key cannot exceed 16 columns and a total key length of 900 bytes, and a foreign key must reference a primary key or a unique key in another table.  
- Key constraints are important for maintaining the integrity, consistency, and accuracy of the data in a relational database. They prevent duplicate, null, or invalid values in the primary key columns, and ensure that the relationships between tables are enforced and consistent.