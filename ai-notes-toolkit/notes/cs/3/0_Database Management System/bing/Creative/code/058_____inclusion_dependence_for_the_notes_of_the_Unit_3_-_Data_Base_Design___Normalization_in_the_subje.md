### Inclusion Dependency in DBMS

- An inclusion dependency (IND) is a statement that some columns of a relation are contained in other columns of the same or another relation.
- An IND has the form `R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn]`, where `R` and `S` are relation names, `A1, A2, ..., An` and `B1, B2, ..., Bn` are attribute names, and `n` is a positive integer.
- An IND means that for every tuple `t` in `R`, there exists a tuple `s` in `S` such that `t[A1] = s[B1], t[A2] = s[B2], ..., t[An] = s[Bn]`.
- An IND is a generalization of a referential constraint or a foreign key constraint, which is a special case of an IND where `n = 1` and `S` is a primary key of `S`.
- An IND can be used to guide the design of the database, but it usually has little influence on how the database is actually designed, since it does not imply any functional dependency, join dependency, or multivalued dependency.
- An IND can be checked by using a relational algebra expression: `πA1,A2,...,An(R) - πB1,B2,...,Bn(S)`, which should return an empty relation if the IND holds.
- An IND can be enforced by using a trigger or a constraint that fires whenever a tuple is inserted, updated, or deleted from `R` or `S`, and checks if the IND is violated.
- An IND can be violated by inserting a tuple in `R` that does not have a matching tuple in `S`, or by deleting or updating a tuple in `S` that has a matching tuple in `R`.
- An example of an IND is `Student[Dept, Major] ⊆ Department[Dept, Major]`, which means that every student's department and major must exist in the department relation.