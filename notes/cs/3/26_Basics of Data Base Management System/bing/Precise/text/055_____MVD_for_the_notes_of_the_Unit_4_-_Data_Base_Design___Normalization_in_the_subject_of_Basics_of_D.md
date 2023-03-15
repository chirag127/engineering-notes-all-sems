### MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for **Multi-Valued Dependency**.
- It is a type of dependency in which the presence of one or more rows in a table implies the presence of one or more other rows in the same table.
- MVD is a constraint between two sets of attributes in a relation.
- It is used in the process of normalization to decompose a relation into smaller relations that are in a higher normal form.
- MVD is a generalization of functional dependency (FD).
- In a relation R, a multi-valued dependency X ->> Y holds if, for every pair of tuples t1 and t2 in R such that t1[X] = t2[X], there exist tuples t3 and t4 in R such that t1[X] = t3[X], t2[X] = t4[X], t3[Y] = t1[Y], t4[Y] = t2[Y], and t3[Z] = t4[Z] for all attributes Z in R that are not in X or Y.
- MVD is used to identify redundancy in a relation and to decompose it into smaller relations that are in 4NF (Fourth Normal Form).
- A relation is in 4NF if, for every non-trivial MVD X ->> Y that holds over the relation, X is a superkey.
- MVD can be used to identify and eliminate redundancy in a relation, resulting in a more efficient and normalized database design.
