### ER model concepts

- The ER model is a conceptual data model that describes the entities, attributes, and relationships in a domain of interest .
- An entity is a real-world object or concept that can be identified uniquely and has some properties . For example, a student, a course, or a book are entities.
- An attribute is a property or characteristic of an entity that describes some aspect of it . For example, a student entity may have attributes such as name, roll number, or age.
- A relationship is an association or connection between two or more entities that expresses some meaningful dependency or interaction . For example, a student entity may have a relationship with a course entity, such as enrolls in or attends.
- An ER diagram is a graphical representation of the ER model using symbols and notation to show the entities, attributes, and relationships . For example, the following ER diagram shows the entities student, course, and instructor, and their relationships.

![ER diagram example](https://www.tutorialspoint.com/dbms/images/er_model_basic_concepts.jpg)

- An entity type is a collection or set of entities that share the same attributes and can be identified by a common name . For example, student is an entity type that represents all the students in a database.
- An entity set is a subset of an entity type that contains the entities that participate in a particular relationship . For example, the entity set of students who enroll in a course is a subset of the student entity type.
- A relationship type is a collection or set of relationships that share the same meaning and involve the same entity types . For example, enrolls in is a relationship type that represents the association between student and course entity types.
- A relationship set is a subset of a relationship type that contains the relationships that occur between the entities in a particular entity set . For example, the relationship set of students who enroll in a specific course is a subset of the enrolls in relationship type.
- An attribute can be classified into different types based on its role and function in the ER model . Some of the common attribute types are:
  - Key attribute: An attribute that uniquely identifies an entity in an entity set. For example, roll number is a key attribute of student entity type.
  - Composite attribute: An attribute that can be divided into smaller sub-attributes. For example, name can be a composite attribute of student entity type, consisting of first name and last name sub-attributes.
  - Multivalued attribute: An attribute that can have more than one value for an entity. For example, phone number can be a multivalued attribute of student entity type, as a student can have multiple phone numbers.
  - Derived attribute: An attribute that can be derived or computed from other attributes. For example, age can be a derived attribute of student entity type, as it can be calculated from the date of birth attribute.
- A relationship can also have attributes that describe some property or condition of the association . For example, a relationship between student and course entity types can have an attribute such as grade or semester.
- A relationship can also have a degree or cardinality that indicates the number of entity types involved in the association . Some of the common relationship degrees are:
  - Unary or recursive relationship: A relationship that involves only one entity type. For example, a relationship between instructor and instructor entity types, such as supervises or advises.
  - Binary relationship: A relationship that involves two entity types. For example, a relationship between student and course entity types, such as enrolls in or attends.
  - Ternary relationship: A relationship that involves three entity types. For example, a relationship between student, course, and instructor entity types, such as evaluates or recommends.
- A relationship can also have a cardinality ratio or multiplicity that specifies the number of entities that can participate in the association from each entity type . Some of the common cardinality ratios are:
  - One-to-one (1:1): A relationship where each entity from one entity type is associated with at most one entity from another entity type. For example, a relationship between student and locker entity types, such