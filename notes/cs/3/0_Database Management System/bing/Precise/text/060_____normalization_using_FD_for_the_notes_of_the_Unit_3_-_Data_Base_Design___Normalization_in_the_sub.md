### Normalization using FD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

Normalization is the process of organizing data in a database to minimize redundancy and dependency. It is a technique used to design a database so that it meets certain requirements, such as minimizing duplicate data and ensuring that data is stored in the most appropriate way. Normalization is achieved by applying a set of rules, known as normal forms, to the database design.

Functional dependencies (FDs) are used in the normalization process to determine the relationships between attributes in a relation. A functional dependency is a constraint between two sets of attributes in a relation. It specifies that the values of one set of attributes, called the determinant, uniquely determine the values of another set of attributes, called the dependent.

There are several normal forms, including first normal form (1NF), second normal form (2NF), third normal form (3NF), and so on. Each normal form has a set of rules that must be followed in order to achieve that level of normalization. The normal forms are applied in order, with each subsequent normal form building on the previous one.

1. **First Normal Form (1NF):** A relation is in 1NF if it contains only atomic values and there are no repeating groups. This means that each attribute in the relation must have a single value, and there can be no sets or arrays of values within a single attribute.

2. **Second Normal Form (2NF):** A relation is in 2NF if it is in 1NF and all non-prime attributes are fully functionally dependent on the primary key. This means that there can be no partial dependencies, where an attribute is dependent on only part of the primary key.

3. **Third Normal Form (3NF):** A relation is in 3NF if it is in 2NF and there are no transitive dependencies. This means that there can be no dependencies between non-prime attributes, where one non-prime attribute is dependent on another non-prime attribute through the primary key.

Normalization using FDs is an important part of the database design process, as it helps to ensure that the data is organized in the most efficient and logical way. By applying the normal forms and using functional dependencies to determine the relationships between attributes, a well-designed and normalized database can be created.