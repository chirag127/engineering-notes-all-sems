 Here is the content in markdown format for the topic ### Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System:

### Relational Calculus

- Relational calculus is a non-procedural query language, that focuses on what to retrieve rather than how to retrieve it. It specifies the properties that the result must satisfy without giving the methods to derive it.
- There are two types of relational calculus:

1. Tuple relational calculus: Specifies a set of tuples (rows) that must be in the result. Uses variables that range over tuples.
2. Domain relational calculus: Specifies conditions that must be satisfied by tuples in the result, without naming the specific tuples. Uses variables that range over values from domains of attributes.

- The relational calculus expressions are formulas which specify the properties that the tuples in the result must satisfy. The tuples which satisfy the properties make up the result of the relational calculus expression.
- Relational calculus is non-procedural as it does not specify the methods or sequence of steps to retrieve data, but only the properties the result must fulfill. The database system determines the most efficient way to retrieve the data.
- Some advantages of relational calculus are:

- It is easy to understand as it is based on mathematical logic and set theory.
- It is a concise and high-level language.
- It can express complex queries in a simple manner.

- Some disadvantages are:

- It may be inefficient to implement as the database system determines the methods to derive the result.
- It is difficult to optimize the queries.
- The expression can become very complex for complicated queries.

- Examples of relational calculus queries:

```
{x| ??x(Employee(x) ?? ??? Salary(x) > 10000)}
{x| ??y(Student(y) ?? Course(y, x) ?? Grade(y, x) = 'A')}
```

- Relational calculus has applications in various database systems to retrieve data in an efficient manner based on the properties specified in the query language. It forms the theoretical foundation for the query languages implemented in database systems.