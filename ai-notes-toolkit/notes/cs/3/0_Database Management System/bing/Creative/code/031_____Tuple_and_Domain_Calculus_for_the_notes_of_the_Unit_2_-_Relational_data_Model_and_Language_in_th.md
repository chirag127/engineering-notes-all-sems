# Tuple and Domain Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Tuple and domain calculus are two forms of relational calculus, which is a non-procedural query language for relational databases.
- Relational calculus allows users to specify what data they want to retrieve from the database, without specifying how to do it.
- Tuple and domain calculus are based on the concepts of mathematical logic and set theory.

## Tuple Relational Calculus (TRC)

- In tuple relational calculus, a query is expressed as a formula that uses tuple variables to denote the rows of a relation.
- A tuple variable is a symbol that ranges over the tuples of a relation.
- A query in TRC has the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a predicate that involves `t` and other constants or attributes.
- The result of the query is the set of all tuples `t` that satisfy the predicate `P(t)`.
- For example, the query `{t | t ∈ Employee and t[Salary] > 5000}` returns the set of all tuples from the Employee relation that have a salary greater than 5000.
- TRC can use logical operators such as `and`, `or`, `not`, `implies`, `forall`, and `exists` to combine predicates and quantify over tuple variables.
- For example, the query `{t | t ∈ Employee and (∃s)(s ∈ Department and s[Mgr_ssn] = t[Ssn])}` returns the set of all tuples from the Employee relation that are managers of some department.

## Domain Relational Calculus (DRC)

- In domain relational calculus, a query is expressed as a formula that uses domain variables to denote the values of the attributes of a relation.
- A domain variable is a symbol that ranges over the values of a domain (a set of atomic values of a certain type).
- A query in DRC has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `<x1, x2, ..., xn>` is a list of domain variables and `P(x1, x2, ..., xn)` is a predicate that involves the domain variables and other constants or attributes.
- The result of the query is the set of all tuples `<x1, x2, ..., xn>` that satisfy the predicate `P(x1, x2, ..., xn)`.
- For example, the query `{<x, y> | (∃z)(Employee(Ssn, x, y, z, ...) and z > 5000)}` returns the set of all pairs of first name and last name of employees who have a salary greater than 5000.
- DRC can also use logical operators and quantifiers to combine predicates and quantify over domain variables.
- For example, the query `{<x, y> | (∀z)(Department(Dnumber, x, y, z) implies z > 5)}` returns the set of all pairs of department number and name of departments that have more than 5 employees.