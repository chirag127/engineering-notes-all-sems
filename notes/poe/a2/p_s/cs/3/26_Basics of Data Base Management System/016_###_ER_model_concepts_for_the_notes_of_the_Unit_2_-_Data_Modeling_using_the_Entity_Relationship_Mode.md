 Here are the ER model concepts in markdown format for the notes of Unit 2 - Data Modeling using the Entity Relationship Model:

### Entities
- Entities are objects or concepts that exist in the real world and can be distinctly identified. For example: students, employees, products, etc.
- Each entity is described by a set of attributes. For example: student entity can have attributes like student ID, student name, department, etc.
- In ER diagrams, entities are represented by rectangles.

### Relationships
- Relationships represent associations between two or more entities. For example: student studies in a course.
- Relationships are represented using diamonds in ER diagrams.
- Cardinality specifies the number of instances of one entity that can be associated with the instances of another entity via the relationship. It has values like 1:1, 1:N, N:M.

### Attributes
- Attributes are properties that describe an entity. For example: student ID, student name, age, etc. describes a student entity.
- In ER diagrams, attributes are listed inside the entity rectangle.

### Keys
- A key is an attribute or set of attributes that uniquely identifies each instance of an entity.
- A primary key is a minimal set of attributes that uniquely identifies each instance of an entity. A weak entity does not have a primary key.
- Foreign keys are attributes of a relation or entity that refer to a primary key of another entity to establish and enforce the link between entities.

[Detailed diagrams and examples can be added here for better understanding.]

The advantages of ER models are:
- They provide a visual representation of data.
- They enable identification of relationships between data and logical structure of databases.
- They are easy to understand and can be mapped to relational models.

The disadvantages are:
- They may not be suitable for complex databases.
- They lack semantics to describe nested relationships.
- They cannot represent certain constraints on relationships.

ER models have applications in database design, systems analysis, and data modeling. They are a major part of conceptual data modeling.