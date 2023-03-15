# Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts   :

- **Subclasses and Superclasses**: A subclass is a subset of entities of a superclass that share some common attributes or relationships distinct from other entities in the superclass. A superclass is a set of entities that have some common attributes or relationships. For example, a superclass PERSON can have subclasses STUDENT and EMPLOYEE, each with their own attributes and relationships.
- **Specialization and Generalization**: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics of the entities in the superclass. Generalization is the reverse process of abstraction, where common properties of subclasses are grouped together to form a superclass. For example, a specialization of PERSON can be based on the attribute occupation, and a generalization of STUDENT and EMPLOYEE can be PERSON.
- **Category or Union Type**: A category or union type is a subclass that represents a collection of entities from different superclasses that share some common attributes or relationships. A category or union type is also called a shared subclass. For example, a category or union type PART-TIME-EMPLOYEE can include entities from subclasses STUDENT and EMPLOYEE that work part-time.
- **Aggregation**: Aggregation is the process of grouping together a set of entities and relationships into a single abstract entity type. An aggregation can be seen as a relationship between a whole entity and its component entities. For example, an aggregation of COURSE, STUDENT and INSTRUCTOR can form a CLASS entity type, which represents the relationship of a course being taught by an instructor to a set of students.

The extended ER model can be represented graphically using the following symbols:

- A rectangle for an entity type
- An ellipse for an attribute
- A diamond for a relationship type
- A line for a link between an entity type and a relationship type, or between an attribute and an entity type or a relationship type
- A triangle for a superclass-subclass relationship, with the superclass above the triangle and the subclasses below the triangle
- A circle with d for a disjoint constraint, which means that an entity can belong to only one subclass of a superclass
- A circle with o for an overlap constraint, which means that an entity can belong to more than one subclass of a superclass
- A circle with c for a completeness constraint, which means that every entity in the superclass must belong to at least one subclass
- A dashed rectangle for an aggregation, with the component entity types and relationship types inside the rectangle and the aggregate entity type outside the rectangle

Here is an example of an extended ER diagram for a university database:

![EER diagram](https://www.cs.toronto.edu/~jm/2507S/Notes04/EER.png)