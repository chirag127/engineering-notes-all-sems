### Third Normal Form (3NF)

Third Normal Form (3NF) is a database design principle that builds on the First Normal Form (1NF) and Second Normal Form (2NF). It is used to eliminate data redundancy and improve data integrity.

A relation is in 3NF if it satisfies the following conditions:
1. It is in Second Normal Form (2NF).
2. There are no transitive dependencies between non-prime attributes.

A transitive dependency occurs when a non-prime attribute depends on another non-prime attribute, which in turn depends on the primary key. In other words, if A is the primary key, B is a non-prime attribute, and C is another non-prime attribute, then a transitive dependency exists if B depends on A and C depends on B.

To bring a relation into 3NF, we need to identify and remove any transitive dependencies. This can be done by creating new relations and moving the dependent attributes to the new relations.

For example, consider a relation with the following attributes: Student ID, Student Name, Course ID, Course Name, Instructor ID, and Instructor Name. In this relation, there is a transitive dependency between the Instructor Name and the Student ID (via the Course ID). To bring this relation into 3NF, we can create a new relation with the attributes Course ID, Instructor ID, and Instructor Name, and remove the Instructor ID and Instructor Name attributes from the original relation.

By following the 3NF design principle, we can ensure that our database is free from data redundancy and has improved data integrity. This can help to reduce the risk of data inconsistencies and improve the efficiency of data retrieval and manipulation.