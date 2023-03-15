# ER model concepts

The ER model is a conceptual data model that describes the entities, attributes, and relationships in a database. It is used to design and represent the logical structure of a database. The ER model consists of the following basic concepts  :

- **Entity**: An entity is a real-world object or thing that can be identified uniquely. For example, a student, a course, a book, etc. An entity type is a collection of similar entities that share the same properties. For example, the entity type STUDENT represents all the students in a database.
- **Attribute**: An attribute is a property or characteristic of an entity that describes some aspect of it. For example, a student entity may have attributes such as name, roll number, age, etc. An attribute can be simple or composite, single-valued or multi-valued, stored or derived, etc. For example, the attribute name can be composite (first name and last name), single-valued (one name per student), and stored (not derived from other attributes).
- **Relationship**: A relationship is an association or connection between two or more entities that expresses some meaningful dependency or interaction. For example, a student entity may have a relationship with a course entity, such as enrolled in, completed, etc. A relationship type is a set of similar relationships that share the same meaning and properties. For example, the relationship type ENROLLED represents all the enrollments of students in courses in a database.
- **Relationship Degree**: The relationship degree is the number of entity types that participate in a relationship type. For example, a binary relationship has a degree of two, a ternary relationship has a degree of three, etc. The degree of a relationship can also be called its arity or cardinality.
- **Relationship Cardinality**: The relationship cardinality is the number of occurrences of one entity type that can be related to one occurrence of another entity type in a relationship type. For example, a one-to-one relationship means that one entity of type A can be related to only one entity of type B, and vice versa. A one-to-many relationship means that one entity of type A can be related to many entities of type B, but one entity of type B can be related to only one entity of type A. A many-to-many relationship means that many entities of type A can be related to many entities of type B, and vice versa.
- **Relationship Attribute**: A relationship attribute is an attribute that belongs to a relationship type rather than an entity type. It describes some property of the relationship itself. For example, a relationship attribute for the ENROLLED relationship type could be grade, which indicates the grade obtained by a student in a course.
- **ER Diagram**: An ER diagram is a graphical representation of the ER model using symbols and notation. It shows the entity types, attributes, relationships, and cardinalities in a database schema. For example, the following ER diagram shows a simplified schema for a university database:

![ER diagram example](https://media.geeksforgeeks.org/wp-content/uploads/ER-Diagram-1.png)

: https://www.tutorialspoint.com/dbms/er_model_basic_concepts.htm
: https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model
: https://www.w3schools.in/dbms/er-model
: https://www.geeksforgeeks.org/introduction-of-er-model