### Normalization using FD for the notes of the Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System

Normalization is the process of organizing data in a database to minimize redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring data integrity.

Functional dependencies (FDs) are used in the normalization process to determine the relationships between attributes in a relation. An FD is a constraint between two sets of attributes in a relation, where the values of one set of attributes (the determinant) uniquely determine the values of the other set of attributes (the dependent).

There are several normal forms, including first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on. Each normal form has a set of rules that must be followed to achieve that normal form.

1. **First Normal Form (1NF)**: A relation is in 1NF if and only if all attributes are atomic, meaning that they cannot be further subdivided. In other words, each attribute must contain only one value per tuple.

2. **Second Normal Form (2NF)**: A relation is in 2NF if and only if it is in 1NF and every non-prime attribute is fully functionally dependent on the primary key. This means that there should be no partial dependencies, where an attribute depends on only part of the primary key.

3. **Third Normal Form (3NF)**: A relation is in 3NF if and only if it is in 2NF and there are no transitive dependencies, where an attribute depends on another attribute that depends on the primary key.

Normalization using FDs involves decomposing a relation into multiple relations that satisfy the requirements of a given normal form. This is done by identifying the functional dependencies between attributes and using them to determine the appropriate decomposition.

In summary, normalization using FDs is a technique used to design a database that minimizes redundancy and dependency by decomposing relations into multiple relations that satisfy the requirements of a given normal form. This is done by identifying the functional dependencies between attributes and using them to determine the appropriate decomposition.