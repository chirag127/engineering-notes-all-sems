### Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a declarative query language for relational databases.
- Relational calculus allows users to specify what they want to retrieve from the database, without describing how to do it.
- Tuple and domain calculus are based on mathematical logic and set theory.

#### Tuple Relational Calculus (TRC)

- In TRC, a query is expressed as a set of tuples that satisfy a certain predicate.
- A tuple is a finite sequence of attribute values that represent a row or record in a relation.
- A predicate is a logical expression that evaluates to true or false for a given tuple.
- A tuple variable is a variable that ranges over the tuples of a relation.
- A query in TRC has the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a predicate involving `t`.
- For example, the query `{t | t ∈ Employee and t[Salary] > 5000}` returns the set of tuples from the Employee relation whose salary is greater than 5000.
- TRC can also use quantifiers, such as `∀` (for all) and `∃` (there exists), to express more complex queries.
- For example, the query `{t | t ∈ Employee and ∀s (s ∈ Department → t[Dno] ≠ s[Dnumber])}` returns the set of tuples from the Employee relation who do not work in any department.

#### Domain Relational Calculus (DRC)

- In DRC, a query is expressed as a set of attribute values that satisfy a certain predicate.
- An attribute value is a value from the domain of an attribute, which is a set of possible values for that attribute.
- A predicate is a logical expression that evaluates to true or false for a given set of attribute values.
- A domain variable is a variable that ranges over the values of a domain.
- A query in DRC has the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where `<x1, x2, ..., xn>` is a list of domain variables and `P(x1, x2, ..., xn)` is a predicate involving those variables.
- For example, the query `{<x, y> | ∃z (Employee(Fname, Lname, Salary) = <x, y, z> and z > 5000)}` returns the set of pairs of first and last names of employees whose salary is greater than 5000.
- DRC can also use quantifiers, such as `∀` (for all) and `∃` (there exists), to express more complex queries.
- For example, the query `{<x> | ∀y (Department(Dname, Dnumber) = <y, x> → ∃z (Employee(Dno, Salary) = <x, z> and z > 10000))}` returns the set of department numbers whose employees all have a salary greater than 10000.