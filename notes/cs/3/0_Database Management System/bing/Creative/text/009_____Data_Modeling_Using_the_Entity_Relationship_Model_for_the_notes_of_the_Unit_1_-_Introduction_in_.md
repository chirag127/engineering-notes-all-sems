### Data Modeling Using the Entity Relationship Model

- Data modeling is a process of designing and representing the structure and relationships of data in a database.
- Entity Relationship Model (ER Model) is a graphical method for data modeling using entities, attributes, and relationships.
- Entities are the basic units of data that have a unique identity and properties. Examples of entities are students, courses, books, etc.
- Attributes are the characteristics or features of entities that describe them. Examples of attributes are name, age, address, etc.
- Relationships are the associations or connections between entities that indicate how they are related to each other. Examples of relationships are enrolls, teaches, borrows, etc.
- Entity Relationship Diagram (ERD) is a diagram that shows the entities, attributes, and relationships in a database using symbols and connectors.
- ERD symbols include:
  - Rectangles for entities
  - Ovals for attributes
  - Diamonds for relationships
  - Lines for connections
  - Cardinality symbols for indicating the number of occurrences of an entity in a relationship
- ERD connectors include:
  - Solid lines for mandatory participation
  - Dashed lines for optional participation
  - Double lines for identifying relationships
  - Single lines for non-identifying relationships
- ERD rules include:
  - Each entity must have a unique name and a primary key attribute
  - Each attribute must belong to one and only one entity
  - Each relationship must have a name and a degree (the number of entities involved)
  - Each relationship must have a cardinality (the number of instances of one entity that can be associated with one instance of another entity)
  - Each relationship must have a participation constraint (the minimum and maximum number of instances of one entity that must be associated with one instance of another entity)
- ERD examples include:

![ERD example 1](https://www.visual-paradigm.com/servlet/editor-content/tutorials/erd/what-is-entity-relationship-diagram/erd-example.png)

This ERD shows the entities Customer, Order, and Product, and their attributes and relationships. The cardinality symbols indicate that a customer can place zero or more orders, an order must belong to one and only one customer, an order can contain one or more products, and a product can be in zero or more orders. The participation constraints indicate that a customer must place at least one order, an order must contain at least one product, and a product does not have to be in any order.

![ERD example 2](https://www.databasestar.com/wp-content/uploads/2017/02/erd-example.png)

This ERD shows the entities Student, Course, and Enrollment, and their attributes and relationships. The cardinality symbols indicate that a student can enroll in zero or more courses, a course can have zero or more students enrolled, and an enrollment must involve one and only one student and one and only one course. The participation constraints indicate that a student does not have to enroll in any course, a course does not have to have any student enrolled, and an enrollment must exist for every pair of student and course. The double lines indicate that the relationship Enrollment is identifying, meaning that the primary key of Enrollment is composed of the primary keys of Student and Course.