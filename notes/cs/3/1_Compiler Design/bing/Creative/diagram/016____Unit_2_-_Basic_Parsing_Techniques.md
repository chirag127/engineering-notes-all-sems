## Unit 2 - Basic Parsing Techniques

Parsing is the process of analyzing the structure and meaning of a sentence or a program based on a given grammar. Parsing techniques are methods for implementing parsers that can handle different kinds of grammars and languages.

Some of the basic parsing techniques are:

- Top-down parsing: This technique starts from the start symbol of the grammar and tries to derive the input string by applying the production rules in a top-down manner. Top-down parsing can be done by using recursive descent or predictive parsing algorithms. Top-down parsing can handle left-recursive and ambiguous grammars, but it may require backtracking or lookahead to resolve conflicts.
- Bottom-up parsing: This technique starts from the input string and tries to reduce it to the start symbol of the grammar by applying the production rules in a bottom-up manner. Bottom-up parsing can be done by using shift-reduce or operator-precedence parsing algorithms. Bottom-up parsing can handle right-recursive and unambiguous grammars, but it may require precedence or associativity rules to resolve conflicts.
- Chart parsing: This technique uses a data structure called a chart to store partial results of parsing and to avoid redundant computations. Chart parsing can be done by using dynamic programming or tabular parsing algorithms. Chart parsing can handle any context-free grammar, but it may require more space and time than other techniques.