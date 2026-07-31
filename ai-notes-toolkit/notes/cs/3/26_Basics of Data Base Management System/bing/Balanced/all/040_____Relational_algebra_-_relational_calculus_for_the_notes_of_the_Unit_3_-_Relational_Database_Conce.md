# Relational Algebra and Relational Calculus

- Relational algebra and relational calculus are two formal languages for manipulating relations in the relational model of data.
- Relational algebra is a procedural language that specifies how to construct a new relation from one or more existing relations in the database.
- Relational calculus is a declarative language that specifies what data to retrieve from the database without specifying how to do it.
- Both languages are equivalent in expressive power, meaning that any query that can be expressed in one language can also be expressed in the other language. This is known as Codd's theorem.
- Relational algebra and relational calculus are the basis for the SQL language, which is the most widely used language for querying and manipulating relational databases.

## Relational Algebra

- Relational algebra consists of a set of basic operations that can be applied to relations, such as selection, projection, union, set difference, Cartesian product, rename, join, division, and assignment.
- Selection (σ) is an operation that selects a subset of tuples from a relation that satisfy a given condition.
- Projection (π) is an operation that extracts a subset of attributes from a relation and eliminates duplicates.
- Union (∪) is an operation that combines two relations with the same set of attributes and eliminates duplicates.
- Set difference (-) is an operation that returns the tuples that are in one relation but not in another relation with the same set of attributes.
- Cartesian product (×) is an operation that combines two relations by forming all possible pairs of tuples from the two relations.
- Rename (ρ) is an operation that changes the name of a relation or its attributes.
- Join (⋈) is an operation that combines two relations by matching tuples based on a join condition.
- Division (÷) is an operation that returns the tuples from one relation that are associated with all tuples from another relation.
- Assignment (←) is an operation that assigns a relation to a temporary relation variable.

## Relational Calculus

- Relational calculus consists of two variants: tuple relational calculus and domain relational calculus.
- Tuple relational calculus (TRC) is a language that uses variables that range over tuples of a relation and a formula that defines the conditions for selecting tuples.
- Domain relational calculus (DRC) is a language that uses variables that range over the domains of attributes of a relation and a formula that defines the conditions for selecting values.
- Both TRC and DRC use quantifiers (∀ and ∃) to express universal and existential conditions, and logical connectives (∧, ∨, ¬) to combine conditions.
- A query in TRC or DRC is a formula that evaluates to true for the tuples or values that should be in the result of the query.