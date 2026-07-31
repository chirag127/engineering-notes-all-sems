# Normalization using FD

Normalization is the process of organizing data in a database to minimize redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way. Normalization is achieved by applying a set of rules, known as normal forms, to the database design.

Functional dependencies (FDs) are used in the normalization process to determine the relationships between attributes in a relation. An FD is a constraint between two sets of attributes in a relation, where the values of one set of attributes (the determinant) uniquely determine the values of the other set of attributes (the dependent).

There are several normal forms, including first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on. Each normal form has a set of rules that must be followed in order to achieve that level of normalization.

1. **First Normal Form (1NF):** A relation is in 1NF if and only if all attributes are atomic, meaning that they cannot be further subdivided. In other words, each attribute must contain only one value per tuple.

2. **Second Normal Form (2NF):** A relation is in 2NF if and only if it is in 1NF and every non-prime attribute is fully functionally dependent on the primary key. This means that there should be no partial dependencies, where an attribute depends on only part of the primary key.

3. **Third Normal Form (3NF):** A relation is in 3NF if and only if it is in 2NF and there are no transitive dependencies, where an attribute depends on another attribute that is not part of the primary key.

Normalization using FDs is an important step in the database design process, as it helps to ensure that the data is organized in the most efficient and logical way. By following the rules of the normal forms, a database designer can create a database that is free of redundancy and dependency issues, making it easier to maintain and update.