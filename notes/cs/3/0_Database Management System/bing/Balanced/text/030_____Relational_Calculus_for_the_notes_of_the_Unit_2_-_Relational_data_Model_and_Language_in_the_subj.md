### Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational calculus is a **non-procedural** query language that describes **what** data to retrieve from a relational database, without specifying **how** to do it  .
- Relational calculus is based on **mathematical logic**, specifically **predicate calculus**, which uses variables, constants, operators, quantifiers, and predicates to form expressions  .
- Relational calculus is an **integral part** of the relational data model, which is the foundation of the relational database management system (RDBMS) .
- Relational calculus can be classified into two types: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**   .
- Tuple relational calculus uses **tuple variables** to represent rows of a relation and **predicate expressions** to specify the conditions for selecting tuples  . For example, the query to find the names and phone numbers of book stores that sell a book titled "Some Sample Book" can be written as:

```
{t.StoreName, t.StorePhone | t ∈ Bookstore ∧ ∃b(b ∈ Book ∧ b.BookstoreID = t.BookstoreID ∧ b.BookTitle = "Some Sample Book")}
```

- Domain relational calculus uses **domain variables** to represent individual values of the attributes of a relation and **predicate expressions** to specify the conditions for selecting values  . For example, the same query as above can be written as:

```
{x, y | ∃z(Bookstore(x, y, z) ∧ ∃w(Book(z, w, "Some Sample Book")))}
```

- Both TRC and DRC are **equivalent** in expressive power, meaning that any query that can be written in one form can also be written in the other form  .
- Relational calculus is also **equivalent** to relational algebra, another query language that is **procedural** and specifies **how** to manipulate the relations to obtain the desired result  .
- Relational calculus is a **declarative** language that allows users to focus on the **logic** of the query, rather than the **implementation** details  .
- Relational calculus is a **formal** language that has a **well-defined syntax** and **semantics**, and can be used to **prove** the correctness and optimality of query processing algorithms  .