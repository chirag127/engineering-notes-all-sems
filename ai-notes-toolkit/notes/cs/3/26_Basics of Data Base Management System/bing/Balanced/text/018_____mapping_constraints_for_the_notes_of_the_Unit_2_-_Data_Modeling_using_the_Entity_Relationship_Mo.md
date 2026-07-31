### Mapping Constraints for the Notes of the Unit 2 - Data Modeling using the Entity Relationship Model in the Subject of Basics of Data Base Management System

- Mapping constraints are also known as the cardinality ratio, which corresponds to the number of relationship occurrences an entity can be involved in an entity-relationship model.
- Mapping constraints are useful for describing the relationship sets that involve more than two entity sets.
- There are two types of mapping constraints on the entity-relationship model: mapping cardinality and participation constraints.
- Mapping cardinality can be one of the following four types for a binary relationship set R on entity sets A and B:
  - One-to-one: Each entity in A is associated with at most one entity in B, and each entity in B is associated with at most one entity in A.
  - One-to-many: Each entity in A is associated with any number of entities in B, but each entity in B is associated with at most one entity in A.
  - Many-to-one: Each entity in A is associated with at most one entity in B, but each entity in B is associated with any number of entities in A.
  - Many-to-many: Each entity in A is associated with any number of entities in B, and each entity in B is associated with any number of entities in A.
- Participation constraints specify whether the existence of an entity depends on its being related to another entity via the relationship set.
- Participation constraints can be either total or partial for each entity set participating in a relationship set:
  - Total: Every entity in the entity set must participate in at least one relationship in the relationship set.
  - Partial: Some entities in the entity set may not participate in any relationship in the relationship set.
- Mapping constraints can be represented by using different notations in the entity-relationship diagrams, such as crow's foot, Chen, or UML.
- Mapping constraints can help to enforce data integrity and avoid redundancy in the database design.