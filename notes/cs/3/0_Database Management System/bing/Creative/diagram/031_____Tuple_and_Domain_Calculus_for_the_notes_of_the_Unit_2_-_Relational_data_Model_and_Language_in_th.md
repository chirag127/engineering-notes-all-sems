# Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a declarative query language for relational databases.
- Relational calculus allows users to specify what they want to retrieve from the database, without describing how to do it.
- Tuple and domain calculus differ in the way they use variables to refer to the data in the database.

## Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables represent tuples (rows) of a relation (table).
- A query in TRC has the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a predicate (condition) involving `t` and other constants or variables.
- The result of a TRC query is the set of all tuples `t` that satisfy the predicate `P(t)`.
- For example, the query `{t | t ∈ Employee and t[Salary] > 5000}` returns the set of all employees who earn more than 5000.
- TRC can also use quantifiers, such as `∀` (for all) and `∃` (there exists), to express more complex queries.
- For example, the query `{t | t ∈ Employee and ∀s (s ∈ Employee → t[Salary] ≥ s[Salary])}` returns the set of all employees who earn the highest salary.

## Domain Relational Calculus (DRC)

- In domain relational calculus, variables represent values from the domains (data types) of the attributes (columns) of a relation.
- A query in DRC has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `<x1, x2, ..., xn>` is a list of domain variables and `P(x1, x2, ..., xn)` is a predicate involving those variables and other constants or variables.
- The result of a DRC query is the set of all tuples `<x1, x2, ..., xn>` that satisfy the predicate `P(x1, x2, ..., xn)`.
- For example, the query `{<x, y> | ∃z (Employee(Name, Salary, Dept) = <x, y, z> and y > 5000)}` returns the set of all pairs of names and salaries of employees who earn more than 5000.
- DRC can also use quantifiers, such as `∀` and `∃`, to express more complex queries.
- For example, the query `{<x> | Employee(Name, Salary, Dept) = <x, y, z> and ∀w (Employee(Name, Salary, Dept) = <w, v, u> → y ≥ v)}` returns the set of all names of employees who earn the highest salary.