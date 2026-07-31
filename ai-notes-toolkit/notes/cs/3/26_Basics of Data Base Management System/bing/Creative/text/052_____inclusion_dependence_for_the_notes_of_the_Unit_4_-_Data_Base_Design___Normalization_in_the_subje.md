### Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a constraint that specifies that some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential integrity constraint, which is a special case of IND where the columns of one relation are a subset of the primary key of another relation .
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed .
- Inclusion dependency can be expressed as R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ denotes the subset relation  .
- The inclusion dependency holds for a database if each tuple that is a member of the relation corresponding to the left-hand side is also in the relation corresponding to the right-hand side.
- Inclusion dependency can be checked by performing a natural join of the two relations and comparing the result with the left-hand side relation.
- Inclusion dependency can be enforced by creating foreign key constraints or triggers in the database.