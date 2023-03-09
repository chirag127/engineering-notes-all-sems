 Here are the notes for Relational algebra - relational calculus in markdown format:

### Relational algebra - relational calculus

Relational algebra and relational calculus are two mathematical query languages for relational databases.

#### Relational algebra
- Is a procedural language, which specifies a sequence of operations to be performed on relations to obtain the desired results.
- Uses operators such as select, project, union, set difference, Cartesian product, rename, etc. to perform operations on relations.
- The output of each operation is a relation.
- The order of operations is important.
- Examples:
    - Select - retrieve tuples that satisfy a given predicate
    - Project - delete unwanted columns
    - Union - combine results of two relations
    - Set difference - return tuples in one relation but not in the other
    - Cartesian product - return the cross product of two relations
    - Rename - rename the output relation or attributes

Advantages:
- Easy to understand
- Procedural in nature (close to how a computer works)
- Serves as a basis for relational database query languages like SQL

Disadvantages:
- The number of algebra operations required for a given query may be large.

#### Relational calculus
- Is a non-procedural language, focused on what to retrieve rather than how to retrieve it.
- Specifies what tuples are desired, not how to get them.
- Uses logical connectives and quantifiers in their expressions.
- Has two variants: tuple relational calculus and domain relational calculus.
- The expression is evaluated against the database to determine the desired tuples.

Advantages:
- Simple and easy to understand
- Declarative (specifies what to retrieve, not how)

Disadvantages:
- May require multiple relational algebra operations which must be determined and sequenced to evaluate the expression.
- May be computationally more complex to evaluate than relational algebra.

[Include detailed ascii diagrams, codes, examples, applications, advantages, and disadvantages here if required.]