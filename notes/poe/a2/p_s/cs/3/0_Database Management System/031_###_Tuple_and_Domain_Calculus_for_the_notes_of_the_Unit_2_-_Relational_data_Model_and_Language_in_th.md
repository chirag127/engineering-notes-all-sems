 Here is the content in markdown format for the topic -

### Tuple and Domain Calculus

- Tuple calculus is a calculus that operates on tuples of a relation. It uses variables that range over tuples and combines tuples using logical connectives and quantifiers.
- The basic components of tuple calculus are:
- Variables - Range over tuples of a relation
- Predicates - Conditions that tuples must satisfy
- Logical connectives - AND, OR, NOT
- Quantifiers - ALL, ANY
- Examples of tuple calculus queries:
- Get all tuples in R where X=5: ∃X(R(X) AND X=5)
- Get tuples in R where X>Y: ∃X∃Y(R(X,Y) AND X>Y)
- Domain calculus is a calculus that focuses on the domains of the attributes of a relation. It uses variables that range over domains of attributes and uses logical connectives and quantifiers to combine conditions on domains.
- The basic components of domain calculus are:
- Domain variables - Range over domains of attributes
- Conditions - Conditions to be satisfied by domains
- Logical connectives - AND, OR, NOT
- Quantifiers - ALL, ANY
- Examples of domain calculus queries:
- Get all tuples in R where some attribute has value 5: ∃X(R(X) AND X=5)
- Get all tuples in R where X>the average of all values of X: ∀X(R(X) → X > AVG(X))

[Include diagrams, codes, tables, advantages, disadvantages, applications, etc if any]