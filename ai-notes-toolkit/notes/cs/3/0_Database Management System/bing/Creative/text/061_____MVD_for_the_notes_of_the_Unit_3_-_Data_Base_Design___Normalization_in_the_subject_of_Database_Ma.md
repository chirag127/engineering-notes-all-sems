### MVD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- MVD stands for **Multivalued Dependency** , which is a type of constraint between two sets of attributes in a relation.
- MVD means that for a single value of attribute A, multiple values of attribute B exist. For example, if a person has multiple hobbies and works on multiple projects, then there is a MVD between the person and the hobbies, and between the person and the projects.
- MVD is written as A --> --> B, which means A is multivalued dependent on B . This implies that the values of B are independent of each other for a given value of A.
- MVD plays a role in the **Fourth Normal Form (4NF)** of database normalization  , which is a process of eliminating redundancy and inconsistency in data .
- A relation is in 4NF if it is in **Boyce-Codd Normal Form (BCNF)** and has no MVD  . BCNF is a stricter version of **Third Normal Form (3NF)**, which requires that every determinant of a relation be a candidate key.
- To check for MVD, we can use the **complementation rule** , which states that if A --> --> B holds in a relation R, then A --> --> (R - (A U B)) also holds, where R - (A U B) is the set of attributes in R that are not in A or B .
- To remove MVD, we can use the **decomposition rule** , which states that if A --> --> B holds in a relation R, then we can decompose R into two relations: R1(A, B) and R2(A, R - (A U B)), where R1 and R2 are in 4NF .
- Decomposing a relation into 4NF preserves the **lossless join property** , which means that we can reconstruct the original relation from the decomposed relations by using the natural join operation .
- Decomposing a relation into 4NF may or may not preserve the **dependency preservation property** , which means that we can check the functional dependencies of the original relation by using the functional dependencies of the decomposed relations .