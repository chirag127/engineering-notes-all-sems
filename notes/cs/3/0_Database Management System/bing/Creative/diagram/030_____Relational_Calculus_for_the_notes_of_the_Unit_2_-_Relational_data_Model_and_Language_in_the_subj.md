### Relational Calculus

- Relational calculus is a **non-procedural query language** that uses **mathematical predicate calculus** to express queries on relational data .
- Relational calculus is **declarative**, meaning it specifies **what** data to retrieve, not **how** to retrieve it   .
- Relational calculus has the same **expressive power** as relational algebra, meaning it can express any query that relational algebra can, and vice versa  .
- Relational calculus can be divided into two variants: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**  .
- Tuple relational calculus uses **variables** that range over **tuples** of a relation, and **formulas** that involve these variables and **atomic predicates** (such as equality, membership, etc.)  .
- Domain relational calculus uses variables that range over **individual values** (or domains) of attributes, and formulas that involve these variables and atomic predicates  .
- A query in relational calculus is of the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a formula involving `t`  .
- A query in relational calculus returns a **relation** that contains all tuples that satisfy the formula  .
- A query in relational calculus is **safe** if it is guaranteed to return a finite relation, and **unsafe** otherwise  .
- A query in relational calculus is **equivalent** to another query if they return the same relation for any database instance .
- A query in relational calculus can be **transformed** into an equivalent query in relational algebra using a set of **rules** .
- A query in relational calculus can be **optimized** by choosing the most efficient equivalent query to execute.