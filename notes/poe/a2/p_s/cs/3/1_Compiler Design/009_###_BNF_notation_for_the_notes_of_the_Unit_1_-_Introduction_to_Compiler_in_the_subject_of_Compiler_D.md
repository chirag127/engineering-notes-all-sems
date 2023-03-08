 Here is the content in markdown format for the given topic:

### BNF Notation for Unit 1 - Introduction to Compiler

1. BNF stands for Backus-Naur Form. It is a formal notation technique to describe the syntax of a programming language.
2. BNF uses a set of rules to define the allowable sequences of symbols in a language. Each rule has a left-hand side and a right-hand side. The left-hand side is a single nonterminal symbol and the right-hand side consists of one or more terminal and/or nonterminal symbols.
3. The symbols used in BNF are:

- <symbol> - Use angle brackets to enclose a terminal symbol. Eg: <digit>, <letter>
- symbol - Nonterminal symbols are just bare symbols. Eg: digit, letter, identifier
- | - The vertical bar indicates a choice between alternatives. Eg: digit | letter
- [...] - Square brackets are used for grouping. Eg: [A-Z]
- {...} - Curly braces are used to indicate zero or more repetitions of what is inside. Eg: {digit}

4. Example BNF rule:
<identifier> ::= <letter> {<letter> | <digit>}

This rule means an identifier starts with a letter followed by zero or more letters or digits.

5. Advantages of BNF:
- It is easy to understand and has a simple notation.
- It is unambiguous and precise.
- It separates the syntax definition from the semantics.
- It can be used to define the syntax of any language.

6. Limitations of BNF:
- It cannot express left recursion.
- The order of choices is not clear in BNF.
- The notation becomes complex for large grammars.
- Associativity of operators cannot be specified.

7. Applications of BNF:
- Used to define the syntax of programming languages.
- Used in compiler construction to define the grammar of the source language.
- Used in software and system specification to precisely define the syntax of data or protocols.