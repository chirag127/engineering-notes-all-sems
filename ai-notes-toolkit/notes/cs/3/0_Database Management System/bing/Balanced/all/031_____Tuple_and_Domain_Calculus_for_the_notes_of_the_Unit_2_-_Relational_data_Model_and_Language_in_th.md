# Tuple and Domain Calculus

- Tuple and domain calculus are two forms of relational calculus, which is a non-procedural query language for relational databases  .
- Non-procedural means that the query does not specify how to retrieve the data, but only what data to retrieve  .
- Tuple and domain calculus are based on mathematical logic and set theory  .
- Tuple and domain calculus are equivalent in expressive power, meaning that any query that can be expressed in one form can also be expressed in the other form.

## Tuple Relational Calculus (TRC)

- Tuple relational calculus uses tuple variables that range over the tuples of a relation   .
- A tuple variable is denoted by a lowercase letter, such as t, s, or x  .
- A tuple relational calculus query has the form {t | P(t)}, where t is a tuple variable and P(t) is a predicate that involves t and possibly other tuple variables    .
- The query returns the set of all tuples t that satisfy the predicate P(t)    .
- The predicate P(t) can use logical operators (such as AND, OR, NOT), relational operators (such as =, <, >), and quantifiers (such as ∃ for exists and ∀ for for all)    .
- The predicate P(t) can also refer to the attributes of the tuple variable t by using the dot notation, such as t.name or t.salary    .
- Example: The query {t | t ∈ Employee ∧ t.salary > 5000} returns the set of all tuples t from the Employee relation that have a salary greater than 5000.

## Domain Relational Calculus (DRC)

- Domain relational calculus uses domain variables that range over the values of the domains of the attributes of a relation   .
- A domain variable is denoted by an uppercase letter, such as A, B, or X   .
- A domain relational calculus query has the form {<A1, A2, ..., An> | P(A1, A2, ..., An)}, where A1, A2, ..., An are domain variables and P(A1, A2, ..., An) is a predicate that involves the domain variables and possibly constants   .
- The query returns the set of all tuples <A1, A2, ..., An> that satisfy the predicate P(A1, A2, ..., An)   .
- The predicate P(A1, A2, ..., An) can use logical operators (such as AND, OR, NOT), relational operators (such as =, <, >), and quantifiers (such as ∃ for exists and ∀ for for all)   .
- The predicate P(A1, A2, ..., An) can also refer to the relations by using the membership operator ∈, such as A ∈ Employee or <A, B> ∈ Department   .
- Example: The query {<A, B> | A ∈ Employee ∧ B ∈ Department ∧ A.deptno = B.deptno} returns the set of all pairs of employee and department names that belong to the same department.