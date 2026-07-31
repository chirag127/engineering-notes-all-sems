Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on functional dependencies for the unit 3 of database design and normalization.

### Functional dependencies

- A functional dependency (FD) is a constraint between two sets of attributes from a relation.
- A functional dependency X -> Y means that the values of Y are determined by the values of X. In other words, for each value of X, there is only one value of Y.
- A functional dependency can be represented by an arrow: X -> Y
- A functional dependency can also be written as a formula: X -> Y iff for any tuples t1 and t2 in the relation, if t1[X] = t2[X], then t1[Y] = t2[Y].
- A functional dependency is a property of the data, not the schema. It reflects the semantics and the meaning of the data.
- A functional dependency can be derived from the real-world constraints, the business rules, or the common sense.
- A functional dependency can be verified by examining the data in the relation. If there is no violation of the dependency, then the dependency holds.
- A functional dependency can be used to check the validity and the consistency of the data. If there is a violation of the dependency, then there is an anomaly or an error in the data.
- A functional dependency can be used to design the schema of the relation. By applying the principles of normalization, we can decompose a relation into smaller relations that satisfy certain normal forms and avoid the anomalies.

Some examples of functional dependencies are:

- StudentID -> Name, Major, GPA
- ISBN -> Title, Author, Publisher
- SSN -> Name, Address, Phone
- CourseID, Semester -> Instructor, Room, Time
- EmployeeID -> Name, Department, Salary

Some properties of functional dependencies are:

- Reflexivity: If Y is a subset of X, then X -> Y
- Augmentation: If X -> Y, then XZ -> YZ for any Z
- Transitivity: If X -> Y and Y -> Z, then X -> Z
- Union: If X -> Y and X -> Z, then X -> YZ
- Decomposition: If X -> YZ, then X -> Y and X -> Z
- Pseudo-transitivity: If X -> Y and WY -> Z, then WX -> Z