### Relational Calculus

- Relational calculus is a **non-procedural query language** that uses **mathematical predicate calculus** to express queries on relational data .
- Relational calculus is **declarative**, meaning that it specifies **what** data to retrieve, not **how** to retrieve it  .
- Relational calculus has the same **expressive power** as relational algebra, meaning that any query that can be expressed in one language can also be expressed in the other  .
- Relational calculus can be divided into two variants: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**  .
- Tuple relational calculus uses **variables** that range over **tuples** of a relation, and **formulas** that involve these variables and **atomic predicates** on the attributes of the relation  .
- Domain relational calculus uses variables that range over **values** of the domains of the attributes, and formulas that involve these variables and atomic predicates on the values  .
- A query in relational calculus is of the form `{t | P(t)}`, where `t` is a tuple variable and `P(t)` is a formula involving `t`  .
- A query in relational calculus returns a **relation** that contains all the tuples that satisfy the formula  .
- For example, the query `{t | t ∈ Bookstore ∧ t.BookTitle = "Some Sample Book"}` returns the relation of all the tuples in the `Bookstore` relation that have the book title "Some Sample Book".
- A query in relational calculus can also use **quantifiers** such as **existential quantifier (∃)** and **universal quantifier (∀)** to express more complex conditions  .
- For example, the query `{t | t ∈ Store ∧ ∃s(s ∈ Bookstore ∧ s.BookstoreID = t.StoreID ∧ s.BookTitle = "Some Sample Book")}` returns the relation of all the tuples in the `Store` relation that have a corresponding tuple in the `Bookstore` relation with the book title "Some Sample Book".
- A query in relational calculus is **safe** if it is guaranteed to return a **finite** relation  .
- A query in relational calculus is **unsafe** if it may return an **infinite** relation or is **undefined**  .
- For example, the query `{t | t ∈ Bookstore ∧ t.BookTitle = x}` is unsafe, because `x` is an unbound variable that can take any value, and the query may return an infinite relation or be undefined.
- A query in relational calculus can be evaluated by **translating** it into an equivalent query in relational algebra, and then applying the relational algebra operators on the relations .
- For example, the query `{t | t ∈ Bookstore ∧ t.BookTitle = "Some Sample Book"}` can be translated into the relational algebra expression `σBookTitle="Some Sample Book"(Bookstore)`, and then evaluated by applying the selection operator on the `Bookstore` relation .