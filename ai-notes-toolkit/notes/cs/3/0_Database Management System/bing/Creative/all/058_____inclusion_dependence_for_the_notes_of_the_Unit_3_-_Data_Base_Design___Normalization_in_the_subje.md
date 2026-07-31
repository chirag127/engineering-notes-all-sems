# Inclusion Dependency in DBMS

- Inclusion dependency (IND) is a constraint that specifies that some columns of a relation are contained in other columns of the same or another relation .
- Inclusion dependency is a generalized form of referential integrity constraint, which is a special case of IND where the columns of one relation are a subset of the primary key of another relation .
- Inclusion dependency can be used to guide the design of the database, but they usually have little influence on how the database is actually designed .
- Inclusion dependency is less prevalent than functional dependency, join dependency and multivalued dependency .
- Inclusion dependency can be represented by the notation R[A1, A2, ..., An] ⊆ S[B1, B2, ..., Bn], which means that the columns A1, A2, ..., An of relation R are a subset of the columns B1, B2, ..., Bn of relation S  .
- Inclusion dependency can be checked by performing a natural join of the two relations and comparing the result with the relation on the left-hand side of the IND.
- Inclusion dependency can be enforced by creating a foreign key constraint on the columns of the relation on the left-hand side of the IND and referencing the columns of the relation on the right-hand side of the IND.
- Inclusion dependency can be violated if a tuple is inserted or updated in the relation on the left-hand side of the IND that does not match any tuple in the relation on the right-hand side of the IND.
- Inclusion dependency can be satisfied if a tuple is deleted or updated in the relation on the right-hand side of the IND that does not affect any tuple in the relation on the left-hand side of the IND.
- Inclusion dependency can be useful for modeling subtyping, inheritance, generalization and specialization in object-oriented and entity-relationship databases.