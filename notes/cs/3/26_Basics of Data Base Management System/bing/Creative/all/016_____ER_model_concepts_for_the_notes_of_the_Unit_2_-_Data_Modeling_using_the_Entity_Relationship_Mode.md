# ER Model Concepts

The ER model is a conceptual data model that describes the data requirements of a system in terms of entities, attributes, relationships, and constraints. It is used to design and document the logical structure of a database. The ER model consists of the following concepts:

- **Entity**: An entity is a real-world object or thing that can be identified uniquely. For example, a student, a course, a book, etc. An entity has a set of properties or attributes that describe its characteristics. For example, a student entity may have attributes like name, roll number, age, etc.

- **Entity type**: An entity type is a collection of entities that share the same attributes. For example, student is an entity type that contains all the student entities in a database. An entity type is represented by a rectangle in an ER diagram.

- **Entity set**: An entity set is a subset of an entity type that contains the entities that participate in a particular relationship. For example, enrolled is an entity set that contains the student entities that are enrolled in a course.

- **Attribute**: An attribute is a property or characteristic of an entity or a relationship. For example, name, age, roll number, etc. are attributes of a student entity. An attribute is represented by an oval in an ER diagram.

- **Attribute domain**: An attribute domain is a set of possible values for an attribute. For example, the domain of the age attribute of a student entity may be the set of positive integers.

- **Key attribute**: A key attribute is an attribute that uniquely identifies an entity in an entity set. For example, roll number is a key attribute of a student entity. A key attribute is underlined in an ER diagram.

- **Composite attribute**: A composite attribute is an attribute that can be divided into sub-attributes. For example, name is a composite attribute that can be divided into first name, middle name, and last name. A composite attribute is represented by an oval with ovals inside it in an ER diagram.

- **Multivalued attribute**: A multivalued attribute is an attribute that can have more than one value for a given entity. For example, phone number is a multivalued attribute of a student entity, as a student may have more than one phone number. A multivalued attribute is represented by a double oval in an ER diagram.

- **Derived attribute**: A derived attribute is an attribute that can be derived from other attributes. For example, age is a derived attribute of a student entity, as it can be derived from the date of birth attribute. A derived attribute is represented by a dashed oval in an ER diagram.

- **Relationship**: A relationship is an association or link between two or more entities. For example, enrolled is a relationship between student and course entities, as it indicates which student is enrolled in which course. A relationship has a degree, which is the number of entity types involved in the relationship. For example, enrolled is a binary relationship, as it involves two entity types. A relationship is represented by a diamond in an ER diagram.

- **Relationship type**: A relationship type is a collection of relationships that share the same meaning and properties. For example, enrolled is a relationship type that contains all the enrolled relationships in a database. A relationship type is represented by a diamond with a name inside it in an ER diagram.

- **Relationship set**: A relationship set is a subset of a relationship type that contains the relationships that participate in a particular entity set. For example, enrolled is a relationship set that contains the enrolled relationships between the student and course entity sets.

- **Role**: A role is the function or purpose of an entity in a relationship. For example, in the enrolled relationship, student plays the role of enrollee and course plays the role of enrollee. A role is represented by a name near the entity type in an ER diagram.

- **Cardinality ratio**: A cardinality ratio is the number of entities that can be associated with another entity in a relationship. For example, in the enrolled relationship, the cardinality ratio of student to course is many-to-one, as a student can be enrolled in many courses, but a course can have only one student. A cardinality ratio is represented by a number or a symbol near the entity type in an ER diagram.

- **Participation constraint**: A participation constraint is a constraint that specifies whether the participation of an entity type in a relationship type is mandatory or optional. For example, in the enrolled relationship, the participation of student is mandatory, as every student must be enrolled in at least one course, but the participation of course is optional, as some courses may