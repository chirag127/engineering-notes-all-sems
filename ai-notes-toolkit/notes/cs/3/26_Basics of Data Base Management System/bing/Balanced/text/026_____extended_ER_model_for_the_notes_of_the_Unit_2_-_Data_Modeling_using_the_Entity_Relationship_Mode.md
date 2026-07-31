### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts in addition to the ER model concepts :

- **Subclasses and Superclasses**: A subclass is a subset of entities of a superclass that share some additional attributes or relationships. A superclass is a superset of entities that have some common attributes or relationships. For example, a STUDENT entity can be a subclass of a PERSON entity, and a PERSON entity can be a superclass of a STUDENT entity.
- **Specialization and Generalization**: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics of the entities in the superclass. Generalization is the reverse process of abstraction, where common properties of subclasses are grouped together to form a superclass. For example, a PERSON entity can be specialized into STUDENT and EMPLOYEE entities based on their roles, and STUDENT and EMPLOYEE entities can be generalized into a PERSON entity based on their common attributes.
- **Category or Union Type**: A category or union type is a subclass that represents a collection of entities from different entity types that share some common characteristics. For example, a VEHICLE entity can be a category of CAR, TRUCK, and BIKE entities, where each entity type has its own attributes and relationships, but they all share some common attributes such as color, model, and license number.
- **Aggregation**: Aggregation is the process of treating a relationship as an entity type, which allows relationships to have attributes and participate in other relationships. For example, a WORKS_ON relationship between an EMPLOYEE entity and a PROJECT entity can be aggregated into a WORK_ASSIGNMENT entity, which can have attributes such as hours, start date, and end date, and can participate in other relationships such as REPORTS_TO or SUPERVISES.

The extended ER model can be represented graphically using the following symbols :

- A rectangle for an entity type
- An ellipse for an attribute
- A diamond for a relationship type
- A line for a link between an entity type and a relationship type, or between an attribute and an entity type or a relationship type
- A double line for a total participation constraint
- A single line for a partial participation constraint
- A dashed line for a weak entity type or a weak relationship type
- A double rectangle for a weak entity type
- A double diamond for a weak relationship type
- A circle with a d inside for a derived attribute
- A triangle with an ISA inside for a superclass/subclass relationship
- A circle with a c inside for a category or union type
- A dashed rectangle for an aggregation

Here is an example of an extended ER diagram for a university database:

![EER diagram example](https://www.cs.toronto.edu/~jm/2507S/Notes04/EER.png)