### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases . It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The EER model includes the following concepts in addition to the ER model concepts  :

- **Subclasses and Superclasses**: A subclass is a subset of entities that belong to a superclass. A superclass is a set of entities that share some common attributes or relationships. For example, a person can be a superclass, and a student can be a subclass of a person.
- **Specialization and Generalization**: Specialization is the process of defining one or more subclasses from a superclass based on some distinguishing characteristics. Generalization is the reverse process of defining a superclass from one or more subclasses based on their common features. For example, a person can be specialized into a student or an employee based on their role, and a student and an employee can be generalized into a person based on their common attributes.
- **Category or Union Type**: A category or union type is a set of entities that belong to different entity types but share some common characteristics. For example, a vehicle can be a category of car, bike, or bus, which are different entity types but share some common attributes such as color or model.
- **Aggregation**: Aggregation is the process of grouping one or more entities and relationships into a single abstract entity type. For example, a course offering can be an aggregation of a course, an instructor, and a semester, which are different entity types but form a meaningful unit.

The EER model can be represented graphically using the following symbols:

- A rectangle for an entity type
- An ellipse for an attribute
- A diamond for a relationship type
- A line for a link between an entity type and a relationship type or between an attribute and an entity type
- A double line for a total participation constraint
- A dashed line for a partial participation constraint
- A double ellipse for a multivalued attribute
- A dashed ellipse for a derived attribute
- A triangle for a superclass-subclass relationship
- A circle with d for a disjoint constraint
- A circle with o for an overlap constraint
- A circle with c for a category or union type
- A dashed rectangle for an aggregation

An example of an EER diagram is shown below:

![EER diagram example](https://media.geeksforgeeks.org/wp-content/uploads/20191121181906/Enhanced-ER-Diagram-Example.jpg)