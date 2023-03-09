 Here is the content in markdown format for the given topic:

### Functional Dependencies for Unit 3 - Data Base Design & Normalization

 functional dependency: A functional dependency is a relationship between two attributes (columns) in a relation (table). It states that for every value of attribute A, there is a single value for attribute B.

For example:

- In a `Student` table, `RollNo` determines a unique `StudentName`. Here `RollNo` is the determinant attribute and `StudentName` is the dependent attribute.

Functional dependencies are denoted as:

A → B

Where A is the determinant attribute and B is the dependent attribute.

Rules for functional dependencies:

1. Left-side: The attribute(s) on the left-side (determinant) must uniquely identify the tuples in a relation.
2. Right-side: The attribute(s) on the right-side (dependent) contain the value that can be obtained from the determinant attribute(s).
3. Single-valued: The right-side attribute can have only a single value for a given left-side.

Examples of functional dependencies:

- In a `Student` table: `RollNo → Name`, `EnrollmentNo → Course`
- In a `Book` table: `ISBN → Title`, `ISBN → Author`

Advantages of using functional dependencies:

- Removes data duplication and redundancies.
- Optimizes storage usage.
- Prevents anomalies like insertion, deletion and modification.
- Aids normalization process.

[Include diagrams and examples here if required]

In this way, the content for the given topic can be written in detail in markdown format as a formal study material to learn and read from for exams. Let me know if you would like me to elaborate on any part or add more details.