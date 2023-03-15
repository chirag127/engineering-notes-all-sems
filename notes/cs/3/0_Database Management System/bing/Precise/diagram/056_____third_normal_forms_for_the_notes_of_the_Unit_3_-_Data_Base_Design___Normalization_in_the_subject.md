### Third Normal Form (3NF)
Third Normal Form (3NF) is a database schema design approach for relational databases which uses normalization rules to reduce data redundancy and prevent certain types of inconsistencies that can arise when data is stored in a relational database.

A relation is in Third Normal Form if and only if:
1. It is in Second Normal Form (2NF).
2. There are no transitive dependencies between non-prime attributes.

A transitive dependency occurs when a non-prime attribute depends on another non-prime attribute, which in turn depends on the primary key. In other words, if attribute A depends on attribute B, and attribute B depends on the primary key, then attribute A transitively depends on the primary key.

To convert a relation into Third Normal Form, we need to identify any transitive dependencies and remove them by splitting the relation into two or more relations. This process is called decomposition.

Example:
Consider a relation `Student` with attributes `StudentID`, `StudentName`, `CourseID`, `CourseName`, and `InstructorName`. The primary key is `StudentID` and `CourseID`.

In this relation, `InstructorName` depends on `CourseName`, which in turn depends on `CourseID`. This is a transitive dependency, and the relation is not in Third Normal Form.

To convert the relation into Third Normal Form, we can decompose it into two relations: `Student` with attributes `StudentID`, `StudentName`, `CourseID`, and `CourseName`, and `Course` with attributes `CourseID`, `CourseName`, and `InstructorName`. The primary key for the `Course` relation is `CourseID`.

Now, the `Student` relation is in Third Normal Form, as there are no transitive dependencies between non-prime attributes.