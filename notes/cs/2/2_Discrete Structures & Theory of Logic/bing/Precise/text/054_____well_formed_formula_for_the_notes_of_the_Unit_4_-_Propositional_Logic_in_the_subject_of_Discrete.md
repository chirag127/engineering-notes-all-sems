### Well Formed Formula

A well-formed formula (WFF) is a finite sequence of symbols from a given alphabet that is part of a formal language. A formal language is a set of finite strings of symbols that are constructed according to specific rules.

In propositional logic, a well-formed formula is a statement that can be assigned a truth value of true or false. The set of well-formed formulas is defined recursively as follows:

1. Any propositional variable is a well-formed formula.
2. If P is a well-formed formula, then so is (¬P).
3. If P and Q are well-formed formulas, then so are (P ∧ Q), (P ∨ Q), (P → Q), and (P ↔ Q).
4. Nothing else is a well-formed formula.

The parentheses are used to indicate the scope of the operators and to disambiguate formulas that would otherwise be ambiguous. For example, the formula P ∧ Q ∨ R is ambiguous because it is not clear whether it should be interpreted as (P ∧ Q) ∨ R or P ∧ (Q ∨ R). By using parentheses, the intended meaning can be made clear.

Well-formed formulas are important in propositional logic because they provide a precise and unambiguous way to represent logical statements. They are used to construct formal proofs and to reason about the truth or falsity of statements. Well-formed formulas are also used in computer science, particularly in the field of automated theorem proving, where they are used to represent and manipulate logical statements in a precise and unambiguous way.