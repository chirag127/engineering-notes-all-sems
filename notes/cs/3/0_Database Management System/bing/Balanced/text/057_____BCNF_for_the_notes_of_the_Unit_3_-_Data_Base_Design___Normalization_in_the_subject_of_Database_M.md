### BCNF

- BCNF stands for **Boyce-Codd Normal Form**     .
- It is an advanced version of **3NF (Third Normal Form)**   .
- A table or a relation is in BCNF if it satisfies two conditions    :
  - It is already in 3NF.
  - For every functional dependency X -> Y, X is either a **super key** or a **candidate key**    .
- A functional dependency X -> Y means that the value of Y is determined by the value of X .
- A super key is a set of attributes that can uniquely identify a tuple in a relation .
- A candidate key is a minimal super key, that is, a super key that does not have any redundant attribute .
- BCNF eliminates the possibility of having **non-trivial functional dependencies** of attributes on anything other than a superset of a candidate key .
- Non-trivial functional dependencies are those that do not follow from the definition of a key.
- BCNF ensures that every attribute in a relation depends only on the key, the whole key, and nothing but the key .
- BCNF is also sometimes referred to as **3.5NF** or **3.5 Normal Form** .

#### Example

- Consider a relation R with five attributes: R(ABCDE).
- The functional dependencies are: FD = {A -> BC, C -> DE).
- The candidate key is: {A}.
- To check if R is in BCNF, we inspect each of the functional dependencies:
  - A -> BC: This satisfies the second condition of BCNF, as A is a candidate key.
  - C -> DE: This violates the second condition of BCNF, as C is not a super key.
- To convert R into BCNF, we decompose it into two relations:
  - R1(ABC) with FD = {A -> BC}.
  - R2(CDE) with FD = {C -> DE}.
- Both R1 and R2 are in BCNF, as they have only one functional dependency each, and the left-hand side is a candidate key.