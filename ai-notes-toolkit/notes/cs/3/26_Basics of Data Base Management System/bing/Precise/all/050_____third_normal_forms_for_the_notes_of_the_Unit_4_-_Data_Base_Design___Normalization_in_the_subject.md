# Third Normal Form (3NF)

Third Normal Form (3NF) is a database normalization technique used to eliminate data redundancy and prevent update anomalies. It is the third step in the normalization process and is built on the principles of the First Normal Form (1NF) and Second Normal Form (2NF).

A relation is in 3NF if it satisfies the following conditions:
- It is in Second Normal Form (2NF).
- There are no transitive dependencies between non-prime attributes.

A transitive dependency occurs when a non-prime attribute depends on another non-prime attribute, which in turn depends on the primary key. In other words, if attribute A depends on attribute B, and attribute B depends on the primary key, then attribute A transitively depends on the primary key.

To bring a relation into 3NF, transitive dependencies must be eliminated by decomposing the relation into two or more relations. Each new relation should have a primary key that is a subset of the original primary key, and the non-prime attributes should depend only on the primary key of the new relation.

For example, consider a relation with the following attributes: Student ID, Course ID, Course Name, Instructor Name. In this relation, the primary key is the combination of Student ID and Course ID. The attribute Instructor Name depends on the attribute Course Name, which in turn depends on the primary key. This is a transitive dependency.

To bring this relation into 3NF, it can be decomposed into two relations: one with the attributes Student ID, Course ID, and Course Name, and another with the attributes Course Name and Instructor Name. The primary key of the first relation is the combination of Student ID and Course ID, while the primary key of the second relation is Course Name. In this way, the transitive dependency is eliminated, and the relation is in 3NF.

In summary, Third Normal Form (3NF) is a database normalization technique used to eliminate data redundancy and prevent update anomalies. It is achieved by ensuring that the relation is in Second Normal Form (2NF) and that there are no transitive dependencies between non-prime attributes. If transitive dependencies exist, the relation can be decomposed into two or more relations to eliminate them and bring the relation into 3NF.