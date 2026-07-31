# Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Data Base Management System

- Mapping constraints are data constraints that express the number of entities to which another entity can be related via a relationship set .
- Mapping constraints are also known as the cardinality ratio, which corresponds to the number of relationship occurrences an entity can be involved in an entity-relationship model.
- Mapping constraints are most useful in describing the relationship sets that involve more than two entity sets, such as ternary or n-ary relationships.
- Mapping constraints can be classified into two types: participation constraints and cardinality constraints.

## Participation Constraints
- Participation constraints specify whether the existence of an entity depends on its being related to another entity via the relationship set.
- Participation constraints can be either total or partial.
- Total participation means that every entity in the entity set must participate in at least one relationship in the relationship set.
- Partial participation means that some entities in the entity set may not participate in any relationship in the relationship set.
- Participation constraints are shown by a double line connecting the entity set and the relationship set in an ER diagram.

## Cardinality Constraints
- Cardinality constraints specify the maximum number of relationship instances that an entity can participate in.
- Cardinality constraints can be one-to-one, one-to-many, many-to-one, or many-to-many.
- One-to-one means that an entity in one entity set can be related to at most one entity in another entity set, and vice versa.
- One-to-many means that an entity in one entity set can be related to many entities in another entity set, but an entity in the other entity set can be related to at most one entity in the first entity set.
- Many-to-one means that an entity in one entity set can be related to at most one entity in another entity set, but an entity in the other entity set can be related to many entities in the first entity set.
- Many-to-many means that an entity in one entity set can be related to many entities in another entity set, and an entity in the other entity set can be related to many entities in the first entity set.
- Cardinality constraints are shown by placing numbers or symbols on the relationship lines in an ER diagram.

## Example of Mapping Constraints
- Consider the following ER diagram of a university database, where the entity sets are Student, Course, and Instructor, and the relationship sets are Enroll, Teach, and Advise.

![ER diagram of a university database](https://opentextbc.ca/dbdesign01/wp-content/uploads/sites/701/2019/09/ERD-University-Database.png)

- The participation constraints are as follows:
  - Every student must enroll in at least one course, so the participation of Student in Enroll is total.
  - Every course must have at least one student enrolled, so the participation of Course in Enroll is total.
  - Every instructor must teach at least one course, so the participation of Instructor in Teach is total.
  - Every course must have at least one instructor teaching it, so the participation of Course in Teach is total.
  - Every student must have exactly one instructor as an advisor, so the participation of Student in Advise is total.
  - Not every instructor must advise a student, so the participation of Instructor in Advise is partial.
- The cardinality constraints are as follows:
  - A student can enroll in many courses, but a course can have at most one student enrolled, so the cardinality of Enroll is one-to-many from Course to Student.
  - An instructor can teach many courses, but a course can have at most one instructor teaching it, so the cardinality of Teach is one-to-many from Course to Instructor.
  - A student can have only one instructor as an advisor, but an instructor can advise many students, so the cardinality of Advise is many-to-one from Student to Instructor.