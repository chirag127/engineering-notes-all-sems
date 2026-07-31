### Tuple and Domain Calculus for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases .
- Relational calculus is a non-procedural language, which means it specifies what data to retrieve, not how to retrieve it .
- Tuple relational calculus (TRC) uses tuple variables that range over the rows of a relation and a predicate that specifies the condition for selecting tuples  .
- Domain relational calculus (DRC) uses domain variables that range over the values of a domain and a predicate that specifies the condition for selecting values  .
- Both TRC and DRC are equivalent in expressive power, which means they can express the same set of queries.
- The syntax of TRC is {t | P(t)}, where t is a tuple variable and P(t) is a predicate involving t and other constants.
- The syntax of DRC is {<x1, x2, ..., xn> | P(x1, x2, ..., xn)}, where x1, x2, ..., xn are domain variables and P(x1, x2, ..., xn) is a predicate involving them and other constants.
- An example of a TRC query is {t | t ∈ Student ∧ t.age > 18}, which returns all the tuples from the Student relation whose age is greater than 18.
- An example of a DRC query is {<x, y> | ∃z(Student(x, y, z) ∧ z > 18)}, which returns all the pairs of values from the Student relation whose third attribute is greater than 18.
- TRC and DRC are safe if they only return finite sets of values, otherwise they are unsafe.