# Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Database Management System

Mapping constraints are also known as the cardinality ratio. They express the number of entities to which another entity can be related via a relationship set. They are useful in describing the relationship sets that involve more than two entity sets. There are two types of mapping constraints in the entity relationship model:

- Mapping cardinality or cardinality ratio: This corresponds to the number of relationship occurrences an entity can be involved in an entity relationship model. For binary relationship set R on an entity set A and B, there are four possible mapping cardinalities:

  - One to one: An entity in A is related to at most one entity in B, and an entity in B is related to at most one entity in A.
  - One to many: An entity in A is related to any number of entities in B, but an entity in B is related to at most one entity in A.
  - Many to one: An entity in A is related to at most one entity in B, but an entity in B is related to any number of entities in A.
  - Many to many: An entity in A is related to any number of entities in B, and an entity in B is related to any number of entities in A.

- Participation constraints: This specifies whether the existence of an entity depends on its being related to another entity via the relationship set. There are two types of participation constraints:

  - Total participation: Every entity in the entity set participates in at least one relationship in the relationship set. This is also called existence dependency.
  - Partial participation: Some entities in the entity set may not participate in any relationship in the relationship set. This is also called weak entity.