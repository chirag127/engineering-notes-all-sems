# Prolog Programming for the notes of the Unit 3 - KNOWLEDGE REPRESENTATION in the subject of ARTIFICIAL INTELLIGENCE KCS

- Prolog is a **logic programming** language that is widely used for **artificial intelligence** applications.
- Prolog allows for the **concise representation of knowledge** and the **efficient execution of inference** using a **declarative** syntax .
- Prolog programs consist of **facts**, **rules**, and **queries** that describe the **relations** among **objects** and **events** in a **domain of interest** .
- Facts are statements that are **unconditionally true** in the domain, such as `parent(john, mary).` which means John is a parent of Mary .
- Rules are statements that are **conditionally true** in the domain, such as `grandparent(X, Y) :- parent(X, Z), parent(Z, Y).` which means X is a grandparent of Y if X is a parent of Z and Z is a parent of Y .
- Queries are statements that **ask for information** or **test a condition** in the domain, such as `?- grandparent(john, alice).` which asks if John is a grandparent of Alice .
- Prolog uses a **backtracking** algorithm to **search** for **possible solutions** to a query by **matching** it with the facts and rules in the program .
- Prolog can also handle **nonmonotonic reasoning** and **answer set programming** which are useful for dealing with **uncertainty**, **inconsistency**, and **default assumptions** in knowledge representation .
- Prolog is a powerful tool for AI because it can **encode and manipulate knowledge** in a **logical and mathematical form** and **implement rule-based systems** which are commonly used in AI applications   .