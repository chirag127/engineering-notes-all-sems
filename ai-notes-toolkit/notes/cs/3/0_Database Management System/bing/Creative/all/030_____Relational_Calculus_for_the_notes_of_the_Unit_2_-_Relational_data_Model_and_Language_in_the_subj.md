# Relational Calculus for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Relational calculus is a **non-procedural** query language that describes **what** data to retrieve from a relational database, without specifying **how** to do it  .
- Relational calculus is based on **mathematical logic**, specifically **predicate calculus**, which uses variables, constants, operators, quantifiers, and predicates to form expressions  .
- Relational calculus is an **integral part** of the relational data model, which is the foundation of the relational database management system (RDBMS) .
- Relational calculus can be divided into two types: **tuple relational calculus (TRC)** and **domain relational calculus (DRC)**   .
- Tuple relational calculus uses **tuple variables** to represent rows of a relation, and checks every row with a **predicate expression** that evaluates to true or false  .
- Domain relational calculus uses **domain variables** to represent individual values of the attributes of a relation, and forms expressions using **membership conditions** that specify which values belong to which relation  .
- Both types of relational calculus are **equivalent** in expressive power, meaning that any query that can be expressed in one type can also be expressed in the other type .
- Relational calculus is also **equivalent** to relational algebra, another query language that is **procedural** and specifies **how** to manipulate the data in a relational database  .
- Relational calculus is a **declarative** language that can express complex queries in a concise and elegant way, but it is not directly executable by a RDBMS  .
- Relational calculus expressions must satisfy the **safe query** condition, which ensures that the result of a query is finite and can be computed in a reasonable amount of time  .