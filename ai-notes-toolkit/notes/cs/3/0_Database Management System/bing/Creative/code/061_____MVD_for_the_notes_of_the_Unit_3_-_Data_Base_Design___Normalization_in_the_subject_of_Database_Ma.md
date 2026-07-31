### MVD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- A multivalued dependency (MVD) is a constraint between two sets of attributes in a relation.
- A MVD means that for a single value of one attribute, multiple values of another attribute exist.
- For example, if a relation R has attributes A, B, and C, and A --> --> B is a MVD, then for each value of A, there can be multiple values of B, and these values are independent of the values of C.
- A MVD is a special case of a join dependency, with only two sets of values involved.
- A MVD can cause redundancy and inconsistency in a relation, as the same values of B may be repeated for different values of C.
- To eliminate MVDs, a relation can be decomposed into two or more relations using the 4th normal form (4NF) rule.
- The 4NF rule states that a relation is in 4NF if it is in Boyce-Codd normal form (BCNF) and has no MVDs.
- To decompose a relation into 4NF, we can use the following algorithm:
  - Start with a relation R and a set of functional dependencies (FDs) and MVDs on R.
  - For each MVD A --> --> B on R, do the following:
    - Remove the MVD from the set of dependencies.
    - Replace R with two relations: R1 = (A, B) and R2 = (A, R - B).
    - Project the FDs on R1 and R2, and add them to the set of dependencies.
  - For each relation Ri, check if it is in BCNF. If not, decompose it further using the BCNF algorithm.
  - The final set of relations is in 4NF.
- Normalization reduces redundancy, inconsistency, and programming effort, as the rules are enforced in one place, one way, one time.