### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts in addition to the ER model concepts :

- Subclasses and superclasses: A subclass is a subset of entities of a superclass that share some common attributes or relationships distinct from other entities of the superclass. A superclass is a set of entities that includes all its subclasses. For example, a superclass PERSON can have subclasses STUDENT and EMPLOYEE, each with their own attributes and relationships.
- Specialization and generalization: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics of the entities in the superclass. Generalization is the reverse process of abstraction, where common properties of lower-level entities are grouped together to form a higher-level entity. For example, a specialization of PERSON can be based on the attribute occupation, and a generalization of STUDENT and EMPLOYEE can be PERSON.
- Category or union type: A category or union type is a subclass that represents a collection of entities from different entity types that share a common relationship with another entity type. For example, a category DEPENDENT can include entities from subclasses SPOUSE and CHILDREN, which are related to the superclass EMPLOYEE.
- Aggregation: Aggregation is the process of treating a relationship as an entity type, which allows relationships between relationships or between entities and relationships. For example, an aggregation PROJECT_ASSIGNMENT can represent the relationship between the entity types EMPLOYEE and PROJECT, and have its own attributes and relationships.

The extended ER model can be represented graphically using the following symbols :

- A rectangle for an entity type, with the name inside.
- An ellipse for an attribute, with the name inside. A key attribute is underlined, a multivalued attribute is double-lined, and a derived attribute is dashed.
- A diamond for a relationship type, with the name inside. A total participation is indicated by a double line, and a partial participation by a single line. A cardinality ratio is shown by placing numbers or symbols near the ends of a relationship line.
- A triangle for an ISA relationship, which connects a superclass to its subclasses. The subclasses are written below the triangle, separated by commas. A disjoint constraint is indicated by placing a D inside the triangle, and an overlap constraint by placing an O. A total specialization is indicated by a double line, and a partial specialization by a single line.
- A circle with a T inside for a category or union type, which connects a category to its member entity types. The category is written below the circle, and the member entity types are written above the circle, separated by commas.
- A dashed rectangle for an aggregation, which encloses the relationship type that is being aggregated and the entity types that participate in that relationship. The aggregation is treated as an entity type and can have its own attributes and relationships.

Here is an example of an extended ER diagram for a university database:

![EER diagram example](https://www.cs.toronto.edu/~jm/2507S/Notes04/EER.png)