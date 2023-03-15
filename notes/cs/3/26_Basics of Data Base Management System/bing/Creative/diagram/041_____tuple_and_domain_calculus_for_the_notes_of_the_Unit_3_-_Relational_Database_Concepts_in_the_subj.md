### Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a non-procedural query language for relational databases  .
- Relational calculus allows users to specify the desired information without giving a specific procedure for obtaining it .
- Tuple and domain calculus differ in the way they use variables to represent the data in a relation  .

#### Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables range over tuples, which are ordered sets of attribute values that represent a single row or record in a database table  .
- A tuple relational calculus query consists of a tuple variable, which is denoted by a lowercase letter, and a formula, which is a logical expression involving the tuple variable, constants, comparison operators, logical connectives and quantifiers  .
- The result of a tuple relational calculus query is the set of all tuples that satisfy the formula  .
- For example, the query {t | t ∈ Student ∧ t.age > 18} returns the set of all tuples t from the Student relation such that t.age is greater than 18.

#### Domain Relational Calculus (DRC)

- In domain relational calculus, variables range over domain elements, which are field values of a relation .
- A domain relational calculus query consists of a list of domain variables, which are denoted by uppercase letters, and a formula, which is a logical expression involving the domain variables, constants, comparison operators, logical connectives and quantifiers .
- The result of a domain relational calculus query is the set of all lists of domain values that satisfy the formula .
- For example, the query {<X, Y> | ∃Z(Student(X, Y, Z) ∧ Z > 18)} returns the set of all pairs of values <X, Y> such that there exists a value Z in the Student relation such that X, Y and Z are the values of the attributes name, rollno and age, respectively, and Z is greater than 18.