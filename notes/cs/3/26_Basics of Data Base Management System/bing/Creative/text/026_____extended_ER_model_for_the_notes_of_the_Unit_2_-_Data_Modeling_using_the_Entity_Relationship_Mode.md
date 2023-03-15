### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. The EER model reflects more precisely the properties and constraints that are found in complex databases, such as inheritance, specialization, generalization, union, and aggregation.

The EER model includes the following concepts in addition to the ER model concepts:

- **Subclasses and Superclasses**: A subclass is a subset of entities that belong to a superclass, and inherits all the attributes and relationships of the superclass. A superclass is a superset of entities that share some common attributes or relationships. For example, a subclass STUDENT can be derived from a superclass PERSON, and inherit the attributes name, address, and phone from the superclass.
- **Specialization and Generalization**: Specialization is the process of defining one or more subclasses from a superclass based on some distinguishing characteristics of the entities in the subclass. Generalization is the reverse process of abstraction, where common attributes and relationships are combined from two or more subclasses to form a superclass. For example, a superclass VEHICLE can be generalized from the subclasses CAR and TRUCK, and have the common attribute license_plate.
- **Union or Category**: A union or category is a subclass that represents a collection of entities from different entity types. A union or category is also called a shared subclass, since it can be a subclass of more than one superclass. For example, a subclass EMPLOYEE can be a union of the subclasses FACULTY and STAFF, and be a subclass of both the superclasses PERSON and ORGANIZATION.
- **Aggregation**: Aggregation is the process of grouping together a set of entities and relationships into a single abstract entity type. Aggregation allows treating the group as a single unit without losing the individual identities of the entities. For example, an entity type PROJECT can be aggregated from the entity types TASK and RESOURCE, and the relationship type ALLOCATE. The aggregated entity type PROJECT can then participate in other relationships, such as MANAGE or EVALUATE.

The EER model can be represented graphically using the following symbols:

- A rectangle for an entity type, with the name of the entity type inside the rectangle.
- An ellipse for an attribute, with the name of the attribute inside the ellipse. A key attribute is underlined, and a multivalued attribute is double-lined. An attribute can be connected to an entity type or a relationship type by a line.
- A diamond for a relationship type, with the name of the relationship type inside the diamond. A relationship type can be connected to one or more entity types by a line, with a cardinality ratio and a participation constraint on each end of the line.
- A triangle for a superclass/subclass relationship, with the name of the relationship type above the triangle. A superclass/subclass relationship can be connected to one or more superclasses and one or more subclasses by a line, with a disjointness constraint and a completeness constraint on the line.
- A circle with a letter "d" for a union or category, with the name of the subclass below the circle. A union or category can be connected to one or more superclasses by a line, with a partial or total participation constraint on the line.
- A dashed rectangle for an aggregation, with the name of the aggregated entity type inside the rectangle. An aggregation can enclose a set of entity types and relationship types, and can be connected to other entity types or relationship types by a line.

Here is an example of an EER diagram for a university database:

![EER diagram example](https://media.geeksforgeeks.org/wp-content/uploads/20190822182101/Enhanced-ER-Diagram-Example.png)