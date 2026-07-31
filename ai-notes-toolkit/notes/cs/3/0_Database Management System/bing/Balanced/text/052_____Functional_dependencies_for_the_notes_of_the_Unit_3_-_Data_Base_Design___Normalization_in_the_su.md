### Functional dependencies

- A functional dependency (FD) is a constraint between two sets of attributes from a relation.
- A functional dependency X -> Y means that the values of Y are determined by the values of X. In other words, if two tuples have the same values for X, they must also have the same values for Y.
- A functional dependency is a property of the semantics or meaning of the attributes. It does not depend on the actual data in the relation.
- A functional dependency can be represented by an arrow diagram, where the attributes on the left of the arrow are called the determinant and the attributes on the right are called the dependent.
- For example, consider a relation Student with attributes RollNo, Name, Branch, and CGPA. A possible functional dependency is RollNo -> Name, which means that the name of a student is uniquely determined by their roll number. This can be represented by the following arrow diagram:

```
RollNo -> Name
```

- A relation is said to satisfy a functional dependency if the dependency holds for every possible instance of the relation.
- A set of functional dependencies F is said to be a cover for a relation R if F logically implies all the functional dependencies that hold on R.
- A set of functional dependencies F is said to be minimal if it is a cover for R and no proper subset of F is a cover for R. A minimal cover has the following properties:
  - No functional dependency in F has an extraneous attribute, i.e., an attribute that can be removed from the determinant or the dependent without affecting the cover.
  - No functional dependency in F can be derived from the other functional dependencies in F, i.e., F has no redundant dependencies.
  - Every functional dependency in F has a single attribute on the right side, i.e., F is in canonical form.
- A set of functional dependencies can be used to test whether a relation is in a certain normal form, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), or Boyce-Codd normal form (BCNF). These normal forms are defined based on the concepts of keys, superkeys, prime attributes, and non-prime attributes, which are explained below:
  - A superkey of a relation R is a set of attributes that uniquely identifies each tuple in R. For example, {RollNo, Name} is a superkey of Student, since no two students can have the same roll number and name.
  - A key of a relation R is a minimal superkey, i.e., a superkey that has no proper subset that is also a superkey. For example, {RollNo} is a key of Student, since it is a superkey and no subset of it is a superkey.
  - A relation R can have more than one key, in which case they are called candidate keys. For example, {RollNo} and {Name, Branch} are both candidate keys of Student.
  - A prime attribute of a relation R is an attribute that belongs to some key of R. For example, RollNo, Name, and Branch are prime attributes of Student.
  - A non-prime attribute of a relation R is an attribute that does not belong to any key of R. For example, CGPA is a non-prime attribute of Student.
- A relation R is in 1NF if every attribute of R is atomic, i.e., it cannot be further decomposed into smaller values. For example, Student is in 1NF, since all its attributes are atomic.
- A relation R is in 2NF if it is in 1NF and every non-prime attribute of R is fully functionally dependent on every key of R, i.e., it does not depend on a proper subset of any key. For example, Student is in 2NF, since CGPA is fully functionally dependent on {RollNo} and {Name, Branch}, which are the keys of Student.
- A relation R is in 3NF if it is in 2NF and every non-prime attribute of R is non-transitively dependent on every key of R, i.e., it does not depend on another non-prime attribute that depends on a key. For example, Student is in 3NF, since CGPA does not depend on any other non-prime attribute that depends on a key of Student.
- A relation R is in BCNF if it is in 3NF and every determinant of R is a superkey of R, i.e., there is no functional dependency X -> Y where X is not a superkey and Y is a non-prime attribute. For example, Student is in BCNF, since the only determinant of Student is RollNo,