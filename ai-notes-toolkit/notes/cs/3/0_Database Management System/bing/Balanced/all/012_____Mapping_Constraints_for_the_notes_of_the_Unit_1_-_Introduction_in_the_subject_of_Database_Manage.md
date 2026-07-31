# Mapping Constraints for the notes of the Unit 1 - Introduction in the subject of Database Management System

- Mapping constraints are rules that define how many entities can be associated with each other in a relationship set .
- Mapping constraints are also known as cardinality ratios or cardinalities.
- Mapping constraints are important for designing and validating the entity-relationship (ER) model of a database .
- Mapping constraints can be classified into four types based on the number of entities involved in a relationship set  :
  - One-to-one: Each entity in one entity set can be related to at most one entity in another entity set, and vice versa. For example, each employee can have one office, and each office can be occupied by one employee.
  - One-to-many: Each entity in one entity set can be related to many entities in another entity set, but each entity in the other entity set can be related to at most one entity in the first entity set. For example, each department can have many employees, but each employee can belong to one department.
  - Many-to-one: Each entity in one entity set can be related to at most one entity in another entity set, but each entity in the other entity set can be related to many entities in the first entity set. This is the inverse of one-to-many. For example, each employee can have one manager, but each manager can supervise many employees.
  - Many-to-many: Each entity in one entity set can be related to many entities in another entity set, and vice versa. For example, each student can enroll in many courses, and each course can have many students.
- Mapping constraints can be represented graphically using the ER diagram notation  . The cardinality ratio is indicated by placing a number (1 or N) or a symbol (| or <) near the end of the relationship line that connects the entity sets. For example, the following ER diagram shows a one-to-many relationship between department and employee:

![ER diagram of one-to-many relationship](https://www.educba.com/wp-content/uploads/2019/12/Mapping-Constraints-in-DBMS-1.png)

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

- Mapping constraints can also be specified using the minimum and maximum participation of each entity set in a relationship set  . The minimum participation indicates whether an entity must participate in at least one relationship instance or not. The maximum participation indicates whether an entity can participate in more than one relationship instance or not. The participation constraints are indicated by placing a double line (for total participation) or a single line (for partial participation) between the entity set and the relationship set. For example, the following ER diagram shows that each employee must belong to one and only one department, and each department can have zero or more employees:

![ER diagram of participation constraints](https://www.educba.com/wp-content/uploads/2019/12/Mapping-Constraints-in-DBMS-2.png)

- Mapping constraints are useful for ensuring the consistency and integrity of the data in a database. They also help to avoid redundancy and ambiguity in the data model  .