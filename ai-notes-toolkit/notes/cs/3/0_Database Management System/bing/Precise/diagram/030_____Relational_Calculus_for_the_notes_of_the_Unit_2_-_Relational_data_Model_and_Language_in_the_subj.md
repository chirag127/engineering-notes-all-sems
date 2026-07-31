### Relational Calculus

Relational calculus is a non-procedural query language used in relational databases to retrieve data from the database. It is a declarative language, meaning that the user specifies the desired result, but not how to compute it.

There are two types of relational calculus: tuple relational calculus and domain relational calculus.

- **Tuple Relational Calculus (TRC)**: In tuple relational calculus, the user specifies the desired tuples by providing a formula in terms of the attributes of the relation. The formula is composed of atoms, which can be either a comparison between two attributes or a comparison between an attribute and a constant.

- **Domain Relational Calculus (DRC)**: In domain relational calculus, the user specifies the desired tuples by providing a formula in terms of the domains of the attributes. The formula is composed of atoms, which can be either a comparison between two domain variables or a comparison between a domain variable and a constant.

Both types of relational calculus are equivalent in expressive power, meaning that any query that can be expressed in one can also be expressed in the other.

Relational calculus is a formal language, with a well-defined syntax and semantics. It is based on first-order logic, and its formulas are evaluated over the tuples of the database to determine which tuples are in the result of the query.

Relational calculus is a powerful query language, capable of expressing complex queries. However, it is not as widely used as its procedural counterpart, relational algebra, due to its more abstract nature and the need for a deeper understanding of logic to use it effectively. Nonetheless, it is an important tool in the study of database theory and the design of query languages.