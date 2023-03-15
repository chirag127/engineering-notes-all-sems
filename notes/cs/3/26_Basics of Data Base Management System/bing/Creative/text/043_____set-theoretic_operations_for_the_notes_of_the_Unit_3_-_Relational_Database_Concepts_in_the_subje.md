### Set-theoretic operations for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- Set-theoretic operations are the standard mathematical operations on sets that can be applied to relations in a database.
- Set-theoretic operations are binary operations, meaning they operate on two relations unlike unary operations like project, select and rename.
- The two relations involved in a set-theoretic operation must be union compatible, meaning they have the same number and type of attributes .
- The major set-theoretic operations are union, intersection and set difference.
- Union operation combines the tuples of two relations and eliminates any duplicates . The symbol for union is ∪.
- Intersection operation returns the tuples that are common to both relations . The symbol for intersection is ∩.
- Set difference operation returns the tuples that are in one relation but not in the other . The symbol for set difference is -.
- An example of set-theoretic operations using two relations R and S is shown below:

| R | A | B |
|---|---|---|
|   | 1 | 2 |
|   | 3 | 4 |
|   | 5 | 6 |

| S | A | B |
|---|---|---|
|   | 3 | 4 |
|   | 7 | 8 |
|   | 9 | 10 |

R ∪ S = 

| A | B |
|---|---|
| 1 | 2 |
| 3 | 4 |
| 5 | 6 |
| 7 | 8 |
| 9 | 10 |

R ∩ S = 

| A | B |
|---|---|
| 3 | 4 |

R - S = 

| A | B |
|---|---|
| 1 | 2 |
| 5 | 6 |

S - R = 

| A | B |
|---|---|
| 7 | 8 |
| 9 | 10 |