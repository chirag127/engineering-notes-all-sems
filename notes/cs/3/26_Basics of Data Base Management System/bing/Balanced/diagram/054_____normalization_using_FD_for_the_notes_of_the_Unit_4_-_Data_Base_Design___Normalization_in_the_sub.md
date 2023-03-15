### Normalization using FD

Normalization is the process of designing a relational database schema to minimize redundancy and anomalies. Redundancy occurs when the same data is stored in more than one place, leading to waste of space and inconsistency. Anomalies are problems that arise when inserting, updating, or deleting data, such as losing information or creating inconsistencies.

Functional dependencies (FDs) are rules that describe how some attributes (columns) of a relation (table) depend on other attributes. For example, a FD `A -> B` means that the values of `B` are determined by the values of `A`. Two tuples (rows) sharing the same values of `A` will necessarily have the same values of `B`.

Normalization using FDs involves applying a series of normal forms, which are criteria to check whether a relation is well-designed or not. The most common normal forms are:

- First normal form (1NF): A relation is in 1NF if it has no repeating groups, that is, no attribute can have multiple values for the same tuple. For example, a relation with an attribute `phone_numbers` that can store more than one phone number for a person is not in 1NF. To convert a relation to 1NF, we need to split the repeating groups into separate attributes or relations.
- Second normal form (2NF): A relation is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, that is, no attribute depends on a proper subset of the primary key. For example, a relation with a composite primary key `(student_id, course_id)` and an attribute `student_name` that depends only on `student_id` is not in 2NF. To convert a relation to 2NF, we need to split the relation into two or more relations, such that each non-key attribute depends on the whole primary key of its relation.
- Third normal form (3NF): A relation is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, that is, no attribute depends on another non-key attribute. For example, a relation with a primary key `employee_id` and attributes `department_id` and `department_name` that depend on each other is not in 3NF. To convert a relation to 3NF, we need to split the relation into two or more relations, such that each non-key attribute depends only on the primary key of its relation.
- Boyce-Codd normal form (BCNF): A relation is in BCNF if it is in 3NF and every determinant is a candidate key, that is, no attribute can determine another attribute unless it is part of a potential primary key. For example, a relation with a candidate key `(student_id, course_id)` and a FD `course_id -> instructor_id` is not in BCNF, because `course_id` is not a candidate key. To convert a relation to BCNF, we need to split the relation into two or more relations, such that each determinant is a candidate key of its relation.

The process of normalization using FDs can be summarized as follows:

- Identify all the FDs that hold in the relation.
- Check whether the relation satisfies each normal form, starting from 1NF to BCNF.
- If the relation does not satisfy a normal form, decompose it into two or more relations that satisfy the normal form and preserve the FDs.
- Repeat the process for each relation until all relations are in BCNF.