### Entity Relationship Diagrams in Software Requirement Specification (SRS)

- An Entity Relationship Diagram (ERD) is a type of diagram that lets you see how different entities (e.g. people, customers, or other objects) relate to each other in an application or a database.
- An entity is a thing or an object that has a distinct and independent existence and can be uniquely identified.
- An attribute is a property or a characteristic of an entity that describes some aspect of it.
- A relationship is a connection or an association between two or more entities that shows how they interact with each other.
- A constraint is a rule or a condition that limits or restricts the possible values or combinations of values for an entity, an attribute, or a relationship.
- An ERD is used to design the database of the software by extracting the requirements, identifying the entities, their attributes, the relationships between the entities, and the constraints.
- An ERD consists of the following symbols:

| Symbol | Meaning |
| ------ | ------- |
| Rectangle | Entity |
| Ellipse | Attribute |
| Diamond | Relationship |
| Line | Connection |
| Double line | Total participation |
| Single line | Partial participation |
| Double ellipse | Multivalued attribute |
| Dashed ellipse | Derived attribute |
| Double rectangle | Weak entity |
| Double diamond | Identifying relationship |

- An example of an ERD for a student registration system is shown below:

```
+----------------+       +----------------+       +----------------+
|    Student     |       |   Course       |       |   Instructor   |
+----------------+       +----------------+       +----------------+
| ID             |       | Code           |       | ID             |
| Name           |       | Name           |       | Name           |
| Address        |       | Credits        |       | Department     |
| Phone          |       | Prerequisites  |       | Phone          |
+----------------+       +----------------+       +----------------+
     |  |  |                  |  |  |                  |  |  |
     |  |  +------------------+  |  +------------------+  |  |
     |  |                       |                       |  |  |
     |  +-----------------------+                       |  |  |
     |                                                  |  |  |
     +--------------------------------------------------+  |  |
                                                           |  |
+----------------+                                         |  |
|   Section      |                                         |  |
+----------------+                                         |  |
| SectionID      |                                         |  |
| Time           |                                         |  |
| Room           |                                         |  |
+----------------+                                         |  |
     |  |  |                                              |  |
     |  |  +----------------------------------------------+  |
     |  |                                                     |
     |  +-----------------------------------------------------+
     |
     +----------------+
     |   Grade        |
     +----------------+
     | Letter         |
     | Points         |
     +----------------+
```

- Some possible mnemonics and learning tricks for ERD are:

  - Remember the acronym EARC: Entity, Attribute, Relationship, Constraint.
  - Use the word ERD to pronounce the sound of a bird: "Erd, erd, erd". Imagine a bird flying over the entities and relationships in the diagram.
  - Think of the rectangle as a table, the ellipse as a column, the diamond as a join, and the line as a foreign key in a relational database.
  - Associate the double line with the word "total", the double ellipse with the word "multiple", the double rectangle with the word "weak", and the double diamond with the word "identify".
  - Use the phrase "Every Relationship Dies" to remember the four types of cardinality: one-to-one, one-to-many, many-to-one, and many-to-many.