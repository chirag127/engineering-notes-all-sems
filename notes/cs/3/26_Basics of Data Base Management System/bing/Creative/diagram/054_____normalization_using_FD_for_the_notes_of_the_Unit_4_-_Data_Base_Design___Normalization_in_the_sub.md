### Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. Redundancy occurs when the same data is stored in more than one place, leading to waste of space and inconsistency. Anomalies occur when the data is not updated correctly, leading to loss of integrity and accuracy.

Functional dependencies (FDs) are rules that describe how the values of some attributes (columns) depend on the values of other attributes in a relation (table). For example, a FD `StudentID -> Name` means that the name of a student is determined by their student ID. If two tuples (rows) have the same student ID, they must have the same name.

Normalization uses FDs to decompose a relation into smaller relations that have less redundancy and anomalies. There are different levels of normalization, each with a set of criteria that a relation must satisfy to be in that level. The most common levels are:

- First normal form (1NF): A relation is in 1NF if it has no repeating groups, that is, no attribute can have more than one value for a given tuple. For example, a relation that stores the courses taken by each student should not have an attribute `Courses` that contains a list of courses, but rather have a separate relation that links each student with each course.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, that is, no attribute depends on a part of the primary key. For example, a relation that stores the name, address, and phone number of each student should not have the phone number as a non-key attribute, because it depends on the name, which is part of the primary key. Rather, the phone number should be in a separate relation that links each student with their phone number.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, that is, no attribute depends on another non-key attribute. For example, a relation that stores the name, address, and city of each student should not have the city as a non-key attribute, because it depends on the address, which is a non-key attribute. Rather, the city should be in a separate relation that links each address with its city.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key, that is, no attribute determines another attribute unless it is part of a key. For example, a relation that stores the name, address, and phone number of each student should not have the phone number as a determinant, because it is not part of a key. Rather, the phone number should be in a separate relation that links each student with their phone number.

The process of normalization using FDs involves the following steps:

- Identify all the FDs that hold in the relation.
- Check if the relation satisfies the desired level of normalization. If not, proceed to the next step.
- Decompose the relation into smaller relations that preserve the FDs and satisfy the desired level of normalization. This may involve creating new attributes and keys.
- Repeat the process for each of the smaller relations until all of them are in the desired level of normalization.