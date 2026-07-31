# Tuple and Domain Calculus

## Tuple Relational Calculus (TRC)

- Tuple relational calculus (TRC) is a **non-procedural** query language used in relational database management systems (RDBMS) to retrieve data from tables.
- TRC is based on the concept of **tuples**, which are ordered sets of attribute values that represent a single row or record in a database table.
- A query in TRC has the form `{t | P(t)}`, where `t` is a tuple variable that ranges over a relation, and `P(t)` is a predicate that evaluates to true or false for each tuple `t` .
- The result of a TRC query is the set of all tuples `t` that satisfy the predicate `P(t)` .
- For example, the query `{t | t ∈ Employee and t[SALARY] > 5000}` returns the set of all tuples `t` that belong to the relation `Employee` and have a salary greater than 5000.

## Domain Relational Calculus (DRC)

- Domain relational calculus (DRC) is another **non-procedural** query language used in RDBMS to retrieve data from tables.
- DRC is based on the concept of **domains**, which are the sets of values that an attribute can take in a relation.
- A query in DRC has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `x1, x2, ..., xn` are domain variables that take values from the domains of attributes, and `P(x1, x2, ..., xn)` is a predicate that evaluates to true or false for each combination of values .
- The result of a DRC query is the set of all tuples `<x1, x2, ..., xn>` that satisfy the predicate `P(x1, x2, ..., xn)` .
- For example, the query `{<E.NAME, E.SALARY> | E ∈ Employee and E.SALARY > 5000}` returns the set of all pairs of name and salary of employees who have a salary greater than 5000 .

## Comparison between TRC and DRC

- Both TRC and DRC are **equivalent** in expressive power, meaning that any query that can be expressed in one language can also be expressed in the other .
- However, TRC and DRC have different **advantages** and **disadvantages** in terms of readability, simplicity, and safety.
- TRC is more **readable** and **simple** than DRC, as it uses tuple variables that directly refer to the rows of a relation, rather than domain variables that have to be matched with the attributes of a relation.
- DRC is more **safe** than TRC, as it avoids the possibility of generating an infinite set of tuples as a result of a query, which can happen in TRC if the predicate does not constrain the tuple variable enough.
- For example, the query `{t | t ∈ Employee}` in TRC returns the entire relation `Employee`, which may be very large or infinite, whereas the query `{<E.NAME, E.SALARY> | E ∈ Employee}` in DRC returns only the name and salary of each employee, which is a finite set.