### Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a constraint that states that some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential integrity constraint, which is a special case of IND where the columns of one relation are a subset of the primary key of another relation .
- Inclusion dependency can be used to guide the design of the database, but it usually has little influence on how the database is actually designed .
- Inclusion dependency can be expressed as R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ denotes the subset relation  .
- Inclusion dependency can be checked by performing a natural join of R and S on the corresponding columns and comparing the result with R. If the result is equal to R, then the IND holds; otherwise, it is violated.
- Inclusion dependency can be enforced by creating a foreign key constraint on R that references S, or by creating a view that joins R and S and restricting the updates on R to the view.