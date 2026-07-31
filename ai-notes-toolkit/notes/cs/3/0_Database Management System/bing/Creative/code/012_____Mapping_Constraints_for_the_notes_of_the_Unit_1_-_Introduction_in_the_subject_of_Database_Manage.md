### Mapping Constraints for the notes of the Unit 1 - Introduction in the subject of Database Management System

- Mapping constraints are rules that define how many entities can be associated with each other in a relationship set .
- Mapping constraints are also known as cardinality ratios or cardinalities.
- Mapping constraints are useful for describing the relationships that involve more than two entity sets, such as ternary or n-ary relationships.
- Mapping constraints can be classified into four types :
  - One-to-one: An entity in one entity set can be associated with at most one entity in another entity set, and vice versa. For example, a person can have at most one passport, and a passport belongs to at most one person.
  - One-to-many: An entity in one entity set can be associated with many entities in another entity set, but an entity in the other entity set can be associated with at most one entity in the first entity set. For example, a department can have many employees, but an employee works for at most one department.
  - Many-to-one: An entity in one entity set can be associated with at most one entity in another entity set, but an entity in the other entity set can be associated with many entities in the first entity set. For example, a student can enroll in at most one course, but a course can have many students.
  - Many-to-many: An entity in one entity set can be associated with many entities in another entity set, and an entity in the other entity set can be associated with many entities in the first entity set. For example, a student can borrow many books from a library, and a book can be borrowed by many students.
- Mapping constraints can be represented graphically using the entity-relationship (ER) diagram notation . The cardinality ratio is indicated by placing the appropriate number (1 or N) on the relationship line near the entity set. For example, the following ER diagram shows a one-to-many relationship between department and employee:

![ER diagram](https://www.educba.com/wp-content/uploads/2019/11/Mapping-Constraints-in-DBMS-1.png)

- Mapping constraints can also be enforced using primary and foreign key constraints in the relational database model . A primary key is a column or a set of columns that uniquely identifies each row in a table. A foreign key is a column or a set of columns that references the primary key of another table. A foreign key constraint ensures that the values in the foreign key column match the values in the referenced primary key column. For example, the following SQL statements create two tables, department and employee, with a one-to-many relationship enforced by a foreign key constraint:

```sql
CREATE TABLE department (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50) NOT NULL,
  dept_id INT NOT NULL,
  FOREIGN KEY (dept_id) REFERENCES department (dept_id)
);
```

- Mapping constraints are important for ensuring the consistency and integrity of the data in a database. They also help to avoid redundancy and anomalies in the data. Mapping constraints should be defined based on the business rules and requirements of the application domain .