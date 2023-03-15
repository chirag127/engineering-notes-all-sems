# Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases . It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The main extensions of the EER model are  :

- **Subclasses and Superclasses**: A subclass is a subset of entities of a superclass that share some common attributes or relationships. A superclass is a superset of entities that have some common attributes or relationships. For example, a superclass PERSON can have subclasses STUDENT and TEACHER, each with their own attributes and relationships.
- **Specialization and Generalization**: Specialization is the process of defining subclasses of a superclass based on some distinguishing characteristics. Generalization is the process of defining a superclass of several subclasses based on their common features. For example, a specialization of PERSON can be based on the occupation attribute, resulting in subclasses STUDENT and TEACHER. A generalization of STUDENT and TEACHER can be based on their common attributes, resulting in a superclass PERSON.
- **Category or Union Type**: A category or union type is a subclass that represents a collection of entities from different superclasses that share some common attributes or relationships. A category or union type can be total or partial, depending on whether all or some entities from the superclasses belong to the subclass. For example, a category or union type EMPLOYEE can represent a collection of entities from the superclasses STUDENT and TEACHER that have a common attribute salary.
- **Aggregation**: Aggregation is the process of treating a relationship as an entity, which can have its own attributes and relationships. Aggregation allows representing complex relationships among entities and relationships. For example, an aggregation of the relationship WORKS_FOR between EMPLOYEE and DEPARTMENT can have an attribute position, which represents the role of the employee in the department.

The EER model can be represented graphically using EER diagrams, which use symbols and notations to depict the entities, attributes, relationships, and constraints of the database. Some of the common symbols and notations are:

- **Entity**: A rectangle with the entity name.
- **Attribute**: An oval with the attribute name, connected to the entity or relationship by a line.
- **Relationship**: A diamond with the relationship name, connected to the entities by lines.
- **Key Attribute**: An attribute that uniquely identifies an entity, underlined in the entity name.
- **Composite Attribute**: An attribute that consists of several sub-attributes, represented by an oval with the attribute name and ovals with the sub-attribute names, connected by lines.
- **Multivalued Attribute**: An attribute that can have more than one value for an entity, represented by a double oval with the attribute name.
- **Derived Attribute**: An attribute that can be derived from other attributes, represented by a dashed oval with the attribute name.
- **Weak Entity**: An entity that depends on another entity for its existence, represented by a double rectangle with the entity name.
- **Identifying Relationship**: A relationship that relates a weak entity to its owner entity, represented by a double diamond with the relationship name and a double line connecting to the weak entity.
- **Subclass**: A rectangle with the subclass name inside the rectangle of the superclass, connected by a line with a triangle pointing to the superclass.
- **Superclass**: A rectangle with the superclass name, containing one or more rectangles with the subclass names.
- **Disjoint Constraint**: A constraint that specifies that the subclasses of a superclass are mutually exclusive, represented by a circle with a 'd' inside, connected to the line with the triangle.
- **Overlap Constraint**: A constraint that specifies that the subclasses of a superclass can have common entities, represented by a circle with an 'o' inside, connected to the line with the triangle.
- **Total Constraint**: A constraint that specifies that every entity in the superclass must belong to at least one subclass, represented by a double line connecting the superclass and the subclasses.
- **Partial Constraint**: A constraint that specifies that some entities in the superclass may not belong to any subclass, represented by a single line connecting the superclass and the subclasses.
- **Category or Union Type**: A circle with the category name inside, connected to the superclasses by lines with a triangle pointing to the circle.
- **Aggregation**: A rectangle with a dashed border, enclosing the relationship and the entities involved in the aggregation, connected to another entity