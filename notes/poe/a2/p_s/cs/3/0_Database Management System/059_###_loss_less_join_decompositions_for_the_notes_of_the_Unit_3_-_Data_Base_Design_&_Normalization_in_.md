 Here is the content in markdown format for the topic - ### Lossless Join Decompositions for the notes of Unit 3 - Data Base Design & Normalization in the subject Database Management System:

### Lossless Join Decompositions

- Lossless join decompositions refer to breaking down a relation into multiple relations such that the original relation can be constructed by joining these decomposed relations without losing any data.
- The decomposed relations are in Boyce-Codd normal form(BCNF) i.e. every determinant is a candidate key.
- The advantages of lossless join decompositions are:
    - The decomposed relations are in BCNF and hence are normalized.
    - The decomposed relations have lesser redundancy as compared to the original relation.
    - The decomposed relations are easier to understand and maintain as compared to the original relation.
- The disadvantages are:
    - Additional joins are required to construct the original relation which can reduce performance.
    - The decomposed schema may not reflect the real-world scenario distinctly.
- Examples:
    - Decompose relation Student(rollno, name, class, age) into Student_detail(rollno, name, age) and Class_detail(class)
    - Decompose relation Employee(empid, name, deptno, salary) into Employee_detail(empid, name) and Salary_detail(empid, salary) and Department(deptno)
- Applications: Used for normalizing relations and reducing redundancy. Helpful in distributed databases for fragmenting and allocating relations.

[Detailed ascii diagrams, examples, codes can be added if required.]