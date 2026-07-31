### MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for **Multi-Valued Dependency**.
- It is a type of dependency in which the presence of one or more rows in a table implies the presence of one or more other rows in the same table.
- MVD is used in the process of database normalization, specifically in the **Fourth Normal Form (4NF)**.
- A table is considered to be in 4NF if it has no multi-valued dependencies.
- MVD can be represented using the notation **X ->> Y**, where X and Y are sets of attributes in a relation.
- To check for MVD, the **complementation rule** can be used. This rule states that if X ->> Y holds, then X ->> (R - XY) must also hold, where R is the set of all attributes in the relation.
- MVD can be removed from a relation by decomposing it into two or more relations, each of which is in 4NF.
