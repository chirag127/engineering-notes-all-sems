 Here is the content in Markdown format without any emojis or external links:

### Prolog Programming for the notes of the Unit 3 - KNOWLEDGE REPRESENTATION in the subject of ARTIFICIAL INTELLIGENCE KCS

- Prolog is a declarative programming language based on first-order logic.
- It is a rule-based language. Rules are statements in the following form:
Head :- Body.

- The head is an atom or atomic formula which is true if the body is true. The body is a conjunction of atomic formulas and expressions.
- Facts are rules with empty bodies:
john :-.

- This states that john is true. Facts represent statements that are always true.
- Queries are expressions preceded by a question mark:
?- Body.

- This asks if body is true. The query succeeds if body can be unified with the body of a rule.
- Unification is a key concept in Prolog. It is a process of making two terms identical by binding variables. This is used for matching rule bodies with queries and predicates.
- Predicates are relations that can be true or false. They have arguments which can be variables or constants.
- Some important built-in predicates:

- =.. : Creates a structure from a name and arguments
- is/2 : Tests if two terms are identical
- var/1 : Tests if a term is a variable
- =/2 : Unifies two terms

- Examples of Prolog rules:

father(X, Y) :- male(X), parent(X, Y).
/* X is the father of Y if X is male and a parent of Y */

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
/* X is a grandparent of Z if X is a parent of Y and Y is a parent of Z */