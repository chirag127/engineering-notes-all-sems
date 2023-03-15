### MVD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- MVD stands for **Multi-Valued Dependency**.
- It is a type of dependency in which the presence of one attribute or set of attributes depends on the presence of another attribute or set of attributes, but not on the key of the relation.
- MVD is used in the process of normalization, specifically in the **Fourth Normal Form (4NF)**.
- A relation is in 4NF if, for every non-trivial MVD, the determinant is a superkey.
- MVD can be represented using the notation `X ->> Y`, where `X` and `Y` are sets of attributes and `X` determines `Y`.
- To check for MVDs, one can use the **chase algorithm** or the **tableau method**.
- MVDs can be used to decompose a relation into smaller relations that are in 4NF.
