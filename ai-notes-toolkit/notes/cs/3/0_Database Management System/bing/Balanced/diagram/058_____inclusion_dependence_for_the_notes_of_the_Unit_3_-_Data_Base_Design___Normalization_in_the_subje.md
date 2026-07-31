### Inclusion Dependency in DBMS

- An inclusion dependency (IND) is a statement that some columns of a relation are contained in other columns of the same or another relation .
- An IND has the form R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are attributes, and n is a positive integer.
- An IND means that for every tuple t in R, there exists a tuple s in S such that t[A1] = s[B1], t[A2] = s[B2], ..., and t[An] = s[Bn].
- An IND is a generalization of a referential constraint or a foreign key constraint, which is a special case of an IND where n = 1  .
- An IND can be used to guide the design of the database, but it usually has little influence on how the database is actually designed .
- An IND can be checked by performing a left outer join of R and S on the corresponding attributes and verifying that there are no null values in the result.