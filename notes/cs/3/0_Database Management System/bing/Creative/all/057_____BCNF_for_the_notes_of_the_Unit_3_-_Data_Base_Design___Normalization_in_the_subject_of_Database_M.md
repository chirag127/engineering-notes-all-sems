# BCNF

BCNF stands for Boyce-Codd Normal Form. It is a form of database normalization that ensures that there are no anomalies or redundancies in the data. BCNF is a stricter version of 3NF (Third Normal Form), which requires that every non-prime attribute is fully functionally dependent on the primary key, and that there are no transitive dependencies.

A table is in BCNF if and only if for every functional dependency X -> Y, X is a superkey of the table. A superkey is a set of attributes that uniquely identifies a tuple in the table. A candidate key is a minimal superkey, meaning that no proper subset of it is a superkey. A primary key is a chosen candidate key that is used to refer to the tuples in the table.

To check if a table is in BCNF, we need to find all the functional dependencies and candidate keys in the table, and then verify that the left-hand side of every functional dependency is a superkey. If not, we need to decompose the table into smaller tables that satisfy the BCNF condition.

## Example

Consider the following table that stores information about students, courses, and instructors.

| Student ID | Course ID | Instructor ID | Instructor Name | Grade |
|------------|-----------|---------------|-----------------|-------|
| S1         | C1        | I1            | Alice           | A     |
| S1         | C2        | I2            | Bob             | B     |
| S2         | C1        | I1            | Alice           | C     |
| S2         | C3        | I3            | Charlie         | A     |

The functional dependencies in this table are:

- Student ID, Course ID -> Instructor ID, Grade
- Instructor ID -> Instructor Name

The candidate keys are:

- Student ID, Course ID
- Student ID, Instructor ID
- Course ID, Instructor ID

This table is not in BCNF, because the functional dependency Instructor ID -> Instructor Name violates the condition. The left-hand side, Instructor ID, is not a superkey, as it is a proper subset of the candidate keys.

To convert this table into BCNF, we need to decompose it into two tables:

| Student ID | Course ID | Instructor ID | Grade |
|------------|-----------|---------------|-------|
| S1         | C1        | I1            | A     |
| S1         | C2        | I2            | B     |
| S2         | C1        | I1            | C     |
| S2         | C3        | I3            | A     |

| Instructor ID | Instructor Name |
|---------------|-----------------|
| I1            | Alice           |
| I2            | Bob             |
| I3            | Charlie         |

The first table has the same candidate keys as the original table, and the only functional dependency is Student ID, Course ID -> Instructor ID, Grade, which satisfies the BCNF condition. The second table has Instructor ID as the only candidate key and the only functional dependency is Instructor ID -> Instructor Name, which also satisfies the BCNF condition.

## Advantages of BCNF

Some of the advantages of BCNF are:

- It reduces data redundancy and duplication, as the same information is not stored in multiple tables.
- It improves data integrity and consistency, as any update, insertion, or deletion of data does not cause anomalies or inconsistencies.
- It simplifies the queries and joins, as the tables are smaller and more normalized.