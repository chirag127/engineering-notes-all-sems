# Extended ER Model

The extended entity-relationship (EER) model is a high-level or conceptual data model that incorporates extensions to the original entity-relationship (ER) model, used in the design of databases. It was developed to reflect more precisely the properties and constraints that are found in complex databases.

The extended ER model includes the following concepts in addition to the ER model concepts :

- Subclasses and superclasses: A subclass is a subset of entities of a superclass that have some additional attributes or relationships. A superclass is a set of entities that share some common attributes or relationships. For example, a student can be a subclass of a person, and a person can be a superclass of a student.
- Specialization and generalization: Specialization is the process of defining a set of subclasses of a superclass based on some distinguishing characteristics. Generalization is the process of defining a superclass from a set of subclasses by identifying their common features. For example, a person can be specialized into student, employee, and customer based on their roles.
- Category or union type: A category or union type is a subclass that represents a collection of entities from different superclasses that share some common attributes or relationships. For example, a part-time employee can be a category of student and employee.
- Aggregation: Aggregation is the process of grouping a set of entities and relationships into a single entity or relationship. For example, a project can be an aggregation of a set of tasks and employees.

The extended ER model can be represented graphically using the following symbols:

- A rectangle for an entity type
- An ellipse for an attribute
- A diamond for a relationship type
- A line for a link between an entity type and a relationship type or between an attribute and an entity type
- A double line for a total participation constraint
- A dashed line for a partial participation constraint
- A double ellipse for a multivalued attribute
- A dashed ellipse for a derived attribute
- A triangle for a superclass or subclass
- A line with a circle for a disjoint constraint
- A line with a double circle for an overlapping constraint
- A line with a d for a specialization or generalization
- A line with a u for a category or union type
- A dashed rectangle for an aggregation

Here is an example of an extended ER diagram for a university database:

![EER diagram](https://www.cs.toronto.edu/~jm/2507S/Notes04/EER.png)