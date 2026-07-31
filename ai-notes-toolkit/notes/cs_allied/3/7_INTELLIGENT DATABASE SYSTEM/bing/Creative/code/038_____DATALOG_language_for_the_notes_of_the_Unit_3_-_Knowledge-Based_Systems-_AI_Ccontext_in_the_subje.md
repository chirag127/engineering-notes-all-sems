### DATALOG language

- Datalog is a **declarative logic programming language** that is based on the concept of **Horn clauses** .
- Datalog is a **subset of Prolog**, but it differs from Prolog in its **evaluation model** and **expressive power** .
- Datalog uses a **bottom-up** evaluation model, which means that it starts from the facts and derives new facts by applying rules, until no more facts can be derived .
- Datalog is **less expressive** than Prolog, because it does not allow function symbols, negation, or recursion through negation .
- Datalog is often used as a **query language for deductive databases**, which are databases that store facts and rules, and can answer queries by applying logical inference .
- Datalog has also found new applications in **data integration, information extraction, networking, program analysis, security, cloud computing and machine learning**.
- Datalog has a simple syntax, which consists of **facts**, **rules**, and **queries** .
- Facts are statements that assert the truth of a relation between some constants, such as `parent(john, mary).` .
- Rules are statements that define new relations in terms of existing ones, using variables and conjunctions, such as `ancestor(X, Y) :- parent(X, Y).` .
- Queries are statements that ask for the values of some variables that satisfy a given relation, such as `?- ancestor(X, mary).` .
- Datalog has a **relational semantics**, which means that every relation is interpreted as a set of tuples, and every query is evaluated as a set of substitutions that make the query true.
- Datalog has a **sound and complete** inference mechanism, which means that it can derive all and only the facts that are logically implied by the facts and rules in the database.
- Datalog has a **polynomial time** complexity, which means that it can answer any query in a time that is proportional to a polynomial function of the size of the database.