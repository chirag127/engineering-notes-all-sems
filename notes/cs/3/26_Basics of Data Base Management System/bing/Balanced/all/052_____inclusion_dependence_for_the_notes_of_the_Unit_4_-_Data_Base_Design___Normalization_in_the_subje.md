# Inclusion Dependency in DBMS

- Inclusion dependency is a statement in which some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential constraints, such as foreign keys  .
- Inclusion dependency can be used to guide the design of the database, but it usually has little influence on how the database is actually designed .
- Inclusion dependency can be represented as R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ means "is contained in" .
- Inclusion dependency holds for a database if every tuple that is a member of the relation R is also a member of the relation S.
- Inclusion dependency can be checked by performing a natural join of R and S on the corresponding columns and comparing the result with R.
- Inclusion dependency can be violated if a tuple is inserted into R that does not have a matching tuple in S, or if a tuple is deleted from S that has a matching tuple in R.
- Inclusion dependency can be enforced by using triggers, assertions, or cascading updates and deletes.