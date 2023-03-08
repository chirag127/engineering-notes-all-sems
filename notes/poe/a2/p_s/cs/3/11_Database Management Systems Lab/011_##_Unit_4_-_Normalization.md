 Here is the content written in markdown format for the topic ## Unit 4 - Normalization:

## Unit 4 - Normalization

Normalization is a database design technique which organizes tables in a database and reduces redundancy and dependency of data. It divides larger tables into smaller tables and links them using relationships.

The key advantages of normalization are:

1. Removes redundancy: Removes duplicate data and ensures that data is stored only once. This reduces storage space and maintains consistency as there is only one copy of data.
2. Removes anomalies: Avoid issues like update, insertion and deletion anomalies which can corrupt data.
3. Maintains integrity: Enforces integrity constraints on the data and prevents inconsistent dependencies.
4. Optimizes performance: Queries on normalized tables are often faster as only relevant data is fetched leading to improved performance.

There are three normal forms for normalization:

1. First Normal Form (1NF): There are no repeating groups or arrays of data. Entities are atomic.
2. Second Normal Form (2NF): The table is in 1NF and all non-key columns are dependent on the primary key.
3. Third Normal Form (3NF): The table is in 2NF and all columns are directly dependent on the primary key and not on other columns.

Normalization is a step-by-step process where each form must be achieved before moving to the next one. Denormalization can be done once for performance optimizations but normalization is critical for maintaining data integrity and consistency.

Detailed examples, codes, diagrams, advantages, disadvantages and applications can be included for each normal form to understand the concepts in depth and practice normalization.