Hello, I am Sydney, your AI assistant. I can help you with writing notes on First Order Predicate Logic for the Unit 3 - KNOWLEDGE REPRESENTATION in the subject of ARTIFICIAL INTELLIGENCE KCS. Here is the content in markdown format:

# First Order Predicate Logic

- First Order Predicate Logic (FOPL) is a form of logic that extends propositional logic by introducing **quantifiers**, **predicates**, **functions**, and **constants**.
- FOPL allows us to express more complex and detailed statements than propositional logic, such as "Every student likes some teacher" or "There is a prime number greater than 100".
- FOPL is also called **First Order Logic (FOL)** or **Predicate Calculus**.

## Syntax of FOPL

- The syntax of FOPL defines the rules for forming **well-formed formulas (wffs)**, which are the basic units of meaning in FOPL.
- A wff can be either an **atomic formula** or a **compound formula**.
- An atomic formula consists of a **predicate** followed by a list of **terms** enclosed in parentheses, separated by commas. For example, `Likes(John, Mary)` is an atomic formula that means "John likes Mary".
- A term can be either a **constant**, a **variable**, or a **function** applied to a list of terms. For example, `John` is a constant, `x` is a variable, and `Father(John)` is a function applied to a term.
- A constant represents a specific object in the domain of discourse, such as a person, a place, or a number. For example, `John`, `Paris`, and `2` are constants.
- A variable represents an unknown or arbitrary object in the domain of discourse. For example, `x`, `y`, and `z` are variables.
- A function represents a mapping from a list of objects to another object in the domain of discourse. For example, `Father(John)` represents the father of John, and `Plus(2, 3)` represents the sum of 2 and 3.
- A compound formula consists of one or more wffs connected by **logical connectives** or **quantifiers**. For example, `Likes(John, Mary) ∧ Likes(Mary, John)` is a compound formula that means "John likes Mary and Mary likes John".
- A logical connective is a symbol that combines two or more wffs to form a new wff. The common logical connectives are **negation (¬)**, **conjunction (∧)**, **disjunction (∨)**, **implication (→)**, and **equivalence (↔)**. They have the same meaning and precedence as in propositional logic.
- A quantifier is a symbol that binds a variable to a wff, indicating how many objects in the domain of discourse satisfy the wff. The common quantifiers are **universal (∀)** and **existential (∃)**. They have higher precedence than logical connectives.
- The universal quantifier means "for all" or "every". For example, `∀x Likes(x, Mary)` means "Everyone likes Mary".
- The existential quantifier means "there exists" or "some". For example, `∃x Likes(John, x)` means "There is someone who John likes".
- A wff that contains no free variables (i.e., variables that are not bound by a quantifier) is called a **sentence**. A sentence is either true or false in a given interpretation of the domain of discourse. For example, `∀x Likes(x, Mary)` is a sentence, but `Likes(x, Mary)` is not.