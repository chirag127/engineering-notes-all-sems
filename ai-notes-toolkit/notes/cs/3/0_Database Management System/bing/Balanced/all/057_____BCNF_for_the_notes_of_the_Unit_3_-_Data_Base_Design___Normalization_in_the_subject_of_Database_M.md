# BCNF

- BCNF stands for Boyce-Codd Normal Form, which is a higher form of normalization than 3NF.
- A relation R is in BCNF if for every non-trivial functional dependency X -> Y, X is a superkey of R.
- A superkey is a set of attributes that uniquely identifies a tuple in a relation.
- BCNF eliminates redundancy and anomalies caused by transitive dependencies, where a non-key attribute depends on another non-key attribute.
- To convert a relation to BCNF, we need to decompose it into smaller relations that satisfy the BCNF condition.
- The decomposition should be lossless, meaning that we can reconstruct the original relation by joining the decomposed relations.
- The decomposition should also preserve the dependencies, meaning that we do not lose any functional dependencies by decomposing the relation.
- An example of a relation that is not in BCNF is:

| Student ID | Course ID | Instructor |
|------------|-----------|------------|
| S1         | C1        | I1         |
| S1         | C2        | I2         |
| S2         | C1        | I1         |
| S2         | C3        | I3         |

- In this relation, the functional dependencies are:

  - Student ID -> Course ID
  - Course ID -> Instructor

- Neither Student ID nor Course ID is a superkey, so the relation is not in BCNF.
- To convert it to BCNF, we can decompose it into two relations:

  - R1(Student ID, Course ID)
  - R2(Course ID, Instructor)

- The decomposition is lossless, as we can join R1 and R2 on Course ID to get the original relation.
- The decomposition also preserves the dependencies, as both R1 and R2 are in BCNF.