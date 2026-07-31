### Functional dependencies for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

Functional dependencies are a fundamental concept in the normalization of relational databases. They are used to define the relationships between attributes in a relation and to identify the keys of a relation.

- A functional dependency is a constraint between two sets of attributes in a relation.
- Given a relation R, a functional dependency X -> Y holds if, for any two tuples t1 and t2 in R, if t1[X] = t2[X], then t1[Y] = t2[Y].
- In other words, if two tuples have the same values for the attributes in set X, then they must also have the same values for the attributes in set Y.
- The set of attributes X is called the determinant, and the set of attributes Y is called the dependent.
- A key of a relation is a set of attributes that uniquely identifies a tuple in the relation. A key is a minimal set of attributes that is a determinant for all attributes in the relation.
- Normalization is the process of organizing the attributes and relations of a relational database to minimize data redundancy and to ensure data integrity.
- Normalization is achieved by decomposing relations with functional dependencies into smaller relations that satisfy certain normal forms.
- The most commonly used normal forms are first normal form (1NF), second normal form (2NF), third normal form (3NF), and Boyce-Codd normal form (BCNF).
- Each normal form has a set of rules that a relation must satisfy to be in that normal form. These rules are based on the functional dependencies between the attributes of the relation.
