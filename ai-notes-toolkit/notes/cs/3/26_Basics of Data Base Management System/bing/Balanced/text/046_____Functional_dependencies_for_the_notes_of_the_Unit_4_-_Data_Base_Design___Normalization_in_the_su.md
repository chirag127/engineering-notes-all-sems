### Functional dependencies for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

- A functional dependency (FD) is a **constraint** between two sets of attributes in a relation from a database.
- A functional dependency mathematically expresses the **relation** between different values in a database management system (DBMS).
- A functional dependency is denoted by an **arrow** (→) that shows which attribute **relies** on the other.
- For example, if A and B are attributes of a relation R, then A → B means that the value of B is **determined** by the value of A.
- There are four primary types of functional dependencies: **trivial**, **non-trivial**, **multivalued**, and **transitive** .
- A trivial functional dependency is when the **dependent** is always a **subset** of the **determinant**. For example, A → A or A → AB are trivial FDs.
- A non-trivial functional dependency is when the dependent is **strictly not** a subset of the determinant. For example, A → B or AB → C are non-trivial FDs.
- A multivalued functional dependency is when the determinant can have **multiple** values for the dependent. For example, A →> B means that for a given value of A, there can be more than one value of B.
- A transitive functional dependency is when the dependent of one FD becomes the determinant of another FD. For example, A → B and B → C imply A → C.
- Functional dependencies are used to establish **relationships** between attributes in a database and to ensure that the database is in a state of **normalization**, which helps to minimize data **redundancy** and improve data **integrity** .