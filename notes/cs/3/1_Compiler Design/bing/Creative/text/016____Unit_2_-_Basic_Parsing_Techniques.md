## Unit 2 - Basic Parsing Techniques

- Parsing is the process of analyzing the syntactic structure of a given input string according to a given grammar.
- A grammar is a set of rules that define the syntax of a language, i.e., how words and symbols can be combined to form valid sentences.
- A parser is a program that implements a parsing algorithm, i.e., a method of applying the grammar rules to the input string and constructing a parse tree or a derivation.
- A parse tree is a hierarchical representation of the syntactic structure of a sentence, where each node corresponds to a grammar rule or a terminal symbol.
- A derivation is a sequence of grammar rule applications that generate a sentence from the start symbol of the grammar.
- There are two main types of parsing techniques: top-down and bottom-up.
- Top-down parsing is a method of parsing that starts from the start symbol of the grammar and tries to match the input string from left to right, using the grammar rules to predict what symbols should come next.
- Bottom-up parsing is a method of parsing that starts from the input string and tries to reduce it to the start symbol of the grammar, using the grammar rules to recognize what symbols can be combined together.
- Both top-down and bottom-up parsing can be implemented using recursive or iterative algorithms, depending on whether the parser calls itself recursively or uses a stack to store intermediate results.
- Some of the common top-down parsing algorithms are recursive descent, predictive parsing, and LL parsing.
- Some of the common bottom-up parsing algorithms are shift-reduce, operator-precedence, LR parsing, and LALR parsing.
- Each parsing technique has its own advantages and disadvantages, such as efficiency, simplicity, generality, and error handling.