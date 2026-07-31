#### CO 3 Design and analyze top down and bottom up parsers. K4, K5

- Top down and bottom up parsers are two types of parsers that are used to construct parse trees from a given input string and a grammar.
- A parse tree is a graphical representation of the syntactic structure of a sentence according to a grammar.
- A grammar is a set of rules that define the syntax of a language, i.e., how words and symbols can be combined to form valid sentences.
- A parser is a program that takes an input string and a grammar as input and outputs a parse tree or an error message if the input string is not syntactically correct.
- Top down and bottom up parsers differ in the direction and the order of applying the rules of grammar to construct the parse tree.

##### Top down parsing
- Top down parsing is a parsing technique that starts from the root of the parse tree and works down to the leaves by using the rules of grammar in a forward order.
- Top down parsing is based on leftmost derivation, i.e., it replaces the leftmost non-terminal symbol in the sentential form with one of its production rules until it reaches the input string.
- Top down parsing can be implemented by two methods: recursive descent parsing and predictive parsing.
- Recursive descent parsing is a method that uses a set of recursive procedures, one for each non-terminal symbol, to parse the input string. Each procedure tries to match the input string with the production rules of the corresponding non-terminal symbol and calls other procedures as needed.
- Predictive parsing is a method that uses a data structure called a parsing table to determine which production rule to apply for each non-terminal symbol and input symbol. A parsing table is a two-dimensional array that maps each non-terminal symbol and input symbol to a production rule or an error. A predictive parser is also called a LL(1) parser, where LL stands for left-to-right scanning and leftmost derivation, and 1 stands for one symbol of lookahead.
- Advantages of top down parsing:
  - It is easy to implement and understand.
  - It can handle left recursion and left factoring in the grammar.
  - It can produce parse trees in the same order as the input string.
- Disadvantages of top down parsing:
  - It may generate unnecessary backtracking and duplication of work.
  - It cannot handle grammars that are ambiguous or have left recursion.
  - It may require more memory and time than bottom up parsing.

##### Bottom up parsing
- Bottom up parsing is a parsing technique that starts from the leaves of the parse tree and works up to the root by using the rules of grammar in a reverse order.
- Bottom up parsing is based on rightmost derivation in reverse, i.e., it replaces the rightmost substring of the input string that matches the right-hand side of a production rule with the corresponding left-hand side non-terminal symbol until it reaches the start symbol.
- Bottom up parsing can be implemented by two methods: shift-reduce parsing and operator-precedence parsing.
- Shift-reduce parsing is a method that uses a data structure called a stack to store the symbols that have been processed and a pointer called the input pointer to scan the input string from left to right. At each step, the parser can perform one of two actions: shift or reduce. A shift action moves the input pointer to the next symbol and pushes it onto the stack. A reduce action pops one or more symbols from the stack that match the right-hand side of a production rule and pushes the corresponding left-hand side non-terminal symbol onto the stack. The parser repeats these actions until it reaches the end of the input string and the stack contains only the start symbol, or until it encounters an error.
- Operator-precedence parsing is a method that uses a data structure called a precedence table to determine the relative precedence and associativity of the operators and operands in the input string. A precedence table is a two-dimensional array that maps each pair of symbols to one of three relations: less than, equal to, or greater than. A less than relation means that the first symbol has lower precedence than the second symbol and should be shifted onto the stack. An equal to relation means that the first symbol has the same precedence as the second symbol and should be reduced by a production rule. A greater than relation means that the first symbol has higher precedence than the second symbol and should be reduced by a production rule. The parser uses the precedence table and the stack to parse the input string from left to right.
- Advantages of bottom up parsing:
  - It can handle a larger class of grammars than top down parsing, including ambiguous and left