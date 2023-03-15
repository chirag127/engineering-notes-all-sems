### Third Normal Form (3NF)
Third Normal Form (3NF) is a database normalization technique that is used to reduce data redundancy and improve data integrity. It is the third step in the normalization process, following First Normal Form (1NF) and Second Normal Form (2NF).

A relation is in 3NF if it satisfies the following conditions:
1. It is in Second Normal Form (2NF).
2. There are no transitive dependencies between non-prime attributes.

A transitive dependency occurs when a non-prime attribute depends on another non-prime attribute, which in turn depends on the primary key. In other words, if attribute A depends on attribute B, and attribute B depends on the primary key, then attribute A transitively depends on the primary key.

To bring a relation into 3NF, we need to remove any transitive dependencies by splitting the relation into two or more relations. Each new relation should have a primary key that is a subset of the original primary key, and all non-prime attributes should depend only on the primary key.

Here is an example to illustrate 3NF:

Suppose we have a relation `Student` with the following attributes:
- `StudentID` (primary key)
- `StudentName`
- `CourseID`
- `CourseName`
- `InstructorID`
- `InstructorName`

In this relation, `CourseName` depends on `CourseID`, and `InstructorName` depends on `InstructorID`. However, `InstructorID` also depends on `CourseID`, since each course has a specific instructor. This creates a transitive dependency between `InstructorName` and `CourseID`.

To bring this relation into 3NF, we need to split it into three relations:
1. `Student` with attributes `StudentID` (primary key), `StudentName`, and `CourseID`.
2. `Course` with attributes `CourseID` (primary key) and `CourseName`.
3. `Instructor` with attributes `InstructorID` (primary key), `InstructorName`, and `CourseID`.

Now, all non-prime attributes depend only on the primary key, and there are no transitive dependencies. The relation is in Third Normal Form.