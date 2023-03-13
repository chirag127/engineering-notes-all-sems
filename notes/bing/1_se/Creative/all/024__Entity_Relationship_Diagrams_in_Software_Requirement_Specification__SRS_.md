### Entity Relationship Diagrams in Software Requirement Specification (SRS)

- Entity Relationship Diagrams (ERDs) are graphical representations of the data model of a software system. They show the entities, attributes, relationships and constraints of the data in a clear and concise way.
- ERDs are used in software engineering during the planning stages of the software project. They help to identify different system elements and their relationships with each other. They also serve as the basis for data flow diagrams or DFDs, which show how data moves through the system.
- ERDs are based on the Entity Relationship (ER) model, which is a high-level conceptual model that describes information as entities, attributes, relationships and constraints. An entity is a thing or object that can be identified uniquely, such as a person, a product, or a course. An attribute is a property or characteristic of an entity, such as a name, a price, or a grade. A relationship is an association or link between two or more entities, such as a student enrolls in a course, or a product belongs to a category. A constraint is a rule or restriction that applies to the data, such as a primary key, a foreign key, or a cardinality .
- To draw an ERD, the following steps are usually followed :
  - Extract the requirements from the SRS document or other sources, such as interviews, surveys, or observations. Identify the main entities, attributes, and relationships that are relevant to the system.
  - Assign a name and a symbol to each entity, attribute, and relationship. The symbols can vary depending on the notation used, but a common one is the Chen notation, which uses rectangles for entities, ovals for attributes, and diamonds for relationships. The name should be descriptive and singular, such as Student, Course, or Enrolls.
  - Connect the entities and relationships with lines, and label the lines with the cardinality of the relationship. The cardinality indicates how many instances of one entity can be related to one instance of another entity, such as one-to-one, one-to-many, or many-to-many. The cardinality can be represented by numbers, such as 1, N, or M, or by symbols, such as crow's feet, bars, or circles.
  - Specify the primary key and foreign key attributes for each entity and relationship. The primary key is a unique identifier for each instance of an entity or relationship, such as a student ID, a course code, or a combination of both. The foreign key is an attribute that references the primary key of another entity or relationship, such as a course code in the Enrolls relationship. The primary key and foreign key attributes can be underlined or marked with a (P) or (F) respectively.
  - Add any other constraints or details that are necessary to complete the data model, such as data types, domains, default values, or optional attributes. These can be written in parentheses or brackets next to the attributes or relationships, or in a separate document or table.

- Here is an example of an ERD for a simple university system, using the Chen notation and the steps above:

```
+-----------+       +----------+       +-----------+
|  Student  |       |  Course  |       |  Faculty  |
+-----------+       +----------+       +-----------+
|  SID (P)  |       |  CID (P) |       |  FID (P)  |
|  Name     |       |  Name    |       |  Name     |
|  Major    |       |  Credits |       |  Dept     |
+-----------+       +----------+       +-----------+
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
     |                  |                   |
+-----------+       +----------+       +-----------+
|  Enrolls  |       |  Teaches |       |  Advises  |
+-----------+       +----------+       +-----------+
|  SID (F)  |       |  CID (F) |       |  SID (