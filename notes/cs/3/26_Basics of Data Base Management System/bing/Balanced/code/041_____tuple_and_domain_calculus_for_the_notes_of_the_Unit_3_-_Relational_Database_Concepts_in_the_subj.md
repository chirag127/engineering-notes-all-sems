### Tuple and Domain Calculus

- Tuple and domain calculus are two types of relational calculus, which is a query language for relational databases.
- Relational calculus is based on the concept of mathematical logic and allows users to specify what data they want to retrieve from the database, without specifying how to do it.
- Tuple and domain calculus differ in the way they use variables to represent data.

#### Tuple Relational Calculus (TRC)

- In tuple relational calculus, variables range over tuples, which are ordered sets of attribute values that represent a single row or record in a database table.
- A tuple variable (t) goes to each row of the table and checks if the predicate is true or false for the given row.
- A query in tuple relational calculus is of the form `{t | P(t)}`, where t is a tuple variable and P(t) is a formula involving t and other constants, comparison operators, logical connectives and quantifiers.
- The result of the query is the set of all tuples t that satisfy the formula P(t).
- For example, the query `{t | t[dept] = 'CS' and t[salary] > 50000}` returns the set of all tuples t from the employee table such that the department is CS and the salary is greater than 50000.

#### Domain Relational Calculus (DRC)

- In domain relational calculus, variables range over domain elements, which are field values of the attributes in the database tables.
- A query in domain relational calculus is of the form `{<x1, x2, ..., xn> | P(x1, x2, ..., xn)}`, where x1, x2, ..., xn are domain variables and P(x1, x2, ..., xn) is a formula involving the variables and other constants, comparison operators, logical connectives and quantifiers.
- The result of the query is the set of all n-tuples <x1, x2, ..., xn> that satisfy the formula P(x1, x2, ..., xn).
- For example, the query `{<name, salary> | exists e (e[name] = name and e[dept] = 'CS' and e[salary] = salary and salary > 50000)}` returns the set of all pairs <name, salary> such that there exists an employee e with the same name and salary, and the department is CS and the salary is greater than 50000.