### MVD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- MVD stands for **Multivalued Dependency**.
- It is a type of dependency in which the presence of one or more rows in a table implies the presence of one or more other rows in the same table.
- MVD is a constraint between two sets of attributes in a relation.
- It is used in the process of normalization, specifically in the **Fourth Normal Form (4NF)**.
- A relation is in 4NF if, for every non-trivial MVD, the determinant is a superkey.
- MVD can be represented using the notation `X ->> Y`, where `X` and `Y` are sets of attributes and `X` is the determinant.
- MVD can be tested using the **chase algorithm**.
- MVD can be removed by decomposing the relation into two or more relations.
