 Here is the content in markdown format for the topic ### and JDs for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System:

### Functional Dependencies

- A functional dependency is a constraint between two sets of attributes in a relation.
- It is denoted as X --> Y, where X is the determinant set of attributes and Y is the dependent set of attributes.
- It means that the value of Y depends on the value of X. For a given value of X, there is only one possible value of Y.
- For example, in a relation Student(RollNo, Name, Class), RollNo --> Name means that the Name of a student depends on the RollNo, for a given RollNo there will be only one Name. Similarly, RollNo, Name --> Class means that the Class of a student depends on both RollNo and Name, for a given combination of RollNo and Name there will be only one Class.

JDs and Normalization

- JDs or Join Dependencies are special types of FDs which involve two or more relations.
- They are used during decomposition to ensure the lossless join between the resultant relations.
- Normalization is the process of organizing data in a database by arranging it into multiple tables to remove redundancy and undesirable characteristics like Insertion, Update and Deletion Anomalies.
- The aim is to achieve higher normal forms to increase data consistency and minimize redundancy. The benefits are:
-- minimized data duplication
-- data consistency
-- efficient data access
-- reduced need for restructuring the database
- The normal forms are:
1NF: Atomic values, no repeating groups
2NF: Full functional dependency, no partial dependency
3NF: Transitive dependency removed
BCNF: Every FD has a candidate key on one side
4NF: No multi-valued dependencies
5NF: No join dependencies

[Detailed explanations and examples can be included here]