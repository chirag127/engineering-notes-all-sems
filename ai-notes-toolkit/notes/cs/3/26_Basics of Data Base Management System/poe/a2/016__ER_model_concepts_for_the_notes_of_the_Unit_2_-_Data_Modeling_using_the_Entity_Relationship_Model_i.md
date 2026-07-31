 Here is the formal content in Markdown format without any emojis or external links for the given topic:

### ER model concepts for the notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the subject of Basics of Data Base Management System

1. Entity: An entity is a physical object or a conceptual thing that has relevance to the data being modeled. For example, EMPLOYEE, PROJECT, DEPARTMENT etc. are entities in a Company database.

2. Entity Type: Entity type defines a collection of entities that share common properties or characteristics. For example, EMPLOYEE is an entity type that represents the collection of all employees.

3. Attribute: An attribute is a property or characteristic of an entity type. For example, Name, Age, Salary etc. are attributes of EMPLOYEE entity type.

4. Relationship: A relationship is an association between two or more entities. For example, WORKS_ON is a relationship between EMPLOYEE and PROJECT entities.

5. Degree: The degree of a relationship is the number of entity types that participate in that relationship. A binary relationship involves two entity types, a ternary relationship involves three entity types and so on.

6. Cardinality: Cardinality specifies the number of instances of one entity type that can be associated with the instances of another entity type. For example, one employee works on one project (1:1), one employee works on multiple projects (1:M) etc.

7. Connectivity: Connectivity specifies whether the instances of an entity type must participate in a relationship. It can be either total (every entity participates) or partial (some entities may not participate).

8. Weak Entity: A weak entity is an entity type that cannot be uniquely identified by its own attributes alone. It needs a identifying relationship with another entity type (owner entity) to identify its instances. For example, CONTRACT is a weak entity if it depends on EMPLOYEE and PROJECT entities to identify each contract.

9. Key: A key is a set of one or more attributes that uniquely identifies each instance of an entity type. For example, SSN is a key for EMPLOYEE entity type. A key that contains two or more attributes is called a composite key.