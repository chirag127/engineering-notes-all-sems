 Here is the content in markdown format without any emojis or external links as per your instructions:

### Notes for Unit 4 - Database Design & Normalization

1. Database Design
- Logical design: What data is stored & relationships between data.
- Physical design: How data is stored & accessed (files, indices, etc.).

2. Normalization
- Remove redundancy & ensure data consistency.
- 1NF: Remove duplicate rows, each cell contains single value.
- 2NF: Remove partial dependencies, columns dependent on part of primary key.
- 3NF: Remove transitive dependencies, columns dependent on other non-key columns.
- BCNF, 4NF, 5NF: Further constraints to remove dependencies & reduce redundancy.

3. Benefits of Normalization
- Minimizes data redundancy.
- Prevents update, insertion & deletion anomalies.
- Makes the database more flexible to changes.
- Maximizes data consistency.
- Provides greater data integrity.

4. When to Denormalize
- To improve performance (less joins).
- When read-only (no update anomalies).
- For specific queries (denormalized views).
- When static data won't change.

The content is written in a formal tone with points in markdown format as per your instructions without any emojis or external links. Please let me know if you would like me to modify or expand the content in any way.