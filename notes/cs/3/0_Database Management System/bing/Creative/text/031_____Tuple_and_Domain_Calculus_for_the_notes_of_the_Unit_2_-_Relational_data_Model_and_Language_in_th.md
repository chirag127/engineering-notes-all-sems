### Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a declarative query language for relational databases.
- Relational calculus allows users to specify what data they want to retrieve from the database, without specifying how to do it.
- Tuple and domain calculus differ in the way they use variables to represent data.

#### Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables are tuples that belong to a relation.
- A query in TRC has the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a predicate that involves `t` and other constants or variables.
- The result of the query is the set of all tuples `t` that satisfy the predicate `P(t)`.
- For example, the query `{t | t ∈ Employee and t[Salary] > 5000}` returns the set of all employees who earn more than 5000.
- TRC can express any query that can be expressed in relational algebra, and vice versa. This means that TRC is relationally complete.

#### Domain Relational Calculus (DRC)

- In domain relational calculus, variables are values that belong to the domains of attributes, rather than tuples of relations.
- A query in DRC has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `x1, x2, ..., xn` are domain variables and `P(x1, x2, ..., xn)` is a predicate that involves the variables and other constants or relations.
- The result of the query is the set of all ordered n-tuples of values that satisfy the predicate `P(x1, x2, ..., xn)`.
- For example, the query `{<e.Name, e.Salary> | e ∈ Employee and e[Salary] > 5000}` returns the set of all pairs of names and salaries of employees who earn more than 5000.
- DRC can also express any query that can be expressed in relational algebra, and vice versa. However, some queries in DRC may be unsafe, meaning that they may return an infinite number of tuples. Therefore, DRC is not relationally complete unless it is restricted to safe queries.