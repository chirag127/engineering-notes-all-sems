### Relational algebra - relational calculus

- Relational algebra and relational calculus are two formal languages for manipulating relations in the relational model of data.
- Relational algebra is a procedural language that specifies how to construct a new relation from one or more existing relations in the database.
- Relational calculus is a declarative language that specifies what data to retrieve from the database without specifying how to do it.
- Both languages are equivalent in expressive power, meaning that any query that can be expressed in one language can also be expressed in the other. This is known as Codd's theorem.
- Relational algebra consists of a set of basic operations, such as selection, projection, join, union, intersection, difference, and division, that can be applied to relations or sets of tuples.
- Relational calculus consists of a set of formulas that use variables to denote relations or tuples, and a quantifier to specify the domain of the variables. There are two variants of relational calculus: tuple relational calculus (TRC) and domain relational calculus (DRC).
- In TRC, each formula is of the form {t | P(t)}, where t is a tuple variable and P(t) is a predicate involving t and other constants or variables. The formula defines the set of all tuples t that satisfy the predicate P(t).
- In DRC, each formula is of the form {<x1, x2, ..., xn> | P(x1, x2, ..., xn)}, where x1, x2, ..., xn are domain variables and P(x1, x2, ..., xn) is a predicate involving the variables and other constants. The formula defines the set of all n-tuples <x1, x2, ..., xn> that satisfy the predicate P(x1, x2, ..., xn).
- An example of a relational algebra query is:

  - σ<sub>BookTitle='Some Sample Book'</sub>(Bookstore ⋈ Book) π<sub>StoreName, StorePhone</sub>

  - This query selects the tuples from the join of Bookstore and Book relations where the BookTitle attribute is 'Some Sample Book', and then projects the StoreName and StorePhone attributes of the selected tuples.

- An example of a TRC query is:

  - {<s, p> | ∃b (Bookstore(s, p, b) ∧ Book(b, 'Some Sample Book'))}

  - This query defines the set of all pairs <s, p> such that there exists a value b that matches the BookstoreID attribute of both Bookstore and Book relations, and the BookTitle attribute of Book relation is 'Some Sample Book'.

- An example of a DRC query is:

  - {<s, p> | ∃b (Bookstore(s, p, b) ∧ Book(b, t) ∧ t = 'Some Sample Book')}

  - This query defines the set of all pairs <s, p> such that there exists a value b that matches the BookstoreID attribute of both Bookstore and Book relations, and there exists a value t that matches the BookTitle attribute of Book relation, and t is 'Some Sample Book'.