# Prolog Programming for the notes of the Unit 3 - KNOWLEDGE REPRESENTATION in the subject of ARTIFICIAL INTELLIGENCE KCS

- Prolog is a **logic programming language** that is widely used in **artificial intelligence** and **computational linguistics** .
- Prolog is based on **first-order logic**, a formal logic that allows expressing facts and rules about some domain of interest.
- Prolog is a **declarative programming language**, which means that the program logic is expressed in terms of **relations**, not in terms of a specific sequence of instructions .
- Prolog programs consist of **facts**, **rules**, and **queries** .
  - Facts are statements that describe the properties or relations of some objects or concepts in the domain. For example, `likes(john, pizza).` is a fact that states that John likes pizza.
  - Rules are statements that define new relations or properties based on existing ones. For example, `likes(X, Y) :- likes(X, Z), likes(Z, Y).` is a rule that states that if X likes Z and Z likes Y, then X likes Y.
  - Queries are statements that ask for information or solutions based on the facts and rules. For example, `?- likes(john, cheese).` is a query that asks if John likes cheese.
- Prolog uses a **backtracking** algorithm to find all possible answers to a query by matching it with the facts and rules in the program .
  - If a query matches a fact, then the query is true and the fact is an answer.
  - If a query matches a rule, then the query is true if the conditions of the rule are true. The rule is an answer with the variables in the query substituted by the values that make the conditions true.
  - If a query does not match any fact or rule, then the query is false and there is no answer.
  - If a query matches more than one fact or rule, then the query has multiple answers and Prolog will try to find them all by backtracking to previous choices and exploring alternative paths.
- Prolog can be used for **knowledge representation and reasoning**, which are essential tasks in artificial intelligence  .
  - Knowledge representation is the process of encoding the information and knowledge about a domain in a formal and structured way that can be manipulated by a computer.
  - Reasoning is the process of inferring new information and knowledge from the existing ones using logical rules and principles.
  - Prolog allows expressing knowledge in a natural and concise way using facts and rules, and allows reasoning by asking queries and finding answers using the backtracking algorithm.
  - Prolog can be used to implement various types of knowledge representation and reasoning systems, such as **expert systems**, **ontologies**, **semantic networks**, **frames**, **planning**, **natural language processing**, etc.