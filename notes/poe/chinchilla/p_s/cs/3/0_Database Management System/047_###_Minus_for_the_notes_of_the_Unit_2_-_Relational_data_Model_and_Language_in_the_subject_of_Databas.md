### Minus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

Relational data model is one of the most widely used data models in Database Management System. It is based on the concept of relations, which are tables with rows and columns. Minus is one of the relational operators used in the relational algebra. It is used to find the difference between two tables, i.e., the tuples that are present in one table but not in the other.

#### Syntax

The syntax for Minus operator is as follows:

```
R - S
```

Where R and S are two relations or tables.

#### Working

The Minus operator works by comparing the tuples of two tables and returning the tuples that are present in the first table but not in the second table. The resulting table will have the same attributes as the first table.

#### Example

Consider two tables T1 and T2:

T1:

| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

T2:

| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |

Applying Minus operator on T1 and T2, we get:

```
T1 - T2:

| A | B | C |
|---|---|---|
| 7 | 8 | 9 |
```

#### Advantages

- Minus operator is useful in finding the difference between two tables.
- It can be used to compare two tables and identify missing or extra data.

#### Disadvantages

- Minus operator can be computationally expensive for large tables.
- It requires the tables to have the same schema.

#### Applications

Minus operator can be used in various applications, such as:

- Data analysis
- Data cleaning
- Data integration

In conclusion, Minus operator is a useful relational operator in Database Management System. It is used to find the difference between two tables and can be applied in various applications.