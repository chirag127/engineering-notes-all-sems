Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of resolution for the unit 3 - knowledge representation in the subject of artificial intelligence KCS. Here is the content in markdown format:

# Resolution

- Resolution is a method of **inference** that can be used to **prove** or **disprove** a logical statement by using a set of **clauses** (disjunctions of literals).
- Resolution is based on the **principle of resolution**, which states that if two clauses contain complementary literals (one positive and one negative), then they can be **resolved** by eliminating those literals and forming a new clause with the remaining literals.
- Resolution can be applied to **propositional logic** or **first-order logic**. In propositional logic, resolution operates on clauses that are composed of **propositional variables** and **negation**. In first-order logic, resolution operates on clauses that are composed of **predicates**, **constants**, **variables**, **negation**, and **quantifiers**.
- Resolution can be used to **prove** a statement by **refutation**. This means that we assume the **negation** of the statement and try to derive a **contradiction** using resolution. If we can derive an **empty clause** (a clause with no literals), then we have shown that the negation of the statement is **unsatisfiable**, and therefore the statement is **valid**.
- Resolution can be used to **disprove** a statement by **satisfiability**. This means that we try to find a **model** (an assignment of truth values to the propositional variables or an interpretation of the predicates and constants) that makes the statement **true**. If we can find such a model, then we have shown that the statement is **satisfiable**, and therefore **not valid**.
- Resolution can be performed in different **strategies** or **orders**. Some common strategies are:

  - **Linear resolution**: only one clause from the original set of clauses is used in each resolution step.
  - **Input resolution**: only one clause from the original set of clauses and one clause from the derived set of clauses are used in each resolution step.
  - **Set-of-support resolution**: only clauses that are derived from the negation of the statement to be proved are used in each resolution step.
  - **Unit resolution**: only clauses that contain a single literal are used in each resolution step.
  - **Ordered resolution**: the literals in each clause are ordered according to some criterion, and only the first literal in each clause can be resolved.
  - **SOS resolution**: a combination of set-of-support and ordered resolution.

- Resolution can be **sound** and **complete**. Soundness means that if a statement can be proved by resolution, then it is valid. Completeness means that if a statement is valid, then it can be proved by resolution. Resolution is sound and complete for both propositional logic and first-order logic, but only under certain **restrictions**. Some of these restrictions are:

  - **Skolemization**: a process of eliminating **existential quantifiers** by replacing them with **Skolem functions** or **Skolem constants** that depend on the **universal quantifiers** in the scope.
  - **Unification**: a process of finding a **substitution** that makes two terms **equal**. A substitution is a mapping from variables to terms. Unification is used to resolve clauses that contain variables in first-order logic.
  - **Standardization**: a process of renaming the variables in different clauses to avoid **clashes** or **conflicts**. A clash occurs when two variables have the same name but different meanings. A conflict occurs when two variables have different names but the same meaning.
  - **Renaming**: a process of replacing a predicate with a new predicate that has the same meaning but a different name. Renaming is used to avoid **tautologies** or **redundancies**. A tautology is a clause that is always true, such as P or not P. A redundancy is a clause that is implied by another clause, such as P or Q and P.