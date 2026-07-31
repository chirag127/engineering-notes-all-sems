# Prolog Programming for the notes of the Unit 3 - KNOWLEDGE REPRESENTATION in the subject of ARTIFICIAL INTELLIGENCE KCS

- Prolog is a **logic programming language** that has an important role in artificial intelligence .
- Unlike many other programming languages, Prolog is intended primarily as a **declarative programming language**. In Prolog, logic is expressed as **relations** (called as Facts and Rules).
- Prolog is based on the idea of **resolution** and **unification**. Resolution is a method of deductive reasoning that uses logical rules to infer new facts from given facts. Unification is a process of finding a substitution that makes two terms equal.
- Prolog programs consist of a **database** of facts and rules, and a **query** that asks for a goal to be proved. Prolog tries to find a **proof** for the query by applying the rules and matching the facts using unification.
- Prolog supports **backtracking**, which means that it can undo the choices made during the search for a proof and try alternative solutions. This allows Prolog to handle **nondeterminism** and **recursion**.
- Prolog also supports **cut** (!), which is a special operator that prunes the search space and prevents backtracking. Cut can be used to improve the efficiency and correctness of Prolog programs, but it can also introduce **side effects** and **non-logical behavior**.
- Prolog can be used for various applications of artificial intelligence, such as **natural language processing**, **expert systems**, **planning**, **knowledge representation and reasoning**, and **machine learning**.
- Knowledge representation and reasoning (KRR) is the subfield of artificial intelligence that studies how to represent and manipulate knowledge in a formal and computable way.
- KRR aims to provide a **common-sense understanding** of the world and enable intelligent agents to **reason** about it and **act** upon it.
- KRR involves various **paradigms** and **techniques**, such as **logic**, **ontology**, **frames**, **semantic networks**, **rules**, **non-monotonic reasoning**, **default reasoning**, **abduction**, **belief revision**, **argumentation**, **answer set programming**, and **description logic**   .
- Prolog is a natural choice for KRR, as it allows the expression of knowledge as logical relations and the inference of new knowledge by resolution and unification.
- Prolog can also be extended with various features and extensions to support different kinds of KRR, such as **negation as failure**, **constraints**, **meta-programming**, **object-oriented programming**, **probabilistic reasoning**, and **fuzzy logic**  .
- AILog is an example of a KRR system built on top of Prolog. It is a **logic programming language** that supports **non-monotonic reasoning** and **default reasoning** using the **answer set semantics** .
- AILog allows the user to define a **knowledge base** of facts, rules, and defaults, and to query it using a **goal-directed** and **interactive** reasoning process.
- AILog can handle various kinds of KRR problems, such as **inheritance**, **exceptions**, **abduction**, **planning**, and **diagnosis**.