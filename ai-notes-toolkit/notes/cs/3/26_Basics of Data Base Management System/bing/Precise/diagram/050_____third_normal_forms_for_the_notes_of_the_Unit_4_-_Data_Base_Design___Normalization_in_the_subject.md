### Third Normal Form (3NF)
Third Normal Form (3NF) is a database schema design approach for relational databases which uses the concept of transitive dependencies. A relation is in 3NF if it is in Second Normal Form (2NF) and no non-prime attribute is transitively dependent on the primary key.

In simpler terms, 3NF can be achieved by ensuring that all data in a table is dependent only on the primary key and not on any other non-key attributes. This means that there should be no functional dependencies between non-key attributes.

To achieve 3NF, the following steps can be taken:
1. Identify all functional dependencies in the relation.
2. Ensure that the relation is in 2NF.
3. Remove any transitive dependencies by creating new relations and adjusting the primary keys accordingly.

By ensuring that a relation is in 3NF, data redundancy and update anomalies can be minimized. This results in a more efficient and consistent database design.