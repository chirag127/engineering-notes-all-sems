### Third Normal Form (3NF)

Third Normal Form (3NF) is a database design technique that is used to reduce data redundancy and improve data integrity. It is the third step in the normalization process, following First Normal Form (1NF) and Second Normal Form (2NF).

A relation is in 3NF if it satisfies the following conditions:

1. It is in Second Normal Form (2NF).
2. There are no transitive dependencies between non-prime attributes.

A transitive dependency occurs when a non-prime attribute depends on another non-prime attribute, which in turn depends on the primary key. In other words, if attribute A depends on attribute B, and attribute B depends on the primary key, then attribute A transitively depends on the primary key.

To bring a relation into 3NF, we need to remove any transitive dependencies by splitting the relation into two or more relations. Each new relation should have a primary key that is a subset of the original primary key, and all non-prime attributes should depend only on the primary key.

Here is an example to illustrate the concept of 3NF:

Suppose we have a relation `Student` with the following attributes: `StudentID`, `StudentName`, `CourseID`, `CourseName`, `InstructorID`, and `InstructorName`. The primary key is `StudentID` and `CourseID`.

This relation is not in 3NF because there is a transitive dependency between `InstructorName` and the primary key. `InstructorName` depends on `InstructorID`, which in turn depends on `CourseID`, which is part of the primary key.

To bring this relation into 3NF, we need to split it into two relations: `Student` and `Course`. The `Student` relation will have the attributes `StudentID`, `StudentName`, `CourseID`, and `InstructorID`. The `Course` relation will have the attributes `CourseID`, `CourseName`, and `InstructorName`. The primary key for the `Student` relation will be `StudentID` and `CourseID`, and the primary key for the `Course` relation will be `CourseID`.

By splitting the relation in this way, we have removed the transitive dependency and brought the relation into 3NF.