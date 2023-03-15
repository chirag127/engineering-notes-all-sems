### Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational calculus is a non-procedural query language that describes what data to retrieve from a relational database without specifying how to do it  .
- Relational calculus is based on mathematical predicate calculus, which is a branch of symbolic logic that deals with predicates and quantifiers .
- Relational calculus is an integral part of the relational data model, which is the foundation of the relational database management system (RDBMS) .
- Relational calculus provides a declarative way of expressing queries, which means that it focuses on the logic of the query rather than the steps to execute it  .
- Relational calculus can be divided into two types: tuple relational calculus (TRC) and domain relational calculus (DRC)   .
  - Tuple relational calculus uses tuple variables to represent rows of a relation and applies predicate expressions to select the tuples that satisfy certain conditions  .
  - Domain relational calculus uses domain variables to represent individual values of the attributes of a relation and applies predicate expressions to select the values that satisfy certain conditions  .
- Relational calculus is a formal language that has a well-defined syntax and semantics  .
  - The syntax of relational calculus consists of variables, constants, operators, predicates, and quantifiers  .
  - The semantics of relational calculus defines the meaning of a query as a set of tuples or values that satisfy the predicate expression  .
- Relational calculus is a powerful and expressive language that can express any query that can be expressed in relational algebra, which is another non-procedural query language  .
  - Relational calculus and relational algebra are equivalent in expressive power, which means that for any query that can be written in one language, there exists a query that can be written in the other language and produces the same result  .
  - Relational calculus and relational algebra are also equivalent in computational complexity, which means that the time and space required to evaluate a query in one language is proportional to the time and space required to evaluate the corresponding query in the other language  .
- Relational calculus is a declarative language that can be used to specify the requirements of a query, but it is not suitable for implementing a query processing system  .
  - Relational calculus does not provide any guidance on how to execute a query efficiently, which is the main concern of a query processing system  .
  - Relational calculus may also allow some queries that are not safe or consistent, which means that they may produce infinite or ambiguous results  .
  - Therefore, relational calculus is usually translated into relational algebra or some other procedural language before being executed by a query processing system  .