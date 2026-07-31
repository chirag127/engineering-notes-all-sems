# Entity Relationship Diagrams

- Entity Relationship Diagrams or ERDs are a type of structural diagram for use in database design   .
- ERDs are used in software engineering to produce a conceptual data model of an information system .
- ERDs help to identify different system elements and their relationships with each other.
- ERDs can be used as the basis for data flow diagrams or DFDs, which show how data flows through the system.
- ERDs consist of different symbols and connectors that represent the following concepts  :
  - Entity: A thing or object in the real world that is distinguishable from others. An entity can be a person, place, event, concept, or physical object. For example, a student, a course, a registration, etc. Entities are represented by rectangles in ERDs.
  - Attribute: A property or characteristic of an entity that describes it. An attribute can have a name and a value. For example, a student entity can have attributes such as name, ID, age, etc. Attributes are represented by ovals in ERDs.
  - Relationship: An association or link between two or more entities that expresses a business rule or a dependency. A relationship can have a name and a cardinality, which indicates the number of instances of each entity that can participate in the relationship. For example, a student can register for many courses, and a course can have many students. Relationships are represented by diamonds in ERDs.
  - Cardinality: The number of instances of one entity that can or must be associated with each instance of another entity. Cardinality can be one-to-one, one-to-many, many-to-one, or many-to-many. Cardinality is shown by placing numbers or symbols near the ends of the relationship lines in ERDs.
  - Primary Key: An attribute or a combination of attributes that uniquely identifies each instance of an entity. A primary key cannot have a null or duplicate value. For example, a student ID can be a primary key for the student entity. Primary keys are underlined in ERDs.
  - Foreign Key: An attribute or a combination of attributes in one entity that refers to the primary key of another entity. A foreign key establishes a relationship between two entities. For example, a course ID can be a foreign key in the registration entity that refers to the primary key of the course entity. Foreign keys are not shown in ERDs, but they are implied by the relationships.

- Here is an example of an ERD for a university information system:

![ERD example](https://www.conceptdraw.com/How-To-Guide/picture/erd-entity-relationship-diagram-software-engineering/Entity-Relationship-Diagram-Software-Engineering.png)

- In this ERD, there are four entities: Student, Course, Department, and Instructor. Each entity has some attributes, such as name, ID, title, etc. The primary keys are underlined, such as Student_ID, Course_ID, etc. There are also four relationships: Enrolled, Teaches, Belongs_to, and Manages. Each relationship has a name and a cardinality, such as 1:N, N:1, etc. For example, the Enrolled relationship between Student and Course has a cardinality of N:1, which means that one student can enroll in many courses, but one course can have only one student. The Teaches relationship between Instructor and Course has a cardinality of N:M, which means that one instructor can teach many courses, and one course can have many instructors.