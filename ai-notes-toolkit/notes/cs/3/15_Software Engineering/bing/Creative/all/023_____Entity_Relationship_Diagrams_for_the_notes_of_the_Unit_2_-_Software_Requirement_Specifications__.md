# Entity Relationship Diagrams

- Entity Relationship Diagrams (ERDs) are a data modeling method used in software engineering to produce a conceptual data model of an information system.
- ERDs help to identify different system elements and their relationships with each other.
- ERDs are often used as the basis for data flow diagrams or DFDs.
- ERDs use different symbols and connectors to visualize two important information: the major entities within the system scope, and the inter-relationships among these entities.
- An entity is a real-world object or concept that can be identified by its attributes. For example, a student, a course, a book, etc.
- A relationship is an association or link between two or more entities. For example, a student enrolls in a course, a course has a book, etc.
- An attribute is a property or characteristic of an entity or a relationship. For example, a student has a name, a course has a code, a book has a title, etc.
- There are different types of entities, relationships and attributes that can be represented in ERDs :
  - A strong entity is an entity that can exist independently of other entities. It has a primary key, which is a unique identifier for each instance of the entity. For example, a student is a strong entity with a student ID as the primary key.
  - A weak entity is an entity that depends on another entity for its existence. It has a partial key, which is a unique identifier for each instance of the entity within the scope of the strong entity. For example, a course is a weak entity that depends on a department, and has a course code as the partial key.
  - A composite entity is an entity that represents the relationship between two or more entities. It has attributes that describe the relationship. For example, an enrollment is a composite entity that represents the relationship between a student and a course, and has attributes such as grade and date.
  - A regular relationship is a relationship that involves only strong entities. It has a degree, which is the number of entities involved in the relationship. For example, a one-to-one relationship is a relationship that involves two entities, and each entity is related to only one instance of the other entity. A one-to-many relationship is a relationship that involves two entities, and one entity is related to many instances of the other entity. A many-to-many relationship is a relationship that involves two entities, and each entity is related to many instances of the other entity.
  - An identifying relationship is a relationship that involves a weak entity and its owner entity. It has a cardinality, which is the number of instances of the weak entity that can be related to one instance of the owner entity. For example, a one-to-one identifying relationship is a relationship that involves a weak entity and its owner entity, and each instance of the weak entity is related to only one instance of the owner entity. A one-to-many identifying relationship is a relationship that involves a weak entity and its owner entity, and one instance of the owner entity can be related to many instances of the weak entity.
  - A simple attribute is an attribute that cannot be divided into smaller parts. It has a domain, which is the set of possible values for the attribute. For example, a name is a simple attribute with a domain of strings.
  - A composite attribute is an attribute that can be divided into smaller parts. It has sub-attributes, which are the smaller parts of the attribute. For example, an address is a composite attribute with sub-attributes such as street, city, state, etc.
  - A single-valued attribute is an attribute that can have only one value for each instance of the entity or relationship. For example, a student ID is a single-valued attribute for a student entity.
  - A multi-valued attribute is an attribute that can have more than one value for each instance of the entity or relationship. For example, a phone number is a multi-valued attribute for a student entity.
  - A derived attribute is an attribute that can be computed from other attributes. For example, an age is a derived attribute for a student entity, which can be computed from the date of birth attribute.
- ERDs use different notations to represent the entities, relationships and attributes. One of the common notations is the Chen notation, which uses the following symbols :

  - A rectangle for a strong entity, with the entity name inside.
  - A double