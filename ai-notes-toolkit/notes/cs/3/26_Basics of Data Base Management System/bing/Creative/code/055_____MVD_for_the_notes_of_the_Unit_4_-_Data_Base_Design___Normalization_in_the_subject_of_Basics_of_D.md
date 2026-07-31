### MVD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- MVD stands for **Multivalued Dependency**, which is a type of constraint between two sets of attributes in a relation.
- MVD means that for a single value of one attribute, multiple values of another attribute exist. For example, if a person has multiple hobbies and works on multiple projects, then there is a MVD between the person and the hobbies, and between the person and the projects.
- MVD is written as `A --> --> B`, which means that `A` is multivalued dependent on `B`. It is also equivalent to `B --> --> A`, which means that `B` is multivalued dependent on `A`.
- MVD is a special case of **Join Dependency**, which is a constraint that requires a relation to be equal to the join of its projections. A Join Dependency is written as `R = (R1, R2, ..., Rn)`, which means that `R` is equal to the natural join of `R1, R2, ..., Rn`.
- MVD is a binary Join Dependency, which means that it involves only two sets of values. A binary Join Dependency is written as `R = (R1, R2)`, which means that `R` is equal to the natural join of `R1` and `R2`.
- MVD plays a role in the **4NF** database normalization, which is a process of reducing redundancy and anomalies in a relation. 4NF is a refinement of **BCNF**, which is a stricter form of **3NF**.
- 4NF requires that a relation should not contain any MVD that is not implied by the candidate keys. A candidate key is a minimal set of attributes that can uniquely identify a tuple in a relation.
- To achieve 4NF, we need to decompose a relation that contains MVD into smaller relations that do not contain MVD. The decomposition should preserve the dependencies and the information in the original relation.
- An example of 4NF decomposition is as follows:

  - Suppose we have a relation `R(A, B, C, D)` with the following dependencies:

    - `A --> B`
    - `A --> --> C`
    - `A --> --> D`

  - The candidate key of `R` is `A`, and there are two MVDs that are not implied by the candidate key: `A --> --> C` and `A --> --> D`.
  - To decompose `R` into 4NF, we need to create three relations: `R1(A, B)`, `R2(A, C)`, and `R3(A, D)`, with the following dependencies:

    - `R1: A --> B`
    - `R2: A --> --> C`
    - `R3: A --> --> D`

  - The decomposition preserves the dependencies and the information in `R`, and eliminates the MVDs. The relations `R1`, `R2`, and `R3` are in 4NF.