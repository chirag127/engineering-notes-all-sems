# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its information needs.
  - Ensure data integrity, consistency, and quality.
  - Minimize data redundancy and duplication.
  - Optimize data access and performance.
  - Facilitate data maintenance and evolution.
- Database design follows a top-down or bottom-up approach, depending on the level of abstraction and detail required.
  - Top-down approach: Starts with a conceptual model that captures the high-level concepts and relationships, and then refines it into a logical model that specifies the data types and constraints, and finally translates it into a physical model that defines the storage and implementation details.
  - Bottom-up approach: Starts with a physical model that reflects the existing data sources and structures, and then abstracts it into a logical model that generalizes the data types and constraints, and finally creates a conceptual model that summarizes the main concepts and relationships.
- Database design can use different data models to represent the data and its structure, such as:
  - Relational model: Represents data as tables (relations) with rows (tuples) and columns (attributes), and defines relationships and constraints using primary keys, foreign keys, and referential integrity rules.
  - Hierarchical model: Represents data as a tree-like structure with nodes (records) and links (pointers), and defines relationships and constraints using parent-child and ancestor-descendant associations.
  - Network model: Represents data as a graph-like structure with nodes (records) and links (pointers), and defines relationships and constraints using owner-member and set associations.
  - Entity-relationship model: Represents data as a set of entities and relationships, and defines attributes and constraints using entity types, relationship types, and cardinality ratios.
  - Object-oriented model: Represents data as a collection of objects and classes, and defines attributes and constraints using inheritance, encapsulation, and polymorphism.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization also helps to improve the database design by ensuring the following properties:
  - Atomicity: Each attribute value is indivisible and cannot be further decomposed.
  - Consistency: Each attribute value conforms to a predefined domain and format.
  - Uniqueness: Each row in a table can be uniquely identified by a primary key or a combination of attributes.
  - Non-redundancy: Each attribute value is stored only once and can be derived from other attributes if needed.
  - Dependency preservation: Each functional dependency between attributes is preserved in the normalized schema.
  - Lossless decomposition: No information is lost or added when splitting or joining tables.
- Normalization is based on the concept of functional dependency, which is a relationship between two sets of attributes, such that the value of one set determines the value of the other set.
- Normalization applies a series of rules or normal forms to check and eliminate the anomalies or problems caused by functional dependencies, such as:
  - First normal form (1NF): Eliminates repeating groups or multivalued attributes by ensuring that each attribute value is atomic and unique within a row.
  - Second normal form (2NF): Eliminates partial dependencies by ensuring that each non-key attribute depends on the whole primary key and not on a subset of it.
  - Third normal form (3NF): Eliminates transitive dependencies by ensuring that each non-key attribute depends only on the primary key and not on any other non-key attribute.
  - Boyce-Codd normal form (BCNF): Eliminates non-trivial dependencies by ensuring that each determinant is a candidate key or a superkey.
  - Fourth normal form (4NF): Eliminates multivalued dependencies by ensuring that each attribute depends on the primary key and not on any other attribute or set of attributes.
  - Fifth normal form (5NF): Eliminates join dependencies by ensuring that each table is irreducible and cannot be further decomposed without losing information.