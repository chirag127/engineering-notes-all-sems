### DATALOG language

- Datalog is a **declarative logic programming language** that is based on **function-free Horn clauses** .
- Datalog is often used as a **query language for deductive databases** , which are databases that can infer new facts from existing facts and rules.
- Datalog is syntactically a **subset of Prolog** , but it has a different **evaluation model**. Datalog uses a **bottom-up** approach, which means it starts from the facts and derives new facts until no more can be derived . Prolog uses a **top-down** approach, which means it starts from the query and tries to find facts and rules that satisfy it .
- Datalog has some advantages over Prolog, such as **guaranteed termination**, **efficient implementation**, and **easier parallelization** .
- Datalog has some limitations, such as **lack of negation**, **lack of functions**, and **lack of arithmetic** . However, some extensions of Datalog have been proposed to overcome these limitations, such as **stratified negation**, **aggregation functions**, and **constraints** .
- Datalog has found new applications in various domains, such as **data integration**, **information extraction**, **networking**, **program analysis**, **security**, **cloud computing** and **machine learning**.