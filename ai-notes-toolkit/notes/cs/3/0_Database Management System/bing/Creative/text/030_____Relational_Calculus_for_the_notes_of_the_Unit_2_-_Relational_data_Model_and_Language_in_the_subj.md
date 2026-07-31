### Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational calculus is a **non-procedural** query language that describes **what** data to retrieve from a relational database, without specifying **how** to do it  .
- Relational calculus is based on **mathematical logic**, specifically **predicate calculus** , which uses variables, constants, operators, quantifiers, and predicates to form expressions.
- Relational calculus is an **integral part** of the relational data model, which is the foundation of the relational database management system (RDBMS) .
- Relational calculus can be classified into two types: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**   .
- Tuple relational calculus uses **tuple variables** to represent rows of a relation, and checks every row with a **predicate expression** condition . For example, the query to find the names of all students who have enrolled in the course CS101 can be written as:

  `{T.name | STUDENT(T) AND T.course = 'CS101'}`

  where T is a tuple variable, STUDENT is a relation, and name and course are attributes.
- Domain relational calculus uses **domain variables** to represent individual values of attributes, and combines them with a **membership condition** to specify a relation  . For example, the same query as above can be written as:

  `{<x> | ∃y (STUDENT(x, y) AND y = 'CS101')}`

  where x and y are domain variables, STUDENT is a relation, and name and course are attributes.
- Both types of relational calculus are **equivalent** in expressive power, meaning that any query that can be written in one form can also be written in the other form  .
- Relational calculus is also **equivalent** to relational algebra, another query language that is **procedural** and specifies **how** to manipulate data in a relational database  .
- Relational calculus is a **declarative** language that focuses on the **semantics** or meaning of the query, rather than the **syntax** or form of the query  .
- Relational calculus is a **safe** language that guarantees to produce a finite and valid result for any query, as long as the query satisfies the **domain and range restrictions**  . These restrictions ensure that the variables in the query are bound to values from the database, and that the result of the query is a subset of the database.