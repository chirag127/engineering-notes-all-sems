# Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases .
- Relational calculus is a declarative language, which means it specifies what data to retrieve, not how to retrieve it .
- Tuple and domain calculus differ in the way they use variables to represent data from a relation.

## Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables range over tuples, which are ordered sets of attribute values that represent a single row or record in a database table .
- A tuple variable (t) goes to each row of the table and checks if a predicate (a logical condition) is true or false for the given row .
- Depending on the predicate, it returns the whole row or part of the row that satisfies the condition .
- The syntax of tuple relational calculus is:

  `{t | P(t)}`

  where t is a tuple variable and P(t) is a predicate involving t .

- For example, the query to find the names of all employees who work in the department 10 is:

  `{t.name | EMPLOYEE(t) AND t.deptno = 10}`

  where EMPLOYEE(t) is a predicate that checks if t is a tuple from the EMPLOYEE relation .

## Domain Relational Calculus (DRC)

- In domain relational calculus, variables range over domain elements, which are field values of a relation .
- A domain variable (x) goes to each value of an attribute and checks if a predicate is true or false for the given value .
- Depending on the predicate, it returns the value or a combination of values that satisfies the condition .
- The syntax of domain relational calculus is:

  `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`

  where x1, x2, ..., xn are domain variables and P(x1, x2, ..., xn) is a predicate involving them .

- For example, the query to find the names of all employees who work in the department 10 is:

  `{<x> | EMPLOYEE(x, y, z, w) AND w = 10}`

  where EMPLOYEE(x, y, z, w) is a predicate that checks if x, y, z, w are values of the attributes name, empno, job, deptno of the EMPLOYEE relation .

## Comparison of TRC and DRC

- Both TRC and DRC are equivalent in expressive power, which means they can express the same queries .
- However, TRC is more intuitive and natural for humans, while DRC is more concise and abstract .
- TRC is closer to the relational algebra, which is a procedural query language, while DRC is closer to the first-order logic, which is a formal system of reasoning .