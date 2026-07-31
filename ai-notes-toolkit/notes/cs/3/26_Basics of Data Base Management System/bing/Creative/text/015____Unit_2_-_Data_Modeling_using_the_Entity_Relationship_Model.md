## Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is the process of designing a conceptual representation of the data that will be stored in a database.
- The Entity Relationship Model (ER Model) is a widely used data modeling technique that uses graphical symbols to represent the entities, attributes, and relationships in a database.
- An entity is a real-world object or concept that can be identified uniquely and has some properties of interest. For example, a student, a course, or a department are entities.
- An attribute is a property or characteristic of an entity that describes some aspect of it. For example, a student entity may have attributes such as name, ID, major, or GPA.
- A relationship is an association or link between two or more entities that expresses some meaningful connection or dependency among them. For example, a student entity may have a relationship with a course entity that indicates that the student is enrolled in the course.
- The ER Model uses the following symbols to represent the entities, attributes, and relationships in a database:

  - A rectangle represents an entity type, which is a collection of entities that share the same attributes. The name of the entity type is written inside the rectangle. For example, Student is an entity type that contains all the student entities in the database.
  - An oval represents an attribute of an entity type. The name of the attribute is written inside the oval. An attribute can be connected to only one entity type by a line. For example, Name is an attribute of the Student entity type.
  - A diamond represents a relationship type, which is a collection of relationships that share the same meaning and involve the same entity types. The name of the relationship type is written inside the diamond. A relationship type can be connected to one or more entity types by a line. For example, Enrolled is a relationship type that connects the Student and Course entity types.
  - A line represents a participation constraint, which specifies the minimum and maximum number of times an entity can participate in a relationship. The participation constraint is indicated by a cardinality ratio, which is a pair of numbers written on either side of the line. For example, a 1:N cardinality ratio means that one entity of the first entity type can participate in the relationship with many entities of the second entity type, but each entity of the second entity type can participate in the relationship with only one entity of the first entity type. A participation constraint can also be indicated by an existence dependency, which is a double line that means that an entity must participate in the relationship. For example, a double line between Student and Enrolled means that every student must be enrolled in at least one course.
  - A dashed oval represents a derived attribute, which is an attribute whose value can be computed from other attributes. The name of the derived attribute is written inside the dashed oval. A derived attribute can be connected to only one entity type by a dashed line. For example, Average is a derived attribute of the Course entity type that can be computed from the grades of the students enrolled in the course.
  - A double rectangle represents a weak entity type, which is an entity type that does not have a key attribute and depends on another entity type for its existence. The name of the weak entity type is written inside the double rectangle. A weak entity type can be connected to only one strong entity type (an entity type that has a key attribute) by a double line. For example, Section is a weak entity type that depends on the Course entity type for its existence.
  - A double oval represents a multivalued attribute, which is an attribute that can have more than one value for a given entity. The name of the multivalued attribute is written inside the double oval. A multivalued attribute can be connected to only one entity type by a line. For example, Phone is a multivalued attribute of the Student entity type that can store multiple phone numbers for a student.
  - A key attribute is an attribute that can uniquely identify an entity within an entity type. A key attribute is underlined in the ER diagram. For example, ID is a key attribute of the Student entity type that can uniquely identify a student.

- An example of an ER diagram for a university database is shown below:

```mermaid
erDiagram
  STUDENT ||--|{ ENROLLED : "1:N"
  ENROLLED ||--|| COURSE : "N:1"
  STUDENT {
    double ID
    string Name
    string Major
    double GPA
    double Phone
  }
  COURSE {
    string Code
    string Title
    double Credits
    double Average
  }
  SECTION ||--||| COURSE : "N:1"
  SECTION {
    double Number

```
