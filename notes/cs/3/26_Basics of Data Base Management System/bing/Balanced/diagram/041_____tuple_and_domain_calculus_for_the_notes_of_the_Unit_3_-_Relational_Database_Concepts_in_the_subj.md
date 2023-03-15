### Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases .
- Relational calculus is a declarative language, which means it specifies what data to retrieve, not how to retrieve it .
- Tuple and domain calculus differ in the way they use variables to represent data from a relation.

#### Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables range over tuples, which are ordered sets of attribute values that represent a single row or record in a database table .
- A tuple relational calculus query consists of a formula that evaluates to true or false for each tuple in a relation .
- The formula can contain constants, comparison operators, logical connectives and quantifiers.
- The result of a tuple relational calculus query is the set of all tuples that satisfy the formula .
- For example, the query `{t | t ∈ Student ∧ t.age > 18}` returns the set of all tuples from the Student relation whose age is greater than 18.

#### Domain Relational Calculus (DRC)

- In domain relational calculus, variables range over domain elements, which are field values of a relation .
- A domain relational calculus query consists of a list of variables, followed by a formula that evaluates to true or false for each assignment of values to the variables .
- The formula can contain constants, comparison operators, logical connectives and quantifiers.
- The result of a domain relational calculus query is the set of all assignments of values to the variables that satisfy the formula .
- For example, the query `{<name, age> | ∃ rollno (Student(rollno, name, age) ∧ age > 18)}` returns the set of all pairs of name and age values from the Student relation whose age is greater than 18.