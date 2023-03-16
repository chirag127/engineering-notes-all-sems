### DATALOG language

- Datalog is a **declarative logic programming language** that is based on **function-free Horn clauses**.
- Datalog is a **subset of Prolog**, but it uses a **bottom-up** rather than top-down evaluation model .
- Datalog is often used as a **query language for deductive databases**, which are databases that can derive new facts from existing facts using logical rules .
- Datalog has also found new applications in **data integration, information extraction, networking, program analysis, security, cloud computing and machine learning**.
- A Datalog program consists of a set of **facts** and a set of **rules**. Facts are ground atoms that represent the data in the database. Rules are logical implications that define how new facts can be derived from existing facts .
- A Datalog query is a **goal** that asks for the values of some variables that satisfy a given condition. A Datalog query can be answered by applying the rules to the facts until no more new facts can be derived, and then checking if the goal matches any of the derived facts .
- Datalog has a well-defined **semantics** based on the **least Herbrand model**, which is the smallest set of facts that satisfies all the rules in the program .
- Datalog has some advantages over SQL, such as **recursion**, **negation**, **rule chaining** and **higher-order predicates** .
- Datalog also has some limitations, such as **lack of arithmetic operations**, **lack of aggregation functions**, **lack of updates** and **lack of user-defined functions** .
- Datalog can be extended with various features, such as **stratified negation**, **aggregation**, **constraints**, **types**, **modules** and **external predicates**  .