### Functional Dependencies

Functional dependency is a concept in the relational model of databases. It is a constraint between two sets of attributes in a relation from a database. Given a relation R, a set of attributes X in R is said to functionally determine another set of attributes Y, also in R, (written X → Y) if, and only if, each X value is associated with precisely one Y value.

- A functional dependency is denoted by X → Y, where X is the determinant set and Y is the dependent attribute.
- The left side of the arrow is called the determinant and the right side is called the dependent.
- The determinant is a set of attributes that uniquely identifies a tuple in a relation.
- The dependent is an attribute that is functionally dependent on the determinant.

Functional dependencies are used to specify constraints on the data in a relation. They are used to define normal forms and to normalize relations. Normalization is the process of organizing the data in a database to minimize redundancy and dependency.