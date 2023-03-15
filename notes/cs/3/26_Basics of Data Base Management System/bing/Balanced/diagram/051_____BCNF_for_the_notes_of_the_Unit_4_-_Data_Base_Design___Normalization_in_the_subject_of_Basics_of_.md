### BCNF

- BCNF stands for **Boyce-Codd Normal Form**     .
- It is an advanced version of **3NF** (Third Normal Form)   .
- It is also sometimes referred to as **3.5NF** or **3.5 Normal Form**.
- A table or a relation is in BCNF if it satisfies the following conditions    :
  - It is already in 3NF.
  - For every functional dependency X -> Y, X is either a **super key** or a **candidate key** of the table or relation.
- A super key is a set of attributes that can uniquely identify a tuple in a relation .
- A candidate key is a minimal super key, that is, a super key that does not have any redundant attribute .
- A functional dependency X -> Y means that the values of Y are determined by the values of X .
- A functional dependency is non-trivial if Y is not a subset of X .
- The purpose of BCNF is to **reduce redundancy** and **eliminate anomalies** in the data   .
- An anomaly is a situation where the data is inconsistent or incorrect due to poor database design .
- There are three types of anomalies: **insertion**, **deletion**, and **update** .
- An insertion anomaly occurs when a new tuple cannot be inserted into a relation without providing some irrelevant or unknown information .
- A deletion anomaly occurs when deleting a tuple from a relation causes some other information to be lost .
- An update anomaly occurs when changing the value of an attribute in a tuple requires changing the same value in multiple tuples .
- To convert a relation into BCNF, we need to **decompose** it into smaller relations that satisfy the BCNF conditions    .
- The decomposition should be **lossless**, meaning that no information is lost when joining the smaller relations back together .
- The decomposition should also **preserve** the functional dependencies of the original relation .
- There are different algorithms for finding a BCNF decomposition, such as the **synthesis algorithm** and the **decomposition algorithm** .
- The synthesis algorithm starts with a set of functional dependencies and generates a set of relations that are in BCNF and preserve the dependencies .
- The decomposition algorithm starts with a relation that is not in BCNF and iteratively splits it into smaller relations that are in BCNF .
- The decomposition algorithm may not always preserve the dependencies, so it may require additional steps to check and restore them .
- BCNF is not always achievable or desirable, as it may result in too many relations or loss of dependencies .
- In such cases, a lower normal form, such as 3NF, may be preferred .

#### Example of BCNF

- Consider the following relation R with four attributes :

| A | B | C | D |
|---|---|---|---|
| 1 | 2 | 3 | 4 |
| 1 | 2 | 5 | 6 |
| 7 | 8 | 9 | 10 |

- The functional dependencies are:

  - A -> B
  - C -> D

- The candidate keys are:

  - {A, C}
  - {B, C}

- The relation R is not in BCNF, because the functional dependency A -> B violates the second condition of BCNF .
- A is not a super