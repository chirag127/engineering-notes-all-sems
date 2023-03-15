### Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases .
- Relational calculus is a non-procedural language, which means it specifies what data to retrieve, not how to retrieve it .
- Tuple and domain calculus are based on the concept of predicates, which are logical expressions that evaluate to true or false for a given row or value in a database table  .
- Tuple and domain calculus differ in the type of variables they use and the way they express queries .

#### Tuple Relational Calculus (TRC)

- Tuple relational calculus uses tuple variables, which are denoted by lowercase letters (such as t, s, u) and range over tuples or rows of a table  .
- A tuple variable can be qualified by an attribute name to refer to a specific value in a tuple, such as t.name or s.age  .
- A query in tuple relational calculus is written as {t | P(t)}, where t is a tuple variable and P(t) is a predicate involving t and possibly other tuple variables or constants  .
- The result of a query in tuple relational calculus is a set of tuples that satisfy the predicate P(t)  .
- For example, the query {t | t ∈ Student ∧ t.age > 20} returns the set of tuples from the Student table whose age is greater than 20  .

#### Domain Relational Calculus (DRC)

- Domain relational calculus uses domain variables, which are denoted by uppercase letters (such as X, Y, Z) and range over domain elements or values of a table  .
- A query in domain relational calculus is written as {<X1, X2, ..., Xn> | P(X1, X2, ..., Xn)}, where X1, X2, ..., Xn are domain variables and P(X1, X2, ..., Xn) is a predicate involving X1, X2, ..., Xn and possibly other domain variables or constants  .
- The result of a query in domain relational calculus is a set of n-tuples that satisfy the predicate P(X1, X2, ..., Xn)  .
- For example, the query {<X, Y> | X ∈ Student.name ∧ Y ∈ Student.age ∧ Y > 20} returns the set of pairs of name and age from the Student table whose age is greater than 20  .

#### References

: https://en.wikipedia.org/wiki/Tuple_relational_calculus
: https://www.scaler.com/topics/dbms/relational-calculus-in-dbms/
: https://www.educba.com/relational-calculus-in-dbms/
: https://www.geeksforgeeks.org/difference-between-tuple-relational-calculus-trc-and-domain-relational-calculus-drc/
: https://www.geeksforgeeks.org/tuple-relational-calculus-trc-in-dbms/
: https://pages.cs.wisc.edu/~dbbook/openAccess/thirdEdition/slides/slides3ed-english/Ch4_Domain_Calculus.pdf