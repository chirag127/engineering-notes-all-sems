### Relational algebra - relational calculus

- Relational algebra and relational calculus are two formal languages for manipulating relations in the relational model of data.
- Relational algebra is a **procedural** language that specifies **how** to construct a new relation from one or more existing relations.
- Relational calculus is a **declarative** language that specifies **what** information is required from the relations, without specifying how to obtain it.
- Relational algebra and relational calculus are **logically equivalent**, meaning that any query that can be expressed in one language can also be expressed in the other language. This is known as **Codd's theorem** .
- Relational algebra consists of a set of basic operations, such as selection, projection, union, set difference, Cartesian product, and renaming, and a set of additional operations, such as join, division, natural join, and assignment, that can be derived from the basic ones.
- Relational calculus can be divided into two variants: **tuple relational calculus** (TRC) and **domain relational calculus** (DRC). Both variants use a notation of **quantified variables** and **logical predicates** to define the result of a query.
- Tuple relational calculus uses variables that range over **tuples** of a relation. A query in TRC consists of a formula that specifies the attributes and conditions for the tuples in the result. For example, the query "Find the names of all customers who have a loan at the bank" can be written in TRC as:

```{x | Customer(x) ∧ ∃y (Loan(y) ∧ x.customer_name = y.customer_name)}```

- Domain relational calculus uses variables that range over **values** of the attributes in a relation. A query in DRC consists of a formula that specifies the values and conditions for the attributes in the result. For example, the same query as above can be written in DRC as:

```{<n> | ∃c, l, b, a (Customer(c, n, a) ∧ Loan(l, c, b)}```

- Both TRC and DRC are **safe** languages, meaning that they can only express queries that are guaranteed to return a finite number of tuples. A query is safe if all the variables in the query are either bound by a quantifier or appear in the output. A query is unsafe if it contains a free variable that can take infinitely many values. For example, the query "Find all customers who have a loan with a branch that is located in the same city as the customer" is safe, but the query "Find all customers who have a loan with a branch that is located in a different city than the customer" is unsafe.