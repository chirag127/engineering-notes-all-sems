# MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for **Multivalued Dependency**, which is a type of constraint between two sets of attributes in a relation.
- MVD means that for a single value of attribute `a`, multiple values of attribute `b` exist. For example, if a person named Geeks is working on two projects Microsoft and Oracle and has two hobbies Reading and Music, then the relation has MVD as follows:

| Name | Project | Hobby |
|------|---------|-------|
| Geeks | Microsoft | Reading |
| Geeks | Microsoft | Music |
| Geeks | Oracle | Reading |
| Geeks | Oracle | Music |

- We write MVD as `a --> --> b`, which is read as `a` is multivalued dependent on `b`.
- MVD plays a role in the **Fourth Normal Form (4NF)** of database normalization. Normalization is a process of organizing the data in a database to avoid redundancy, inconsistency, and anomalies.
- A relation is in 4NF if it is in **Boyce-Codd Normal Form (BCNF)** and has no MVD. BCNF is a stricter version of **Third Normal Form (3NF)**, which requires that every determinant in a relation is a candidate key.
- To remove MVD from a relation, we can use the following steps:
  - Identify the MVD in the relation, such as `a --> --> b`.
  - Decompose the relation into two relations, one with attributes `a` and `b`, and the other with attributes `a` and the rest of the attributes.
  - Check if the resulting relations are in 4NF, and repeat the process if necessary.
- For example, to remove the MVD from the relation above, we can decompose it into two relations as follows:

| Name | Project |
|------|---------|
| Geeks | Microsoft |
| Geeks | Oracle |

| Name | Hobby |
|------|-------|
| Geeks | Reading |
| Geeks | Music |

- These two relations are in 4NF, as they have no MVD and are in BCNF.