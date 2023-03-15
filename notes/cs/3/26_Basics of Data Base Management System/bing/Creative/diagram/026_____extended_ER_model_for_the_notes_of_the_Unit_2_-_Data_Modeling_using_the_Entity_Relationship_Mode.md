### Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. The EER model reflects more precisely the properties and constraints that are found in complex databases. The EER model includes the following concepts in addition to the ER model concepts:

- Subclasses and Superclasses: A subclass is a subset of entities of a superclass that share some common attributes or relationships. A superclass is a superset of entities that have one or more subclasses. For example, a superclass PERSON can have subclasses STUDENT and EMPLOYEE.
- Specialization and Generalization: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics. Generalization is the reverse process of abstraction, where common properties of subclasses are grouped together to form a superclass. For example, a specialization of PERSON can be based on the attribute occupation, and a generalization of STUDENT and EMPLOYEE can be PERSON.
- Category or Union Type: A category or union type is a subclass that represents a collection of entities from different superclasses that share a common attribute or relationship. A category or union type is also called a shared subclass. For example, a category or union type PART_TIME can represent entities from both STUDENT and EMPLOYEE superclasses that work part-time.
- Aggregation: Aggregation is the process of treating a relationship as an entity, which allows relationships to have attributes and participate in other relationships. Aggregation is also called a composite entity. For example, an aggregation of the relationship WORKS_ON between EMPLOYEE and PROJECT can have an attribute HOURS and participate in another relationship with DEPARTMENT.

The EER model can be represented graphically using the following symbols:

![EER Symbols](https://www.cs.toronto.edu/~jm/2507S/Notes04/EER.png)

An example of an EER diagram for a university database is shown below:

![EER Example](https://media.geeksforgeeks.org/wp-content/uploads/20191121174419/Enhanced-ER-Diagram-Example.jpg)