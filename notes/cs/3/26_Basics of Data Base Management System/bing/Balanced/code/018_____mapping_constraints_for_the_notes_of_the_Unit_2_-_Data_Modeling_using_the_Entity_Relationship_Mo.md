### Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Data Base Management System

- Mapping constraints are also known as the cardinality ratio. They express the number of entities to which another entity can be related via a relationship set.
- Mapping constraints are most useful in describing the relationship sets that involve more than two entity sets.
- There are two types of mapping constraints in the entity relationship model:
  - Mapping cardinality or cardinality ratio: It specifies the maximum number of relationship instances that an entity can participate in. There are four possible mapping cardinalities for binary relationship sets :
    - One to one: Each entity in the relationship set can be related to at most one entity of the other set. For example, a person can have at most one passport, and a passport belongs to at most one person.
    - One to many: An entity in one set can be related to many entities of the other set, but not vice versa. For example, a department can have many employees, but an employee belongs to at most one department.
    - Many to one: An entity in one set can be related to at most one entity of the other set, but not vice versa. For example, a course can have at most one instructor, but an instructor can teach many courses.
    - Many to many: An entity in one set can be related to many entities of the other set, and vice versa. For example, a student can enroll in many courses, and a course can have many students.
  - Participation constraints: They specify whether the existence of an entity depends on its being related to another entity via the relationship set. There are two types of participation constraints:
    - Total participation: Every entity in the entity set must participate in at least one relationship in the relationship set. For example, every employee must work for a department.
    - Partial participation: Some entities in the entity set may not participate in any relationship in the relationship set. For example, some instructors may not teach any course.