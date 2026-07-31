## Unit 2 - Data Modeling using the Entity Relationship Model

Data modeling is the process of creating a conceptual representation of data structures. The Entity Relationship Model (ER Model) is a widely-used data modeling technique that helps in defining data entities and their relationships.

### Entities

An entity is an object or concept that is relevant to the business domain being modeled. Entities have attributes that describe their characteristics. For example, in a university database, a student is an entity with attributes like name, ID, and date of birth.

### Relationships

Relationships between entities describe how entities are related to each other. There are three types of relationships:

- One-to-One: One entity is related to only one instance of another entity. For example, a person can have only one passport, and a passport belongs to only one person.
- One-to-Many: One entity is related to many instances of another entity. For example, a customer can have many orders, but an order belongs to only one customer.
- Many-to-Many: Many instances of one entity are related to many instances of another entity. For example, a student can enroll in many courses, and a course can have many students.

### Cardinality

Cardinality describes the number of instances of one entity that can be related to the number of instances of another entity. There are two types of cardinality:

- Minimum Cardinality: The minimum number of instances of one entity that must be related to the other entity. For example, a course must have at least one student enrolled.
- Maximum Cardinality: The maximum number of instances of one entity that can be related to the other entity. For example, a person can have at most one passport.

### Entity Relationship Diagrams (ER Diagrams)

ER Diagrams are graphical representations of entities, their attributes, and their relationships. ER Diagrams use symbols to represent entities, relationships, and cardinality.

- Entity symbol: A rectangle with the entity name inside.
- Attribute symbol: An oval with the attribute name inside.
- Relationship symbol: A diamond with the relationship name inside.
- Cardinality symbol: A line with a crow's foot at one or both ends, representing the minimum and maximum cardinality.

### Conclusion

The Entity Relationship Model is a powerful technique for data modeling. By defining entities, relationships, and cardinality, we can create a conceptual representation of data structures that can be used to design databases. ER Diagrams provide a visual representation of the model, making it easier to understand and communicate.