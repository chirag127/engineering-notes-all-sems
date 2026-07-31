# E-R Modeling from the Problem Statements

- Entity-Relationship (ER) model is a high-level data model that represents the logical design of a database.
- ER model abstracts real-world objects or concepts as entities, and their associations as relationships.
- ER model helps to identify the possible entity sets, their attributes, and the constraints among them from a given problem statement.
- ER model can be represented pictorially as an ER diagram, using graphical notations for entities, relationships, and attributes.
- ER diagram can be used to design, analyze, or troubleshoot relational databases used in business processes or information systems.
- ER model can be extended to Enhanced Entity-Relationship (EER) model, which supports more complex and detailed design of databases.

## Steps to create an ER diagram from a problem statement

- Identify the main entities involved in the problem domain. Entities are usually nouns in the problem statement, such as student, school, course, etc.
- Identify the attributes of each entity. Attributes are usually adjectives or qualifiers that describe the entities, such as name, age, address, etc.
- Identify the key attribute or primary key of each entity. A key attribute uniquely identifies each instance of an entity, such as student ID, course code, etc.
- Identify the relationships among the entities. Relationships are usually verbs or phrases that indicate how the entities are associated, such as enrolls, teaches, belongs to, etc.
- Identify the cardinality and participation constraints of each relationship. Cardinality specifies how many instances of one entity can be related to one instance of another entity, such as one-to-one, one-to-many, many-to-many, etc. Participation specifies whether an entity must participate in a relationship or not, such as total or partial.
- Draw the ER diagram using the appropriate symbols and notations for entities, attributes, relationships, and constraints. Refer to the graphical notations for ER diagram for the standard symbols and notations.

## Example of an ER diagram from a problem statement

- Problem statement: A university consists of a number of departments. Each department offers a number of courses. Each course may have one or more instructors, and each instructor may teach one or more courses. Each course has a number of enrolled students, and each student may enroll in a number of courses. Each student has a unique ID, a name, and a major. Each instructor has a unique ID, a name, and a salary. Each department has a unique name, a head, and a budget.

- ER diagram:

![ER diagram example](https://i.imgur.com/0xZxq8a.png)

- Explanation:

  - The entities are: student, instructor, course, and department.
  - The attributes of each entity are: student (ID, name, major), instructor (ID, name, salary), course (code, title, credits), and department (name, head, budget).
  - The key attributes of each entity are: student (ID), instructor (ID), course (code), and department (name).
  - The relationships among the entities are: enrolls (between student and course), teaches (between instructor and course), and offers (between department and course).
  - The cardinality and participation constraints of each relationship are: enrolls (many-to-many, total on both sides), teaches (many-to-many, total on both sides), and offers (one-to-many, total on the department side and partial on the course side).