### DATALOG language

- Datalog is a **declarative logic programming language** that is based on **function-free Horn clauses** .
- Datalog is often used as a **query language for deductive databases** , which are databases that can infer new facts from existing facts and rules.
- Datalog is syntactically a **subset of Prolog**, but it differs from Prolog in its **evaluation model** and **properties** .
- Datalog uses a **bottom-up evaluation model** , which means that it starts from the facts and applies the rules repeatedly until no new facts can be derived. Prolog uses a **top-down evaluation model** , which means that it starts from a query and tries to find facts and rules that can prove it.
- Datalog has some advantages over Prolog, such as **guaranteed termination**, **efficient implementation**, **parallelizability**, and **modularity**  .
- Datalog has some limitations, such as **lack of negation**, **recursion**, and **arithmetic**  . However, some extensions of Datalog have been proposed to overcome these limitations, such as **stratified negation**, **aggregation**, and **constraints** .
- Datalog has found new applications in various domains, such as **data integration**, **information extraction**, **networking**, **program analysis**, **security**, **cloud computing** and **machine learning**.