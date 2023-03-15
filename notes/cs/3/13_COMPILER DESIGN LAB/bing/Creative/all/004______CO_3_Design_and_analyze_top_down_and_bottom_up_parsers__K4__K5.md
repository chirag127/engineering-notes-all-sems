#### CO 3 Design and analyze top down and bottom up parsers. K4, K5

- Top down and bottom up parsers are two types of parsers that are used to construct parse trees from a given input string and a grammar.
- A parse tree is a graphical representation of the syntactic structure of a sentence according to a grammar.
- A grammar is a set of rules that define the syntax of a language, i.e., how words and symbols can be combined to form valid sentences.
- A parser is a program that takes an input string and a grammar as input and outputs a parse tree or an error message if the input string is not syntactically correct.
- Top down and bottom up parsers differ in the direction and the order of applying the rules of grammar to construct the parse tree.

##### Top down parsing
- Top down parsing is a parsing technique that starts from the root of the parse tree and works down to the leaves by using the rules of grammar in a forward order.
- Top down parsing is based on leftmost derivation, i.e., it expands the leftmost non-terminal symbol in each step until it reaches the input string.
- Top down parsing can be implemented by two methods: recursive descent parsing and predictive parsing.
- Recursive descent parsing is a method that uses a set of recursive procedures, one for each non-terminal symbol, to parse the input string. Each procedure tries to match the input string with the right hand side of the production rule for that non-terminal symbol. If the match fails, the procedure backtracks and tries another alternative.
- Predictive parsing is a method that uses a data structure called a parsing table to guide the parsing process. A parsing table is a two-dimensional array that maps each pair of a non-terminal symbol and an input symbol to a production rule or an error. A predictive parser uses a stack to keep track of the non-terminal symbols that need to be expanded and a pointer to scan the input string. It consults the parsing table to determine which production rule to apply or whether to report an error.
- Advantages of top down parsing:
  - It is easy to implement and understand.
  - It can handle left factored grammars, i.e., grammars that do not have common prefixes in the right hand side of the production rules.
  - It can handle left recursive grammars, i.e., grammars that have production rules of the form A -> Aα, where A is a non-terminal symbol and α is a string of terminal and non-terminal symbols.
- Disadvantages of top down parsing:
  - It may perform unnecessary backtracking, which is inefficient and time-consuming.
  - It cannot handle left recursive grammars, i.e., grammars that have production rules of the form A -> Aα, where A is a non-terminal symbol and α is a string of terminal and non-terminal symbols.
  - It cannot handle ambiguous grammars, i.e., grammars that have more than one parse tree for the same input string.

##### Bottom up parsing
- Bottom up parsing is a parsing technique that starts from the leaves of the parse tree and works up to the root by using the rules of grammar in a reverse order.
- Bottom up parsing is based on rightmost derivation, i.e., it reduces the rightmost non-terminal symbol in each step until it reaches the start symbol.
- Bottom up parsing can be implemented by two methods: shift-reduce parsing and operator precedence parsing.
- Shift-reduce parsing is a method that uses a data structure called a stack to store the symbols that have been scanned from the input string. It performs two operations: shift and reduce. A shift operation moves the next input symbol to the top of the stack. A reduce operation applies a production rule in reverse to replace the right hand side of the rule with the left hand side of the rule on the top of the stack. The parsing process ends when the stack contains only the start symbol and the input string is empty.
- Operator precedence parsing is a method that uses a data structure called a precedence table to guide the parsing process. A precedence table is a two-dimensional array that maps each pair of terminal symbols to a precedence relation: less than, equal to, or greater than. A operator precedence parser uses a stack to store the symbols that have been scanned from the input string. It compares the top symbol of the stack with the next input symbol using the precedence table to determine whether to shift or reduce. It shifts if the top symbol is less than the next input symbol, and reduces if the top symbol is greater than or equal to the next input symbol. The parsing process ends when the stack contains only the start symbol and the