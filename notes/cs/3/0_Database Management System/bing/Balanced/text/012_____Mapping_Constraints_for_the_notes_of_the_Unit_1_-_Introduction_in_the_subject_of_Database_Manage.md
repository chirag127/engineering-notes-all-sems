### Mapping Constraints

- Mapping constraints are rules that define how the entities and relationships in an ER diagram can be mapped to the tables and columns in a relational schema.
- Mapping constraints can be classified into three types: cardinality ratio, participation constraint, and key constraint.
- Cardinality ratio specifies the maximum number of relationship instances that an entity can participate in. It can be one-to-one, one-to-many, many-to-one, or many-to-many.
- Participation constraint specifies whether the participation of an entity in a relationship is mandatory or optional. It can be total or partial.
- Key constraint specifies that an entity set must have a primary key that uniquely identifies each entity. It can also specify that a relationship set must have a primary key that uniquely identifies each relationship.

- Some examples of mapping constraints are:

  - A student can enroll in at most one department. This is a one-to-many cardinality ratio from department to student.
  - A department must have at least one student enrolled. This is a total participation constraint from department to student.
  - A student must have a unique student ID. This is a key constraint for the student entity set.
  - A student can register for multiple courses, and a course can have multiple students registered. This is a many-to-many cardinality ratio from student to course.
  - A course must have a unique course ID. This is a key constraint for the course entity set.
  - A student and a course can have at most one grade for each other. This is a key constraint for the grade relationship set.