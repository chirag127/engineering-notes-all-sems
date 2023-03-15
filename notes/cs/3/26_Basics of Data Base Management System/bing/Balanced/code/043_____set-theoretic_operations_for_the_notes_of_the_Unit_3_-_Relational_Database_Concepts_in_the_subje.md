### Set-theoretic operations for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System

- Set-theoretic operations are operations that are based on the mathematical concept of sets. Sets are collections of distinct elements that have some common property or relation.
- In relational database, set-theoretic operations are used to combine or compare two or more relations (tables) that have the same attributes (columns) and domains (data types).
- The main set-theoretic operations in relational database are union, intersection, and difference. These operations are also called relational set operators.
- Union: The union operation combines two relations and returns a new relation that contains all the tuples (rows) that are either in the first relation or in the second relation or in both. The union operation is denoted by the symbol ∪.
- Intersection: The intersection operation returns a new relation that contains only the tuples that are common to both the relations. The intersection operation is denoted by the symbol ∩.
- Difference: The difference operation returns a new relation that contains only the tuples that are in the first relation but not in the second relation. The difference operation is denoted by the symbol -.
- The condition for using set-theoretic operations is that the relations must be union compatible, which means that they must have the same number of attributes, the same attribute names, and the same attribute domains.
- Example: Consider the following two relations Student and Teacher, which have the same attributes Name, Age, and Subject.

| Name | Age | Subject |
| --- | --- | --- |
| Alice | 20 | Math |
| Bob | 21 | Physics |
| Carol | 22 | Chemistry |
| David | 23 | Biology |

Student

| Name | Age | Subject |
| --- | --- | --- |
| Eve | 24 | Math |
| Frank | 25 | Physics |
| Carol | 22 | Chemistry |
| George | 26 | History |

Teacher

- The union of Student and Teacher is:

| Name | Age | Subject |
| --- | --- | --- |
| Alice | 20 | Math |
| Bob | 21 | Physics |
| Carol | 22 | Chemistry |
| David | 23 | Biology |
| Eve | 24 | Math |
| Frank | 25 | Physics |
| George | 26 | History |

Student ∪ Teacher

- The intersection of Student and Teacher is:

| Name | Age | Subject |
| --- | --- | --- |
| Carol | 22 | Chemistry |

Student ∩ Teacher

- The difference of Student and Teacher is:

| Name | Age | Subject |
| --- | --- | --- |
| Alice | 20 | Math |
| Bob | 21 | Physics |
| David | 23 | Biology |

Student - Teacher

- The difference of Teacher and Student is:

| Name | Age | Subject |
| --- | --- | --- |
| Eve | 24 | Math |
| Frank | 25 | Physics |
| George | 26 | History |

Teacher - Student

- Set-theoretic operations can be implemented in DBMS using different queries, such as SQL (Structured Query Language). For example, the union operation can be performed using the keyword UNION, the intersection operation can be performed using the keyword INTERSECT, and the difference operation can be performed using the keyword EXCEPT or MINUS.