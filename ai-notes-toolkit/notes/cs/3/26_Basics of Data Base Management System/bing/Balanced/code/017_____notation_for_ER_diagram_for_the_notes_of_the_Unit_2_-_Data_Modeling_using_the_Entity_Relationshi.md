# Notation for ER Diagram

An ER diagram is a graphical representation of the entities and their relationships in a database. It helps to design and understand the logical structure of the data. There are different notations and symbols used to create an ER diagram, depending on the preference and purpose of the modeler. Some of the common notations and symbols are:

- **Crow's foot notation**: This is the most intuitive and widely used notation for ER diagrams. It uses different shapes and lines to indicate the entities, attributes, and relationships. The main symbols are:

  - **Entity**: A rectangle represents an entity, which is a real-world object or concept that can be identified and stored in the database. For example, a student, a course, or a department can be entities. The name of the entity is written inside the rectangle.

  - **Attribute**: An oval represents an attribute, which is a property or characteristic of an entity. For example, a student entity can have attributes such as name, ID, or major. The name of the attribute is written inside the oval. There are different types of attributes, such as:

    - **Simple attribute**: An attribute that cannot be divided into smaller parts. For example, name or ID.

    - **Composite attribute**: An attribute that can be divided into smaller parts. For example, address can be composed of street, city, and state.

    - **Single-valued attribute**: An attribute that has only one value for each entity. For example, ID or major.

    - **Multi-valued attribute**: An attribute that can have more than one value for each entity. For example, phone number or email. A multi-valued attribute is shown by a double oval.

    - **Derived attribute**: An attribute that can be derived from other attributes. For example, age can be derived from date of birth. A derived attribute is shown by a dashed oval.

  - **Relationship**: A diamond represents a relationship, which is an association or interaction between two or more entities. For example, a student can enroll in a course, or a department can offer a course. The name of the relationship is written inside the diamond. There are different types of relationships, such as:

    - **One-to-one relationship**: A relationship where each entity in one set is associated with only one entity in another set. For example, a student can have only one advisor, and an advisor can advise only one student. A one-to-one relationship is shown by a single line connecting the entities.

    - **One-to-many relationship**: A relationship where each entity in one set is associated with many entities in another set. For example, a department can offer many courses, but a course can belong to only one department. A one-to-many relationship is shown by a single line connecting the entity in the one side, and a crow's foot (three prongs) connecting the entity in the many side.

    - **Many-to-many relationship**: A relationship where each entity in one set is associated with many entities in another set. For example, a student can enroll in many courses, and a course can have many students. A many-to-many relationship is shown by a crow's foot connecting both entities.

  - **Cardinality**: The cardinality of a relationship specifies the number of instances of one entity that can be associated with each instance of another entity. For example, a student can enroll in zero or more courses, and a course can have zero or more students. The cardinality of a relationship is shown by placing a number or a symbol next to the line connecting the entities. Some of the common symbols are:

    - **0**: Zero or optional. For example, a student may or may not enroll in a course.

    - **1**: One or mandatory. For example, a course must belong to one department.

    - **N**: Many or unspecified. For example, a student can enroll in many courses.

    - **M**: A specific number. For example, a student can enroll in at most four courses.

- **Other notations**: There are some other notations that are used for ER diagrams, such as arrow notation, Barker's notation, UML notation, etc. They have different symbols and conventions to represent the entities, attributes, and relationships. However, they all convey the same information and can be converted to each other. The choice of notation depends on the preference and purpose of the modeler.