# Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a non-procedural query language for relational databases  .
- Relational calculus allows users to specify what data they want to retrieve from the database, without specifying how to do it .
- Tuple and domain calculus differ in the way they use variables to represent data elements.

## Tuple Relational Calculus (TRC)

- Tuple relational calculus uses tuple variables that range over the tuples of a relation  .
- A tuple variable is denoted by a lowercase letter, such as t, and can be used to refer to the attribute values of a tuple.
- A tuple relational calculus query is an expression of the form {t | P(t)}, where t is a tuple variable and P(t) is a predicate involving t and other constants .
- The result of a tuple relational calculus query is the set of all tuples t that satisfy the predicate P(t) in the database .
- For example, the query {t | t ∈ EMPLOYEE ∧ t.SALARY > 50000} returns the set of all tuples in the EMPLOYEE relation whose salary is greater than 50000.

## Domain Relational Calculus (DRC)

- Domain relational calculus uses domain variables that range over the values of a domain  .
- A domain variable is denoted by a lowercase letter, such as x, and can be used to refer to a single value in a domain.
- A domain relational calculus query is an expression of the form {x1, x2, ..., xn | P(x1, x2, ..., xn)}, where x1, x2, ..., xn are domain variables and P(x1, x2, ..., xn) is a predicate involving x1, x2, ..., xn and other constants .
- The result of a domain relational calculus query is the set of all n-tuples (x1, x2, ..., xn) that satisfy the predicate P(x1, x2, ..., xn) in the database .
- For example, the query {x, y | ∃z (EMPLOYEE(x, y, z) ∧ z > 50000)} returns the set of all pairs of values (x, y) such that there exists a tuple in the EMPLOYEE relation with x as the name, y as the department, and z as the salary greater than 50000.

## References

: https://en.wikipedia.org/wiki/Tuple_relational_calculus
: https://www.scaler.com/topics/dbms/relational-calculus-in-dbms/
: https://www.educba.com/relational-calculus-in-dbms/
: https://www.geeksforgeeks.org/difference-between-tuple-relational-calculus-trc-and-domain-relational-calculus-drc/
: https://www.geeksforgeeks.org/tuple-relational-calculus-trc-in-dbms/
: https://pages.cs.wisc.edu/~dbbook/openAccess/thirdEdition/slides/slides3ed-english/Ch4_Domain_Calculus.pdf