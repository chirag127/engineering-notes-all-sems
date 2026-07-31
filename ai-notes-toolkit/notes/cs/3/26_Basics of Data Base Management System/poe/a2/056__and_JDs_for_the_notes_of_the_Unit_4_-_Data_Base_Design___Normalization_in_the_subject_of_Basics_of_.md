 Here is the formal content in Markdown format without any emojis or external links for the given topic:

### Notes for Unit 4 - Database Design & Normalization

1. Database Design
- Logical design: Conceptual structure of the database in terms of entities, attributes and relationships.ER modelling is used.
- Physical design: Implementation of the logical design using a specific DBMS. Decisions are taken regarding the actual storage structures, indexes, access paths, etc.

2. Functional Dependencies
- Determining attributes of a relation that uniquely determine other attributes.
- Examples: In a relation R(A,B,C), if each value of A uniquely determines a value of B, then B is functionally dependent on A.
- Notation: B → A or B → {A} ("B functionally determines A")

3. Normalization
- Removing redundancies and ensuring data dependencies make sense to prevent anomalies.
- 1NF: No repeating groups, all attributes have unique names.
- 2NF: Meeting 1NF and no partial dependencies, i.e. no non-prime attributes dependent on a proper subset of candidate keys.
- 3NF: Meeting 2NF and no transitive dependencies, i.e. no non-prime attribute dependent on another non-prime attribute.
- BCNF, 4NF, 5NF: Further normal forms to remove more complex dependencies and anomalies.

[Content continues in the same formal tone...]