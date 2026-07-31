# Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a constraint that states that some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential integrity constraint, which is a special case of IND where the columns of one relation are a subset of the primary key of another relation .
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed .
- Inclusion dependency is less prevalent than functional dependency, join dependency and multivalued dependency .
- Inclusion dependency can be represented by the notation R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], where R and S are relations, A1, A2, ..., An and B1, B2, ..., Bn are columns, and ⊆ means "is contained in" .
- Inclusion dependency holds for a database if every tuple that is a member of the relation corresponding to the left-hand side is also in the relation corresponding to the right-hand side.
- Inclusion dependency can be checked by performing a natural join of the two relations and comparing the result with the left-hand side relation.
- Inclusion dependency can be enforced by using triggers or assertions in the database system.

: https://www.scaler.com/topics/dbms/inclusion-dependency-in-dbms/
: https://www.w3schools.blog/inclusion-dependency-in-dbms/
: https://link.springer.com/chapter/10.1007/978-3-663-12018-6_6