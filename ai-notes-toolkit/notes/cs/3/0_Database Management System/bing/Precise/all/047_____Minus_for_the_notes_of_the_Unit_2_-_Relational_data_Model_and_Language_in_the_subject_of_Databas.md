# Unit 2 - Relational Data Model and Language

## Relational Data Model
- The relational data model is a way to represent data in a structured format using relations (tables).
- Each relation consists of a set of attributes (columns) and a set of tuples (rows).
- Each tuple represents a unique entity or relationship in the data.
- The attributes of a relation define the characteristics of the entities or relationships represented by the tuples.
- The relational model is based on the concept of mathematical relations, and it uses set theory and predicate logic to define and manipulate data.

## Relational Algebra
- Relational algebra is a procedural query language used to manipulate relations.
- It consists of a set of operators that can be applied to relations to produce new relations as a result.
- The basic operators of relational algebra are:
  - Selection: selects a subset of tuples from a relation based on a condition.
  - Projection: selects a subset of attributes from a relation.
  - Union: combines two relations with the same set of attributes.
  - Difference: removes tuples from one relation that are also present in another relation.
  - Cartesian product: combines tuples from two relations by forming all possible combinations.
  - Join: combines tuples from two relations based on a common attribute.

## Structured Query Language (SQL)
- SQL is a declarative language used to manipulate and query data in a relational database.
- It is based on relational algebra and allows users to specify the desired result without specifying how to achieve it.
- SQL consists of a set of commands used to define, manipulate, and query data.
- The main commands of SQL are:
  - SELECT: used to query data from one or more relations.
  - INSERT: used to insert new tuples into a relation.
  - UPDATE: used to modify existing tuples in a relation.
  - DELETE: used to remove tuples from a relation.
  - CREATE: used to define new relations, views, and indexes.
  - ALTER: used to modify the structure of existing relations.
  - DROP: used to remove relations, views, and indexes.
