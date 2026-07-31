# ER Model Concepts

The ER model is a conceptual data model that describes the entities, attributes, and relationships in a database. It is used to design and represent the logical structure of a database. The ER model consists of the following basic concepts:

- **Entity**: An entity is a real-world object or thing that can be identified uniquely. For example, a student, a course, a teacher, etc. An entity is represented by a rectangle in an ER diagram.
- **Entity type**: An entity type is a collection of entities that share the same properties or characteristics. For example, the entity type Student represents all the students in a database. An entity type has a name and a set of attributes.
- **Entity set**: An entity set is a set of entities of the same entity type. For example, the entity set Students contains all the student entities in a database. An entity set is also represented by a rectangle in an ER diagram.
- **Attribute**: An attribute is a property or characteristic of an entity or a relationship. For example, the attributes of the entity type Student are Name, Roll No, Age, etc. An attribute has a name and a domain (or data type). An attribute is represented by an ellipse in an ER diagram.
- **Attribute types**: There are different types of attributes based on their values and dependencies. Some common attribute types are:

  - **Simple attribute**: An attribute that cannot be divided into subparts. For example, Name, Age, etc.
  - **Composite attribute**: An attribute that can be divided into subparts. For example, Address can be divided into Street, City, State, etc.
  - **Single-valued attribute**: An attribute that has only one value for a given entity. For example, Roll No, Age, etc.
  - **Multi-valued attribute**: An attribute that can have more than one value for a given entity. For example, Phone No, Email, etc.
  - **Derived attribute**: An attribute that can be derived from other attributes. For example, Total Marks can be derived from Marks of different subjects.
  - **Key attribute**: An attribute that can uniquely identify an entity in an entity set. For example, Roll No, Employee ID, etc.

- **Relationship**: A relationship is an association or connection between two or more entities. For example, a student enrolls in a course, a teacher teaches a course, etc. A relationship is represented by a diamond in an ER diagram.
- **Relationship type**: A relationship type is a collection of relationships that share the same meaning and properties. For example, the relationship type Enrolls represents all the enrollments of students in courses. A relationship type has a name and a degree (or number of participating entity types).
- **Relationship set**: A relationship set is a set of relationships of the same relationship type. For example, the relationship set Enrolls contains all the enrollments of students in courses in a database. A relationship set is also represented by a diamond in an ER diagram.
- **Relationship degree**: The degree of a relationship is the number of entity types that participate in the relationship. For example, the degree of the relationship type Enrolls is 2, as it involves two entity types: Student and Course. Some common relationship degrees are:

  - **Unary relationship**: A relationship that involves only one entity type. For example, a student is a friend of another student.
  - **Binary relationship**: A relationship that involves two entity types. For example, a student enrolls in a course.
  - **Ternary relationship**: A relationship that involves three entity types. For example, a student takes a course from a teacher.
  - **N-ary relationship**: A relationship that involves n entity types. For example, a student works on a project with other students and a supervisor.

- **Relationship cardinality**: The cardinality of a relationship is the number of occurrences of one entity type that can be associated with one occurrence of another entity type. For example, the cardinality of the relationship type Enrolls is one-to-many, as one student can enroll in many courses, but one course can be enrolled by only one student. Some common relationship cardinalities are:

  - **One-to-one**: A relationship where one entity of one entity type can be associated with only one entity of another entity type. For example, a student has a locker.
  - **One-to-many**: A relationship where one entity of one entity type can be associated with many entities of another entity type. For example, a teacher teaches many courses.
  - **Many-to-one**: A relationship where many entities of one entity