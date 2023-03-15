### Third Normal Form (3NF)
Third Normal Form (3NF) is a database design principle that builds on the First Normal Form (1NF) and Second Normal Form (2NF) to further reduce data redundancy and improve data integrity. A relation is in 3NF if it satisfies the following conditions:
- It is in Second Normal Form (2NF).
- There are no transitive dependencies between non-prime attributes.

A transitive dependency occurs when a non-prime attribute depends on another non-prime attribute, which in turn depends on the primary key. In other words, if attribute A depends on attribute B, and attribute B depends on the primary key, then attribute A transitively depends on the primary key.

To bring a relation into 3NF, we need to identify and remove any transitive dependencies. This can be done by creating new relations to hold the dependent attributes and establishing a foreign key relationship between the original relation and the new relation.

Here is an example to illustrate 3NF:
Suppose we have a relation `Student` with the following attributes:
- `StudentID` (primary key)
- `StudentName`
- `CourseID`
- `CourseName`
- `InstructorID`
- `InstructorName`

In this relation, `CourseName` depends on `CourseID`, and `InstructorName` depends on `InstructorID`. However, `CourseID` and `InstructorID` both depend on `StudentID`, the primary key. This means that `CourseName` and `InstructorName` transitively depend on `StudentID`.

To bring this relation into 3NF, we can create two new relations: `Course` and `Instructor`. The `Course` relation will have the attributes `CourseID` (primary key) and `CourseName`, and the `Instructor` relation will have the attributes `InstructorID` (primary key) and `InstructorName`. The `Student` relation will be modified to remove the `CourseName` and `InstructorName` attributes, and foreign key relationships will be established between `Student` and `Course`, and between `Student` and `Instructor`.

The resulting relations will be in 3NF, with no transitive dependencies between non-prime attributes. This design reduces data redundancy and improves data integrity by ensuring that changes to course or instructor information only need to be made in one place.