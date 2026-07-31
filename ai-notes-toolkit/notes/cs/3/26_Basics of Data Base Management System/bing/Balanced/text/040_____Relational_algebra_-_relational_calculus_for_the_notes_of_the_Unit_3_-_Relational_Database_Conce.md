### Relational algebra - relational calculus

- Relational algebra and relational calculus are two formal languages for manipulating data in relational databases.
- Relational algebra is a **procedural** language that specifies **how** to construct a new relation from one or more existing relations.
- Relational calculus is a **non-procedural** language that specifies **what** data to retrieve from the database without describing how to do it.
- Relational algebra and relational calculus are **logically equivalent**, meaning that any query expressed in one language can be translated into an equivalent query in the other language. This is known as **Codd's theorem**  .
- Relational algebra consists of a set of basic operations, such as selection, projection, join, union, difference, and renaming, that can be applied to relations or sets of tuples.
- Relational calculus consists of a set of formulas that use variables to represent relations or tuples, and logical connectives, such as and, or, not, and implies, to express conditions on the variables.
- There are two types of relational calculus: **tuple relational calculus** (TRC) and **domain relational calculus** (DRC).
- Tuple relational calculus uses tuple variables that range over a relation and specifies the tuples to be selected by a predicate (a logical expression) involving the tuple variables.
- Domain relational calculus uses domain variables that range over the attributes of a relation and specifies the tuples to be selected by a predicate involving the domain variables.
- Both tuple relational calculus and domain relational calculus are **safe**, meaning that they only express queries that are guaranteed to return a finite number of tuples .