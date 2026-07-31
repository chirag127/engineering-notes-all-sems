# Unit 2 - Creating Entity-Relationship Diagram using case tools

- An entity-relationship diagram (ERD) is a graphical representation of the data and relationships in a database system.
- A case tool is a software application that helps in designing, developing, and maintaining a database system.
- Some examples of case tools are Microsoft Visio, Oracle SQL Developer Data Modeler, and MySQL Workbench.
- To create an ERD using a case tool, the following steps are usually followed:

  - Identify the entities and attributes in the database system. Entities are the objects or concepts that store data, such as students, courses, or books. Attributes are the properties or characteristics of entities, such as name, age, or title.
  - Identify the relationships and cardinalities between the entities. Relationships are the associations or interactions between entities, such as enrolls, teaches, or borrows. Cardinalities are the number of occurrences of one entity that can be related to another entity, such as one-to-one, one-to-many, or many-to-many.
  - Draw the ERD using the case tool. Each entity is represented by a rectangle with the entity name and attributes inside. Each relationship is represented by a diamond with the relationship name and cardinality symbols on the edges. The primary key of each entity is underlined.

- An example of an ERD for a university database system using Microsoft Visio is shown below:

![ERD example](https://i.imgur.com/8wZ6wQy.png)

- The ERD shows that a student can enroll in many courses, a course can be taught by many instructors, an instructor can teach many courses, and a book can be borrowed by many students. The primary keys are student_id, course_id, instructor_id, and book_id. The attributes are name, age, department, title, edition, and due_date.