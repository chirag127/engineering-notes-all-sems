### Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a declarative query language for relational databases.
- Relational calculus allows users to specify what they want to retrieve from the database, without describing how to do it.
- Tuple and domain calculus differ in the way they use variables to represent the data.

#### Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables are tuples that belong to a relation.
- A query in TRC has the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a predicate that involves `t` and possibly other tuple variables.
- The result of the query is the set of all tuples `t` that satisfy the predicate `P(t)`.
- For example, the query `{t | t ∈ Employee and t[Salary] > 5000}` returns the tuples of the `Employee` relation that have a salary greater than 5000.
- TRC can express any query that can be expressed in relational algebra, and vice versa. This means that TRC is relationally complete.

#### Domain Relational Calculus (DRC)

- In domain relational calculus, variables are values from the domains of the attributes, rather than tuples.
- A query in DRC has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `x1, x2, ..., xn` are domain variables and `P(x1, x2, ..., xn)` is a predicate that involves the domain variables and possibly constants.
- The result of the query is the set of all ordered n-tuples of values that satisfy the predicate `P(x1, x2, ..., xn)`.
- For example, the query `{<e.Name, e.Salary> | e ∈ Employee and e[Salary] > 5000}` returns the names and salaries of the employees that have a salary greater than 5000.
- DRC can also express any query that can be expressed in relational algebra, and vice versa. However, some queries in DRC may be unsafe, meaning that they may return an infinite number of tuples. Therefore, only safe queries in DRC are allowed in practice.