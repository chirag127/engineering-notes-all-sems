### Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Data Base Management System

- Mapping constraints are also known as the cardinality ratio. They express the number of entities to which another entity can be related via a relationship set.
- Mapping constraints are useful in describing the relationship sets that involve more than two entity sets. They also help to specify the business rules and requirements of the database design.
- There are two types of mapping constraints in the entity relationship model:
  - Mapping cardinality or cardinality ratio: This corresponds to the number of relationship occurrences an entity can be involved in an entity-relationship model. There are four possible mapping cardinalities for binary relationship sets:
    - One-to-one: An entity in entity set A can be related to at most one entity in entity set B, and vice versa. For example, a person can have only one passport, and a passport belongs to only one person.
    - One-to-many: An entity in entity set A can be related to any number of entities in entity set B, but an entity in entity set B can be related to at most one entity in entity set A. For example, a department can have many employees, but an employee belongs to only one department.
    - Many-to-one: An entity in entity set A can be related to at most one entity in entity set B, but an entity in entity set B can be related to any number of entities in entity set A. For example, a student can enroll in only one course, but a course can have many students.
    - Many-to-many: An entity in entity set A can be related to any number of entities in entity set B, and vice versa. For example, a student can take many courses, and a course can have many students.
  - Participation constraints: This specifies whether the existence of an entity depends on its being related to another entity via the relationship set. There are two types of participation constraints:
    - Total participation: This means that every entity in the entity set must participate in at least one relationship in the relationship set. For example, every employee must work for a department. Total participation is also called existence dependency.
    - Partial participation: This means that some entities in the entity set may not participate in any relationship in the relationship set. For example, some courses may not have any students enrolled. Partial participation is also called weak entity.

- Mapping constraints can be represented by using different notations in the entity relationship diagrams. For example, the cardinality ratio can be shown by using the symbols 1, N, or M on the relationship lines, and the participation constraints can be shown by using double lines for total participation and single lines for partial participation. Here is an example of an entity relationship diagram with mapping constraints:

![ER diagram with mapping constraints](https://www.educba.com/wp-content/uploads/2019/12/Mapping-Constraints-in-DBMS-1.png)