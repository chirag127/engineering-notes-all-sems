## Unit 2 - Data Modeling using the Entity Relationship Model

- Data modeling is the process of designing and documenting the structure and semantics of data for a specific application domain.
- The Entity Relationship (ER) model is a widely used conceptual data model that represents data as entities, attributes, and relationships.
- An entity is an object or concept that can be identified and distinguished from others in the domain. For example, a student, a course, or a department.
- An attribute is a property or characteristic of an entity that describes some aspect of it. For example, a student has a name, an ID, and a major.
- A relationship is an association or connection between two or more entities that expresses some meaningful dependency or interaction. For example, a student enrolls in a course, or a department offers a course.
- The ER model can be represented graphically using an ER diagram, which consists of the following symbols:

  - A rectangle for an entity set, which is a collection of entities of the same type. The name of the entity set is written inside the rectangle. For example, STUDENT, COURSE, or DEPARTMENT.
  - An oval for an attribute, which is connected to the entity set it belongs to by a line. The name of the attribute is written inside the oval. For example, Name, ID, or Major.
  - A diamond for a relationship set, which is a collection of relationships of the same type. The name of the relationship set is written inside the diamond. For example, ENROLLS, or OFFERS.
  - A line for a participation, which connects an entity set to a relationship set and indicates that the entities in the entity set participate in the relationships in the relationship set. For example, a line connects STUDENT to ENROLLS, and another line connects COURSE to ENROLLS.
  - A double line for a total participation, which indicates that every entity in the entity set must participate in at least one relationship in the relationship set. For example, a double line connects COURSE to OFFERS, which means that every course must be offered by some department.
  - A single line for a partial participation, which indicates that some entities in the entity set may not participate in any relationship in the relationship set. For example, a single line connects STUDENT to ENROLLS, which means that some students may not enroll in any course.
  - A number or a letter for a cardinality ratio, which specifies the maximum number of relationships that an entity in one entity set can participate in with entities in another entity set. For example, a 1 on the line connecting COURSE to ENROLLS means that a course can be enrolled by at most one student, and an N on the line connecting STUDENT to ENROLLS means that a student can enroll in any number of courses. Alternatively, a 1:N can be written on the diamond of ENROLLS to indicate the same cardinality ratio.
  - A line with an arrow for a participation role, which indicates the role that an entity set plays in a relationship set. For example, a line with an arrow from STUDENT to ENROLLS means that a student is the enrollee in the ENROLLS relationship, and a line with an arrow from COURSE to ENROLLS means that a course is the enrolled in the ENROLLS relationship.
  - A dashed oval for a derived attribute, which is an attribute whose value can be computed from other attributes. For example, Age can be a derived attribute of STUDENT, which can be computed from the Date of Birth attribute.
  - A double oval for a multivalued attribute, which is an attribute that can have more than one value for a given entity. For example, Phone Number can be a multivalued attribute of STUDENT, which can have multiple phone numbers for a given student.
  - A composite attribute, which is an attribute that can be divided into sub-attributes. For example, Name can be a composite attribute of STUDENT, which can be divided into First Name and Last Name. A composite attribute is represented by an oval with ovals inside it, connected by lines.

- Here is an example of an ER diagram for a university database:

![ER diagram for a university database](https://i.imgur.com/8n0zZ7R.png)

- The ER model can be converted into a relational model, which is a logical data model that represents data as tables, columns, and keys.
- A table, also called a relation, is a collection of rows, also called tuples, that store data about a specific entity set or relationship set. The name of the table is the same as the name of the entity set or relationship set. For example, STUDENT, COURSE, or