### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts in addition to the ER model concepts :

- Subclasses and superclasses: A subclass is a subset of entities of a superclass that share some additional attributes or relationships. A superclass is a superset of entities that have some common attributes or relationships. For example, a student can be a subclass of a person, and a person can be a superclass of a student.
- Specialization and generalization: A specialization is a process of defining a set of subclasses of a superclass based on some distinguishing characteristics. A generalization is a process of defining a superclass from a set of subclasses by identifying their common attributes or relationships. For example, a person can be specialized into student, employee, and customer based on their roles.
- Category or union type: A category or union type is a subclass that represents a collection of entities from different superclasses that share some common attributes or relationships. A category or union type can have partial or total participation from its superclasses. For example, a project can be a category of research project and development project, and a project member can be a union of student, employee, and customer.
- Aggregation: An aggregation is a process of treating a relationship as an entity, which allows relationships between relationships. An aggregation can be used to model a part-of relationship between an entity and a collection of entities. For example, a department can be an aggregation of employees, and a department can have a relationship with a project.

The extended ER model can be represented graphically using the following symbols:

- A rectangle for an entity type
- An ellipse for an attribute
- A diamond for a relationship type
- A line for a link between an entity type and a relationship type or between an attribute and an entity type or a relationship type
- A double ellipse for a multivalued attribute
- A dashed ellipse for a derived attribute
- A double line for a total participation constraint
- A single line for a partial participation constraint
- A double rectangle for a weak entity type
- A double diamond for an identifying relationship type
- A triangle for a superclass/subclass relationship
- A circle with d for a disjoint constraint
- A circle with o for an overlap constraint
- A circle with u for a union type
- A dashed rectangle for an aggregation

The following diagram shows an example of an extended ER model for a university database:

![EER diagram](https://media.geeksforgeeks.org/wp-content/uploads/20190828171906/Enhanced-ER-Diagram-1.png)