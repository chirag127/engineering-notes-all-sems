### Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a declarative query language for relational databases.
- Relational calculus allows users to specify what they want to retrieve from the database, without describing how to do it.
- Tuple and domain calculus differ in the way they use variables to represent the data.

#### Tuple Relational Calculus (TRC)

- In TRC, variables are tuples that belong to a relation.
- A TRC query has the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a predicate that involves `t` and possibly other tuple variables.
- A TRC query returns the set of all tuples `t` that satisfy the predicate `P(t)`.
- For example, the query `{t | t ∈ Employee and t[Salary] > 5000}` returns the set of all employees who earn more than 5000.
- TRC can express any query that can be expressed in relational algebra, and vice versa. This means that TRC is relationally complete.

#### Domain Relational Calculus (DRC)

- In DRC, variables are values that belong to the domains of the attributes of a relation.
- A DRC query has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `<x1, x2, ..., xn>` is a list of domain variables and `P(x1, x2, ..., xn)` is a predicate that involves the domain variables and possibly constants.
- A DRC query returns the set of all tuples `<x1, x2, ..., xn>` that satisfy the predicate `P(x1, x2, ..., xn)`.
- For example, the query `{<E.Name, E.Salary> | E ∈ Employee and E.Salary > 5000}` returns the set of names and salaries of all employees who earn more than 5000.
- DRC can also express any query that can be expressed in relational algebra, and vice versa. This means that DRC is also relationally complete.

#### Comparison of TRC and DRC

- Both TRC and DRC are declarative and expressive query languages for relational databases.
- TRC is more intuitive and natural for users who are familiar with the concept of tuples and relations.
- DRC is more flexible and concise for users who want to specify the attributes and values of interest.
- TRC and DRC are equivalent in expressive power, but some queries may be easier to write in one form than the other.