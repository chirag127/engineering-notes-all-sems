### Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a statement in which some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed .
- Inclusion dependency is a generalized form of referential constraints, which specify that a foreign key of one relation must be a subset of the primary key of another relation  .
- The syntax of inclusion dependency is `R1[A1, A2, ..., An] ⊆ R2[B1, B2, ..., Bn]`, where `R1` and `R2` are relations, `A1, A2, ..., An` and `B1, B2, ..., Bn` are attributes, and `⊆` denotes the subset relation  .
- The semantics of inclusion dependency is that for every tuple `t1` in `R1`, there exists a tuple `t2` in `R2` such that `t1[A1] = t2[B1]`, `t1[A2] = t2[B2]`, ..., and `t1[An] = t2[Bn]`  .
- An example of inclusion dependency is `Student[StudentID, Name, Major] ⊆ Person[PersonID, Name, Address]`, which means that every student is a person and has the same ID and name in both relations .
- Inclusion dependency can be checked by using the SQL query `SELECT * FROM R1 WHERE NOT EXISTS (SELECT * FROM R2 WHERE R1.A1 = R2.B1 AND R1.A2 = R2.B2 AND ... AND R1.An = R2.Bn)`, which returns an empty result if the inclusion dependency holds  .
- Inclusion dependency can be enforced by using foreign key constraints, which are a special case of inclusion dependency where the right-hand side is a primary key  .
- Inclusion dependency can also be expressed by using universal relation assumption, which states that there is a single relation that contains all the attributes of the database and every other relation is a projection of this universal relation .
- Inclusion dependency can be used to normalize a database by decomposing a relation into smaller relations that satisfy inclusion dependency and other dependencies .